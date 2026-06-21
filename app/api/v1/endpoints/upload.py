from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
import uuid
from datetime import datetime
import os
from PIL import Image
import io

from app.db import get_db
from app.models import ProcessingJob, JobStatus
from app.services.validator import validate_image
from app.services.sanitizer import sanitize_image
from app.workers.tasks import process_image_task

router = APIRouter()

@router.post("/upload")
async def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # 1. Dosyayı validate et
    is_valid, error = validate_image(file)
    if not is_valid:
        raise HTTPException(400, error)
    
    # 2. Dosyayı oku ve geçici kaydet
    content = await file.read()
    
    # 3. Job oluştur (status: pending)
    job = ProcessingJob(
        original_filename=file.filename,
        original_size=file.size or len(content),
        status=JobStatus.PENDING,
        created_at=datetime.utcnow()
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    
    try:
        # 4. Dosyayı geçici kaydet
        temp_path = f"/app/storage/{job.id}.tmp"
        os.makedirs("/app/storage", exist_ok=True)
        with open(temp_path, "wb") as f:
            f.write(content)
        job.original_path = temp_path
        db.commit()
        
        # 5. Celery task'ini başlat
        process_image_task.delay(str(job.id))
        
        return {
            "job_id": str(job.id),
            "status": "queued",
            "message": "Image queued for processing",
            "check_status": f"/api/v1/status/{job.id}"
        }
        
    except Exception as e:
        job.status = JobStatus.FAILED
        job.error_message = str(e)
        db.commit()
        raise HTTPException(500, f"Failed to queue job: {str(e)}")