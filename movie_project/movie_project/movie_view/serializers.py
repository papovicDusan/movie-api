from rest_framework import serializers
from .models import Movie, Reaction, Comment


class MovieSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(read_only=True, default=0)
    dislikes = serializers.IntegerField(read_only=True, default=0)
    liked_or_disliked_user = serializers.IntegerField(read_only=True, default=0)
    in_user_watchlist = serializers.BooleanField(read_only=True, default=None)
    user_watched = serializers.BooleanField(read_only=True, default=None)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_url', 'genre', 'visits', 'likes', 'dislikes',
                  'liked_or_disliked_user', 'in_user_watchlist', 'user_watched', ]

class BasicMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_url', 'genre']

class AddReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['like']

class AddCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'created_at']

class PopularMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title']

class RelatedMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title']
