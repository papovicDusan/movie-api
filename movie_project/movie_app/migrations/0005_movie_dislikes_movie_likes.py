# Generated by Django 4.0.2 on 2022-02-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_movie_genre_movielike'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]