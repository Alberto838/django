from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import BookSerializer, OrderSerializer, EmployeeSerializer, ClientSerializer, PaymentSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User
from .custompermission import IsCurrentUserOwnerOrReadOnly
from django.http import HttpResponse
from .models import Book
# Create your views here.



def index(request):
    return HttpResponse("Witajcie w księgarni śmiertelnicy")


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    filter_fields = ['title', 'author', 'genre', 'publisher', 'language', 'ISBN']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author', 'genre', 'ISBN']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

