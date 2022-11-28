from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookList.as_view(), name=views.BookList.name),
    path('books/<int:pk>', views.BookDetail.as_view(), name=views.BookDetail.name),
    path('clients/', views.ClientList.as_view(), name=views.ClientList.name),
    path('clients/<int:pk>', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('orders/', views.OrderList.as_view(), name=views.OrderList.name),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name=views.OrderDetail.name),
    path('employees/', views.EmployeeList.as_view(), name=views.EmployeeList.name),
    path('employees/<int:pk>', views.EmployeeDetail.as_view(), name=views.EmployeeDetail.name),
    path('api-auth/', include('rest_framework.urls')),
]

