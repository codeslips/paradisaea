from ..models import ListModel
import json
import hashlib
import random
from django.utils import timezone
from . import entry as Entry

error = "error"

def update_todo(data):
   todo = ListModel.objects.filter(todo_code=data["todo_code"]).first()
   if todo:
      return todo
   else:
      return Entry.note_entry(data)

def update_todo_model(dbmodel, data):
   try:
      n = data["todo_desc"]
      nt = data["todo_title"]
   except:
      return False

   if dbmodel:
      dbmodel.todo_desc = n
      dbmodel.todo_title = nt
      dbmodel.save()
      return dbmodel
   return False
