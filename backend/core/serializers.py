from decimal import Decimal, InvalidOperation
from rest_framework import serializers
from .services import CATEGORIES
from .models import Profile, Product, Expense, Inventory, Plan
class ProfileSerializer(serializers.ModelSerializer):
 class Meta: model=Profile; exclude=['user','id']
 def validate_language(self,v):
  if v not in ('ru','uz','en'): raise serializers.ValidationError('Unsupported language.')
  return v
 def validate_currency(self,v):
  if v != 'UZS': raise serializers.ValidationError('Демо-каталог поддерживает только UZS; конвертация не настроена.')
  return v
 def validate_budget(self,v):
  if v<=0: raise serializers.ValidationError('Бюджет должен быть больше нуля.')
  return v
 def validate_mandatory(self,v):
  if v<0: raise serializers.ValidationError('Сумма не может быть отрицательной.')
  return v
 def validate_goal_target(self,v):
  if v<0: raise serializers.ValidationError('Сумма не может быть отрицательной.')
  return v
 def validate_goal_saved(self,v):
  return self.validate_goal_target(v)
 def validate_goal_monthly(self,v):
  return self.validate_goal_target(v)
 def validate_reserve(self,v):
  if v<0: raise serializers.ValidationError('Сумма не может быть отрицательной.')
  return v
 def validate_allocations(self,v):
  if not isinstance(v,dict) or any(k not in CATEGORIES for k in v): raise serializers.ValidationError('Недопустимые категории.')
  result={}
  for key,value in v.items():
   try:
    if isinstance(value,bool): raise ValueError()
    amount=Decimal(str(value))
    if not amount.is_finite() or amount<0 or amount>Decimal('999999999999.99') or amount.as_tuple().exponent < -2: raise ValueError()
   except (InvalidOperation,ValueError,TypeError): raise serializers.ValidationError('Укажите неотрицательную сумму до 999999999999.99.')
   result[key]=str(amount)
  return result
 def validate_household(self,v):
  if not 1<=v<=20: raise serializers.ValidationError('Укажите от 1 до 20 человек.')
  return v
class ProductSerializer(serializers.ModelSerializer):
 class Meta: model=Product; fields='__all__'
class ExpenseSerializer(serializers.ModelSerializer):
 class Meta: model=Expense; exclude=['user']
 def validate_amount(self,v):
  if v<=0: raise serializers.ValidationError('Сумма должна быть положительной.')
  return v
class InventorySerializer(serializers.ModelSerializer):
 class Meta: model=Inventory; exclude=['user']
class PlanSerializer(serializers.ModelSerializer):
 class Meta: model=Plan; exclude=['user']

class AuditRequestSerializer(serializers.Serializer):
 goal_name=serializers.CharField(max_length=120,required=False,allow_blank=True,default='')
 goal_target=serializers.DecimalField(max_digits=14,decimal_places=2,required=False,default=0,min_value=0)
 goal_saved=serializers.DecimalField(max_digits=14,decimal_places=2,required=False,default=0,min_value=0)
 goal_monthly=serializers.DecimalField(max_digits=14,decimal_places=2,required=False,default=0,min_value=0)
 def validate(self,attrs):
  if attrs['goal_name'] and attrs['goal_target']<=0: raise serializers.ValidationError('Для цели укажите положительную стоимость.')
  if not attrs['goal_name'] and any(attrs[k] for k in ('goal_target','goal_saved','goal_monthly')): raise serializers.ValidationError('Укажите название цели.')
  return attrs
