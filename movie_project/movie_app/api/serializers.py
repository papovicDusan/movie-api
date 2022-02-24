from rest_framework import serializers
from ..models import Movie, MovieLike

class MovieLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLike
        fields = ['like']

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_url', 'genre', 'likes', 'dislikes', 'is_liked', 'number_visit', ]
