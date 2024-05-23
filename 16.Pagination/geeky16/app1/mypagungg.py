# -------->>>

#from rest_framework.pagination import PageNumberPagination # locally apply page number
# class MyPageNumber(PageNumberPagination):
#     page_size = 5
#     # page_query_param ='p'
#     # page_size_query_param = 'records'
#     max_page_size = 7
#   # last_page_query_param ='end


# ---------->>>Limit Offset Pagination 
# from rest_framework.pagination import LimitOffsetPagination 

# class MyPageNumber(LimitOffsetPagination):
#    default_limit = 5
#    limit_query_param = 'mylimit'
#    offset_query_param ='myoffset'
#    max_limit = 6

#------------>>>Cursor Pagination

from rest_framework.pagination import CursorPagination 

class MyPageNumber(CursorPagination):
    page_size = 5
    # ordering = 'name'
    ordering = 'id'