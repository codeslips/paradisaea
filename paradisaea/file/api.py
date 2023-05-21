from ninja import Router
from .ninja.file import router as fileRouter


router = Router()

router.add_router("/", fileRouter, tags=["file"])
