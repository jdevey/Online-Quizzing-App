
from rest_framework import serializers
from quizmeapp import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('owner', 'username', 'games')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = ('owner', 'game_title', 'pub_date')
