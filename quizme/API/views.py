from django.shortcuts import render
from rest_framework import generics, permissions
from quizmeapp.models import User, Game, Question
from .serializers import UserSerializer, GameSerializer

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    #permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    #permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GameSerializer