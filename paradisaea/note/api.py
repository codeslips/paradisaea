from ninja import Router
from .napi.rating import router as NoteRatingRouter
from .napi.crud import router as NoteCRUDRouter

router = Router()

router.add_router("/rating", NoteRatingRouter, tags=["note"])
router.add_router("/", NoteCRUDRouter, tags=["note"])

