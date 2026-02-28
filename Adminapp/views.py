from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDict, MultiValueDictKeyError

from Adminapp.models import CategoryDb,ProductDb
from webapp.models import ContactDb


# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")
def add_category(request):
    return render(request,"add_category.html")

def add_product(request):
    category=CategoryDb.objects.all()
    return render(request,"add_product.html",{'category':category})
def display_product(request):
    product=ProductDb.objects.all()
    return render(request,"view_product.html",{'product':product})
def admin_loginpage(request):
    return render(request,"admin_loginpage.html")
def admin_login(request):
    if request.method=="POST":
        uname= request.POST.get('username')
        pswd= request.POST.get('password')

        if User.objects.filter(username__contains=uname).exists():
            user= authenticate(username=uname, password=pswd)
            if user is not None:
                login(request,user)
                request.session['username'] = uname
                request.session['password'] = pswd
                return redirect(dashboard)
            else:
                print("invalid details")
                return redirect(admin_loginpage)
        else:
            print("user not found")
            return redirect(admin_loginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_loginpage)

def save_category(request):
    if request.method=="POST":
        a=request.POST.get('CategoryName')
        b=request.POST.get('Description')
        image=request.FILES.get('CategoryImage')
        obj=CategoryDb(CategoryName=a,Description=b,CategoryImage=image)
        obj.save()
        return redirect(add_category)



def display_category(request):
    category=CategoryDb.objects.all()
    return render(request,"view_category.html",{'category':category})

def edit_category(request,category_id):
    data=CategoryDb.objects.get(id=category_id)
    return render(request,"edit_category.html",{'data':data})

def delete_category(request,category_id):
    category=CategoryDb.objects.filter(id=category_id)
    category.delete()
    return redirect(display_category)

def save_products(request):
    if request.method=="POST":
        a=request.POST.get('Category_name')
        b=request.POST.get('Product_name')
        c=request.POST.get('Price')
        d=request.POST.get('Description')
        image=request.FILES.get('ProductImage')
        obj= ProductDb(Category_name=a,Product_name=b,Price=c,Description=d,ProductImage=image)
        obj.save()
        return redirect(add_product)

def edit_products(request,product_id):
    data=ProductDb.objects.get(id=product_id)
    return render(request,"edit_product.html",{'data':data})

def delete_products(request,product_id):
    product=ProductDb.objects.filter(id=product_id)
    product.delete()
    return redirect(display_product)

def contact_data(request):
    data=ContactDb.objects.all()
    return render(request,"contact_data.html",{'data':data})
