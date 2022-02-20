from django.db import models
from .utils import MOVIE_GENRES

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    image_url = models.TextField()
    genre = models.CharField(max_length=20, choices=MOVIE_GENRES, default=MOVIE_GENRES.historical)

    def __str__(self):
        return self.title