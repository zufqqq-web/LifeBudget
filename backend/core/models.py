from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
 user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
 country=models.CharField(max_length=80,default='Узбекистан')
 city=models.CharField(max_length=80,default='Ташкент')
 currency=models.CharField(max_length=10,default='UZS')
 budget=models.DecimalField(max_digits=14,decimal_places=2,default=5000000)
 household=models.PositiveSmallIntegerField(default=1)
 preferences=models.CharField(max_length=255,blank=True)
 allergies=models.CharField(max_length=255,blank=True)
 mandatory=models.DecimalField(max_digits=14,decimal_places=2,default=1500000)
 reserve=models.DecimalField(max_digits=14,decimal_places=2,default=0)
 allocations=models.JSONField(default=dict,blank=True)
 language=models.CharField(max_length=2,default='ru')
 goal_name=models.CharField(max_length=120,blank=True,default='')
 goal_target=models.DecimalField(max_digits=14,decimal_places=2,default=0)
 goal_saved=models.DecimalField(max_digits=14,decimal_places=2,default=0)
 goal_monthly=models.DecimalField(max_digits=14,decimal_places=2,default=0)

class Product(models.Model):
 name=models.CharField(max_length=120)
 category=models.CharField(max_length=80)
 unit=models.CharField(max_length=20,default='шт')
 price=models.DecimalField(max_digits=12,decimal_places=2)
 city=models.CharField(max_length=80,default='Ташкент')
 store=models.CharField(max_length=100,default='Демо-магазин')
 source=models.CharField(max_length=200,default='Демонстрационные данные')
 updated_at=models.DateTimeField(auto_now=True)
 is_demo=models.BooleanField(default=True)
 def __str__(self): return self.name

class Plan(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='plans')
 created_at=models.DateTimeField(auto_now_add=True)
 meals=models.JSONField(default=list)
 shopping=models.JSONField(default=list)
 estimated_savings=models.DecimalField(max_digits=12,decimal_places=2,default=0)

class Expense(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='expenses')
 title=models.CharField(max_length=120)
 category=models.CharField(max_length=80)
 amount=models.DecimalField(max_digits=12,decimal_places=2)
 date=models.DateField()

class Inventory(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='inventory')
 name=models.CharField(max_length=120)
 quantity=models.CharField(max_length=80)

class Feedback(models.Model):
 user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
 message=models.TextField(max_length=2000)
 created_at=models.DateTimeField(auto_now_add=True)

class CatalogSnapshot(models.Model):
 source=models.CharField(max_length=40,unique=True)
 offers=models.JSONField(default=list)
 last_attempt=models.DateTimeField(null=True,blank=True)
 updated_at=models.DateTimeField(null=True,blank=True)
 last_error=models.BooleanField(default=False)

class Family(models.Model):
 name=models.CharField(max_length=80)
 owner=models.ForeignKey(User,on_delete=models.PROTECT,related_name='owned_families')
 invite_code=models.CharField(max_length=64,unique=True)
 created_at=models.DateTimeField(auto_now_add=True)

class FamilyMembership(models.Model):
 user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='family_membership')
 family=models.ForeignKey(Family,on_delete=models.CASCADE,related_name='memberships')
 joined_at=models.DateTimeField(auto_now_add=True)

class SavingsGoal(models.Model):
 owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='savings_goals')
 family=models.ForeignKey(Family,on_delete=models.CASCADE,related_name='savings_goals',null=True,blank=True)
 name=models.CharField(max_length=120)
 target=models.DecimalField(max_digits=14,decimal_places=2)
 created_at=models.DateTimeField(auto_now_add=True)

class SavingsContribution(models.Model):
 goal=models.ForeignKey(SavingsGoal,on_delete=models.CASCADE,related_name='contributions')
 user=models.ForeignKey(User,on_delete=models.PROTECT,related_name='savings_contributions')
 amount=models.DecimalField(max_digits=14,decimal_places=2)
 created_at=models.DateTimeField(auto_now_add=True)
