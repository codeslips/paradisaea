from ..models import ListModel
import json
import hashlib
import random
from django.utils import timezone
from . import entry as Entry

error = "error"

def update_note(data):
   note = ListModel.objects.filter(note_code=data["note_code"]).first()
   if note:
      return note
   else:
      return Entry.note_entry(data)

def update_note_model(dbmodel, data):
   try:
      n = data["note"]
      nt = data["note_title"]
   except:
      return False

   if dbmodel:
      dbmodel.note = n
      dbmodel.note_title = nt
      dbmodel.save()
      return dbmodel
   return False
