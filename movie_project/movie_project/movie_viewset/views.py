from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Like, Reaction
from .serializers import MovieSerializer, AddReactionSerializer
from django.db.models import Q, Count, Sum
from django.db.models.functions import Coalesce
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


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
