from collections import OrderedDict
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param, remove_query_param
from .models import BambooListModel as bamboo

class MyPageNumberPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = "max_page"
    max_page_size = 1000
    page_query_param = 'page'

    def get_paginated_response(self, data):
    
        bamboo_data = bamboo.objects.filter(is_delete=False)
        bamboo_name_list = []
        for i in range(len(bamboo_data)):
            bamboo_name_list.append(bamboo_data[i].bamboo_name)
        return Response(OrderedDict([
            ('bamboo_name_list', bamboo_name_list),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
