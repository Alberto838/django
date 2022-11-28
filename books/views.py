from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import BookSerializer, OrderSerializer, EmployeeSerializer, ClientSerializer, PaymentSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Book, Client, Order, Employee
# Create your views here.



def index(request):
    return HttpResponse("Witajcie w księgarni")


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    permission_classes = (permissions.IsAuthenticated,)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # filter_class = ClientFilter
    name = 'client-list'
    ordering_fields = ['surname', 'name']

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # filter_class = OrderFilter
    name = 'order-list'

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-detail'

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # filter_class = OrderFilter
    name = 'employee-list'

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-detail'



# class ApiRoot(generics.GenericAPIView):
#     name = 'api-root'
#     def get(self, request, *args, **kwargs):
#         return Response({'book-categories': reverse(BookCategoryList.name, request=request),
#                          'books': reverse(BookList.name, request=request),
#                          'clients': reverse(ClientList.name, request=request),
#                          'orders': reverse(OrderList.name, request=request),
#                          'users': reverse(UserList.name, request=request)
# })