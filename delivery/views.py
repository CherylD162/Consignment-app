from django.contrib.auth import authenticate
from django.http import HttpResponse

from .forms import *
from django.shortcuts import render, redirect
from .models import *


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user.is_active:
            return render(request, 'delivery/dashboard.html')
        else:
            return HttpResponse("Invalid login details given")

    return render(request, 'delivery/login.html')


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'customers': customers, 'orders': orders, 'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}
    return render(request, 'delivery/dashboard.html', context)


def customer(request, pk_test):
    customers = Customer.objects.get(id=pk_test)
    orders = customers.order_set.all()
    order_count = orders.count()
    context = {'customers': customers, 'orders': orders, 'order_count': order_count}
    return render(request, 'delivery/customer.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {'form': form}
    return render(request, 'delivery/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {'form': form}
    return render(request, 'delivery/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/home')
    context = {'item': order}
    return render(request, 'delivery/delete.html', context)


def addCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {'form': form}
    return render(request, 'delivery/customer_form.html', context)
