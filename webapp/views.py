from django.shortcuts import render, redirect
from unicodedata import category
from webapp.models import ContactDb, RegistrationDb, CartDb,OrderDb
from django.contrib import messages
from Adminapp.models import *

# Create your views here.
def home(request):
    categories = CategoryDb.objects.all()
    latest_products = ProductDb.objects.all()
    uname = request.session.get('username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Username=uname).count()
    return render(request, "home.html", {
        'categories': categories,
        'latest_products': latest_products,
        'cart_count': cart_count
    })
def about(request):
    categories = CategoryDb.objects.all()
    latest_products = ProductDb.objects.all()
    uname = request.session.get('username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Username=uname).count()
    return render(request,"About.html",{'categories': categories,'latest_products': latest_products,'cart_count':cart_count})

def all_products(request):
    categories=CategoryDb.objects.all()
    products=ProductDb.objects.order_by('-id')[:3]
    allproducts=ProductDb.objects.all()
    our_products=ProductDb.objects.order_by('-id')[:8]

    return render(request,"all_products.html",{'categories':categories,'products':products,'our_products':our_products,'allproducts':allproducts})

def filter_products(request,cat_name):
    categories = CategoryDb.objects.all()
    latest_products = ProductDb.objects.all()
    products_filtered=ProductDb.objects.filter(Category_name=cat_name)
    products1 = ProductDb.objects.order_by('-id')[:3]
    our_products = ProductDb.objects.order_by('-id')[:8]
    uname = request.session.get('username')  # lowercase
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Username=uname).count()
    return render(request,"filtered_products.html",{'products_filtered':products_filtered,'categories':categories,'latest_products':latest_products,'cart_count':cart_count,'products1':products1,'our_products':our_products})

def single_product(request,product_id):
    categories = CategoryDb.objects.all()
    latest_products = ProductDb.objects.all()
    single_item=ProductDb.objects.get(id=product_id)
    uname = request.session.get('username')  # lowercase
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Username=uname).count()
    return render(request,"single_product.html",{'single_item':single_item,'categories':categories,'latest_products':latest_products,'cart_count':cart_count})

def contact(request):
    categories = CategoryDb.objects.all()
    latest_products = ProductDb.objects.all()
    uname = request.session.get('username')  # lowercase
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Username=uname).count()
    return render(request,"contact.html",{'categories': categories,'latest_products':latest_products,'cart_count':cart_count})

def save_contact(request):
    if request.method == "POST":
        name    = request.POST.get('Name')
        email   = request.POST.get('Email')
        message = request.POST.get('Message')

        # Check if this email has already submitted a message
        if ContactDb.objects.filter(Email=email).exists():
            messages.error(request, "This email address has already been used to send a message.")
            return redirect(contact)

        obj = ContactDb(Name=name, Email=email, Message=message)
        obj.save()
        messages.success(request, "Message sent successfully! We will get back to you soon.")
        return redirect(contact)

def Sign_in(request):
    return render(request,"Sign_in.html")

def Sign_up(request):
    return render(request,"Sign_up.html")

def save_registration(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password1 = request.POST.get('password1', '')

        # Validate passwords match
        if password != password1:
            messages.error(request, "Passwords do not match.")
            return redirect('Sign_up')

        # Validate password length
        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters.")
            return redirect('Sign_up')

        # Check if username already exists
        if RegistrationDb.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return redirect('Sign_up')

        # Check if email already exists
        if RegistrationDb.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('Sign_up')

        # Save the new user
        obj = RegistrationDb(username=username, email=email, password=password, password1=password1)
        obj.save()
        messages.success(request, "Account created successfully! Please sign in.")
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

    request.session.pop('username', None)
    request.session.pop('password', None)
    return redirect(home)

def services(request):
    from Adminapp.models import ServiceDb
    services    = ServiceDb.objects.all()
    categories  = CategoryDb.objects.all()
    uname       = request.session.get('username')
    cart_count  = 0
    if uname:
        cart_count = CartDb.objects.filter(Username=uname).count()
    return render(request, "services.html", {
        'services'   : services,
        'categories' : categories,
        'cart_count' : cart_count,
    })

def cart(request):
    categories = CategoryDb.objects.all()
    latest_products = ProductDb.objects.all()
    uname = request.session.get('username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Username=uname).count()
    data=CartDb.objects.filter(Username=request.session['username'])
    sub_total=0
    delivery=0
    grand_total=0
    user_data=CartDb.objects.filter(Username=request.session['username'])
    for i in data:
        sub_total+=i.Totalprice
        if sub_total>1000:
            delivery=0
        elif sub_total>500:
            delivery=50
        else:
            delivery=100
        grand_total=sub_total + delivery
    uname = request.session.get('username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Username=uname).count()
        return render(request,"cart.html",{
        'data':data,
        'sub_total':sub_total,
        'delivery':delivery,
        'grand_total':grand_total,
      'cart_count':cart_count,'categories':categories,'latest_products':latest_products})

def add_to_cart(request):
    if request.method == "POST":
        uname = request.session.get('username')
        product = request.POST.get('Product_name')
        price = request.POST.get('Price')
        total = request.POST.get('Totalprice')
        quantity = request.POST.get('Quantity')
        pro = ProductDb.objects.filter(Product_name=product).first()
        img = pro.ProductImage if pro else None
        obj = CartDb(Username=uname, Product_name=product, Price=price, Totalprice=total, Quantity=quantity, Product_image=img)
        obj.save()
        return redirect(cart)


def checkout(request):
    uname = request.session.get('username')
    cart_data = CartDb.objects.filter(Username=uname)

    sub_total = 0
    for item in cart_data:
        sub_total += item.Totalprice

    if sub_total > 1000:
        delivery = 0
    elif sub_total > 500:
        delivery = 50
    else:
        delivery = 100

    grand_total = sub_total + delivery

    return render(request, "checkout.html", {
        'cart_data': cart_data,
        'sub_total': sub_total,
        'delivery': delivery,
        'grand_total': grand_total,
    })


def save_order(request):
    if request.method == "POST":
        uname = request.session.get('username')


        cart_data = CartDb.objects.filter(Username=uname)
        sub_total = sum(item.Totalprice for item in cart_data)
        if sub_total > 1000:
            delivery = 0
        elif sub_total > 500:
            delivery = 50
        else:
            delivery = 100
        grand_total = sub_total + delivery

        obj = OrderDb(
            First_Name=request.POST.get('First_Name'),
            Last_Name=request.POST.get('Last_Name'),
            Email=request.POST.get('Email'),
            Place=request.POST.get('Place'),
            Address=request.POST.get('Address'),
            Mobile=request.POST.get('Mobile'),
            State=request.POST.get('State'),
            Pin=request.POST.get('Pin'),
            TotalPrice=grand_total,
        )
        obj.save()
        return redirect(payment)

def payment(request):
        return render(request,"payment.html")

