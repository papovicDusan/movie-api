from .views import UserViewSet, WatchlistViewSet
from rest_framework import routers

router_user = routers.SimpleRouter()
router_user.register(r'users', UserViewSet)
router_user.register(r'watchlist', WatchlistViewSet)
urlpatterns = router_user.urls


