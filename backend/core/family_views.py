import secrets
from decimal import Decimal
from django.db import transaction
from django.db.models import Q,Sum
from rest_framework import serializers, status
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from .models import Family, FamilyMembership, SavingsGoal, SavingsContribution

class JoinThrottle(UserRateThrottle):
 scope='family_join'

class FamilyNameSerializer(serializers.Serializer):
 name=serializers.CharField(max_length=80,trim_whitespace=True)

class JoinSerializer(serializers.Serializer):
 code=serializers.CharField(max_length=64,trim_whitespace=True)

class GoalSerializer(serializers.Serializer):
 name=serializers.CharField(max_length=120,trim_whitespace=True)
 target=serializers.DecimalField(max_digits=14,decimal_places=2,min_value=Decimal('0.01'))
 scope=serializers.ChoiceField(choices=['personal','family'])

class ContributionSerializer(serializers.Serializer):
 amount=serializers.DecimalField(max_digits=14,decimal_places=2,min_value=Decimal('0.01'))

def family_for(user):
 membership=FamilyMembership.objects.select_related('family').filter(user=user).first()
 return membership.family if membership else None

def serialize_family(family,user):
 return {'id':family.id,'name':family.name,'is_owner':family.owner_id==user.id,'invite_code':family.invite_code if family.owner_id==user.id else None,'members':[{'id':m.user_id,'name':m.user.username,'is_owner':m.user_id==family.owner_id} for m in family.memberships.select_related('user').order_by('joined_at')]}

def accessible(user):
 family=family_for(user)
 predicate=Q(owner=user,family__isnull=True)
 if family: predicate |= Q(family=family)
 return SavingsGoal.objects.filter(predicate)

def serialize_goal(goal):
 contributions=goal.contributions.select_related('user').order_by('-created_at','-id')
 total=sum((c.amount for c in contributions),Decimal('0'))
 return {'id':goal.id,'name':goal.name,'target':str(goal.target),'saved':str(total),'remaining':str(max(goal.target-total,Decimal('0'))),'scope':'family' if goal.family_id else 'personal','created_at':goal.created_at,'contributions':[{'id':c.id,'user':c.user.username,'amount':str(c.amount),'created_at':c.created_at} for c in contributions]}

@api_view(['GET','POST'])
def family_view(request):
 family=family_for(request.user)
 if request.method=='GET': return Response({'family':serialize_family(family,request.user) if family else None})
 if family: return Response({'detail':'Вы уже состоите в семье.'},status=400)
 s=FamilyNameSerializer(data=request.data);s.is_valid(raise_exception=True)
 with transaction.atomic():
  family=Family.objects.create(name=s.validated_data['name'],owner=request.user,invite_code=secrets.token_urlsafe(24))
  FamilyMembership.objects.create(user=request.user,family=family)
 return Response({'family':serialize_family(family,request.user)},status=201)

@api_view(['POST'])
@throttle_classes([JoinThrottle])
def join_family(request):
 if family_for(request.user): return Response({'detail':'Вы уже состоите в семье.'},status=400)
 s=JoinSerializer(data=request.data);s.is_valid(raise_exception=True)
 family=Family.objects.filter(invite_code=s.validated_data['code']).first()
 if not family: return Response({'detail':'Код приглашения недействителен.'},status=404)
 try:
  with transaction.atomic(): FamilyMembership.objects.create(user=request.user,family=family)
 except Exception as e:
  from django.db import IntegrityError
  if isinstance(e,IntegrityError): return Response({'detail':'Вы уже состоите в семье.'},status=400)
  raise
 return Response({'family':serialize_family(family,request.user)})

@api_view(['POST'])
def rotate_invite(request):
 family=family_for(request.user)
 if not family or family.owner_id!=request.user.id: return Response({'detail':'Доступ запрещён.'},status=403)
 family.invite_code=secrets.token_urlsafe(24);family.save(update_fields=['invite_code'])
 return Response({'family':serialize_family(family,request.user)})

@api_view(['POST'])
def leave_family(request):
 family=family_for(request.user)
 if not family: return Response({'detail':'Вы не состоите в семье.'},status=400)
 if family.owner_id==request.user.id: return Response({'detail':'Создатель семьи не может выйти из неё.'},status=400)
 FamilyMembership.objects.filter(user=request.user,family=family).delete()
 return Response(status=204)

@api_view(['GET','POST'])
def savings_goals(request):
 if request.method=='GET': return Response([serialize_goal(x) for x in accessible(request.user).order_by('-created_at').prefetch_related('contributions__user')])
 s=GoalSerializer(data=request.data);s.is_valid(raise_exception=True)
 family=family_for(request.user) if s.validated_data['scope']=='family' else None
 if s.validated_data['scope']=='family' and not family: return Response({'detail':'Сначала создайте семью или присоединитесь к ней.'},status=400)
 goal=SavingsGoal.objects.create(owner=request.user,family=family,name=s.validated_data['name'],target=s.validated_data['target'])
 return Response(serialize_goal(goal),status=201)

@api_view(['POST'])
def contribute(request,pk):
 s=ContributionSerializer(data=request.data);s.is_valid(raise_exception=True)
 with transaction.atomic():
  goal=accessible(request.user).select_for_update().filter(pk=pk).first()
  if not goal: return Response({'detail':'Цель не найдена.'},status=404)
  total=goal.contributions.aggregate(total=Sum('amount'))['total'] or Decimal('0')
  if total+s.validated_data['amount']>Decimal('999999999999.99'): return Response({'detail':'Сумма накоплений слишком велика.'},status=400)
  SavingsContribution.objects.create(goal=goal,user=request.user,amount=s.validated_data['amount'])
 return Response(serialize_goal(goal),status=201)

@api_view(['DELETE'])
def delete_contribution(request,pk,contribution_id):
 with transaction.atomic():
  goal=accessible(request.user).select_for_update().filter(pk=pk).first()
  if not goal: return Response({'detail':'Цель не найдена.'},status=404)
  record=goal.contributions.filter(pk=contribution_id,user=request.user).first()
  if not record: return Response({'detail':'Запись не найдена.'},status=404)
  record.delete()
 return Response(status=204)
