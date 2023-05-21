from django.urls import path, re_path
from . import views
from django.urls import path,include

urlpatterns = [
path(r'', views.ChatAPIViewSet.as_view({"get": "list"}), name="chat"),
]
