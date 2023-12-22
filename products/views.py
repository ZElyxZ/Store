from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from products.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'products/index.html', context)

#Pray to god that this works
def products(request, cat_id = None, page = 1):

    if cat_id:
        product = Product.objects.filter(category_id = cat_id)
    else:
        product = Product.objects.all()
    per_page = 3
    paginator = Paginator(object_list=product, per_page=per_page)
    product_paginator = paginator.page(number=page)
    context = {
        'title': 'Продукты',
        'products': product_paginator,
        'category': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id = product_id)
    basket = Basket.objects.filter(user = request.user, product = product).first()
    if not basket:
        Basket.objects.create(user = request.user, product = product, quantity = 1)
    else:
        basket.quantity +=1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required()
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id = basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
