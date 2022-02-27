from rest_framework import routers
from .views import MovieViewSet

router_movie = routers.SimpleRouter()
router_movie.register(r'movies', MovieViewSet, basename='Movie')
urlpatterns = router_movie.urls
