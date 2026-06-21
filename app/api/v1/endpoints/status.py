from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import ProcessingJob

router = APIRouter()

@router.get("/status/{job_id}")
async def get_job_status(
    job_id: str,
    db: Session = Depends(get_db)
):
    job = db.query(ProcessingJob).filter(ProcessingJob.id == job_id).first()
    if not job:
        raise HTTPException(404, "Job not found")
    
    response = {
        "job_id": str(job.id),
        "status": job.status.value,
        "original_filename": job.original_filename,
        "original_size": job.original_size,
        "created_at": job.created_at.isoformat() if job.created_at else None,
        "started_at": job.started_at.isoformat() if job.started_at else None,
        "completed_at": job.completed_at.isoformat() if job.completed_at else None,
    }
    
    if job.status.value == "completed":
        response["download_url"] = f"/api/v1/download/{job.id}"
        response["processed_size"] = job.processed_size
        response["processing_time_ms"] = job.processing_time_ms
    
    if job.status.value == "failed":
        response["error_message"] = job.error_message
    
    return response 
