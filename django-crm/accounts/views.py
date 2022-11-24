from accounts.models import *
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    customer = Customer.objects.all()
    orders = Order.objects.all()

    content = {"customer":customer, "order":orders}
    return render(request, 'accounts/dashboard.html')

def products(request):
    products = Products.objects.all()
    return render(request, 'accounts/products.html', {"prod": products})
    
def customer(request):
    return render(request, 'accounts/customer.html')