from ninja import Router
from datetime import date
from ninja import Schema,Router
from typing import List
from ..models import ListModel
from ..dbm import rating as KnowRating


router = Router()

class KnowOut(Schema):
   know_code: str
   rating: int


@router.get("/",response=KnowOut)
def get_know(request,know_code: str):
    know = ListModel.objects.filter(know_code=know_code).first()
    if know:
       return know
    know_update = KnowRating.know_rating_update_data({'know_code':know_code,'updateRating':5})
    if know_update:
       return know_update
    return {}

