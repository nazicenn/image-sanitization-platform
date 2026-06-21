from sqlalchemy import Column, String, Integer, DateTime, JSON, BigInteger, Text, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base
import uuid
from datetime import datetime
import enum

class JobStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

class ProcessingJob(Base):
    __tablename__ = "processing_jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(SQLEnum(JobStatus), default=JobStatus.PENDING, nullable=False)

    # Dosya bilgileri
    original_filename = Column(String(255), nullable=False)
    original_size = Column(BigInteger, nullable=False)
    processed_size = Column(BigInteger, nullable=True)
    mime_type = Column(String(100), nullable=True)
    file_hash = Column(String(64), nullable=True)

    # Storage paths
    original_path = Column(String(500), nullable=True)
    processed_path = Column(String(500), nullable=True)
    thumbnail_path = Column(String(500), nullable=True)

    # İşlem parametreleri
    options = Column(JSON, default={})
    error_message = Column(Text, nullable=True)

    # Retry
    retry_count = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)

    # Zaman damgaları
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    expires_at = Column(DateTime, nullable=True)

    # Metrikler
    processing_time_ms = Column(Integer, nullable=True)
    memory_usage_mb = Column(Integer, nullable=True)

    # Güvenlik
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(String(255), nullable=True)
    api_key_id = Column(String(36), nullable=True)

    # Soft delete
    deleted_at = Column(DateTime, nullable=True)