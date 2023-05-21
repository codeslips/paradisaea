from ninja import Router
from datetime import date
from ninja import Schema,Router
from django.shortcuts import get_object_or_404
from typing import List
from utils import postWS as WS
import asyncio

router = Router()


class SendSocketOut(Schema):
   message: str

class SendSocketIn(Schema):
   message: str
   sender: str
   receiver: str
   
@router.post("sendws/",response=SendSocketOut)
async def utils_send_websocket(request,payload:SendSocketIn):
   data = payload.dict()
   message = ''
   try:
      await WS.send_message(data["message"], data["receiver"], data["sender"])
      message = 'send ok'
   except:
      message = 'send error'      
   return { 'message': message }


   
@router.post("sendws/batch",response=SendSocketOut)
async def utils_send_websocket_batch(request,payload:SendSocketIn):
   data = payload.dict()
   message = ''
   try:
      await WS.test_websocket_batch(data["message"], data["receiver"], data["sender"])
      message = 'send ok'
   except:
      message = 'send error'      
   return { 'message': message }




