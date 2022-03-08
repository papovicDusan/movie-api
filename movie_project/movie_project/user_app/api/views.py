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
    MovieWatchlistSerializer
)
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
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated, ]
    pagination_class = None
    queryset = MovieWatchlist.objects.all()
    serializer_class = MovieWatchlistSerializer
