from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn
import os
from dotenv import load_dotenv
from datetime import datetime

from app.db import get_db, engine, Base
from app.api import router as api_router
from app.utils.metrics import get_metrics

load_dotenv()

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)
print("✅ Database tables created")

app = FastAPI(
    title="Image Sanitization Platform",
    version="1.0.0",
    description="Privacy-first image processing backend",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API router'larını ekle
app.include_router(api_router)

@app.get("/")
async def root():
    return {
        "service": "Image Sanitization Platform",
        "version": "1.0.0",
        "status": "healthy"
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.get("/ready")
async def ready(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "ready", "database": "connected"}
    except Exception as e:
        return {"status": "not ready", "database": "disconnected", "error": str(e)}

@app.get("/metrics")
async def metrics():
    return get_metrics()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.getenv("API_PORT", 8000)),
        reload=True
    )