"""Import the public Korzinka catalogue without mapping packages to recipe units."""
import re
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation
import requests
from django.db import transaction
from django.utils import timezone
from .models import CatalogSnapshot

API_URL='https://catalog.korzinka.uz/api/catalogs/categories'
SOURCE_URL='https://www.korzinka.uz/ru/catalog/super-prices-of-the-week'
SLUG='super-prices-of-the-week'
PERIOD=re.compile(r'(\d{2}\.\d{2}\.\d{4})\s*[-–—]\s*(\d{2}\.\d{2}\.\d{4})')

def parse_offers(payload):
 if not isinstance(payload,dict) or not isinstance(payload.get('data'),list): raise ValueError('Invalid catalog response')
 matches=[x for x in payload['data'] if isinstance(x,dict) and x.get('slug')==SLUG]
 if len(matches)!=1 or not isinstance(matches[0].get('products'),list) or not matches[0]['products']: raise ValueError('Catalog category missing or empty')
 offers=[]; seen=set()
 for item in matches[0]['products']:
  if not isinstance(item,dict) or item.get('is_banner'): continue
  name=item.get('title_ru') or item.get('title'); price_data=item.get('prices') or {}; identifier=item.get('id')
  if not isinstance(name,str) or not name.strip() or not isinstance(price_data,dict) or not isinstance(identifier,int) or identifier in seen: continue
  price_text=str(price_data.get('actual_price','')).replace(' ','').replace('\u00a0','').replace('\u202f','').replace(',','.')
  try:
   price=Decimal(price_text)
   if not price.is_finite() or price<=0 or price>Decimal('9999999999') or price.as_tuple().exponent < -2: continue
  except (InvalidOperation,ValueError): continue
  valid_from=valid_to=None
  tags=item.get('promotion_tags') or []
  if isinstance(tags,list):
   for tag in tags:
    if not isinstance(tag,dict): continue
    period=PERIOD.search(str(tag.get('value','')))
    if period:
     try: valid_from=datetime.strptime(period.group(1),'%d.%m.%Y').date().isoformat(); valid_to=datetime.strptime(period.group(2),'%d.%m.%Y').date().isoformat()
     except ValueError: pass
     break
  weight=item.get('weight_param')
  offers.append({'id':identifier,'name':name.strip()[:200],'price':str(price),'unit':str(weight or 'единица товара')[:80], 'valid_from':valid_from,'valid_to':valid_to,'card_required':bool(item.get('discount_by_card')),'condition':str(price_data.get('promotion_condition') or '')[:300]})
  seen.add(identifier)
 if not offers: raise ValueError('No valid catalog prices')
 return offers[:500]

def sync_if_due(force=False):
 with transaction.atomic():
  CatalogSnapshot.objects.get_or_create(source='korzinka')
  snapshot=CatalogSnapshot.objects.select_for_update().get(source='korzinka')
  now=timezone.now()
  if not force and snapshot.last_attempt and now-snapshot.last_attempt < (timedelta(minutes=30) if snapshot.last_error else timedelta(hours=6)): return snapshot
  snapshot.last_attempt=now; snapshot.save(update_fields=['last_attempt'])
 try:
  response=requests.get(API_URL,headers={'User-Agent':'LifeBudget/1.0 (+https://lifebudget-nick.marsdot.uz)','Accept':'application/json'},timeout=(4,12),allow_redirects=False)
  response.raise_for_status()
  if response.status_code!=200 or len(response.content)>5_000_000: raise ValueError('Unexpected response')
  offers=parse_offers(response.json())
 except (requests.RequestException,ValueError,TypeError):
  CatalogSnapshot.objects.filter(pk=snapshot.pk).update(last_error=True)
 else:
  CatalogSnapshot.objects.filter(pk=snapshot.pk).update(offers=offers,updated_at=timezone.now(),last_error=False)
 snapshot.refresh_from_db()
 return snapshot
