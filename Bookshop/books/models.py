from django.db import models

# Create your models here.
class Book(models.model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    genre = models.CharField(max_length=45)
    publisher = models.CharField(max_length=45)
    language = models.CharField(max_length=45)
    isbn = models.CharField(max_length=45)
    price = models.DecimalField()
    stock = models.IntegerField()
