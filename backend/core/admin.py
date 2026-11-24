from django.contrib import admin
from .models import Product, Profile, Plan, Expense, Inventory, Feedback
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
 list_display=('name','category','price','city','store','source','is_demo','updated_at')
 list_filter=('category','city','is_demo')
 search_fields=('name','store')
admin.site.register([Profile,Plan,Expense,Inventory,Feedback])
