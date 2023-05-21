from django.urls import path, re_path
from . import views
from django.urls import path,include

urlpatterns = [
path(r'', views.TodoAPIViewSet.as_view({"get": "list"}), name="todo"),
]
