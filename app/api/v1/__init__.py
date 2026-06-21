from fastapi import APIRouter
from .endpoints import upload, download, status

router = APIRouter()
router.include_router(upload.router, prefix="/api/v1", tags=["upload"])
router.include_router(download.router, prefix="/api/v1", tags=["download"])
router.include_router(status.router, prefix="/api/v1", tags=["status"])