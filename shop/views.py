from django.shortcuts import render,redirect
from django.http import response,request
from .models import *

# Create your views here.
def Index(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,'index.html',context)
def Products(request):
    product = Product.objects.all(),
    categories=Categories.objects.all()
    color=Color.objects.all()
    context = {
        'product': product,
        'categories': categories,
        'color':color,
    }
    return render(request,'product.html',context)

