from ninja import Router
from datetime import date
from ninja import Schema,Router
from ..models import ListModel as BambooOpenModel
from django.shortcuts import get_object_or_404
from typing import List


router = Router()

class BambooOpenIn(Schema):
    open_name: str
    open_int: int
    creater: str = None
    update_time: date = None

class BambooOpenOut(Schema):
    open_name: str
    open_int: int
    open_float: float
    open_text: str


@router.post("/bamboo")
def create_bamboo(request, payload:BambooOpenIn):
    bamboo = BambooOpenModel.objects.create(**payload.dict())
    return {"bamboo": bamboo.open_name}

@router.get("/bamboo/{open_id}",response=BambooOpenOut)
def get_bamboo_open(request,open_id:int):
    bamboo_open = get_object_or_404(BambooOpenModel,open_id=open_id)
    return bamboo_open

@router.get("/bamboo",response=List[BambooOpenOut])
def list_bamboo_open(request):
    qs = BambooOpenModel.objects.all()
    return qs


@router.put("/bamboo/{open_id}")
def update_bamboo(request,open_id:int,payload:BambooOpenIn):
    bamboo = get_object_or_404(BambooOpenModel,open_id=open_id)
    for attr,value in payload.dict().items():
        setattr(bamboo,attr,value)
        bmaboo.save()
    return {"success": True}

@router.delete("/bmaboo/{open_id}")
def delete_bmaboo(request,open_id: int):
    bamboo = get_object_or_404(BambooOpenModel,open_id=open_id)
    bamboo.delete()
    return {"success": True}