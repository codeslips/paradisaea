from ninja import Router
from .napi.status import router as TodoStatusRouter
from .napi.crud import router as TodoCRUDRouter

router = Router()

router.add_router("/status", TodoStatusRouter, tags=["todo"])
router.add_router("/", TodoCRUDRouter, tags=["todo"])

