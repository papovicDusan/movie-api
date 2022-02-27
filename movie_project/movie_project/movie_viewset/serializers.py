from rest_framework import serializers
from .models import Movie, Reaction


class MovieSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(read_only=True, default=0)
    dislikes = serializers.IntegerField(read_only=True, default=0)
    liked_or_disliked_user = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_url', 'genre', 'visits', 'likes', 'dislikes', 'liked_or_disliked_user', ]

class AddReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['like']