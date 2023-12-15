from django.shortcuts import render,redirect
from django.http import response,request
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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


def HandelRegister(request):
    if request.method=="POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        customer=User.objects.create_user(username,email,pass1)
        customer.first_name=first_name
        customer.last_name=last_name
        customer.save()
        return redirect("shop:Register")
    return render(request,'registration/auth.html')
def HandelLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password=  request.POST.get('password')
        user=authenticate(username=username,password=password)
        # print(username,password)
        if user is not None:
            login(request,user)
            return redirect('shop:index')
        else:
            return redirect('shop:Login')
    return render(request,'registration/auth.html')
def HandelLogout(request):
    logout(request)
    redirect('shop:index')
    return render(request, 'registration/auth.html')