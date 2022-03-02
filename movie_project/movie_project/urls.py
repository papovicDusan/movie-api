"""movie_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from movie_project.movie_viewset.urls import router_movie

from .movie_viewset.urls import router_movie, router_comment, router_popular_movie
from .user_app.api.urls import router_user
from rest_framework_simplejwt.views import TokenObtainPairView
from .user_app.api.views import EmailTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('movies/', include('movie_app.api.urls')),
    path('login/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router_movie.urls)),
    path('', include(router_comment.urls)),
    path('', include(router_popular_movie.urls)),
    # path('auth/', include('user_app.api.urls')),
    path('', include(router_user.urls)),
]
