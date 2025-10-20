from django.contrib import admin
from django.urls import path
from auth_users.views import UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='users_id'),
]
