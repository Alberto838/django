import graphene
from graphene_django import  DjangoObjectType
from .models import Client, Order, Book, Book_has_Order

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = ('id', 'name', 'surname', 'address', 'phone')

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ('id', 'status', 'client')

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genre', 'publisher', 'language', 'ISBN', 'price', 'stock')

class Book_has_OrderType(DjangoObjectType):
    class Meta:
        model = Book_has_Order
        fields = ('id', 'Book_idBook', 'Order_idOrder')

class Query(graphene.ObjectType):
    clients = graphene.List(ClientType)
    orders = graphene.List(OrderType)
    books = graphene.List(BookType)
    book_has_order = graphene.List(Book_has_OrderType)

    def resolve_clients(root, info, **kwargs):
        return Client.objects.all()

    def resolve_orders(root, info, **kwargs):
        return Order.objects.all()

    def resolve_books(root, info, **kwargs):
        return Book.objects.all()

    def resolve_book_has_order(root, info, **kwargs):
        return Book_has_Order.objects.all()


schema = graphene.Schema(query=Query)
