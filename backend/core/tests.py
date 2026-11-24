from decimal import Decimal
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.management import call_command
from rest_framework.test import APIClient
from .models import Profile,Expense,Product
from .services import budget,generate
class PlanningTests(TestCase):
 @classmethod
 def setUpTestData(cls):
  call_command('seed',verbosity=0)
  cls.user=User.objects.get(username='demo')
 def test_budget_and_warning(self):
  p=self.user.profile; p.budget=Decimal('1000');p.mandatory=Decimal('950');p.reserve=Decimal('100');p.allocations={'Транспорт':'200'}
  result=budget(p,[])
  self.assertTrue(result['warning']);self.assertEqual(result['reserve'],Decimal('100'));self.assertEqual(result['allocations']['Транспорт'],200);self.assertEqual(result['unallocated'],Decimal('-250'))
 def test_complete_meals_shopping_and_allergies(self):
  p=self.user.profile;p.allergies='молоко'
  meals,shopping=generate(p)
  self.assertEqual(len(meals),90)
  self.assertEqual(len({(x['day'],x['kind']) for x in meals}),90)
  self.assertFalse(any(i['name']=='Молоко' for m in meals for i in m['ingredients']))
  self.assertTrue(shopping)
 def test_api_isolation_and_validation(self):
  client=APIClient();client.force_authenticate(self.user)
  self.assertEqual(client.post('/api/expenses/',{'title':'x','category':'Быт','amount':-1,'date':'2026-01-01'}).status_code,400)
  self.assertEqual(client.post('/api/plans/generate/').status_code,201)
  other=User.objects.create_user('other',password='safe-password-123');client.force_authenticate(other)
  self.assertIsNone(client.get('/api/dashboard/').data['plan'])
 def test_registration_password_validation(self):
  client=APIClient();self.assertEqual(client.post('/api/register/',{'username':'newuser','password':'123'}).status_code,400)
  self.assertEqual(client.post('/api/register/',{'username':'newuser','password':'valid-password-123','language':'uz'},format='json').status_code,201)
  self.assertEqual(User.objects.get(username='newuser').profile.language,'uz')

 def test_manual_allocations_and_shopping(self):
  client=APIClient();client.force_authenticate(self.user)
  response=client.patch('/api/profile/',{'reserve':'100','allocations':{'Транспорт':'200','Продукты':'300'}},format='json')
  self.assertEqual(response.status_code,200)
  self.assertEqual(client.patch('/api/profile/',{'allocations':{'Транспорт':'-1'}},format='json').status_code,400)
  self.assertEqual(client.patch('/api/profile/',{'allocations':{'Транспорт':'NaN'}},format='json').status_code,400)
  dashboard=client.get('/api/dashboard/').data
  self.assertEqual(dashboard['allocations']['Транспорт'],Decimal('200'))
  response=client.post('/api/shopping/items/',{'name':'Чай','quantity':'2','unit':'шт','price':'123','category':'Продукты'},format='json')
  self.assertEqual(response.status_code,201)
  plan_id=response.data['id']
  self.assertEqual(response.data['shopping'][0]['price'],123)
  self.assertEqual(client.post('/api/plans/generate/').data['shopping'][-1]['name'],'Чай')
  other=User.objects.create_user('another',password='strong-pass-123')
  client.force_authenticate(other)
  self.assertEqual(client.delete(f'/api/plans/{plan_id}/shopping/0/').status_code,404)
  self.assertEqual(client.get('/api/assistant/').status_code,404)

class KorzinkaTests(TestCase):
 def setUp(self):
  self.user=User.objects.create_user('cataloguser',password='safe-password-123')
  self.client=APIClient();self.client.force_authenticate(self.user)
 def payload(self):
  return {'data':[{'slug':'super-prices-of-the-week','products':[{'id':123,'title_ru':'Макароны 400 г','weight_param':'400 г','prices':{'actual_price':'7 990'},'promotion_tags':[{'value':'19.11.2026-25.11.2026'}]}]}]}
 def test_parse_package_and_period(self):
  from .korzinka import parse_offers
  offer=parse_offers(self.payload())[0]
  self.assertEqual(offer['price'],'7990');self.assertEqual(offer['unit'],'400 г');self.assertEqual(offer['valid_to'],'2026-11-25')
 def test_refresh_and_upstream_failure_preserves_last_result(self):
  from unittest.mock import patch, Mock
  from .models import CatalogSnapshot
  import requests
  response=Mock(status_code=200,content=b'valid');response.json.return_value=self.payload()
  with patch('core.korzinka.requests.get',return_value=response):
   result=self.client.get('/api/korzinka/')
   self.assertEqual(result.status_code,200);self.assertEqual(result.data['offers'][0]['name'],'Макароны 400 г')
  CatalogSnapshot.objects.filter(source='korzinka').update(last_attempt=None)
  with patch('core.korzinka.requests.get',side_effect=requests.Timeout):
   result=self.client.get('/api/korzinka/')
   self.assertTrue(result.data['last_error']);self.assertEqual(result.data['offers'][0]['price'],'7990')
 def test_invalid_catalog_does_not_delete_cached_offers(self):
  from unittest.mock import patch, Mock
  from .models import CatalogSnapshot
  CatalogSnapshot.objects.create(source='korzinka',offers=[{'id':1,'name':'Старый'}])
  response=Mock(status_code=200,content=b'{}');response.json.return_value={'data':[]}
  with patch('core.korzinka.requests.get',return_value=response):
   result=self.client.get('/api/korzinka/')
  self.assertTrue(result.data['last_error']);self.assertEqual(result.data['offers'][0]['name'],'Старый')

class MealLanguageTests(TestCase):
 @classmethod
 def setUpTestData(cls):
  call_command('seed',verbosity=0)
  cls.user=User.objects.get(username='demo')
 def test_variety_and_english_uzbek_allergens(self):
  profile=self.user.profile
  meals,_=generate(profile)
  self.assertGreaterEqual(len({x['name'] for x in meals}),24)
  for allergy in ['milk','sut','eggs','tuxum']:
   profile.allergies=allergy
   meals,_=generate(profile)
   forbidden={'Молоко','Творог'} if allergy in ('milk','sut') else {'Яйца'}
   self.assertFalse(any(item['name'] in forbidden for meal in meals for item in meal['ingredients']))
 def test_unknown_allergen_fails_closed(self):
  self.user.profile.allergies='unknown-allergen'
  with self.assertRaises(ValueError): generate(self.user.profile)
 def test_language_is_saved_and_validated(self):
  client=APIClient();client.force_authenticate(self.user)
  self.assertEqual(client.patch('/api/profile/',{'language':'uz'},format='json').status_code,200)
  self.assertEqual(client.get('/api/profile/').data['language'],'uz')
  self.assertEqual(client.patch('/api/profile/',{'language':'de'},format='json').status_code,400)

class ExpenseAuditTests(TestCase):
 def setUp(self):
  from django.utils import timezone
  self.user=User.objects.create_user('reviewuser',password='safe-password-123')
  Profile.objects.create(user=self.user,budget=Decimal('5000000'),mandatory=Decimal('1000000'),reserve=Decimal('500000'))
  self.client=APIClient();self.client.force_authenticate(self.user)
  self.today=timezone.localdate()
 def test_calculation_excludes_other_users_and_other_months(self):
  from .audit import build_summary
  from datetime import timedelta
  Expense.objects.create(user=self.user,title='Pepsi',category='Продукты',amount=Decimal('7000'),date=self.today)
  other=User.objects.create_user('someone',password='safe-password-123')
  Expense.objects.create(user=other,title='Private',category='Другое',amount=Decimal('900000'),date=self.today)
  old=self.today.replace(day=1)-timedelta(days=1)
  Expense.objects.create(user=self.user,title='Old',category='Другое',amount=Decimal('800000'),date=old)
  goal={'name':'Laptop','target':Decimal('12000000'),'saved':Decimal('2000000'),'monthly':Decimal('1000000')}
  data=build_summary(self.user,goal)
  self.assertEqual(data['recorded_expenses'],'7000.00');self.assertEqual(data['goal']['months_at_contribution'],10)
  self.assertEqual([x['name'] for x in data['top_items']],['Pepsi']);self.assertNotIn('username',data)
 def test_requires_expenses_and_validates_goal(self):
  self.assertEqual(self.client.post('/api/expense-audit/',{},format='json').status_code,400)
  self.assertEqual(self.client.post('/api/expense-audit/',{'goal_name':'Laptop','goal_target':'-1'},format='json').status_code,400)
 def test_unconfigured_and_provider_failure_report_unavailable(self):
  from unittest.mock import patch
  import requests
  Expense.objects.create(user=self.user,title='Tea',category='Продукты',amount=1000,date=self.today)
  with patch.dict('os.environ',{'AI_API_KEY':'','AI_BASE_URL':'','AI_MODEL':''}):
   self.assertEqual(self.client.post('/api/expense-audit/',{},format='json').status_code,503)
  with patch.dict('os.environ',{'AI_API_KEY':'not-real','AI_BASE_URL':'https://example.test/v1','AI_MODEL':'fake'}),patch('core.audit.requests.post',side_effect=requests.Timeout):
   self.assertEqual(self.client.post('/api/expense-audit/',{},format='json').status_code,503)

class FamilySavingsTests(TestCase):
 def setUp(self):
  from django.core.cache import cache
  cache.clear()
  self.owner=User.objects.create_user('owner',password='password-12345')
  self.member=User.objects.create_user('member',password='password-12345')
  self.outsider=User.objects.create_user('outsider',password='password-12345')
  self.client=APIClient();self.client.force_authenticate(self.owner)
 def test_family_goal_privacy_and_contributions(self):
  response=self.client.post('/api/family/',{'name':'Семья'},format='json');self.assertEqual(response.status_code,201)
  code=response.data['family']['invite_code']
  personal=self.client.post('/api/savings/',{'name':'Личный','target':'1000','scope':'personal'},format='json').data
  shared=self.client.post('/api/savings/',{'name':'Общий','target':'10000','scope':'family'},format='json').data
  self.client.force_authenticate(self.member)
  self.assertEqual(self.client.post('/api/family/join/',{'code':code},format='json').status_code,200)
  self.assertIsNone(self.client.get('/api/family/').data['family']['invite_code'])
  self.assertEqual([g['id'] for g in self.client.get('/api/savings/').data],[shared['id']])
  self.assertEqual(self.client.post(f"/api/savings/{personal['id']}/contributions/",{'amount':'100'},format='json').status_code,404)
  response=self.client.post(f"/api/savings/{shared['id']}/contributions/",{'amount':'2500'},format='json')
  self.assertEqual(response.status_code,201);self.assertEqual(response.data['saved'],'2500.00');self.assertEqual(response.data['remaining'],'7500.00')
  contribution_id=response.data['contributions'][0]['id']
  self.client.force_authenticate(self.owner)
  self.assertEqual(self.client.delete(f"/api/savings/{shared['id']}/contributions/{contribution_id}/").status_code,404)
  self.client.force_authenticate(self.member)
  self.assertEqual(self.client.delete(f"/api/savings/{shared['id']}/contributions/{contribution_id}/").status_code,204)
  self.assertEqual(self.client.get('/api/savings/').data[0]['saved'],'0')
  self.client.force_authenticate(self.outsider)
  self.assertEqual(self.client.get('/api/savings/').data,[])
  self.assertEqual(self.client.post(f"/api/savings/{shared['id']}/contributions/",{'amount':'100'},format='json').status_code,404)
 def test_invite_rotation_and_leaving(self):
  code=self.client.post('/api/family/',{'name':'Дом'},format='json').data['family']['invite_code']
  new=self.client.post('/api/family/invite/rotate/',{},format='json').data['family']['invite_code'];self.assertNotEqual(code,new)
  self.client.force_authenticate(self.member)
  self.assertEqual(self.client.post('/api/family/join/',{'code':code},format='json').status_code,404)
  self.assertEqual(self.client.post('/api/family/join/',{'code':new},format='json').status_code,200)
  self.assertEqual(self.client.post('/api/family/invite/rotate/',{},format='json').status_code,403)
  self.assertEqual(self.client.post('/api/family/leave/',{},format='json').status_code,204)
 def test_invalid_contributions_are_rejected(self):
  goal=self.client.post('/api/savings/',{'name':'Цель','target':'1000','scope':'personal'},format='json').data
  for amount in ['0','-1','NaN']:
   self.assertEqual(self.client.post(f"/api/savings/{goal['id']}/contributions/",{'amount':amount},format='json').status_code,400)
  self.assertEqual(self.client.post('/api/savings/',{'name':'Общая','target':'1000','scope':'family'},format='json').status_code,400)
