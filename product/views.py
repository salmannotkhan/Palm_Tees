from django.shortcuts import render
from .models import Product

def index(request):
    product = Product.objects.all()
    context = {
        'products': product
    }
    return render(request, 'product/index.html', context)


def productdetail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product/detail.html', context)