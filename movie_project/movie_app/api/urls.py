from django.urls import path
from .views import MovieListCreate, MovieDetail, LikeCreate, CommentCreate

urlpatterns = [
    path('', MovieListCreate.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('likes/<int:pk>/like-create/', LikeCreate.as_view(), name='like-create'),
    path('comments/<int:pk>/comment-create/', CommentCreate.as_view(), name='comment-create'),
]