from rest_framework import generics
from ..models import Movie
from .serializers import MovieSerializer
from .pagination import MovieListPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MovieListPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['genre']

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer