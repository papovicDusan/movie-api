
from .views import MovieViewSet, CommentViewSet, PopularMovieViewSet
from rest_framework_nested import routers

router_movie = routers.SimpleRouter()
router_movie.register(r'movies', MovieViewSet, basename='movie')

router_comment = routers.NestedSimpleRouter(router_movie, r'movies', lookup='movie')
router_comment.register(r'comments', CommentViewSet, basename='comment')

router_popular_movie = routers.SimpleRouter()
router_popular_movie.register(r'popular-movies', PopularMovieViewSet, basename='popular-movie')
urlpatterns = router_movie.urls
