# Generated by Django 2.1.2 on 2018-11-08 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_title', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('game_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizmeapp.Game')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizmeapp.User'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizmeapp.Question'),
        ),
    ]
