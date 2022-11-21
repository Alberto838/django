from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookList.as_view(), name=views.BookList.name),
    path('api-auth/', include('rest_framework.urls')),
]

