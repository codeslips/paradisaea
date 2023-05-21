from ninja import Router
from datetime import date
from ninja import Schema,Router
from typing import List
from ..dbm import rating as NoteRating


router = Router()

class NoteRatingIn(Schema):
   note_code: str = None
   rating: int = None
   updateRating: int = None

class NoteRatingOut(Schema):
   content: str
   tips: str
   fileInfo: dict


@router.put("/")
def update_note_rating(request, payload:NoteRatingIn):
    note_update = NoteRating.note_rating_update_data(payload.dict())
    if note_update:
       return 'success'
    return 'error'

