# Generated by Django 4.1.5 on 2023-05-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beat_the_odds', '0018_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_id',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='pick',
            name='game_id',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
