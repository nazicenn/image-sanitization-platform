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

# 🚀 Quick Start

## Clone Repository

```bash
git clone https://github.com/nazicenn/image-sanitization-platform.git

cd image-sanitization-platform
```

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

# 📄 License

Licensed under the MIT License.

---

<p align="center">
Built for secure, scalable, privacy-first image processing.
</p>
