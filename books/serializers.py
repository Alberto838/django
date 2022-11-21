from rest_framework import serializers
from books.models import Book, Order, Employee, Client, Payment, Book_has_Order
from django.contrib.auth.models import User

class BookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="books:book-detail")
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'author', 'genre', 'publisher', 'language', 'ISBN', 'price', 'stock']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'id', 'status', 'client', 'employee']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'id', 'name', 'surname', 'birthdate', 'salary', 'address', 'phone']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['url', 'id', 'name', 'surname', 'address', 'phone']

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['url', 'id', 'date', 'type', 'value']

class Book_has_Order(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book_has_Order
        fields = ['Book_idBook', 'Order_idOrder']

# class UserSerializer(serializers.ModelSerializer):
#     books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'books']
