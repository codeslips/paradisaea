from ninja import Router
from datetime import date
from ninja import Schema,Router
from typing import List
from ..models import ListModel
from ..dbm import entry as Entry


router = Router()

class TodoOut(Schema):
    id: str = None
    todo_code: str = None
    todo_desc: str = None
    todo_title: str = None    
    todo_tags: list = None
    pervious: list = None    
    next: list = None    
    status: int = None
    creater: str = None
    is_delete: bool = None
    create_time: date = None
    update_time: date = None
    
class TodoIn(Schema):
    todo_code: str = None
    todo_desc: str = None
    todo_title: str    
    todo_tags: list = None
    pervious: list = None   
    next: list = None   
    status: int
    creater: str

@router.get("/",response=TodoOut)
def get_todo(request,todo_code: str):
    todo = ListModel.objects.filter(todo_code=todo_code).first()
    if todo:
       return todo
    return {}


@router.post("/",response=TodoOut)
def create_todo(request,payload: TodoIn):
    todo = Entry.todo_entry(payload.dict())
    if todo:
       return todo
    return {}




