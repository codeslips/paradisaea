from ninja import Router
from datetime import date
from ninja import Schema,Router
from typing import List
from ..dbm import rating as KnowRating


router = Router()

class KnowRatingIn(Schema):
   know_code: str = None
   rating: int = None
   updateRating: int = None

class KnowRatingOut(Schema):
   content: str
   tips: str
   fileInfo: dict


@router.put("/")
def update_file_content(request, payload:KnowRatingIn):
    know_update = KnowRating.know_rating_update_data(payload.dict())
    if know_update:
       return 'success'
    return 'error'

