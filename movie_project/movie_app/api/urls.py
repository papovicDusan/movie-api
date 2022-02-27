# from django.urls import path
#
# from .views import MovieListCreate, MovieDetail, LikeCreate, CommentCreate, CommentList, MovieGenreList, MoviePopularList
#
#
# urlpatterns = [
#     path('', MovieListCreate.as_view(), name='movie-list'),
#     path('<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
#     path('likes/<int:pk>/like-create/', LikeCreate.as_view(), name='like-create'),
#
#     path('comments/<int:pk>/comment-create/', CommentCreate.as_view(), name='comment-create'),
#     path('comments/<int:pk>/comment-list/', CommentList.as_view(), name='comment-list'),
#     path('<int:pk>/movie-genre-list/', MovieGenreList.as_view(), name='movie-genre-list'),
#     path('movie-popular-list/', MoviePopularList.as_view(), name='movie-popular-list'),
# ]