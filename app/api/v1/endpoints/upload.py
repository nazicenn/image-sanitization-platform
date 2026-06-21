from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
import uuid
from datetime import datetime
import os
import shutil
from PIL import Image
import io

from app.db import get_db
from app.models import ProcessingJob, JobStatus
from app.services.validator import validate_image
from app.services.sanitizer import sanitize_image

router = APIRouter()

@router.post("/upload")
async def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # 1. Dosyayı validate et
    is_valid, error_message = validate_image(file)
    if not is_valid:
        raise HTTPException(400, error_message)
    
    # 2. Job oluştur
    job = ProcessingJob(
        original_filename=file.filename,
        original_size=file.size or 0,
        status=JobStatus.PROCESSING,
        created_at=datetime.utcnow()
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    
    try:
        # 3. Dosyayı oku
        contents = await file.read()
        
        # 4. Metadata temizle (EXIF, IPTC, XMP)
        cleaned_image = sanitize_image(contents)
        
        # 5. WEBP'ye dönüştür ve optimize et
        img = Image.open(io.BytesIO(cleaned_image))
        
        # Resize (max 1920x1080)
        if img.width > 1920 or img.height > 1080:
            img.thumbnail((1920, 1080), Image.Resampling.LANCZOS)
        
        # WEBP olarak kaydet
        output = io.BytesIO()
        img.save(output, format="WEBP", quality=92, method=6)
        processed_data = output.getvalue()
        
        # 6. Dosyayı kaydet (geçici olarak local)
        filename = f"{job.id}.webp"
        filepath = f"/app/storage/{filename}"
        
        os.makedirs("/app/storage", exist_ok=True)
        with open(filepath, "wb") as f:
            f.write(processed_data)
        
        # 7. Job'u güncelle
        job.processed_size = len(processed_data)
        job.processed_path = filepath
        job.status = JobStatus.COMPLETED
        job.completed_at = datetime.utcnow()
        db.commit()
        
        return {
            "job_id": str(job.id),
            "status": job.status,
            "original_filename": job.original_filename,
            "original_size": job.original_size,
            "processed_size": job.processed_size,
            "download_url": f"/api/v1/download/{job.id}"
        }
        
    except Exception as e:
        job.status = JobStatus.FAILED
        job.error_message = str(e)
        db.commit()
        raise HTTPException(500, f"Processing failed: {str(e)}")
