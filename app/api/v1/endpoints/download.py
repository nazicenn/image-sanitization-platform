from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os

from app.db import get_db
from app.models import ProcessingJob, JobStatus

router = APIRouter()

@router.get("/download/{job_id}")
async def download_image(
    job_id: str,
    db: Session = Depends(get_db)
):
    # Job'u bul
    job = db.query(ProcessingJob).filter(ProcessingJob.id == job_id).first()
    if not job:
        raise HTTPException(404, "Job not found")
    
    # Tamamlanmış mı kontrol et
    if job.status != JobStatus.COMPLETED:
        raise HTTPException(400, f"Job not ready. Status: {job.status}")
    
    # Dosya var mı kontrol et
    if not job.processed_path or not os.path.exists(job.processed_path):
        raise HTTPException(404, "Processed file not found")
    
    # Dosyayı döndür
    return FileResponse(
        job.processed_path,
        filename=f"{job.original_filename}.webp",
        media_type="image/webp"
    ) 
