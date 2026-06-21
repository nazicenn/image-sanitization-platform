CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

INSERT INTO system_settings (key, value, description) VALUES
('max_file_size', '{"bytes": 10485760, "human": "10MB"}', 'Maximum file size allowed'),
('allowed_formats', '["jpeg", "png", "webp", "heic"]', 'Allowed image formats'),
('max_image_pixels', '{"value": 50000000, "human": "50MP"}', 'Maximum image dimensions'),
('job_expiration_days', '{"value": 7}', 'Days until job expires'),
('cleanup_batch_size', '{"value": 100}', 'Batch size for cleanup jobs')
ON CONFLICT (key) DO NOTHING;