from rest_framework import generics
from ..models import Movie
from .serializers import MovieSerializer
from .pagination import MovieListPagination
from rest_framework import filters

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MovieListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer