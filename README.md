# 🛡️ Image Sanitization Platform

> Enterprise-grade privacy-focused image processing pipeline for metadata sanitization, optimization, and forensic trace reduction.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Production-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker">
  <img src="https://img.shields.io/badge/Kubernetes-Scalable-326ce5?style=for-the-badge&logo=kubernetes">
  <img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge">
</p>

---

# 📖 Overview

**Image Sanitization Platform** is a scalable and production-ready image processing infrastructure designed for secure and privacy-conscious media handling.

The platform provides:

* Metadata sanitization
* Image optimization & compression
* Distributed asynchronous processing
* Secure API architecture
* Monitoring & observability stack
* Advanced forensic-cleaning pipeline

Built with a modern cloud-native stack using:

* FastAPI
* Celery
* Redis
* PostgreSQL
* MinIO
* Docker
* Kubernetes

---

# ✨ Features

## 🔒 Metadata Sanitization

Removes embedded metadata from uploaded images:

* EXIF metadata
* IPTC metadata
* XMP metadata
* PNG textual chunks
* Camera information
* GPS coordinates
* Device signatures
* Timestamps

---

## 🖼️ Image Optimization

Automatic optimization pipeline:

* WEBP conversion
* Smart compression
* Resolution normalization
* Thumbnail generation
* Storage-efficient encoding

---

## 🧠 Forensic Cleaning Pipeline

Multi-stage image normalization system:

* Frequency-domain normalization
* Compression artifact balancing
* Color-space normalization
* Texture smoothing
* Sensor-noise equalization
* Statistical refinement

---

## ⚡ Async Distributed Processing

Scalable background processing architecture:

* Celery task queues
* Redis broker/backend
* Retry mechanisms
* Parallel workers
* Queue monitoring
* Job lifecycle tracking

---

## 🛡️ Security

Security-first architecture:

* API Key authentication
* Rate limiting
* File validation
* MIME verification
* Structured logging
* CORS protection

---

## 📊 Monitoring & Observability

Integrated monitoring stack:

* Prometheus metrics
* Grafana dashboards
* Health probes
* Queue metrics
* Processing duration metrics
* Structured JSON logs

---

# 🏗️ System Architecture

```text
Client
   │
   ▼
NGINX Reverse Proxy
   │
   ▼
FastAPI Application
   │
   ├── PostgreSQL
   ├── Redis
   ├── MinIO
   └── Celery Workers
            │
            ▼
   Image Processing Pipeline
            │
            ▼
 Monitoring Stack
(Prometheus + Grafana)
```

---

# 🧰 Technology Stack

## Backend

| Technology   | Purpose                |
| ------------ | ---------------------- |
| Python 3.10  | Core language          |
| FastAPI      | API framework          |
| SQLAlchemy   | ORM                    |
| Alembic      | Database migrations    |
| Celery       | Distributed task queue |
| Redis        | Broker & caching       |
| Pillow       | Image processing       |
| OpenCV       | Computer vision        |
| Scikit-Image | Processing algorithms  |

---

## Frontend

| Technology   | Purpose            |
| ------------ | ------------------ |
| React 18     | Frontend framework |
| TypeScript   | Type safety        |
| Vite         | Build tooling      |
| Tailwind CSS | UI styling         |
| Axios        | API communication  |

---

## Infrastructure

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Docker         | Containerization       |
| Kubernetes     | Orchestration          |
| Nginx          | Reverse proxy          |
| GitHub Actions | CI/CD                  |
| Terraform      | Infrastructure as Code |

---

## Storage & Database

| Technology  | Purpose               |
| ----------- | --------------------- |
| PostgreSQL  | Relational database   |
| TimescaleDB | Time-series extension |
| MinIO       | Object storage        |

---

## Monitoring

| Technology | Purpose            |
| ---------- | ------------------ |
| Prometheus | Metrics collection |
| Grafana    | Visualization      |

---

# 📁 Project Structure

```text
image-sanitization-platform/
│
├── app/
│   ├── api/
│   ├── db/
│   ├── models/
│   ├── services/
│   ├── storage/
│   ├── utils/
│   ├── workers/
│   └── main.py
│
├── frontend/
├── infrastructure/
├── docker/
├── scripts/
├── tests/
│
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── Makefile
│
├── README.md
├── API.md
├── ARCHITECTURE.md
└── DEPLOYMENT.md
```

---

# 🚀 API Endpoints

| Method | Endpoint                    | Description                | Auth |
| ------ | --------------------------- | -------------------------- | ---- |
| POST   | `/api/v1/upload`            | Upload & process image     | ✅    |
| GET    | `/api/v1/status/{job_id}`   | Retrieve processing status | ❌    |
| GET    | `/api/v1/download/{job_id}` | Download processed image   | ❌    |
| GET    | `/health`                   | Liveness probe             | ❌    |
| GET    | `/ready`                    | Readiness probe            | ❌    |
| GET    | `/metrics`                  | Prometheus metrics         | ❌    |

---

# ⚙️ Processing Pipeline

## 1. Upload Validation

* File integrity validation
* MIME verification
* Size limitation checks
* Security validation

---

## 2. Metadata Sanitization

* EXIF cleanup
* XMP cleanup
* IPTC cleanup
* PNG chunk stripping

---

## 3. Image Optimization

* Compression
* Resizing
* Format conversion
* Thumbnail generation

---

## 4. Forensic Cleaning

* Frequency normalization
* Noise balancing
* Texture harmonization
* Compression normalization

---

## 5. Secure Delivery

* Object storage upload
* Signed retrieval
* Download endpoint generation

---

# 🔐 Security Features

```text
✔ API Key Authentication
✔ Request Rate Limiting
✔ File Integrity Validation
✔ MIME-Type Verification
✔ Structured Logging
✔ CORS Policies
✔ Async Isolation
✔ Secure Object Storage
```

---

# 📊 Monitoring Stack

## Prometheus Metrics

Tracked metrics include:

* Queue sizes
* Processing durations
* Request throughput
* Error rates
* Worker health
* Storage usage

---

## Grafana Dashboards

Included dashboards:

* API performance
* Worker activity
* Queue analytics
* Infrastructure monitoring
* System health overview

---

# 🚀 Quick Start

## Prerequisites

* Docker
* Docker Compose
* Python 3.10+
* Node.js 18+

---

## Clone Repository

```bash
git clone https://github.com/nazicenn/image-sanitization-platform.git
cd image-sanitization-platform
```

---

## Environment Configuration

```bash
cp .env.example .env
```

Update environment variables as needed.

---

## Start Services

```bash
docker-compose up -d --build
```

---

# 🌐 Service URLs

| Service       | URL                        |
| ------------- | -------------------------- |
| API           | http://localhost:8000      |
| Swagger Docs  | http://localhost:8000/docs |
| MinIO Console | http://localhost:9001      |
| Prometheus    | http://localhost:9090      |
| Grafana       | http://localhost:3000      |
| Frontend      | http://localhost:5173      |

---

# 🧪 Example Request

```bash
curl -X POST \
  -H "X-API-Key: your-api-key" \
  -F "file=@image.jpg" \
  http://localhost:8000/api/v1/upload
```

---

# 🐳 Docker Services

| Container            | Description          |
| -------------------- | -------------------- |
| sanitizer-api        | FastAPI backend      |
| sanitizer-db         | PostgreSQL database  |
| sanitizer-redis      | Redis broker         |
| sanitizer-storage    | MinIO object storage |
| sanitizer-worker     | Celery worker        |
| sanitizer-prometheus | Prometheus           |
| sanitizer-grafana    | Grafana              |

---

# 🧪 Testing

## Backend Tests

```bash
pytest tests/ -v --cov=app
```

---

## Frontend Tests

```bash
cd frontend
npm test
```

---

## Load Testing

```bash
k6 run load-test.js
```

---

# 📦 Environment Variables

```env
# Database
DB_HOST=postgres
DB_PORT=5432
DB_NAME=sanitizer
DB_USER=user
DB_PASSWORD=password

# Redis
REDIS_HOST=redis
REDIS_PORT=6379

# MinIO
MINIO_ENDPOINT=minio:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin123

# Security
API_SECRET_KEY=your-secret-key
RATE_LIMIT_PER_MINUTE=100

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json
```

---

# ☁️ Deployment

Supported deployment environments:

* Docker Compose
* Kubernetes
* Cloud-native infrastructure
* Horizontal worker scaling
* Infrastructure-as-Code provisioning

---

# 📈 Scalability

Designed for production workloads:

* Stateless API architecture
* Horizontally scalable workers
* Distributed task queues
* Object-storage abstraction
* Cloud-native infrastructure

---

# 🤝 Contributing

Contributions are welcome.

## Development Workflow

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push updates
5. Open a Pull Request

---

# 📄 License

Licensed under the **MIT License**.

---

# 👨‍💻 Author

Developed by **nazicenn**

GitHub:
https://github.com/nazicenn

---

# ⭐ Acknowledgements

Special thanks to the communities behind:

* FastAPI
* Celery
* PostgreSQL
* MinIO
* OpenCV
* Pillow

---

<p align="center">
  Built for secure, scalable, privacy-first image processing.
</p>
