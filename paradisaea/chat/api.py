from ninja import Router
from .napi.chat import router as ChatRouter

router = Router()

router.add_router("/chat", ChatRouter, tags=["chat"])

