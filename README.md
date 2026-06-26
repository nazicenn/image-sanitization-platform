<div align="center">

# 🛡️ Image Sanitization Platform

**Enterprise-grade, privacy-focused image processing pipeline for metadata sanitization, optimization, and forensic trace reduction.**

[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Production-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Scalable-326ce5?style=for-the-badge&logo=kubernetes)](https://kubernetes.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)](LICENSE)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Service Endpoints](#service-endpoints)
- [Configuration](#configuration)
- [Monitoring & Observability](#monitoring--observability)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Image Sanitization Platform** is a scalable, production-ready infrastructure for secure and privacy-conscious media handling. It ingests images, strips identifying metadata, normalizes file characteristics, and returns optimized output through a fully asynchronous, horizontally scalable pipeline.

The platform is built on a modern cloud-native stack and is designed to be deployed standalone, behind an existing API gateway, or as part of a larger media-processing system.

**Core capabilities:**

| Capability | Description |
|---|---|
| Metadata Sanitization | Strips EXIF, IPTC, XMP, and embedded device/location data |
| Image Optimization | Compression, format conversion, and resolution normalization |
| Forensic Trace Reduction | Multi-stage normalization to reduce residual artifacts |
| Distributed Processing | Asynchronous task queue with horizontal worker scaling |
| Secure API | Authenticated, rate-limited, validated request handling |
| Observability | Full metrics and dashboarding via Prometheus/Grafana |

---

## Key Features

### 🔒 Metadata Sanitization

Removes embedded metadata that could identify a device, location, or originator:

- EXIF metadata
- IPTC metadata
- XMP metadata
- PNG textual chunks
- Camera make/model information
- GPS coordinates
- Device-specific signatures
- Original timestamps

### 🖼️ Image Optimization

An automated pipeline for storage- and bandwidth-efficient delivery:

- WebP conversion
- Smart, quality-aware compression
- Resolution normalization
- Thumbnail generation
- Storage-efficient encoding

### 🧠 Forensic Cleaning Pipeline

A multi-stage normalization pass intended to reduce residual processing artifacts and standardize image statistics across the output set:

- Frequency-domain normalization
- Compression artifact balancing
- Color-space normalization
- Texture smoothing
- Sensor-noise equalization
- Statistical refinement

### ⚡ Asynchronous Distributed Processing

A scalable background-processing architecture built on Celery and Redis:

- Celery task queues
- Redis broker/backend
- Automatic retry handling
- Parallel worker pools
- Queue depth and throughput monitoring
- Full job lifecycle tracking

### 🛡️ Security

A security-first request and processing pipeline:

- API key authentication
- Per-key rate limiting
- File validation (size, dimensions, integrity)
- MIME-type verification independent of file extension
- Structured, auditable logging
- CORS policy enforcement

### 📊 Monitoring & Observability

An integrated observability stack for production operation:

- Prometheus metrics export
- Pre-built Grafana dashboards
- Liveness/readiness health probes
- Queue and worker metrics
- Per-stage processing duration metrics
- Structured JSON logs

---

## System Architecture

```text
                    ┌──────────┐
                    │  Client  │
                    └────┬─────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  NGINX Reverse Proxy │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  FastAPI Application │
              └──────────┬──────────┘
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
      ┌───────────┐ ┌───────────┐ ┌───────────┐
      │PostgreSQL │ │   Redis   │ │   MinIO   │
      └───────────┘ └───────────┘ └───────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Celery Workers     │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Image Processing      │
              │ Pipeline               │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Monitoring Stack     │
              │ (Prometheus + Grafana)│
              └─────────────────────┘
```

---

## Technology Stack

### Backend

| Technology | Purpose |
|---|---|
| Python 3.10 | Core language |
| FastAPI | API framework |
| SQLAlchemy | ORM |
| Alembic | Database migrations |
| Celery | Distributed task queue |
| Redis | Broker & caching layer |
| Pillow | Core image processing |
| OpenCV | Computer vision operations |
| scikit-image | Advanced processing algorithms |

### Frontend

| Technology | Purpose |
|---|---|
| React 18 | Frontend framework |
| TypeScript | Static typing |
| Vite | Build tooling |
| Tailwind CSS | UI styling |
| Axios | API communication |

### Infrastructure

| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Kubernetes | Orchestration |
| NGINX | Reverse proxy |
| GitHub Actions | CI/CD |
| Terraform | Infrastructure as Code |

---

## Getting Started

### Prerequisites

- Docker 24+ and Docker Compose
- 4 GB+ available RAM (recommended for local worker pools)
- Ports `8000`, `9001`, `9090`, `3000`, and `5173` available locally

### Installation

```bash
# Clone the repository
git clone https://github.com/nazicenn/image-sanitization-platform.git
cd image-sanitization-platform

# Build and start all services
docker-compose up -d --build
```

### Verifying the Installation

```bash
# Check that all containers are healthy
docker-compose ps

# Tail API logs
docker-compose logs -f api
```

---

## Service Endpoints

| Service | URL | Description |
|---|---|---|
| API | http://localhost:8000 | Core REST API |
| Swagger Docs | http://localhost:8000/docs | Interactive API documentation |
| MinIO Console | http://localhost:9001 | Object storage management |
| Prometheus | http://localhost:9090 | Metrics collection |
| Grafana | http://localhost:3000 | Dashboards & visualization |
| Frontend | http://localhost:5173 | Web client |

---

## Configuration

Configuration is managed via environment variables, typically supplied through a `.env` file at the project root. At minimum, set:

```env
API_KEY_SECRET=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
REDIS_URL=
MINIO_ROOT_USER=
MINIO_ROOT_PASSWORD=
```

See `docker-compose.yml` for the full list of supported variables and defaults.

---

## Monitoring & Observability

Metrics are exposed in Prometheus format at `/metrics` and scraped automatically by the bundled Prometheus instance. Pre-configured Grafana dashboards cover:

- Request throughput and latency
- Queue depth and worker utilization
- Per-stage processing duration
- Error rates by endpoint

---

## Security

- All write endpoints require API key authentication.
- Uploaded files are validated for size, dimensions, and MIME type prior to processing.
- Rate limiting is enforced per API key to mitigate abuse.
- All requests and processing events are logged in structured JSON for auditability.

If you discover a security vulnerability, please report it privately rather than opening a public issue.

---

## Contributing

Contributions are welcome. Please open an issue to discuss significant changes before submitting a pull request, and ensure new code is covered by tests where applicable.

---

## License

Licensed under the [MIT License](LICENSE).

<div align="center">

Built for secure, scalable, privacy-first image processing.

</div>
