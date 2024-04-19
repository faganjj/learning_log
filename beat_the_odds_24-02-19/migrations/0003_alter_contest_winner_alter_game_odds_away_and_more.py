# Generated by Django 4.1.5 on 2023-03-15 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beat_the_odds', '0002_alter_contest_league_alter_stat_league_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='winner',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='game',
            name='odds_away',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='odds_home',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='outcome_away',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='outcome_home',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='score_away',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='score_home',
            field=models.IntegerField(null=True),
        ),
    ]