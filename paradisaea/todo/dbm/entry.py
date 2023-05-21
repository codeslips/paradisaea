from ..models import ListModel
import json
import hashlib
import random
from django.utils import timezone
from . import todo as Todo

error = "error"

def todo_entry(data):
   todo = ListModel.objects.filter(todo_code=data["todo_code"]).first()
   if todo:
      return Todo.update_todo_model(todo, data)
   else:
      return create_new_todo(data)

def create_new_todo(data):
      ntodo = ListModel()
      ntodo.todo_code = get_todo_code()
      ntodo.status = data['status']
      ntodo.pervious = data['pervious']
      ntodo.next = data['next']
      ntodo.todo_title = data['todo_title']
      ntodo.todo_desc = data['todo_desc']
      ntodo.todo_tags = data['todo_tags']
      ntodo.creater = data['creater']
      ntodo.save()
      return ntodo


def get_todo_code():
   from datetime import datetime
   dt = datetime.now()
   i = 0
   todo_code = 'T'+str(dt.strftime('%Y%m%d%H%M%S%f'))[2:16]
   while i<100:
      todo_exists = ListModel.objects.filter(todo_code=todo_code).exists()
      if todo_exists:
         todo_code = 'T'+str(dt.strftime('%Y%m%d%H%M%S%f'))[2:16] + str(i)
      else:
         return todo_code
      i = i + 1