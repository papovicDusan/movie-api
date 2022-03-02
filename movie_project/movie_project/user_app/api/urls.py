# from django.urls import path,include
# from rest_framework_simplejwt.views import TokenRefreshView
#
# from .views import EmailTokenObtainPairView, RegisterView
#
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='token_obtain_pair'),
#     path('login/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

from django.urls import path
from rest_framework import routers
from .views import UserViewSet

router_user = routers.SimpleRouter()
router_user.register(r'users', UserViewSet)
