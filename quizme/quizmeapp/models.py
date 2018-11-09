import datetime
from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.conf import settings
import uuid



class Game(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #owner = models.CharField(default=settings.AUTH_USER_MODEL, max_length=30)
    game_title = models.CharField(max_length=30)
    game_id = models.UUIDField(default=uuid.uuid1, editable=False)
    game_pin = models.IntegerField(primary_key=True, default=123123, editable=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.game_id

    def game_pin(self):
        generate_pin = str(self.game_id)[:6]
        game_pin = generate_pin
        return 123123

    def add_question(question):
        questions.add(question)

class Question(models.Model):
    game_parent = models.ForeignKey(Game, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    choices = []
    correct_answer = models.CharField(max_length=200, default="no answers")

    def __init__(_question_text, _pub_date, _choices):
        question_text = _question_text
        pub_date = _pub_date
        choices = _choices

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question_parent = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __init__(_choice_text):
        choice_text = _choice_text

    def __str__(self):
        return self.choice_text

