from rest_framework import serializers
from .models import Movie, Reaction, Comment

class MovieSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(read_only=True, default=0)
    dislikes = serializers.IntegerField(read_only=True, default=0)
    liked_or_disliked_user = serializers.IntegerField(read_only=True, default=0)
    thumbnail = serializers.SerializerMethodField()
    full_size = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_url', 'genre', 'visits', 'likes', 'dislikes',
                  'liked_or_disliked_user', 'thumbnail', 'full_size']

    def get_thumbnail(self, obj):
        return obj.image_url.thumbnail.url if obj.image_url is not None else False

    def get_full_size(self, obj):
        return obj.image_url.full_size.url if obj.image_url is not None else False


class AddMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'genre', 'visits']


class BasicMovieSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    full_size = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_url', 'genre', 'thumbnail', 'full_size']

    def get_thumbnail(self, obj):
        return obj.image_url.thumbnail.url if obj.image_url is not None else False

    def get_full_size(self, obj):
        return obj.image_url.full_size.url if obj.image_url is not None else False

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

