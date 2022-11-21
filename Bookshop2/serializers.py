from rest_framework import serializers
from Bookshop.models import Book, Order, Employee, Client, Payments

class BookSerializer(serializers.HyperlinkedModelSerializer):
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
