from rest_framework.pagination import PageNumberPagination


class ProjectPageNumberPagination(PageNumberPagination):
    page_size = 10
