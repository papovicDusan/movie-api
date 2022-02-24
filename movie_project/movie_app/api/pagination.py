from rest_framework.pagination import PageNumberPagination

class MovieListPagination(PageNumberPagination):
    page_size=10

class CommentListPagination(PageNumberPagination):
    page_size = 2