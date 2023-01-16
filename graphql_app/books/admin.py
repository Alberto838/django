from django.contrib import admin

# Register your models here.

from .models import Client, Order, Book, Book_has_Order

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Book)
admin.site.register(Book_has_Order)