from prometheus_client import Counter, Histogram, Gauge, generate_latest, REGISTRY
from fastapi import Response

# Metrikler
jobs_total = Counter(
    "image_sanitization_jobs_total",
    "Total number of jobs",
    ["status"]
)

jobs_processing_duration = Histogram(
    "image_sanitization_jobs_processing_duration_seconds",
    "Time spent processing images",
    buckets=[0.5, 1, 2, 5, 10, 30, 60]
)

active_jobs = Gauge(
    "image_sanitization_active_jobs",
    "Number of currently active jobs"
)

queue_size = Gauge(
    "image_sanitization_queue_size",
    "Number of jobs in queue"
)

http_requests_total = Counter(
    "image_sanitization_http_requests_total",
    "Total HTTP requests",
    ["endpoint", "method", "status"]
)

http_request_duration = Histogram(
    "image_sanitization_http_request_duration_seconds",
    "HTTP request duration",
    ["endpoint", "method"],
    buckets=[0.01, 0.05, 0.1, 0.5, 1, 2, 5, 10]
)

storage_used_bytes = Gauge(
    "image_sanitization_storage_used_bytes",
    "Total storage used in bytes"
)

storage_file_count = Gauge(
    "image_sanitization_storage_file_count",
    "Total number of files in storage"
)

def get_metrics():
    return Response(generate_latest(REGISTRY), media_type="text/plain") 
