from fastapi import UploadFile
import os

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".heic"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def validate_image(file: UploadFile) -> tuple:
    # Boyut kontrolü
    if file.size and file.size > MAX_FILE_SIZE:
        return False, f"File too large. Max: {MAX_FILE_SIZE/1024/1024}MB"
    
    # Dosya uzantısı kontrolü
    filename = file.filename.lower()
    ext = os.path.splitext(filename)[1]
    if ext not in ALLOWED_EXTENSIONS:
        return False, f"Unsupported file extension: {ext}. Allowed: {ALLOWED_EXTENSIONS}"
    
    return True, None