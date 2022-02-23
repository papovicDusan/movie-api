from rest_framework import generics
from ..models import Movie, MovieLike, MovieComment
from .serializers import MovieSerializer, MovieLikeSerializer, MovieCommentSerializer
from .pagination import MovieListPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.response import Response

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MovieListPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['genre']
    permission_classes = [IsAuthenticated]

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        user = self.request.user

        like_queryset = MovieLike.objects.filter(movie=movie, user=user)
        if like_queryset.exists():
            movie.is_liked = True
        if not like_queryset.exists():
            movie.is_liked = False

        movie.number_visit = movie.number_visit+1
        movie.save()
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

class LikeCreate(generics.CreateAPIView):
    serializer_class = MovieLikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MovieLike.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)
        user = self.request.user

        like_queryset = MovieLike.objects.filter(movie=movie, user=user)
        if like_queryset.exists():
            raise ValidationError("You have already like this movie")
        print(self.request.data['like'])
        if self.request.data['like'] == 1:
            movie.likes = movie.likes+1
        if self.request.data['like'] == -1:
            movie.dislikes = movie.dislikes+1

        movie.save()
        serializer.save(movie=movie, user=user)

class CommentCreate(generics.CreateAPIView):
    serializer_class = MovieCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MovieComment.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)
        user = self.request.user

        serializer.save(movie=movie, user=user)
        print(serializer)
