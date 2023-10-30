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
def Search(request):
    query=request.GET.get('query')
    product=Product.objects.filter(name__icontains=query)

    context={
        'product':product
    }
    return render(request,'search.html',context)
def Single_product(request,id):
    product=Product.objects.filter(id = id).first()
    context={
        'prod':product,
    }
    return render(request,'single_product.html',context)

def Products(request):
    categories=Categories.objects.all()
    color=Color.objects.all()
    filter_price=Filter_price.objects.all()
    brands=Brands.objects.all()
    tags=Tags.objects.all()


    CATID = request.GET.get('category')
    F_PRICEID=request.GET.get('filter_price')
    COLORID=request.GET.get('color')
    BRANDSID=request.GET.get('brands')
    ATOZID=request.GET.get('AtoZ')
    ZTOAID = request.GET.get('ZtoA')
    LOWTOHIGH=request.GET.get('lowtohigh')
    HIGHTOLOW=request.GET.get('hightolow')
    NEWID=request.GET.get('new')
    OLDID=request.GET.get('old')

    if CATID:
        product = Product.objects.filter(categories=CATID,status='Publish')
        print(CATID)
    elif F_PRICEID:
        product = Product.objects.filter(filter_price=F_PRICEID, status='Publish')
    elif COLORID:
        product = Product.objects.filter(color=COLORID, status='Publish')
    elif BRANDSID:
        product = Product.objects.filter(brand=BRANDSID, status='Publish')
    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')
    elif LOWTOHIGH:
        product = Product.objects.filter(status='Publish').order_by('price')
    elif HIGHTOLOW:
        product = Product.objects.filter(status='Publish').order_by('-price')
    elif NEWID:
        product = Product.objects.filter(condition='New',status='Publish').order_by('-id')
    elif OLDID:
        product = Product.objects.filter(condition='Old',status='Publish')



    else:
        product = Product.objects.filter(status='Publish')
        print("else")




    context = {
        'product': product,
        'categories': categories,
        'color':color,
        'filter_price':filter_price,
        'brands':brands,
        'tags':tags,
    }
    return render(request,'product.html',context)


