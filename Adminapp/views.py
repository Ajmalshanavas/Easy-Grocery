from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDict, MultiValueDictKeyError

from Adminapp.models import CategoryDb,ProductDb,ServiceDb
from webapp.models import ContactDb
from django.contrib import messages


# Create your views here.
def dashboard(request):
    categories=CategoryDb.objects.count()
    products=ProductDb.objects.count()
    return render(request,"dashboard.html",{
        'categories': categories,
        'products': products,
    })
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
        if CategoryDb.objects.filter(CategoryName__iexact=a).exists():
            messages.error(request,"Category is already added!")
            return redirect(add_category)
        obj=CategoryDb(CategoryName=a,Description=b,CategoryImage=image)
        obj.save()
        messages.success(request,"Category added successfully...!")
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
    messages.error(request,"category deleted successfully")
    return redirect(display_category)
def update_category(request, category_id):
    if request.method == "POST":
        category = CategoryDb.objects.get(id=category_id)
        category.CategoryName = request.POST.get('CategoryName')
        category.Description  = request.POST.get('Description')
        if request.FILES.get('CategoryImage'):
            category.CategoryImage = request.FILES.get('CategoryImage')
        category.save()
        messages.success(request, "Category updated successfully!")
        return redirect(display_category)

def save_products(request):
    if request.method=="POST":
        a=request.POST.get('Category_name')
        b=request.POST.get('Product_name')
        c=request.POST.get('Price')
        d=request.POST.get('Description')
        image=request.FILES.get('ProductImage')
        if ProductDb.objects.filter(Product_name__iexact=b).exists():
            messages.error(request,"Product name is already added!")
            return redirect(add_product)
        obj= ProductDb(Category_name=a,Product_name=b,Price=c,Description=d,ProductImage=image)
        obj.save()
        messages.success(request,"Product added successfully....!")
        return redirect(add_product)

def edit_products(request,product_id):
    data=ProductDb.objects.get(id=product_id)
    return render(request,"edit_product.html",{'data':data})

def delete_products(request,product_id):
    product=ProductDb.objects.filter(id=product_id)
    product.delete()
    return redirect(display_product)

def update_product(request, product_id):
    if request.method == "POST":
        product = ProductDb.objects.get(id=product_id)
        product.Category_name = request.POST.get('Category_name')
        product.Product_name  = request.POST.get('Product_name')
        product.Price         = request.POST.get('Price')
        product.Description   = request.POST.get('Description')
        if request.FILES.get('ProductImage'):
            product.ProductImage = request.FILES.get('ProductImage')
        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect(display_product)

def contact_data(request):
    data=ContactDb.objects.all()
    return render(request,"contact_data.html",{'data':data})

def add_service(request):
    return render(request, "add_service.html")

def save_service(request):
    if request.method == "POST":
        name  = request.POST.get('Service_name')
        desc  = request.POST.get('Description')
        icon  = request.POST.get('Icon')
        image = request.FILES.get('ServiceImage')
        obj   = ServiceDb(Service_name=name, Description=desc, Icon=icon, ServiceImage=image)
        obj.save()
        messages.success(request, "Service added successfully!")
        return redirect(add_service)

def view_services_admin(request):
    services = ServiceDb.objects.all()
    return render(request, "view_service.html", {'services': services})

def edit_service(request, service_id):
    data = ServiceDb.objects.get(id=service_id)
    return render(request, "edit_service.html", {'data': data})

def update_service(request, service_id):
    if request.method == "POST":
        service = ServiceDb.objects.get(id=service_id)
        service.Service_name = request.POST.get('Service_name')
        service.Description  = request.POST.get('Description')
        service.Icon         = request.POST.get('Icon')
        if request.FILES.get('ServiceImage'):
            service.ServiceImage = request.FILES.get('ServiceImage')
        service.save()
        messages.success(request, "Service updated successfully!")
        return redirect(view_services_admin)

def delete_service(request, service_id):
    ServiceDb.objects.filter(id=service_id).delete()
    messages.error(request, "Service deleted successfully.")
    return redirect(view_services_admin)
