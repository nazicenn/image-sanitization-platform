from PIL import Image
import io

def sanitize_image(image_data: bytes) -> bytes:
    """EXIF/IPTC/XMP metadata'larını temizle"""
    img = Image.open(io.BytesIO(image_data))
    
    # Yeni bir image oluştur (metadata'sız)
    data = list(img.getdata())
    img_clean = Image.new(img.mode, img.size)
    img_clean.putdata(data)
    
    # JPEG ise RGB'ye çevir
    if img.format == 'JPEG':
        if img_clean.mode in ('RGBA', 'LA', 'P'):
            img_clean = img_clean.convert('RGB')
    
    output = io.BytesIO()
    img_clean.save(output, format='PNG')  # Metadata kaybetmeden PNG olarak kaydet
    return output.getvalue()
