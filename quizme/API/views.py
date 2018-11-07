from django.shortcuts import render
from rest_framework import generics, permissions
from quizmeapp.models import User, Question
from .serializers import UserSerializer

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer