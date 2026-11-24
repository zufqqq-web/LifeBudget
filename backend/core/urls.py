from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, family_views
router=DefaultRouter()
router.register('products',views.ProductView,basename='products')
router.register('expenses',views.ExpenseView,basename='expenses')
router.register('inventory',views.InventoryView,basename='inventory')
urlpatterns=[path('register/',views.register),path('login/',views.login),path('profile/',views.profile),path('family/',family_views.family_view),path('family/join/',family_views.join_family),path('family/invite/rotate/',family_views.rotate_invite),path('family/leave/',family_views.leave_family),path('savings/',family_views.savings_goals),path('savings/<int:pk>/contributions/',family_views.contribute),path('savings/<int:pk>/contributions/<int:contribution_id>/',family_views.delete_contribution),path('dashboard/',views.dashboard),path('plans/generate/',views.create_plan),path('plans/<int:pk>/shopping/',views.shopping),path('shopping/items/',views.add_shopping_item),path('plans/<int:pk>/shopping/<int:index>/',views.remove_shopping_item),path('feedback/',views.feedback),path('stats/',views.stats),path('korzinka/',views.korzinka_offers),path('expense-audit/',views.expense_audit),path('',include(router.urls))]
