from django.urls import path
from webapp import views


urlpatterns=[
path('home/',views.home,name="home"),
path('about/',views.about,name="about"),
path('our_products/',views.all_products,name="our_products"),
path('filtered_products/<cat_name>/',views.filter_products,name="filtered_products"),
path('single_product/<int:product_id>/',views.single_product,name="single_product"),
path('contact/',views.contact,name="contact"),
path('save_contact/',views.save_contact,name="save_contact"),
path('Sign_in/',views.Sign_in,name="Sign_in"),
path('Sign_up/',views.Sign_up,name="Sign_up"),
path('save_registration/',views.save_registration,name="save_registration"),
path('user_login/',views.user_login,name="user_login"),
path('user_logout/',views.user_logout,name="user_logout"),
path('cart/',views.cart,name="cart"),
path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
path('checkout/',views.checkout,name="checkout"),
path('save_order/', views.save_order, name='save_order'),
path('payment/',views.payment, name='payment'),
path('services/', views.services, name='services')
]