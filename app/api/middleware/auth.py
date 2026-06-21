from fastapi import HTTPException, Security, Depends
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
import hashlib

from app.db import get_db
from app.models import APIKey

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def verify_api_key(
    api_key: str = Security(api_key_header),
    db: Session = Depends(get_db)
):
    if not api_key:
        raise HTTPException(status_code=401, detail="API Key required")
    
    key_hash = hashlib.sha256(api_key.encode()).hexdigest()
    
    db_key = db.query(APIKey).filter(
        APIKey.key_hash == key_hash,
        APIKey.is_active == True
    ).first()
    
    if not db_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    from datetime import datetime
    db_key.last_used_at = datetime.utcnow()
    db.commit()
    
    return db_key