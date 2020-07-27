from django.shortcuts import render
from account.models import User
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


def cart(request):
    user = request.user

    if request.method == 'POST':
        id = request.POST['product_id']
        product = Product.objects.get(id=id)
        user.cart.add(product)
        user.save()

    product = user.cart.all()
    context = {
        'products': product,
    }
    return render(request, 'product/cart.html', context)