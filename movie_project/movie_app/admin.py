from django.contrib import admin

from .models import Movie, MovieLike, MovieComment

# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieLike)
admin.site.register(MovieComment)

