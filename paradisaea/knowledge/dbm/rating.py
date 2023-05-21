from ..models import ListModel
from django.http import HttpResponse
import json
from . import entry as KnowEntry

global error
error = 'testError'

def know_rating_update_data(data):
   know = ListModel.objects.filter(know_code=data["know_code"]).first()
   if know:
      return  know_rating_update_model(data,know)
   data['rating'] = data["updateRating"]
   return KnowEntry.know_entry(data)

def know_rating_update_model(data,dbmodel):
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
      error = "can't find this task"
      return False
   return False