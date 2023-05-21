from ..models import ListModel
import json
import hashlib
import random
from django.utils import timezone

error = "error"

def know_entry(data):
   know = ListModel.objects.filter(know_code=data["know_code"]).first()
   if know:
      return know
   else:
      return create_new_know(data)

def create_new_know(data):
      nknow = ListModel()
      nknow.know_code = data['know_code']
      nknow.rating = data['rating']
      nknow.save()
      return nknow
