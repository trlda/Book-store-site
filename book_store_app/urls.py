from django.contrib import admin
from django.urls import path
from book_store_app import views 

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('publishers/', views.PublisherList.as_view(), name='publishers'),
    path('genres/', views.GenreList.as_view(), name='genres'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
]