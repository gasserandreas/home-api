from fastapi import APIRouter
from app.api.v1.endpoints import coffee

router = APIRouter()
router.include_router(coffee.router, prefix="/coffee", tags=["coffee"]) 