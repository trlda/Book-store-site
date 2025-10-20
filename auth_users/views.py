from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.authtoken.admin import User
from rest_framework.response import Response
from rest_framework.views import APIView
from auth_users.serializers import UserSerializer, RegistrationSerializer

class UserList(APIView):
    def get(self, reauest):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)