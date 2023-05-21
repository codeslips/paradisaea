from rest_framework import viewsets
from .models import ListModel
from . import serializers
from .page import MyPageNumberPagination
#from utils.md5 import Md5
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import Filter
from rest_framework.exceptions import APIException
from django.http import StreamingHttpResponse
from rest_framework.settings import api_settings


class ChatAPIViewSet(viewsets.ModelViewSet):
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filterset_class = Filter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
       return ListModel.objects.all()
       id = self.get_project()
       if self.request.user:
           if id is None:
               return ListModel.objects.all()
           else:
               return ListModel.objects.all()
       else:
           return ListModel.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'destroy']:
            return serializers.ChatSerializers
        elif self.action in ['create']:
            return serializers.ChatSerializers
        elif self.action in ['update']:
            return serializers.ChatSerializers
        elif self.action in ['partial_update']:
            return serializers.ChatSerializers
        else:
            return self.http_method_not_allowed(request=self.request)