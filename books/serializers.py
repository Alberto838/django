from rest_framework import serializers
from books.models import Book, Order, Employee, Client, Payment, Book_has_Order
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="books")
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'author', 'genre', 'publisher', 'language', 'ISBN', 'price', 'stock']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='surname')
    employee = serializers.SlugRelatedField(queryset=Employee.objects.all(), slug_field='surname')
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
    Order_idOrder = serializers.SlugRelatedField(queryset=Order.objects.all(), slug_field='idOrder')
    class Meta:
        model = Payment
        fields = ['url', 'id', 'date', 'type', 'value']

class Book_has_OrderSerializer(serializers.HyperlinkedModelSerializer):
    Book_idBook = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')
    Order_idOrder = serializers.SlugRelatedField(queryset=Order.objects.all(), slug_field='idOrder')
    orders = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='order-detail')
    books = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='book-detail')
    class Meta:
        model = Book_has_Order
        fields = ['Book_idBook', 'Order_idOrder']

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'books']
