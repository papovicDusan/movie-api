from django.db import models
from .utils import MOVIE_GENRES
from django.contrib.auth import get_user_model

User = get_user_model()


class Like(models.IntegerChoices):
    LIKE = 1
    DISLIKE = -1


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    image_url = models.TextField()
    genre = models.CharField(max_length=20, choices=MOVIE_GENRES, default=MOVIE_GENRES.historical)
    visits = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title


class Reaction(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    like = models.IntegerField(choices=Like.choices)

    class Meta:
        unique_together = ('movie', 'user',)

    def __str__(self):
        return f'{self.movie} | {self.user}'
