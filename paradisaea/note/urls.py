from django.urls import path, re_path
from . import views
from django.urls import path,include

urlpatterns = [
path(r'', views.NoteAPIViewSet.as_view({"get": "list"}), name="note"),
]
