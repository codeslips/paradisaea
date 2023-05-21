from ninja import Router
from datetime import date
from ninja import Schema,Router
from typing import List
from ..dbm import status as Status


router = Router()

class TodoStatusIn(Schema):
   todo_code: str = None
   status: int = None
   updateStatus: int = None

class TodoStatusOut(Schema):
   content: str
   tips: str
   fileInfo: dict


@router.put("/")
def update_note_rating(request, payload:TodoStatusIn):
    todo_update = Status.todo_status_update_data(payload.dict())
    if todo_update:
       return 'success'
    return 'error'

