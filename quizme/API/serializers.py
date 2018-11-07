
from rest_framework import serializers
from quizmeapp import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'games')


