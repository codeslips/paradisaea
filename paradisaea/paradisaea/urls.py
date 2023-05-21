"""paradisaea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.views import serve
from django.views.static import serve as static_serve
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#from utils.apitag import api_tags
#from . import views
from django.views.generic import RedirectView
from .api import api



from drf_yasg.generators import OpenAPISchemaGenerator

class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
  def get_schema(self, request=None, public=False):
    """Generate a :class:`.Swagger` object with custom tags"""
    swagger = super().get_schema(request, public)
    #swagger.tags = api_tags(request.META.get("HTTP_ACCEPT_LANGUAGE", ''))
    return swagger

schema_view = get_schema_view(
    openapi.Info(
       title="Paradisaea--API Docs",
       default_version='v0.0.4',
       description=
       """
        openid:
            Openid is the only mark of your data group, You should add it to you request headers.token .
        """
       ,
       terms_of_service="https://www.paradisaea.cn/",
       license=openapi.License(name="MIT"),
    ),
    public=True,
    generator_class=CustomOpenAPISchemaGenerator,
    permission_classes=(permissions.AllowAny, ),
)

def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)

urlpatterns = [
    path('api/v1/', api.urls), 
    path('admin/', admin.site.urls),
    path('note/', include('note.urls')),
    path('todo/', include('todo.urls')),  
    path('chat/', include('chat.urls')),    
    #path('login/', include('userlogin.urls')),
    #path('register/', include('userregister.urls')),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
