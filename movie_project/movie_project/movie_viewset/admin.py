from django.contrib import admin
from .models import Movie, Reaction, Comment

admin.site.register(Movie)
admin.site.register(Reaction)
admin.site.register(Comment)