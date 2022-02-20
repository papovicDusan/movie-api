from django.urls import path
from .views import MovieListCreate, MovieDetail

urlpatterns = [
    path('', MovieListCreate.as_view()),
    path('<int:pk>/', MovieDetail.as_view())
]