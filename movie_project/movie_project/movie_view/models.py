from django.db import models
from .utils import MOVIE_GENRES
from django.contrib.auth import get_user_model
from easy_thumbnails.fields import ThumbnailerImageField

User = get_user_model()


class MovieImage(models.Model):
    thumbnail = ThumbnailerImageField(
        upload_to='static/thumbnails/', blank=True, null=True, resize_source=dict(size=(200, 200)))
    full_size = ThumbnailerImageField(
        upload_to='static/full-size/', blank=True, null=True, resize_source=dict(size=(400, 400)))


class Like(models.IntegerChoices):
    LIKE = 1
    DISLIKE = -1


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    image_url = models.OneToOneField(MovieImage, on_delete=models.CASCADE, blank=True, null=True)
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


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie} | {self.user}'


class MovieWatchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_watchlist')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_watchlist')
    is_watched = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'movie')
