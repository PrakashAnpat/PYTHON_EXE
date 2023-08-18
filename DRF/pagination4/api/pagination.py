from rest_framework.pagination import CursorPagination

class StudentCursorPagination(CursorPagination):
    page_size = 4
    ordering = 'name'
    cursor_query_param = 'cu'
    
    