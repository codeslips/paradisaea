from ..models import ListModel
from django.http import HttpResponse
import json
from . import entry as Entry

global error
error = 'testError'

def todo_status_update_data(data):
   todo = ListModel.objects.filter(todo_code=data["todo_code"]).first()
   if todo:
      return  todo_status_update_model(data,todo)
   data['todo'] = ''
   data['todo_tags'] = []
   data['status'] = data["updateStatus"]
   data['creater'] = 'AutoStatus'
   return Entry.todo_entry(data)

def todo_status_update_model(data,dbmodel):
   print(data)
   try:
      ur = int(data["updateStatus"])
   except:
      return False

   if dbmodel:
      if ur >= 0:
         dbmodel.status = ur
         if dbmodel.status == 11:
            dbmodel.is_delete = True
         else:
            dbmodel.is_delete = False
         dbmodel.save()
         return dbmodel
      return dbmodel
   else:
      error = "can't find this task"
      return False
   return False