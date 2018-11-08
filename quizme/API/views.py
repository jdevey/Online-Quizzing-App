from django.shortcuts import render
from rest_framework import generics, permissions
from quizmeapp.models import Game, Question
from users.models import CustomUser
from .serializers import GameSerializer

# Create your views here.
#class UserList(generics.ListAPIView):
#    queryset = CustomUser.objects.all()
#    permission_classes = (permissions.IsAuthenticated,)
#    serializer_class = UserSerializer

#class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = CustomUser.objects.all()
#    permission_classes = (permissions.IsAuthenticated,)
#    serializer_class = UserSerializer

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GameSerializer