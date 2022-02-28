from rest_framework import serializers
from .models import Movie, Reaction, Comment


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
        fields = ['id', 'title', 'likes']

class RelatedMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title']
