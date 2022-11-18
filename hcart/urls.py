from django.urls import path
from . import views

urlpatterns = [
    path('login',views.cart_login,name='clogin'),
    path('log',views.cart_log,name='login'),
    path('pass',views.cart_password,name='pass'),
    path('home',views.cust_home,name='home'),
]
