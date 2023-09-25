from fastapi import APIRouter

from app.api.api_v1.endpoints.ok import router as ok_router

api_router = APIRouter()
api_router.include_router(ok_router, tags=["ok"])
