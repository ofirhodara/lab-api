from fastapi import APIRouter

from app.api.api_v1.endpoints import ok

api_router = APIRouter()
api_router.include_router(ok.router, tags=["ok"])

