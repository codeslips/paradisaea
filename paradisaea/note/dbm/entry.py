from ..models import ListModel
import json
import hashlib
import random
from django.utils import timezone
from . import note as Note

error = "error"

def note_entry(data):
   note = ListModel.objects.filter(note_code=data["note_code"]).first()
   if note:
      return Note.update_note_model(note, data)
   else:
      return create_new_note(data)

def create_new_note(data):
      nnote = ListModel()
      nnote.note_code = get_note_code()
      nnote.rating = data['rating']
      nnote.note_title = data['note_title']
      nnote.note = data['note']
      nnote.note_tags = data['note_tags']
      nnote.creater = data['creater']
      nnote.save()
      return nnote


def get_note_code():
   from datetime import datetime
   dt = datetime.now()
   i = 0
   note_code = 'N'+str(dt.strftime('%Y%m%d%H%M%S%f'))[2:16]
   while i<100:
      note_exists = ListModel.objects.filter(note_code=note_code).exists()
      if note_exists:
         note_code = 'N'+str(dt.strftime('%Y%m%d%H%M%S%f'))[2:16] + str(i)
      else:
         return note_code
      i = i + 1