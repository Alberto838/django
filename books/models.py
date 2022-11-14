from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    genre = models.CharField(max_length=45)
    publisher = models.CharField(max_length=45)
    language = models.CharField(max_length=45)
    ISBN = models.CharField(max_length=13)
    price = models.DecimalField()
    stock = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Order(models.Model):
    status = models.CharField(max_length=45)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Employee(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    birthdate = models.DateTimeField()
    salary = models.DecimalField()
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)

class Client(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)

class Payment(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=45)
    value = models.DecimalField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)