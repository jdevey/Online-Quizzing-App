from django.shortcuts import render
from rest_framework import generics, permissions
from quizmeapp.models import Game, Question
from users.models import CustomUser
from .serializers import GameSerializer, QuestionSerializer
from .permissions import MyUserPermissions


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
    permission_classes = (MyUserPermissions, permissions.IsAuthenticated,)
    serializer_class = GameSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Game.objects.filter(owner=user)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GameSerializer

class GameUpdateView(generics.UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    permission_classes = (MyUserPermissions, permissions.IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        id = Game.id
        return Question.objects.filter(game_id=id)
