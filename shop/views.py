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


