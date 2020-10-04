from django.shortcuts import render, redirect
from account.models import User
from django.contrib import messages
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
        if user.is_authenticated:
            id = request.POST['product_id']
            product = Product.objects.get(id=id)
            user.cart.add(product)
            user.save()
        else:
            return redirect('login')

    product = user.cart.all()
    context = {
        'products': product,
    }
    return render(request, 'product/cart.html', context)


def removeitem(request):
    if request.method == 'POST':
        user = request.user
        id = request.POST['id']
        product = Product.objects.get(id=id)
        user.cart.remove(product)
        user.save()
        
    return redirect('cart')


def checkout(request):
    return render(request, 'product/checkout.html', context)