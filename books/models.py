from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    birthdate = models.DateTimeField()
    salary = models.DecimalField(decimal_places=2, max_digits=7)
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)

class Client(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)


class Order(models.Model):
    status = models.CharField(max_length=45)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    genre = models.CharField(max_length=45)
    publisher = models.CharField(max_length=45)
    language = models.CharField(max_length=45)
    ISBN = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

class Payment(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=45)
    value = models.DecimalField(decimal_places=2, max_digits=6)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Book_has_Order(models.Model):
    Book_idBook = models.ForeignKey(Book, on_delete=models.CASCADE)
    Order_idOrder = models.ForeignKey(Order, on_delete=models.CASCADE)