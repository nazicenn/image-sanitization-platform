🛡️ Image Sanitization Platform

Enterprise-grade privacy-focused image processing pipeline for metadata sanitization, optimization, and forensic trace reduction.

Overview

Image Sanitization Platform is a scalable, production-ready image processing system designed for secure and privacy-conscious media handling.

The platform provides:

Advanced metadata sanitization
Image optimization and compression
Asynchronous distributed processing
Secure API-based architecture
Monitoring and observability stack
Modular forensic-cleaning pipeline

Built with a modern cloud-native architecture using FastAPI, Celery, Redis, PostgreSQL, MinIO, and Docker/Kubernetes.

✨ Core Capabilities
Metadata Sanitization

Completely removes embedded metadata from uploaded images:

EXIF metadata
IPTC metadata
XMP metadata
PNG textual chunks
Camera/device information
GPS coordinates
Timestamps and software signatures
Image Optimization

Automatic image optimization pipeline:

WEBP conversion
Smart compression
Resolution normalization
Thumbnail generation
Storage-efficient encoding
Forensic Cleaning Pipeline

Multi-stage image normalization and artifact reduction system:

Frequency-domain normalization
Compression artifact balancing
Color-space normalization
Texture distribution smoothing
Sensor-noise equalization
Statistical image refinement
Distributed Async Processing

Built for scalability using background workers:

Celery task queues
Redis broker/backend
Retry mechanisms
Parallel processing
Queue monitoring
Job lifecycle tracking
Enterprise Security

Security-first architecture:

API key authentication
Rate limiting
File validation
MIME verification
CORS policies
Structured logging
Monitoring & Observability

Integrated observability stack:

Prometheus metrics
Grafana dashboards
Health probes
Queue monitoring
Processing duration metrics
Structured JSON logs
🏗️ Architecture
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
🧰 Technology Stack
Backend
Technology	Purpose
Python 3.10	Core programming language
FastAPI	High-performance API framework
SQLAlchemy	ORM layer
Alembic	Database migrations
Celery	Distributed task queue
Redis	Broker & caching
Pillow	Image manipulation
OpenCV	Computer vision operations
Scikit-Image	Image processing algorithms
Frontend
Technology	Purpose
React 18	Frontend framework
TypeScript	Type-safe development
Vite	Build tooling
Tailwind CSS	UI styling
Axios	API communication
Infrastructure
Technology	Purpose
Docker	Containerization
Kubernetes	Orchestration
Nginx	Reverse proxy
GitHub Actions	CI/CD
Terraform	Infrastructure as Code
Storage & Data
Technology	Purpose
PostgreSQL	Relational database
TimescaleDB	Time-series extension
MinIO	S3-compatible object storage
Monitoring
Technology	Purpose
Prometheus	Metrics collection
Grafana	Visualization dashboards
📁 Project Structure
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
🚀 API Endpoints
Method	Endpoint	Description	Authentication
POST	/api/v1/upload	Upload and process image	✅
GET	/api/v1/status/{job_id}	Retrieve processing status	❌
GET	/api/v1/download/{job_id}	Download processed image	❌
GET	/health	Liveness probe	❌
GET	/ready	Readiness probe	❌
GET	/metrics	Prometheus metrics	❌
⚙️ Processing Pipeline
1. Upload Validation
File integrity validation
MIME verification
Size limitation checks
Security validation
2. Metadata Sanitization
EXIF removal
XMP cleanup
IPTC cleanup
PNG chunk stripping
3. Image Optimization
Compression
Resizing
Format conversion
Thumbnail generation
4. Forensic Cleaning
Frequency normalization
Noise balancing
Texture harmonization
Compression normalization
5. Secure Delivery
Object storage upload
Signed retrieval
Download endpoint generation
🔐 Security Features
✔ API Key Authentication
✔ Request Rate Limiting
✔ File Integrity Validation
✔ MIME-Type Verification
✔ Structured Logging
✔ CORS Policies
✔ Async Isolation
✔ Secure Object Storage
📊 Monitoring Stack
Prometheus Metrics

Tracked metrics include:

Queue sizes
Processing durations
Request throughput
Error rates
Worker health
Storage usage
Grafana Dashboards

Included dashboards:

API performance
Worker activity
Queue analytics
Infrastructure monitoring
System health overview
🚀 Quick Start
Prerequisites
Docker
Docker Compose
Python 3.10+
Node.js 18+
Clone Repository
git clone https://github.com/nazicenn/image-sanitization-platform.git
cd image-sanitization-platform
Environment Configuration
cp .env.example .env

Update your environment variables.

Start Services
docker-compose up -d --build
Access Services
Service	URL
API	http://localhost:8000
Swagger Docs	http://localhost:8000/docs
MinIO Console	http://localhost:9001
Prometheus	http://localhost:9090
Grafana	http://localhost:3000
Frontend	http://localhost:5173
🧪 Example Request
curl -X POST \
  -H "X-API-Key: your-api-key" \
  -F "file=@image.jpg" \
  http://localhost:8000/api/v1/upload
🐳 Docker Services
Container	Description
sanitizer-api	FastAPI backend
sanitizer-db	PostgreSQL database
sanitizer-redis	Redis broker
sanitizer-storage	MinIO object storage
sanitizer-worker	Celery worker
sanitizer-prometheus	Prometheus
sanitizer-grafana	Grafana
🧪 Testing
Backend Tests
pytest tests/ -v --cov=app
Frontend Tests
cd frontend
npm test
Load Testing
k6 run load-test.js
📦 Environment Variables
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
☁️ Deployment

The platform supports:

Docker Compose deployments
Kubernetes deployments
Cloud-native scaling
Horizontal worker scaling
Infrastructure-as-Code provisioning
📈 Scalability

Designed for production workloads:

Stateless API architecture
Horizontally scalable workers
Distributed task queues
Object-storage abstraction
Cloud-native infrastructure
🤝 Contributing

Contributions are welcome.

Development Workflow
Fork the repository
Create a feature branch
Commit changes
Push updates
Open a Pull Request
📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Developed by nazicenn

GitHub Repository:

image-sanitization-platform

⭐ Acknowledgements

Special thanks to the communities behind:

FastAPI
Celery
PostgreSQL
MinIO
OpenCV
<div align="center">
Built for secure, scalable, privacy-first image processing.
</div>
