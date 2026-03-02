from django.urls import path
from Adminapp import  views

urlpatterns=[
    path('dashboard/',views.dashboard,name="dashboard"),
    path('add_category/',views.add_category,name="add_category"),
    path('add_product/',views.add_product,name="add_product"),
    path('view_product/',views.display_product,name="view_product"),
    path('view_category/',views.display_category,name="view_category"),
    path('admin_loginpage/',views.admin_loginpage,name="admin_loginpage"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('save_category/',views.save_category,name="save_category"),
    path('edit_category/<int:category_id>/',views.edit_category,name="edit_category"),
path('update_category/<int:category_id>/', views.update_category, name='update_category'),
path('update_product/<int:product_id>/',   views.update_product,   name='update_product'),
    path('delete_category/<int:category_id>/',views.delete_category,name="delete_category"),
    path('save_product/',views.save_products,name="save_product"),
    path('edit_product/<int:product_id>/',views.edit_products,name="edit_product"),
    path('delete_product/<int:product_id>/',views.delete_products,name="delete_product"),
    path('contact_data/',views.contact_data,name="contact_data"),
    path('add_service/',             views.add_service,           name='add_service'),
    path('save_service/',            views.save_service,           name='save_service'),
    path('view_services/',           views.view_services_admin,    name='view_services'),
    path('edit_service/<int:service_id>/',   views.edit_service,   name='edit_service'),
    path('update_service/<int:service_id>/', views.update_service, name='update_service'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service')
]