export type Language = 'ru' | 'uz' | 'en';
// Russian text is the source key. User-entered names and shop descriptions stay untouched.
const rows = `
Войти|Kirish|Sign in
Обзор|Umumiy|Overview
Мой бюджет|Mening budjetim|My budget
Бюджет|Budjet|Budget
План питания|Ovqatlanish rejasi|Meal plan
Питание|Taomlar|Meals
Список покупок|Xaridlar ro‘yxati|Shopping list
Покупки|Xaridlar|Shopping
Цены|Narxlar|Prices
Обзор цен|Narxlarni ko‘rish|Price explorer
Домашние запасы|Uy zaxiralari|Home inventory
Настройки|Sozlamalar|Settings
Ваши финансы и планы в одном месте|Moliyangiz va rejalaringiz bir joyda|Your finances and plans in one place
Управляйте деньгами с уверенностью|Pulni ishonch bilan boshqaring|Manage your money with confidence
Хорошее питание начинается с плана|Yaxshi ovqatlanish rejadan boshlanadi|Good meals start with a plan
Всё необходимое на первую неделю|Birinchi hafta uchun kerakli narsalar|Everything for the first week
Каталог товаров в вашем городе|Shahringizdagi mahsulotlar katalogi|Products in your city
Используйте то, что уже есть|Bor mahsulotlardan foydalaning|Use what you already have
Ваши предпочтения и бюджет|Did va budjetingiz|Your preferences and budget
ВАШ ПЛАН НА КАЖДЫЙ ДЕНЬ|HAR KUN UCHUN REJANGIZ|YOUR PLAN FOR EVERY DAY
Больше жизни|Hayotingizga ko‘proq|More life
в вашем бюджете.|imkon bering.|in your budget.
Планируйте расходы, питание и покупки в одном месте. Понятно, спокойно и с заботой о каждом дне.|Xarajat, taom va xaridlaringizni bir joyda rejalashtiring.|Plan spending, meals and shopping in one place.
Начать планировать|Rejalashtirishni boshlash|Start planning
У меня уже есть аккаунт|Menda hisob bor|I already have an account
Ваши планы принадлежат только вам|Rejalaringiz faqat sizga tegishli|Your plans belong to you
Ваш баланс|Balansingiz|Your balance
Этот месяц|Shu oy|This month
сум|so‘m|UZS
Всё под контролем|Hammasi nazorat ostida|Everything under control
Продукты|Oziq-ovqat|Groceries
Транспорт|Transport|Transport
Связь|Aloqa|Communications
Быт|Ro‘zg‘or|Household
Другое|Boshqa|Other
Резерв|Zaxira|Reserve
Бюджет с ясностью|Aniq budjet|A clearer budget
Знайте, куда идут ваши деньги|Pul qayerga sarflanishini biling|Know where your money goes
Меню на месяц|Oylik menyu|Monthly menu
Меньше вопросов о том, что готовить|Nima pishirishni oldindan biling|Know what to cook
Покупки по плану|Rejali xaridlar|Planned shopping
Только нужное, без лишних трат|Faqat kerakli xaridlar|Buy what you need
← На главную|← Bosh sahifaga|← Home
Имя пользователя|Foydalanuvchi nomi|Username
Пароль|Parol|Password
Для начала создайте личный аккаунт.|Boshlash uchun hisob yarating.|Create an account to get started.
С возвращением|Yana xush kelibsiz|Welcome back
Начнём с главного|Asosiysidan boshlaymiz|Let’s get started
Войдите, чтобы продолжить планирование|Rejalashtirishni davom ettirish uchun kiring|Sign in to continue planning
Создайте аккаунт и настройте свой план|Hisob yarating va rejangizni sozlang|Create an account and set up your plan
Создать аккаунт|Hisob yaratish|Create account
Ещё нет аккаунта?|Hisobingiz yo‘qmi?|Don’t have an account?
Уже есть аккаунт?|Hisobingiz bormi?|Already have an account?
Зарегистрироваться|Ro‘yxatdan o‘tish|Sign up
Страна|Mamlakat|Country
Город|Shahar|City
Валюта|Valyuta|Currency
Членов семьи|Oila a’zolari|Household members
Месячный бюджет|Oylik budjet|Monthly budget
Обязательные расходы|Majburiy xarajatlar|Fixed expenses
Аллергии (через запятую)|Allergiyalar (vergul bilan)|Allergies (comma-separated)
Например, молоко, яйца|Masalan: sut, tuxum|For example, milk, eggs
Исключить продукты|Mahsulotlarni istisno qilish|Exclude ingredients
Например, курица|Masalan, tovuq|For example, chicken
Демо-каталог содержит условные цены Ташкента в UZS. Перечислите конкретные ингредиенты, которые необходимо исключить из меню.|Demo-katalogda Toshkent uchun shartli narxlar berilgan. Menyudan chiqariladigan mahsulotlarni sanang.|The demo catalog contains illustrative Tashkent prices in UZS. List ingredients to exclude from the menu.
Сохранить настройки|Sozlamalarni saqlash|Save settings
Закрыть меню|Menyuni yopish|Close menu
ЛИЧНОЕ ПРОСТРАНСТВО|SHAXSIY HUDUD|PERSONAL SPACE
Немного ясности каждый день|Har kuni ko‘proq aniqlik|A little clarity every day
Маленькие решения складываются в большие перемены.|Kichik qarorlar katta o‘zgarishlarga olib keladi.|Small decisions add up to big changes.
Личный аккаунт|Shaxsiy hisob|Personal account
Открыть меню|Menyuni ochish|Open menu
Моё пространство|Mening hududim|My space
Источники цен|Narx manbalari|Price sources
Переключить тему|Mavzuni o‘zgartirish|Toggle theme
ВАШ LIFE BUDGET|SIZNING LIFE BUDGET|YOUR LIFE BUDGET
Закрыть|Yopish|Close
Планируемый остаток|Kutilayotgan qoldiq|Projected balance
После обязательных расходов и учтённых трат|Majburiy va qayd etilgan xarajatlardan keyin|After fixed and recorded expenses
Учтено расходов|Qayd etilgan xarajatlar|Recorded expenses
Открыть бюджет|Budjetni ochish|Open budget
Финансовая подушка|Moliyaviy zaxira|Financial cushion
Резерв на непредвиденное|Kutilmagan xarajatlar zaxirasi|Emergency reserve
Сумма, которую вы выбрали|Siz tanlagan summa|The amount you chose
Изменить|O‘zgartirish|Edit
ВАШ ПЛАН|SIZNING REJANGIZ|YOUR PLAN
Распределение бюджета|Budjet taqsimoti|Budget allocation
После обязательных расходов и резерва|Majburiy xarajatlar va zaxiradan keyin|After fixed expenses and reserve
Распределено|Taqsimlangan|Allocated
ПЛАНИРУЙТЕ ЗАРАНЕЕ|OLDINDAN REJALASHTIRING|PLAN AHEAD
Питание на месяц|Oylik ovqatlanish|Meals for the month
Сбалансированное меню без лишних хлопот|Ortiqcha tashvishsiz menyu|A menu without the hassle
Ваш план готов|Rejangiz tayyor|Your plan is ready
Время составить меню|Menyu tuzish vaqti|Time to plan your meals
30 дней · 3 приёма пищи|30 kun · 3 mahal ovqat|30 days · 3 meals
Завтраки, обеды и ужины на каждый день|Har kun uchun nonushta, tushlik va kechki ovqat|Breakfast, lunch and dinner every day
Посмотреть меню|Menyuni ko‘rish|View menu
Создать план|Reja yaratish|Create plan
Создать план питания|Ovqatlanish rejasi yaratish|Create meal plan
Обновить план|Rejani yangilash|Update plan
ПОСЛЕДНИЕ ДЕЙСТВИЯ|SO‘NGGI AMALLAR|RECENT ACTIVITY
Ваши расходы|Xarajatlaringiz|Your expenses
Все расходы|Barcha xarajatlar|All expenses
Пока нет расходов. Добавьте первую покупку в разделе бюджета.|Hali xarajatlar yo‘q. Budjet bo‘limida xarajat qo‘shing.|No expenses yet. Add one in your budget.
Небольшой шаг к большой цели|Katta maqsad sari kichik qadam|A small step toward a bigger goal
Начните с плана питания — список покупок сформируется автоматически.|Ovqatlanish rejasidan boshlang — xaridlar ro‘yxati avtomatik tuziladi.|Start with a meal plan to create your shopping list.
Перейти к плану|Rejaga o‘tish|Go to plan
ВАШИ ЦИФРЫ|SIZNING RAQAMLARINGIZ|YOUR NUMBERS
План на месяц|Oylik reja|Monthly plan
Учтённые расходы|Qayd etilgan xarajatlar|Recorded expenses
Остаток|Qoldiq|Balance
Запланированные суммы превышают месячный бюджет. Измените суммы ниже.|Rejalashtirilgan summalar oylik budjetdan oshadi. Quyida ularni o‘zgartiring.|Your planned amounts exceed your monthly budget. Adjust them below.
Стоимость выбранного меню превышает сумму, выделенную на продукты. Проверьте бюджет и цены; не сокращайте приёмы пищи.|Menyu narxi oziq-ovqat uchun ajratilgan summadan oshadi. Budjet va narxlarni tekshiring; ovqatlanishni kamaytirmang.|The menu costs more than your grocery allocation. Review your budget and prices; do not skip meals.
Ваши суммы на месяц|Oylik summalaringiz|Your monthly amounts
Укажите, сколько хотите выделить на каждую категорию. Фактические расходы добавляются отдельно.|Har bir toifaga ajratiladigan summani kiriting. Haqiqiy xarajatlar alohida qo‘shiladi.|Enter an amount for each category. Actual expenses are recorded separately.
Потрачено:|Sarflangan:|Spent:
Осталось распределить|Taqsimlanmagan qoldiq|Left to allocate
Сохранить суммы|Summalarni saqlash|Save amounts
УЧЁТ РАСХОДОВ|XARAJATLAR HISOBI|EXPENSE TRACKING
Добавить расход|Xarajat qo‘shish|Add expense
Название|Nomi|Name
Например, продукты|Masalan, oziq-ovqat|For example, groceries
Сумма|Summa|Amount
Категория|Toifa|Category
Дата|Sana|Date
История расходов|Xarajatlar tarixi|Expense history
Удалить расход|Xarajatni o‘chirish|Delete expense
Ваше меню пока не создано|Menyu hali yaratilmagan|Your menu has not been created yet
Создайте план на 30 дней с завтраками, обедами и ужинами.|30 kunlik nonushta, tushlik va kechki ovqat rejasini yarating.|Create a 30-day plan with breakfast, lunch and dinner.
30 ДНЕЙ ВАШЕГО ПЛАНА|REJANGIZNING 30 KUNI|YOUR 30-DAY PLAN
Меню на каждый день|Har kunlik menyu|Daily menu
Стоимость рассчитана по демонстрационным ценам.|Narxlar demo-ma’lumotlar asosida hisoblangan.|Costs use illustrative demo prices.
Создать заново|Qayta yaratish|Generate again
День|Kun|Day
Выбрать день|Kunni tanlang|Select day
мин|daq|min
МИН|DAQ|MIN
Завтрак|Nonushta|Breakfast
Обед|Tushlik|Lunch
Ужин|Kechki ovqat|Dinner
ПЕРВАЯ НЕДЕЛЯ|BIRINCHI HAFTA|FIRST WEEK
Ваш список покупок|Xaridlar ro‘yxatingiz|Your shopping list
Количество рассчитано по меню для|Menyu bo‘yicha hisoblangan:|Calculated from the menu for
чел. Цены демонстрационные.|kishi. Narxlar shartli.|people. Prices are illustrative.
Список пуст. Добавьте товар ниже или создайте план питания.|Ro‘yxat bo‘sh. Mahsulot qo‘shing yoki ovqatlanish rejasi tuzing.|Your list is empty. Add an item or create a meal plan.
Итого за неделю|Haftalik jami|Weekly total
Добавить товар вручную|Mahsulotni qo‘lda qo‘shish|Add item manually
Количество|Miqdor|Quantity
Единица|Birlik|Unit
Цена за единицу, сум|Birlik narxi, so‘m|Price per unit, UZS
Для добавленного вручную товара сохранится указанная вами цена.|Qo‘lda qo‘shilgan mahsulot uchun kiritgan narxingiz saqlanadi.|The price you enter is saved for this item.
Добавить товар|Mahsulot qo‘shish|Add item
ПРЕДЛОЖЕНИЯ МАГАЗИНА|DO‘KON TAKLIFLARI|STORE OFFERS
Цены на товары|Mahsulot narxlari|Product prices
Акции Korzinka для Ташкента и Ташкентской области. Цена указана за размер упаковки; проверяйте условия и наличие в магазине.|Korzinka aksiyalari Toshkent shahri va viloyati uchun. Narx qadoq uchun; shartlar va mavjudlikni tekshiring.|Korzinka offers for Tashkent city and region. Prices are per package; check conditions and availability.
Найти товар|Mahsulot qidirish|Search products
Суперцены недели · Korzinka|Hafta super narxlari · Korzinka|Weekly super prices · Korzinka
Источник|Manba|Source
Не удалось обновить каталог. Показаны последние сохранённые предложения, если они есть; проверьте даты акций.|Katalogni yangilab bo‘lmadi. So‘nggi saqlangan takliflar ko‘rsatiladi; aksiya sanalarini tekshiring.|Could not refresh the catalog. The last saved offers are shown; check their dates.
· Korzinka · Ташкент и область|· Korzinka · Toshkent va viloyat|· Korzinka · Tashkent region
В список|Ro‘yxatga|Add to list
Предложения временно недоступны. Попробуйте позже или перейдите к источнику.|Takliflar vaqtincha mavjud emas. Keyinroq urinib ko‘ring yoki manbaga o‘ting.|Offers are temporarily unavailable. Try again or visit the source.
ДЕМОНСТРАЦИОННЫЕ ДАННЫЕ|DEMO MA’LUMOTLAR|DEMO DATA
Демо-каталог|Demo-katalog|Demo catalog
Цены ниже вымышлены для демонстрации и не являются рыночными. Они используются в расчёте меню.|Quyidagi narxlar shartli. Ular menyuni hisoblashda ishlatiladi.|The prices below are illustrative, not market prices. They are used to cost the menu.
ВАШ ДОМ|UYINGIZ|YOUR HOME
Отслеживайте продукты, которые уже есть дома.|Uydagi mahsulotlarni hisobga oling.|Track the food you already have.
Продукт|Mahsulot|Product
Например, 1 кг|Masalan, 1 kg|For example, 1 kg
Добавить|Qo‘shish|Add
Уже дома|Uyda bor|Already at home
Удалить|O‘chirish|Delete
Ваш список пока пуст.|Ro‘yxatingiz hozircha bo‘sh.|Your list is empty.
Открыть план питания|Ovqatlanish rejasini ochish|Open meal plan
ПЕРСОНАЛИЗАЦИЯ|SHAXSIYLASHTIRISH|PERSONALIZATION
Настройки профиля|Profil sozlamalari|Profile settings
ОБРАТНАЯ СВЯЗЬ|FIKR-MULOHAZALAR|FEEDBACK
Помогите нам стать лучше|Yaxshiroq bo‘lishimizga yordam bering|Help us improve
Расскажите, чего вам не хватает или что можно улучшить.|Nimani yaxshilash mumkinligini ayting.|Tell us what is missing or could improve.
Ваши идеи и замечания|Fikr va takliflaringiz|Your ideas and feedback
Отправить отзыв|Fikr yuborish|Send feedback
Аккаунт|Hisob|Account
Вы вошли как|Hisobingiz:|Signed in as
Панель администратора|Administrator paneli|Admin dashboard
Выйти|Chiqish|Sign out
Планируйте жизнь с уверенностью|Hayotni ishonch bilan rejalashtiring|Plan life with confidence
Цены демо-каталога условные; акции проверяйте в магазине|Demo narxlari shartli; aksiyalarni do‘konda tekshiring|Demo prices are illustrative; check offers in store
Основная навигация|Asosiy navigatsiya|Main navigation
Ещё|Yana|More
Рецепт|Retsept|Recipe
Примерная стоимость:|Taxminiy narx:|Estimated cost:
· демо-цены|· demo narxlar|· demo prices
Ингредиенты|Masalliqlar|Ingredients
Приготовление|Tayyorlanishi|Preparation
ДОБРО ПОЖАЛОВАТЬ|XUSH KELIBSIZ|WELCOME
Давайте настроим ваш план|Rejangizni sozlaymiz|Let’s set up your plan
Эти данные помогут рассчитать бюджет и подходящее меню. Их можно изменить позже.|Bu ma’lumotlar budjet va menyuni hisoblashga yordam beradi. Ularni keyin o‘zgartirish mumkin.|These details help calculate your budget and menu. You can change them later.
Здравствуйте|Salom|Hello
Язык|Til|Language
Русский|Русский|Русский
O‘zbekcha|O‘zbekcha|O‘zbekcha
English|English|English
Настройки сохранены|Sozlamalar saqlandi|Settings saved
План на 30 дней создан|30 kunlik reja yaratildi|30-day plan created
Распределение сохранено|Taqsimot saqlandi|Allocation saved
Расход добавлен|Xarajat qo‘shildi|Expense added
Товар добавлен|Mahsulot qo‘shildi|Item added
Спасибо за обратную связь!|Fikringiz uchun rahmat!|Thank you for your feedback!
`.trim().split('\n').map(line => line.split('|'));
const translations: Record<string, [string,string]> = Object.fromEntries(rows.filter(row=>row.length===3).map(([ru,uz,en])=>[ru,[uz,en]]));
export function translate(text: string, language: Language): string { return language==='ru'?text:(translations[text]?.[language==='uz'?0:1] || text); }

const recipeRows = `
Овсяная каша с яблоком|Olmali suli bo‘tqasi|Oatmeal with apple
Омлет с помидорами|Pomidorli omlet|Tomato omelette
Творог с бананом|Bananli tvorog|Cottage cheese with banana
Рис с курицей и овощами|Tovuq va sabzavotli guruch|Rice with chicken and vegetables
Чечевичный суп|Yasmiq sho‘rvasi|Lentil soup
Макароны с говядиной|Mol go‘shtli makaron|Pasta with beef
Гречка с овощами и яйцом|Sabzavot va tuxumli grechka|Buckwheat with vegetables and egg
Картофель с курицей|Tovuqli kartoshka|Chicken with potatoes
Фасоль с рисом и салатом|Guruch va salatli loviya|Beans with rice and salad
Овсянка с бананом|Bananli suli bo‘tqasi|Oatmeal with banana
Яйца с огурцом и хлебом|Bodring va non bilan tuxum|Eggs with cucumber and bread
Творог с яблоком|Olmali tvorog|Cottage cheese with apple
Пшённая каша с тыквой|Qovoqli tariq bo‘tqasi|Millet porridge with pumpkin
Гречка с молоком и бананом|Sut va bananli grechka|Buckwheat with milk and banana
Овощной суп с курицей|Tovuqli sabzavot sho‘rvasi|Chicken vegetable soup
Нут с рисом и овощами|Guruch va sabzavotli no‘xat|Chickpeas with rice and vegetables
Гречка с говядиной|Mol go‘shtli grechka|Buckwheat with beef
Макароны с курицей и помидорами|Tovuq va pomidorli makaron|Pasta with chicken and tomatoes
Чечевица с овощами и рисом|Sabzavot va guruchli yasmiq|Lentils with vegetables and rice
Овощное рагу с фасолью|Loviyali sabzavot dimlama|Vegetable and bean stew
Рис с яйцом и овощами|Tuxum va sabzavotli guruch|Rice with egg and vegetables
Запечённая рыба с картофелем|Kartoshka bilan pishirilgan baliq|Baked fish with potatoes
Тушёная капуста с курицей|Tovuqli dimlangan karam|Stewed cabbage with chicken
Гороховый суп с овощами|Sabzavotli no‘xat sho‘rvasi|Pea and vegetable soup
Сварите хлопья в молоке.|Suli yormasini sutda pishiring.|Cook the oats in milk.
Добавьте нарезанное яблоко.|To‘g‘ralgan olmani qo‘shing.|Add the sliced apple.
Нарежьте помидоры.|Pomidorlarni to‘g‘rang.|Slice the tomatoes.
Приготовьте омлет и подайте с хлебом.|Omlet tayyorlab, non bilan torting.|Cook the omelette and serve with bread.
Нарежьте банан.|Bananni to‘g‘rang.|Slice the banana.
Подавайте с творогом и хлебом.|Tvorog va non bilan torting.|Serve with cottage cheese and bread.
Отварите рис.|Guruchni pishiring.|Cook the rice.
Потушите курицу с овощами и соедините с рисом.|Tovuq va sabzavotlarni dimlab, guruchga qo‘shing.|Stew the chicken and vegetables and combine with rice.
Нарежьте овощи.|Sabzavotlarni to‘g‘rang.|Chop the vegetables.
Варите с чечевицей до готовности.|Yasmiq bilan tayyor bo‘lguncha qaynatib pishiring.|Simmer with lentils until cooked.
Отварите макароны.|Makaronni pishiring.|Cook the pasta.
Потушите мясо с овощами и подайте вместе.|Go‘shtni sabzavotlar bilan dimlab, birga torting.|Stew the meat and vegetables and serve together.
Отварите гречку и яйца.|Grechka va tuxumni pishiring.|Cook the buckwheat and eggs.
Потушите морковь и подайте вместе.|Sabzini dimlab, birga torting.|Stew the carrots and serve together.
Нарежьте ингредиенты.|Masalliqlarni to‘g‘rang.|Chop the ingredients.
Запекайте до полной готовности курицы.|Tovuq to‘liq pishguncha duxovkada pishiring.|Bake until the chicken is fully cooked.
Заранее замочите и отварите фасоль.|Loviyani avval ivitib, pishiring.|Soak the beans in advance and cook thoroughly.
Отварите рис и приготовьте салат.|Guruchni pishirib, salat tayyorlang.|Cook the rice and prepare the salad.
Добавьте нарезанный банан.|To‘g‘ralgan bananni qo‘shing.|Add the sliced banana.
Отварите яйца.|Tuxumni qaynatib pishiring.|Boil the eggs.
Нарежьте огурец и подайте с хлебом.|Bodringni to‘g‘rab, non bilan torting.|Slice the cucumber and serve with bread.
Нарежьте яблоко.|Olmani to‘g‘rang.|Slice the apple.
Промойте пшено и нарежьте тыкву.|Tariqni yuvib, qovoqni to‘g‘rang.|Rinse the millet and chop the pumpkin.
Варите с молоком до мягкости.|Sut bilan yumshaguncha pishiring.|Simmer with milk until soft.
Отварите гречку.|Grechkani pishiring.|Cook the buckwheat.
Добавьте молоко и нарезанный банан.|Sut va to‘g‘ralgan bananni qo‘shing.|Add milk and sliced banana.
Отварите курицу до готовности.|Tovuqni to‘liq pishguncha qaynatib oling.|Boil the chicken until fully cooked.
Добавьте овощи и варите до мягкости.|Sabzavotlarni qo‘shib, yumshaguncha pishiring.|Add the vegetables and simmer until soft.
Заранее замочите и отварите нут.|No‘xatni avval ivitib, pishiring.|Soak the chickpeas in advance and cook thoroughly.
Отварите рис и потушите овощи.|Guruchni pishirib, sabzavotlarni dimlang.|Cook the rice and stew the vegetables.
Потушите говядину с морковью до готовности.|Mol go‘shti va sabzini tayyor bo‘lguncha dimlang.|Stew the beef and carrots until fully cooked.
Потушите курицу с помидорами до готовности.|Tovuqni pomidor bilan to‘liq pishguncha dimlang.|Stew the chicken and tomatoes until fully cooked.
Отварите чечевицу и рис.|Yasmiq va guruchni pishiring.|Cook the lentils and rice.
Потушите морковь и соедините ингредиенты.|Sabzini dimlab, masalliqlarni qo‘shing.|Stew the carrots and combine the ingredients.
Потушите овощи и добавьте фасоль.|Sabzavotlarni dimlab, loviyani qo‘shing.|Stew the vegetables and add the beans.
Приготовьте яйца и морковь, подайте с рисом.|Tuxum va sabzini pishirib, guruch bilan torting.|Cook the eggs and carrots; serve with rice.
Запекайте рыбу с овощами до полной готовности.|Baliqni sabzavotlar bilan to‘liq pishguncha duxovkada pishiring.|Bake the fish and vegetables until fully cooked.
Нашинкуйте капусту и лук.|Karam va piyozni mayda to‘g‘rang.|Shred the cabbage and onion.
Потушите овощи с курицей до готовности.|Sabzavotlarni tovuq bilan to‘liq pishguncha dimlang.|Stew the vegetables and chicken until fully cooked.
Заранее замочите горох.|No‘xatni avval iviting.|Soak the peas in advance.
Варите горох с овощами до мягкости.|No‘xatni sabzavotlar bilan yumshaguncha pishiring.|Simmer the peas and vegetables until soft.
Овсяные хлопья|Suli yormasi|Oats
Молоко|Sut|Milk
Яблоки|Olma|Apples
Яйца|Tuxum|Eggs
Помидоры|Pomidor|Tomatoes
Хлеб|Non|Bread
Творог|Tvorog|Cottage cheese
Бананы|Banan|Bananas
Рис|Guruch|Rice
Курица|Tovuq|Chicken
Морковь|Sabzi|Carrots
Лук|Piyoz|Onions
Чечевица|Yasmiq|Lentils
Картофель|Kartoshka|Potatoes
Макароны|Makaron|Pasta
Говядина|Mol go‘shti|Beef
Гречка|Grechka|Buckwheat
Фасоль|Loviya|Beans
Огурцы|Bodring|Cucumbers
Пшено|Tariq|Millet
Тыква|Qovoq|Pumpkin
Нут|No‘xat|Chickpeas
Рыба|Baliq|Fish
Капуста|Karam|Cabbage
Горох|No‘xat|Peas
шт|dona|pcs
кг|kg|kg
л|l|L
`.trim().split('\n').map(line=>line.split('|'));
for (const [ru,uz,en] of recipeRows) translations[ru]=[uz,en];
const extraRows = `
Обновляем каталог…|Katalog yangilanmoqda…|Refreshing catalog…
Цены пока не загружены|Narxlar hali yuklanmagan|Prices have not been loaded
Получено:|Yuklangan:|Retrieved:
обновление при посещении не чаще раза в 6 часов|sahifa ochilganda 6 soatda ko‘pi bilan bir marta yangilanadi|refreshed on visits at most every 6 hours
Срок акции не указан|Aksiya muddati ko‘rsatilmagan|Offer dates not provided
акция закончилась|aksiya tugagan|offer expired
акция ещё не началась|aksiya hali boshlanmagan|offer has not started
по карте|karta bilan|loyalty card required
Товар добавлен в список покупок по сохранённой цене|Mahsulot saqlangan narxda ro‘yxatga qo‘shildi|Item added with the saved price
Куплено:|Xarid qilindi:|Purchased:
Демонстрационные данные|Demo ma’lumotlar|Demo data
Демо-магазин|Demo do‘kon|Demo store
Овощи и фрукты|Meva va sabzavotlar|Fruit and vegetables
Бытовые товары|Ro‘zg‘or buyumlari|Household goods
Ташкент|Toshkent|Tashkent
Узбекистан|O‘zbekiston|Uzbekistan
Ошибка запроса|So‘rov xatosi|Request failed
Не удалось подобрать полное меню с указанными ограничениями. Уточните аллергию или предпочтения.|Ushbu cheklovlar bilan to‘liq menyu tuzib bo‘lmadi. Allergiya yoki istaklaringizni aniqlashtiring.|A complete menu could not be created with these restrictions. Review your allergies or preferences.
`.trim().split('\n').map(line=>line.split('|'));
for (const [ru,uz,en] of extraRows) translations[ru]=[uz,en];
const auditRows = `
АНАЛИЗ РАСХОДОВ|XARAJATLAR TAHLILI|EXPENSE REVIEW
Цель и анализ расходов|Maqsad va xarajatlar tahlili|Goal and expense review
Запишите расходы за текущий месяц, добавьте цель и получите рекомендации по запросу.|Joriy oy xarajatlarini yozing, maqsad qo‘shing va tavsiyalar oling.|Record this month’s expenses, add a goal and request recommendations.
Цель|Maqsad|Goal
Например, ноутбук|Masalan, noutbuk|For example, a laptop
Стоимость цели|Maqsad narxi|Goal cost
Уже накоплено|Jamg‘arilgan summa|Already saved
Планирую откладывать в месяц|Oyiga jamg‘armoqchiman|Monthly contribution
Сохранить цель|Maqsadni saqlash|Save goal
Цель сохранена|Maqsad saqlandi|Goal saved
Для анализа во внешний сервис factory.marshub.uz будут переданы суммы бюджета, обязательных расходов и резерва, валюта, расходы за текущий месяц, категории и количество покупок, до 15 названий покупок и указанная цель. Не указывайте в названиях конфиденциальные данные.|Tahlil uchun factory.marshub.uz tashqi xizmatiga joriy oy budjeti, majburiy xarajatlar, zaxira, valyuta, xarajatlar, toifalar, xaridlar soni, 15 tagacha xarid nomi va maqsadingiz yuboriladi. Nomlarda maxfiy ma’lumot kiritmang.|For this review, factory.marshub.uz will receive your budget, fixed expenses, reserve, currency, this month’s expenses, categories, purchase counts, up to 15 purchase names and your goal. Do not put confidential information in names.
Согласен отправить эти данные для анализа|Ushbu ma’lumotlarni tahlil uchun yuborishga roziman|I agree to send this data for analysis
Анализируем…|Tahlil qilinmoqda…|Analyzing…
Проанализировать расходы|Xarajatlarni tahlil qilish|Analyze expenses
ВАШ АНАЛИЗ|SIZNING TAHLILINGIZ|YOUR REVIEW
Расходы за месяц|Oylik xarajatlar|Expenses this month
До цели осталось|Maqsadgacha qoldi|Remaining toward your goal
При выбранном взносе, месяцев|Tanlangan jamg‘arma bilan, oy|Months at your chosen contribution
Это простой расчёт по вашему взносу, не прогноз доходов и расходов.|Bu siz tanlagan jamg‘arma bo‘yicha oddiy hisob, daromad va xarajatlar prognozi emas.|This is simple arithmetic based on your contribution, not an income or spending forecast.
Рекомендации AI могут содержать ошибки и не заменяют профессиональную финансовую или медицинскую консультацию.|AI tavsiyalarida xatolar bo‘lishi mumkin; ular professional moliyaviy yoki tibbiy maslahat o‘rnini bosmaydi.|AI recommendations may contain errors and are not a substitute for professional financial or medical advice.
Добавьте хотя бы один расход за текущий месяц для анализа.|Tahlil uchun joriy oyda kamida bitta xarajat qo‘shing.|Add at least one expense for the current month to get a review.
AI-анализ пока не настроен администратором.|AI tahlili hali sozlanmagan.|AI review has not been configured yet.
Сервис AI временно недоступен. Попробуйте позже.|AI xizmati vaqtincha mavjud emas. Keyinroq qayta urinib ko‘ring.|The AI service is temporarily unavailable. Please try again later.
`.trim().split('\n').map(line=>line.split('|'));
for (const [ru,uz,en] of auditRows) translations[ru]=[uz,en];
const familyRows = `
Удалить пополнение|Qo‘shilgan summani o‘chirish|Delete contribution
Удалить запись о пополнении?|Qo‘shilgan summa yozuvi o‘chirilsinmi?|Delete this contribution record?
Запись удалена|Yozuv o‘chirildi|Record deleted
Семья|Oila|Family
Копилка|Jamg‘arma|Savings
Семейное пространство и приглашения|Oila va takliflar|Family space and invitations
Личные и семейные цели накоплений|Shaxsiy va oilaviy jamg‘arma maqsadlari|Personal and family savings goals
Загрузка…|Yuklanmoqda…|Loading…
СЕМЕЙНОЕ ПРОСТРАНСТВО|OILAVIY HUDUD|FAMILY SPACE
Вместе планируйте общие накопления. Личные расходы и личные копилки остаются приватными.|Umumiy jamg‘armani birga rejalashtiring. Shaxsiy xarajatlar va jamg‘armalar maxfiy qoladi.|Plan shared savings together. Personal expenses and savings remain private.
Участники семьи|Oila a’zolari|Family members
Создатель|Yaratuvchi|Owner
Участник|A’zo|Member
Пригласить участника|A’zoni taklif qilish|Invite a member
Передайте код лично тому, кого приглашаете. Любой, у кого есть код, сможет присоединиться и видеть семейные копилки.|Kodni faqat taklif qilmoqchi bo‘lgan kishiga bering. Kod egasi oilaga qo‘shilib, umumiy jamg‘armalarni ko‘ra oladi.|Share this code privately with the person you invite. Anyone with the code can join and see family savings.
Скопировать код|Kodni nusxalash|Copy code
Код скопирован|Kod nusxalandi|Code copied
Обновить код|Kodni yangilash|Rotate code
Старый код больше не действует|Eski kod endi ishlamaydi|The old code is no longer valid
Выйти из семьи|Oiladan chiqish|Leave family
Вы вышли из семьи|Siz oiladan chiqdingiz|You left the family
СЕМЬЯ|OILA|FAMILY
Создать семью|Oila yaratish|Create a family
Пригласите близких и копите вместе на общую цель.|Yaqinlaringizni taklif qiling va birga jamg‘aring.|Invite your family and save toward a shared goal.
Название семьи|Oila nomi|Family name
ПРИГЛАШЕНИЕ|TAKLIF|INVITATION
Присоединиться к семье|Oilaga qo‘shilish|Join a family
Введите код, полученный от создателя семьи.|Oila yaratuvchisi bergan kodni kiriting.|Enter the code provided by the family owner.
Код приглашения|Taklif kodi|Invitation code
Присоединиться|Qo‘shilish|Join
ВАШИ НАКОПЛЕНИЯ|JAMG‘ARMALARINGIZ|YOUR SAVINGS
Следите за личными и семейными целями. Это учёт записей, деньги не переводятся автоматически.|Shaxsiy va oilaviy maqsadlarni kuzating. Bu hisob yuritish, pul avtomatik o‘tkazilmaydi.|Track personal and family goals. Entries are records; no money is transferred automatically.
ЦЕЛЬ ИЗ БЮДЖЕТА|BUDJETDAGI MAQSAD|GOAL FROM YOUR BUDGET
Эта цель сохранена в разделе бюджета и учитывается отдельно от копилок ниже.|Bu maqsad budjetda saqlangan va quyidagi jamg‘armalardan alohida hisoblanadi.|This goal is saved in your budget and tracked separately from the savings goals below.
НОВАЯ ЦЕЛЬ|YANGI MAQSAD|NEW GOAL
Создать копилку|Jamg‘arma yaratish|Create a savings goal
Название цели|Maqsad nomi|Goal name
Сколько нужно накопить|Qancha jamg‘arish kerak|Target amount
Кому видна копилка|Jamg‘armani kim ko‘radi|Who can see this goal
Только мне|Faqat men|Only me
Моей семье|Oilam|My family
Чтобы создать общую копилку, сначала создайте семью или присоединитесь к ней.|Umumiy jamg‘arma yaratish uchun avval oila yarating yoki oilaga qo‘shiling.|Create or join a family first to create a shared goal.
Копилка создана|Jamg‘arma yaratildi|Savings goal created
СЕМЕЙНАЯ КОПИЛКА|OILAVIY JAMG‘ARMA|FAMILY SAVINGS
ЛИЧНАЯ КОПИЛКА|SHAXSIY JAMG‘ARMA|PERSONAL SAVINGS
Осталось накопить|Yana jamg‘arish kerak|Left to save
Сумма пополнения|Qo‘shiladigan summa|Contribution amount
Пополнить|Qo‘shish|Add contribution
Пополнение записано|Qo‘shilgan summa qayd etildi|Contribution recorded
История пополнений|Qo‘shilgan summalar tarixi|Contribution history
Пока нет копилок|Jamg‘armalar hali yo‘q|No savings goals yet
Создайте первую цель и отмечайте свои пополнения.|Birinchi maqsadni yarating va jamg‘armalaringizni qayd eting.|Create your first goal and record contributions.
`.trim().split('\n').map(line=>line.split('|'));
for (const [ru,uz,en] of familyRows) translations[ru]=[uz,en];
const landingRows = `
ДЕНЬГИ ДЛЯ ЖИЗНИ|HAYOT UCHUN MABLAG‘|MONEY FOR LIFE
Планируйте деньги.|Pulni rejalashtiring.|Plan your money.
Живите спокойнее.|Xotirjam yashang.|Live with more ease.
LifeBudget помогает понять, куда уходят деньги, спланировать покупки и постепенно приблизиться к важным целям.|LifeBudget pulingiz qayerga ketayotganini tushunishga, xaridlarni rejalashtirishga va muhim maqsadlarga yaqinlashishga yordam beradi.|LifeBudget helps you understand where your money goes, plan purchases and make progress toward what matters.
Создать свой план|O‘z rejangizni yarating|Create your plan
Как это работает|Bu qanday ishlaydi|How it works
Для студентов, специалистов и семей|Talabalar, mutaxassislar va oilalar uchun|For students, professionals and families
Пример интерфейса LifeBudget|LifeBudget interfeysi namunasi|LifeBudget interface example
ПРИМЕР|NAMUNA|EXAMPLE
Осталось в этом месяце|Bu oy qolgan mablag‘|Left this month
После записанных расходов|Qayd etilgan xarajatlardan so‘ng|After recorded expenses
Запланировано|Rejalashtirilgan|Planned
Цель накопления|Jamg‘arma maqsadi|Savings goal
Новый ноутбук|Yangi noutbuk|A new laptop
ОДИН ПЛАН НА КАЖДЫЙ ДЕНЬ|HAR KUN UCHUN BITTA REJA|ONE PLAN FOR EVERY DAY
Бюджет — это не только цифры.|Budjet — bu shunchaki raqamlar emas.|A budget is about more than numbers.
От продуктов на неделю до общей мечты семьи: соберите повседневные решения в одном месте и принимайте их увереннее.|Haftalik mahsulotlardan oilaning umumiy orzusigacha: kundalik qarorlaringizni bir joyda jamlang.|From weekly groceries to a shared family goal, bring everyday decisions together and make them with confidence.
Возможности LifeBudget|LifeBudget imkoniyatlari|LifeBudget features
Видьте картину целиком|Hammasini bir joyda ko‘ring|See the whole picture
Укажите доход и сами распределите бюджет. Записывайте расходы, чтобы видеть, сколько осталось.|Daromadingizni kiriting va budjetni o‘zingiz taqsimlang. Qoldiqni ko‘rish uchun xarajatlarni qayd eting.|Enter your income and allocate your budget yourself. Record expenses to see what remains.
Ваш бюджет|Sizning budjetingiz|Your budget
Вы решаете, куда направить деньги|Mablag‘ni qayerga yo‘naltirishni o‘zingiz hal qilasiz|You decide where your money goes
Меньше думайте о покупках|Xaridlar haqida kamroq bosh qotiring|Take the guesswork out of shopping
Составьте меню на месяц, откройте рецепты и соберите список покупок. Добавляйте свои товары и цены.|Oylik menyu tuzing, retseptlarni ko‘ring va xaridlar ro‘yxatini yarating. O‘z mahsulotlaringiz va narxlaringizni qo‘shing.|Make a monthly menu, explore recipes and build a shopping list. Add your own items and prices.
Меню и список на неделю|Menyu va haftalik ro‘yxat|A menu and weekly list
Копите вместе или для себя|Birga yoki o‘zingiz uchun jamg‘aring|Save together or on your own
Создавайте личные копилки или приглашайте близких к общей цели. Отмечайте взносы и следите за прогрессом.|Shaxsiy jamg‘armalar yarating yoki yaqinlaringizni umumiy maqsadga taklif qiling. Badallarni va natijani kuzating.|Create personal savings goals or invite family to a shared one. Record contributions and follow your progress.
Личные и семейные цели|Shaxsiy va oilaviy maqsadlar|Personal and family goals
ПРОСТО НАЧАТЬ|BOSHLASH OSON|EASY TO GET STARTED
Три шага к вашему плану|Rejangizga uch qadam|Three steps to your plan
Настройте бюджет|Budjetni sozlang|Set your budget
Укажите доход, обязательные расходы и суммы по категориям.|Daromad, majburiy xarajatlar va toifalar bo‘yicha summalarni kiriting.|Enter your income, fixed expenses and category amounts.
Планируйте и записывайте|Rejalashtiring va qayd eting|Plan and record
Добавляйте расходы и покупки, создавайте меню и списки.|Xarid va xarajatlarni qo‘shing, menyu va ro‘yxatlar yarating.|Add expenses and purchases, and create menus and lists.
Двигайтесь к целям|Maqsadlar sari yuring|Move toward your goals
Откладывайте на важное и отмечайте прогресс в копилке.|Muhim narsalar uchun jamg‘aring va natijangizni kuzatib boring.|Set money aside for what matters and record your progress.
Понятно, откуда берутся цены|Narxlarning manbasi aniq|Know where prices come from
В каталоге есть акции Korzinka для Ташкента и области. Цены для расчёта меню пока демонстрационные — они отмечены в приложении.|Katalogda Toshkent shahri va viloyati uchun Korzinka aksiyalari bor. Menyu hisobidagi narxlar hozircha namunaviy va ilovada belgilangan.|The catalog includes Korzinka offers for Tashkent city and region. Menu calculations currently use clearly marked demo prices.
Копилка помогает вести учёт: реальные деньги приложение не хранит и не переводит.|Jamg‘arma hisob yuritishga yordam beradi: ilova pul saqlamaydi va o‘tkazmaydi.|Savings goals are for tracking: the app does not hold or transfer real money.
Начать бесплатно|Bepul boshlash|Get started free
`.trim().split('\n').map(line=>line.split('|'));
for (const [ru,uz,en] of landingRows) translations[ru]=[uz,en];
