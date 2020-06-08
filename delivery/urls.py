from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    url('', views.login,name="login"),
    path('home', views.home, name="home"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('customer_order/', views.addCustomer, name="customer_order"),
]
