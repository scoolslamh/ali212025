from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← هذا هو التصحيح المطلوب
    path('products/', views.product_list, name='product_list'),
]
