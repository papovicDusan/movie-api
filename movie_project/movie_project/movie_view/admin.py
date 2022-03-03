from django.contrib import admin
from .models import Movie, Reaction, Comment, MovieWatchlist

admin.site.register(Movie)
admin.site.register(Reaction)
admin.site.register(Comment)
admin.site.register(MovieWatchlist)