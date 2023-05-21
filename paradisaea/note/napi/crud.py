from ninja import Router
from datetime import date
from ninja import Schema,Router
from typing import List
from ..models import ListModel
from ..dbm import entry as NoteEntry


router = Router()

class NoteOut(Schema):
    note_code: str
    note: str
    note_title: str    
    note_tags: list
    rating: int
    creater: str
    is_delete: bool
    create_time: date
    update_time: date
    
class NoteIn(Schema):
    note: str
    note_code:str = None
    note_title: str    
    note_tags: list = None
    rating: int
    creater: str

@router.get("/",response=NoteOut)
def get_note(request,note_code: str):
    note = ListModel.objects.filter(note_code=note_code).first()
    if note:
       return note
    return {}


@router.post("/",response=NoteOut)
def create_note(request,payload: NoteIn):
    note = NoteEntry.note_entry(payload.dict())
    if note:
       return note
    return {}




