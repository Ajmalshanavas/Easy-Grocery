from django.shortcuts import render, redirect
from unicodedata import category
from webapp.models import ContactDb,RegistrationDb

from Adminapp.models import *

# Create your views here.
def home(request):
    categories=CategoryDb.objects.all()
    latest_products=ProductDb.objects.all()
    return render(request,"home.html",{'categories':categories,'latest_products':latest_products})

def about(request):
    return render(request,"About.html")

def all_products(request):
    categories=CategoryDb.objects.all()
    products=ProductDb.objects.order_by('-id')[:3]
    allproducts=ProductDb.objects.all()
    our_products=ProductDb.objects.order_by('-id')[:8]
    return render(request,"all_products.html",{'categories':categories,'products':products,'our_products':our_products,'allproducts':allproducts})

def filter_products(request,cat_name):
    products_filtered=ProductDb.objects.filter(Category_name=cat_name)
    return render(request,"filtered_products.html",{'products_filtered':products_filtered})

def single_product(request,product_id):
    single_item=ProductDb.objects.get(id=product_id)
    return render(request,"single_product.html",{'single_item':single_item})

def contact(request):
    return render(request,"contact.html")

def save_contact(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        email = request.POST.get('Email')
        message = request.POST.get('Message')
        obj=ContactDb(Name=name,Email=email,Message=message)
        obj.save()
        return redirect(contact)

def Sign_in(request):
    return render(request,"Sign_in.html")

def Sign_up(request):
    return render(request,"Sign_up.html")

def save_registration(request):
    if request.method=="POST":
        print("POST WORKING")
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        obj=RegistrationDb(username=username,email=email,password=password,password1=password1)
        if RegistrationDb.objects.filter(username=username,password=password).exists():
            print("Username already exists")
            return redirect(Sign_up)
        elif RegistrationDb.objects.filter(email=email).exists():
            print("Email already exists")
            return redirect(Sign_up)
        else:
            obj.save()
        return redirect('Sign_in')

def user_login(request):
   if request.method=="POST":
       uname=request.POST.get('username')
       pswd=request.POST.get('password')
       if RegistrationDb.objects.filter(username=uname,password=pswd).exists():
           request.session['username']=uname
           request.session['password']=pswd
           return redirect(home)
       else:
           return redirect(Sign_in)
   else:
       return redirect(Sign_in)

def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(home)

def cart(request):
    return render(request,"cart.html")

