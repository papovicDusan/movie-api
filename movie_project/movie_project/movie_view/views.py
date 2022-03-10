from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Like, Reaction, Comment, MovieImage
from .serializers import MovieSerializer, AddReactionSerializer, AddCommentSerializer, CommentSerializer,\
    PopularMovieSerializer, RelatedMovieSerializer, AddMovieSerializer
from django.db.models import Q, Count, Sum
from django.db.models.functions import Coalesce
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

class PopularMovieViewSet(viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        likesQuery = Coalesce(Count('movie_likes__like', filter=Q(movie_likes__like=Like.LIKE)), 0)
        queryset = Movie.objects.annotate(likes=likesQuery).filter(likes__gt=0).order_by('-likes')[:10]
        response_serializer = PopularMovieSerializer(queryset, many=True)
        return Response(response_serializer.data, status=HTTP_200_OK)


class CommentViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(movie=self.kwargs['movie_pk']).order_by('-created_at')

    def create(self, request, movie_pk):
        serializer = AddCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie_comment = Comment.objects.create(**serializer.data, movie_id=movie_pk, user=request.user)
        response_serializer = self.get_serializer(movie_comment)
        return Response(response_serializer.data, status=HTTP_201_CREATED)


class MovieViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['genre']

    def get_queryset(self):
        return Movie.objects.annotate(
            likes=Coalesce(Count('movie_likes__like', filter=Q(movie_likes__like=Like.LIKE)), 0),
            dislikes=Coalesce(Count('movie_likes__like', filter=Q(movie_likes__like=Like.DISLIKE)), 0),
            liked_or_disliked_user=Coalesce(Sum('movie_likes__like', filter=Q(movie_likes__user=self.request.user)), 0),
        ).order_by('id')

    def create(self, request):
        serializer = AddMovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        image = MovieImage.objects.create(thumbnail=request.FILES.get('image_url'), full_size=request.FILES.get('image_url'))
        movie = Movie.objects.create(**serializer.data, image_url=image)
        response_serializer = self.get_serializer(movie)
        return Response(response_serializer.data, status=HTTP_201_CREATED)


    @action(detail=True, url_path='related-movies')
    def related_movies(self, request, pk):
        movie = self.get_object()
        queryset = Movie.objects.filter(genre=movie.genre).exclude(pk=pk)[:10]
        response_serializer = RelatedMovieSerializer(queryset, many=True)
        return Response(response_serializer.data, status=HTTP_200_OK)

    @action(methods=['POST'], detail=True, url_path='like')
    def like(self, request, pk):
        serializer = AddReactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Reaction.objects.update_or_create(movie=self.get_object(), user=request.user, defaults={**serializer.data})
        return Response(status=HTTP_200_OK)

    @action(methods=['DELETE'], detail=True, url_path='delete-like')
    def delete_like(self, request, pk):
        movie_likes = Reaction.objects.filter(movie_id=pk, user=request.user)
        if not movie_likes.exists():
            error = {"not_exists_error": ["There is no like/dislike for the selected movie and user"]}
            return Response(error, status=HTTP_404_NOT_FOUND)
        movie_likes.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    @action(methods=['PATCH'], detail=True, url_path='visits')
    def visits(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.visits = movie.visits + 1
        movie.save()
        return Response(status=HTTP_200_OK)
