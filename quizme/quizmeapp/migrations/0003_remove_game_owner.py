# Generated by Django 2.1.2 on 2018-11-08 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizmeapp', '0002_question_correct_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='owner',
        ),
    ]
