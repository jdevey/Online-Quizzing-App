
from rest_framework import serializers
from quizmeapp.models import Game, Question, Choice
from users.models import CustomUser
from drf_writable_nested import WritableNestedModelSerializer


#class UserSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = CustomUser
   #     fields = ('games')


class GameSerializer(serializers.ModelSerializer):
    #owner = serializers.Field(source=Game.owner)
    class Meta:
        model = Game
        fields = ('owner', 'game_id', 'game_pin', 'game_title', 'pub_date')



class QuestionSerializer(serializers.ModelSerializer):
    game_parent = GameSerializer()
    class Meta:
        model = Question
        fields = ('game_parent', 'queston_text', 'pub_date', 'choices', 'correct_answer')
