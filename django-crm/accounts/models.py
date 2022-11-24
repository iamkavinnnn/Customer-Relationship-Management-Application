from pickle import TRUE

from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    CATEGORY = [
        ('Fruit', 'Fruit'),
        ('Vegetable', 'Vegetable'),
        ('Utensil', 'Utensil'),
        ('Dairy', 'Dairy')
    ]

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    STATUS_MENU = [
        ('Pendin', 'Pending'),
        ('Out for delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered')
        ]

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, choices=STATUS_MENU)
    date_created = models.DateTimeField(auto_now_add=True)
