from django.http import HttpResponse
import asyncio
import websockets
from django.utils import timezone


CONECTINGS = {}

async def test_websocket_batch(s='Hello World',receiver="user",sender="system"):
   try:
      i = 1
      while i < 2:
         await send_message()
         i = i + 1
   except:
      pass
   return HttpResponse("hello")



WsBaseUrl = "ws://127.0.0.1:6069/?"

async def send_message(s='Hello World',receiver="user",sender = 'system'):
    async with websockets.connect(WsBaseUrl + "sender=" + sender + "&receiver=" + receiver) as websocket:
        await websocket.send(s)

