from rest_framework import serializers

from ..models import Movie, MovieLike, MovieComment

class MoviePopularSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'likes']

class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title']

class MovieCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieComment
        fields = ['id', 'content']


class MovieLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLike
        fields = ['like']

class MovieSerializer(serializers.ModelSerializer):

    movie_comments = MovieCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_url', 'genre', 'likes', 'dislikes', 'number_visit', 'movie_comments',  ]

