from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenObtainPairSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from ...movie_view.models import MovieWatchlist
from .serializers import (
    CreateUserSerializer,
    UserSerializer,
    AddMovieWatchlistSerializer,
    MovieWatchlistSerializer
)
# from .permissions import UserAccessPermission
User = get_user_model()

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class UserViewSet(mixins.CreateModelMixin,
                viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.data)
        return Response(status=HTTP_201_CREATED)

    @action(detail=False, url_path='me', permission_classes=[IsAuthenticated])
    def get_current_user(self, request):
        response_serializer = UserSerializer(request.user)
        return Response(response_serializer.data, HTTP_200_OK)

class WatchlistViewSet(mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    # permission_classes = [IsAuthenticated, UserAccessPermission]
    permission_classes = [IsAuthenticated, ]
    pagination_class = None
    queryset = MovieWatchlist.objects.all()
    serializer_class = MovieWatchlistSerializer

    def create(self, request, *args, **kwargs):
        serializer = AddMovieWatchlistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie_id = serializer.data['movie']
        watchlist_movie = MovieWatchlist.objects.update_or_create(user_id=request.user.id, movie_id=movie_id)[0]
        response_serializer = self.get_serializer(watchlist_movie)
        return Response(response_serializer.data, status=HTTP_201_CREATED)