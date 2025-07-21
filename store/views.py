from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'store/product_list.html', {'products': products})

def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:6]
    return render(request, 'home.html', {'latest_products': latest_products})
