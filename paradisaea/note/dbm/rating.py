from ..models import ListModel
from django.http import HttpResponse
import json
from . import entry as NoteEntry

global error
error = 'testError'

def note_rating_update_data(data):
   note = ListModel.objects.filter(note_code=data["note_code"]).first()
   if note:
      return  note_rating_update_model(data,know)
   data['note'] = ''
   data['note_tags'] = []
   data['rating'] = data["updateRating"]
   data['creater'] = 'AutoRating'
   return NoteEntry.note_entry(data)

def note_rating_update_model(data,dbmodel):
   print(data)
   try:
      ur = int(data["updateRating"])
   except:
      return False

   if dbmodel:
      if ur >= 0:      
         dbmodel.rating = ur
         dbmodel.save()
         return dbmodel
      return dbmodel
   else:
      error = "can't find this note"
      return False
   return False