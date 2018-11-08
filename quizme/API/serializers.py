
from rest_framework import serializers
from quizmeapp.models import Game
from users.models import CustomUser


#class UserSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = CustomUser
   #     fields = ('games')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('owner', 'game_title', 'pub_date')
