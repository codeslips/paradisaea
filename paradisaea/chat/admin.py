from django.contrib import admin
from . models import ListModel


@admin.register(ListModel,site=admin.site)
class ChatAdmin(admin.ModelAdmin):
   def get_list_display(self,request):
      return [field.name for field in self.model._meta.concrete_fields]
   pass 