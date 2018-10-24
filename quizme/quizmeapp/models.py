import datetime
from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=15)
    games = []

    def __init__(_username):
        username = _username

    def add_game(game):
        games.append(game)

class Game(models.Model):
    game_title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    question1 = models.CharField(max_length=30)
    questions = Question

    def __str__(self):
        return self.game_title

    # def __init__(_game_title, _pub_date, _questions):
    #     game_title = _game_title
    #     pub_date = _pub_date
    #     questions = _questions

    # def __str__(self):
    #     return self.game_title

    def add_question(question):
        questions.add(question)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    choices = []

    def __init__(_question_text, _pub_date, _choices):
        question_text = _question_text
        pub_date = _pub_date
        choices = _choices

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __init__(_choice_text):
        choice_text = _choice_text

    def __str__(self):
        return self.choice_text

    def add_vote():
        votes += 1
