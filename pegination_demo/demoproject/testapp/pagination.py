from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPagination(PageNumberPagination):
    page_size = 5 
    page_query_param = 'mypage'  # default value is ---- page
    page_size_query_param = 'num'
    max_page_size = 10
    last_page_strings = ('endpage',) #default value is ----- last



class MyPagination2(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'  # default value is limit
    offset_query_param = 'myoffset' # default value is offset
    max_limit = 20




class MyPagination3(CursorPagination):
    ordering = 'esal'
    page_size = 5
    cursor_query_param = 'mycursor'

