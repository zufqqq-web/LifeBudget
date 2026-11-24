import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Product, Profile
class Command(BaseCommand):
 help='Create demo catalog and demo accounts'
 def handle(self,*args,**kwargs):
  names=['Овсяные хлопья','Молоко','Яблоки','Яйца','Помидоры','Хлеб','Творог','Бананы','Рис','Курица','Морковь','Лук','Чечевица','Картофель','Макароны','Говядина','Гречка','Фасоль','Огурцы','Кефир','Йогурт','Сыр','Сливочное масло','Растительное масло','Мука','Сахар','Соль','Чай','Кофе','Свёкла','Капуста','Перец','Баклажаны','Кабачки','Тыква','Чеснок','Зелень','Лимоны','Апельсины','Мандарины','Груши','Виноград','Абрикосы','Персики','Арбуз','Дыня','Клубника','Изюм','Курага','Грецкие орехи','Арахис','Семечки','Мёд','Джем','Сметана','Сливки','Ряженка','Айран','Кукурузная крупа','Пшено','Манная крупа','Перловка','Булгур','Нут','Горох','Лаваш','Лепёшка','Сухари','Печенье','Шоколад','Томатная паста','Консервы рыбные','Тунец','Рыба','Индейка','Баранина','Фарш','Сосиски','Шампиньоны','Замороженные овощи','Кукуруза','Зелёный горошек','Уксус','Специи','Вода','Сок','Стиральный порошок','Мыло','Шампунь','Зубная паста','Туалетная бумага','Бумажные полотенца','Средство для посуды','Губки','Мусорные пакеты','Чистящее средство','Салфетки','Лампочка','Батарейки','Фольга']
  prices=[18000,12000,18000,1800,15000,8000,30000,25000,22000,45000,8000,6000,22000,7000,14000,115000,25000,24000,14000]
  for i,name in enumerate(names):
   category='Бытовые товары' if i>=86 else ('Овощи и фрукты' if i in [2,4,7,10,11,13,18] or 29<=i<=49 else 'Продукты')
   unit='шт' if name in ['Яйца','Лепёшка','Лампочка','Батарейки'] or i>=86 else ('л' if name in ['Молоко','Кефир','Растительное масло','Вода','Сок'] else 'кг')
   Product.objects.get_or_create(name=name,defaults={'category':category,'unit':unit,'price':prices[i] if i<len(prices) else 10000+(i*1379)%35000})
  for username,staff in ([('demo',False),('admin',True)] if os.environ.get('SEED_DEMO_ACCOUNTS','1') == '1' else []):
   user,created=User.objects.get_or_create(username=username,defaults={'is_staff':staff,'is_superuser':staff})
   if created: user.set_password('LifeBudget2026!'); user.save()
   Profile.objects.get_or_create(user=user)
  self.stdout.write(self.style.SUCCESS(f'Каталог: {Product.objects.count()} товаров.'))
