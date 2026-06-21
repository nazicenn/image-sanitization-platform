# Image Sanitization Platform

Privacy-first image processing pipeline with FastAPI, PostgreSQL, Celery, and MinIO.

## Features

- Upload images (async with Celery)
- Remove EXIF/IPTC/XMP metadata
- Convert to WebP format
- Job status tracking
- Download processed images
- Docker Compose for local development

## Quick Start

```bash
git clone https://github.com/nazicenn/image-sanitization-platform.git
cd image-sanitization-platform
docker-compose up -d --build

API Endpoints
Method	Endpoint	Description
POST	/api/v1/upload	Upload an image
GET	/api/v1/status/{job_id}	Check job status
GET	/api/v1/download/{job_id}	Download processed image
Tech Stack
API: FastAPI

Database: PostgreSQL

Queue: Celery + Redis

Storage: MinIO

Processing: Pillow

Container: Docker Compose