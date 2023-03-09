from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import BookSerializer, OrderSerializer, EmployeeSerializer, ClientSerializer, PaymentSerializer
from .serializers import UserSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet, DateFromToRangeFilter, RangeFilter
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Book, Client, Order, Employee
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .custompermissions import IsCurrentUserOwnerOrReadOnly
# Create your views here.



def index(request):
    return HttpResponse("Witajcie w księgarni")

class BookFilter(FilterSet):
    stock = RangeFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'stock']

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    permission_classes = (permissions.IsAuthenticated, IsCurrentUserOwnerOrReadOnly,)
    filterset_class = BookFilter
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['title', 'price', 'stock']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'
    permission_classes = (permissions.IsAuthenticated, IsCurrentUserOwnerOrReadOnly,)

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['surname', 'name']
    ordering_fields = ['surname']

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-list'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'client', 'employee']

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-detail'

class EmployeeFilter(FilterSet):
    birthdate = DateFromToRangeFilter()

    class Meta:
        model = Employee
        fields = ['birthdate', 'surname', 'name', 'salary']

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-list'
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = EmployeeFilter
    ordering_fields = ['surname', 'salary']
    permission_classes = (permissions.IsAuthenticated, IsCurrentUserOwnerOrReadOnly,)


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-detail'
    permission_classes = (permissions.IsAuthenticated, IsCurrentUserOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (permissions.IsAuthenticated, IsCurrentUserOwnerOrReadOnly,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = (permissions.IsAuthenticated, IsCurrentUserOwnerOrReadOnly,)


class ApiRoot(generics.GenericAPIView):
     name = 'api-root'
     def get(self, request, *args, **kwargs):
         return Response({'books': reverse(BookList.name, request=request),
                          'clients': reverse(ClientList.name, request=request),
                          'orders': reverse(OrderList.name, request=request),
                          'users': reverse(UserList.name, request=request)
 })