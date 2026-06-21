from celery import Celery
import os

# Redis URL
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

# Celery app
celery_app = Celery(
    "image_sanitizer",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["app.workers.tasks"]
)

# Celery config
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=300,  # 5 dakika
    task_soft_time_limit=240,  # 4 dakika
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    task_default_retry_delay=60,
    task_max_retries=3,
)

if __name__ == "__main__":
    celery_app.start() 
