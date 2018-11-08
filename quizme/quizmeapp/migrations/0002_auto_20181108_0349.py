# Generated by Django 2.1.2 on 2018-11-08 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizmeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
