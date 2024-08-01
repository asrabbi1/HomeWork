from rest_framework.pagination import PageNumberPagination

class TodoPagination(PageNumberPagination):
    page_size=1
    max_page_size=1000
    page_size_query_param='page_size'