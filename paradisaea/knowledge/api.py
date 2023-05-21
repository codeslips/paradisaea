from ninja import Router
from .ninja.rating import router as KnowRatingRouter
from .ninja.crud import router as KnowCRUDRouter

router = Router()

router.add_router("/rating", KnowRatingRouter, tags=["know"])
router.add_router("/", KnowCRUDRouter, tags=["know"])

