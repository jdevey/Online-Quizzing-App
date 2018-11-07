from django.shortcuts import render
from rest_framework import generics
from quizmeapp.models import User, Question
from .serializers import UserSerializer

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer