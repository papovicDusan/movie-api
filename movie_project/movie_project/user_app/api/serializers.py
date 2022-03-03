from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer

from ..models import CustomUser
from ...movie_view.models import MovieWatchlist
from ...movie_view.serializers import BasicMovieSerializer


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = CustomUser.USERNAME_FIELD

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']

    name = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name']

# from movie_project.movies.serializers import BasicMovieSerializer

class MovieWatchlistSerializer(serializers.ModelSerializer):

    movie = BasicMovieSerializer(read_only=True)

    class Meta:
        model = MovieWatchlist
        fields = ['id', 'movie', 'is_watched']

class AddAndRemoveMovieWatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieWatchlist
        fields = ['movie']

class UpdateMovieWatchlistSerializer(serializers.ModelSerializer):

    is_watched = serializers.BooleanField(required=True)

    class Meta:
        model = MovieWatchlist
        fields = ['movie', 'is_watched']
