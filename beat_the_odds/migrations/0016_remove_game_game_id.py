# Generated by Django 4.1.5 on 2023-05-23 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beat_the_odds', '0015_game_game_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_id',
        ),
    ]