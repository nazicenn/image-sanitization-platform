from celery import Task
from app.workers.celery_app import celery_app
from app.db.session import SessionLocal
from app.models import ProcessingJob, JobStatus
from app.services.sanitizer import sanitize_image
from PIL import Image
import io
import os
from datetime import datetime
import uuid

class ProcessImageTask(Task):
    _db = None

    @property
    def db(self):
        if self._db is None:
            self._db = SessionLocal()
        return self._db

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        if self._db is not None:
            self._db.close()

@celery_app.task(bind=True, base=ProcessImageTask, max_retries=3)
def process_image_task(self, job_id: str):
    """
    Image processing task
    """
    db = self.db

    try:
        # 1. Job'u bul
        job = db.query(ProcessingJob).filter(ProcessingJob.id == job_id).first()
        if not job:
            raise ValueError(f"Job {job_id} not found")

        # 2. Status: processing
        job.status = JobStatus.PROCESSING
        job.started_at = datetime.utcnow()
        db.commit()

        # 3. Dosyayı oku (storage'dan)
        filepath = job.original_path
        if not filepath or not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        with open(filepath, "rb") as f:
            content = f.read()

        # 4. Metadata temizle
        cleaned = sanitize_image(content)

        # 5. WEBP'ye dönüştür
        img = Image.open(io.BytesIO(cleaned))
        if img.width > 1920 or img.height > 1080:
            img.thumbnail((1920, 1080), Image.Resampling.LANCZOS)

        output = io.BytesIO()
        img.save(output, format="WEBP", quality=92, method=6)
        processed_data = output.getvalue()

        # 6. Kaydet
        filename = f"{job_id}.webp"
        processed_path = f"/app/storage/{filename}"
        os.makedirs("/app/storage", exist_ok=True)
        with open(processed_path, "wb") as f:
            f.write(processed_data)

        # 7. Job'u güncelle
        job.processed_size = len(processed_data)
        job.processed_path = processed_path
        job.status = JobStatus.COMPLETED
        job.completed_at = datetime.utcnow()
        job.processing_time_ms = int((datetime.utcnow() - job.started_at).total_seconds() * 1000)
        db.commit()

        return {
            "job_id": str(job.id),
            "status": "completed",
            "processed_size": job.processed_size,
            "download_url": f"/api/v1/download/{job.id}"
        }

    except Exception as e:
        # Hata durumunda job'u güncelle
        job = db.query(ProcessingJob).filter(ProcessingJob.id == job_id).first()
        if job:
            job.status = JobStatus.FAILED
            job.error_message = str(e)
            job.completed_at = datetime.utcnow()
            db.commit()

        # Retry
        if self.request.retries < self.max_retries:
            raise self.retry(exc=e, countdown=60 * (self.request.retries + 1))
        raise
