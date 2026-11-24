from decimal import Decimal, InvalidOperation
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Profile, Product, Plan, Expense, Inventory, Feedback
from .serializers import ProfileSerializer,ProductSerializer,ExpenseSerializer,InventorySerializer,PlanSerializer
from .services import budget, generate

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
 username=str(request.data.get('username','')).strip(); password=request.data.get('password','')
 if not username or len(username)>150 or User.objects.filter(username__iexact=username).exists(): return Response({'detail':'Укажите уникальное имя пользователя.'},status=400)
 try: validate_password(password,User(username=username))
 except DjangoValidationError as e: return Response({'detail':' '.join(e.messages)},status=400)
 with transaction.atomic():
  user=User.objects.create_user(username=username,password=password); Profile.objects.create(user=user)
 return Response({'token':Token.objects.create(user=user).key,'username':user.username},status=201)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
 user=authenticate(username=request.data.get('username'),password=request.data.get('password'))
 if not user: return Response({'detail':'Неверное имя пользователя или пароль.'},status=400)
 return Response({'token':Token.objects.get_or_create(user=user)[0].key,'username':user.username,'is_staff':user.is_staff})

@api_view(['GET','PATCH'])
def profile(request):
 obj,_=Profile.objects.get_or_create(user=request.user)
 if request.method=='PATCH':
  s=ProfileSerializer(obj,data=request.data,partial=True); s.is_valid(raise_exception=True); s.save()
 return Response(ProfileSerializer(obj).data)

@api_view(['GET'])
def dashboard(request):
 p,_=Profile.objects.get_or_create(user=request.user); today=timezone.localdate()
 expenses=Expense.objects.filter(user=request.user,date__year=today.year,date__month=today.month)
 data=budget(p,expenses)
 plan=Plan.objects.filter(user=request.user).order_by('-created_at').first()
 data['plan']=PlanSerializer(plan).data if plan else None
 if data['plan']:
  prices={x.name:float(x.price) for x in Product.objects.all()}
  for item in data['plan']['shopping']:
   if not item.get('manual') and item['name'] in prices: item['price']=prices[item['name']]
  meal_total=sum(x['cost'] for x in data['plan']['meals'])
  data['meal_cost']=round(meal_total,2)
  data['food_warning']=bool(data['allocations']['Продукты']) and meal_total>float(data['allocations']['Продукты'])
 return Response(data)

@api_view(['POST'])
def create_plan(request):
 p,_=Profile.objects.get_or_create(user=request.user)
 try: meals,shopping=generate(p)
 except ValueError as e: return Response({'detail':str(e)},status=400)
 previous=Plan.objects.filter(user=request.user).order_by('-created_at').first()
 if previous: shopping.extend(x for x in previous.shopping if x.get('manual'))
 plan=Plan.objects.create(user=request.user,meals=meals,shopping=shopping)
 return Response(PlanSerializer(plan).data,status=201)

@api_view(['PATCH'])
def shopping(request,pk):
 plan=Plan.objects.filter(user=request.user,pk=pk).first()
 if not plan: return Response({'detail':'План не найден'},status=404)
 index=request.data.get('index'); checked=request.data.get('checked')
 if not isinstance(index,int) or not 0<=index<len(plan.shopping) or not isinstance(checked,bool): return Response({'detail':'Некорректные данные'},status=400)
 plan.shopping[index]['checked']=checked; plan.save(update_fields=['shopping']); return Response(PlanSerializer(plan).data)

@api_view(['POST'])
def add_shopping_item(request):
 name=str(request.data.get('name','')).strip()
 unit=str(request.data.get('unit','шт')).strip()
 category=str(request.data.get('category','Другое')).strip()
 try:
  quantity=Decimal(str(request.data.get('quantity',''))); price=Decimal(str(request.data.get('price','')))
  if not quantity.is_finite() or not price.is_finite() or not (0<quantity<=1000000) or not (0<=price<=9999999999) or quantity.as_tuple().exponent < -2 or price.as_tuple().exponent < -2: raise ValueError()
 except (InvalidOperation,ValueError,TypeError): return Response({'detail':'Укажите корректные количество и цену.'},status=400)
 if not name or len(name)>120 or not unit or len(unit)>20 or not category or len(category)>80: return Response({'detail':'Проверьте название, единицу и категорию.'},status=400)
 plan=Plan.objects.filter(user=request.user).order_by('-created_at').first()
 if not plan: plan=Plan.objects.create(user=request.user,meals=[],shopping=[])
 plan.shopping.append({'name':name,'quantity':float(quantity),'unit':unit,'category':category,'price':float(price),'checked':False,'manual':True})
 plan.save(update_fields=['shopping'])
 return Response(PlanSerializer(plan).data,status=201)

@api_view(['DELETE'])
def remove_shopping_item(request,pk,index):
 plan=Plan.objects.filter(user=request.user,pk=pk).first()
 if not plan or not 0<=index<len(plan.shopping): return Response({'detail':'Товар не найден.'},status=404)
 del plan.shopping[index]; plan.save(update_fields=['shopping'])
 return Response(status=204)

class ProductView(viewsets.ReadOnlyModelViewSet):
 queryset=Product.objects.all().order_by('category','name'); serializer_class=ProductSerializer
class ExpenseView(viewsets.ModelViewSet):
 serializer_class=ExpenseSerializer
 def get_queryset(self): return Expense.objects.filter(user=self.request.user).order_by('-date','-id')
 def perform_create(self,serializer): serializer.save(user=self.request.user)
class InventoryView(viewsets.ModelViewSet):
 serializer_class=InventorySerializer
 def get_queryset(self): return Inventory.objects.filter(user=self.request.user).order_by('name')
 def perform_create(self,serializer): serializer.save(user=self.request.user)

@api_view(['POST'])
def feedback(request):
 message=str(request.data.get('message','')).strip()
 if not message or len(message)>2000: return Response({'detail':'Сообщение должно содержать от 1 до 2000 символов.'},status=400)
 Feedback.objects.create(user=request.user,message=message); return Response({'ok':True},status=201)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def stats(request):
 return Response({'registrations':User.objects.filter(is_staff=False).count(),'plans':Plan.objects.count(),'estimated_savings':Plan.objects.aggregate(s=Sum('estimated_savings'))['s'] or 0})


@api_view(['GET'])
def korzinka_offers(request):
 from .korzinka import sync_if_due, SOURCE_URL
 snapshot=sync_if_due()
 return Response({'offers':snapshot.offers,'updated_at':snapshot.updated_at,'last_error':snapshot.last_error,'source_url':SOURCE_URL})

from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import throttle_classes
class AuditRateThrottle(UserRateThrottle):
 scope='audit'

@api_view(['POST'])
@throttle_classes([AuditRateThrottle])
def expense_audit(request):
 from .serializers import AuditRequestSerializer
 from .audit import build_summary, generate_review, AuditUnavailable
 serializer=AuditRequestSerializer(data=request.data);serializer.is_valid(raise_exception=True)
 data=serializer.validated_data
 goal={'name':data['goal_name'],'target':data['goal_target'],'saved':data['goal_saved'],'monthly':data['goal_monthly']} if data['goal_name'] else None
 summary=build_summary(request.user,goal)
 if not summary['expense_count']: return Response({'detail':'Добавьте хотя бы один расход за текущий месяц для анализа.'},status=400)
 try: review=generate_review(summary)
 except AuditUnavailable as e: return Response({'detail':str(e)},status=503)
 return Response({'summary':summary,'review':review})
