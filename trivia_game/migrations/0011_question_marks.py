# Generated by Django 3.2.6 on 2021-09-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_game', '0010_game_is_housefull'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='marks',
            field=models.IntegerField(default=1),
        ),
    ]