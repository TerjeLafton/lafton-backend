from fastapi import APIRouter

from app.api.endpoints import albums

router = APIRouter(prefix="/api")
router.include_router(albums.router)
