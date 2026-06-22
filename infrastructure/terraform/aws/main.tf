provider "aws" {
  region = "eu-west-1"
}

# VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = "image-sanitization-vpc"
  }
}

# Subnet'ler
resource "aws_subnet" "public" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true
  tags = {
    Name = "image-sanitization-subnet-${count.index}"
  }
}

# EKS Cluster
resource "aws_eks_cluster" "main" {
  name = "image-sanitization-cluster"
  role_arn = aws_iam_role.eks.arn
  vpc_config {
    subnet_ids = aws_subnet.public[*].id
  }
}

# RDS PostgreSQL
resource "aws_db_instance" "postgres" {
  identifier = "image-sanitization-db"
  engine = "postgres"
  engine_version = "15"
  instance_class = "db.t4g.micro"
  allocated_storage = 20
  db_name = "sanitizer"
  username = "user"
  password = random_password.db_password.result
  vpc_security_group_ids = [aws_security_group.db.id]
  publicly_accessible = false
  skip_final_snapshot = true
  tags = {
    Name = "image-sanitization-db"
  }
}

# S3 Bucket (MinIO yerine)
resource "aws_s3_bucket" "images" {
  bucket = "image-sanitization-${random_id.bucket_suffix.hex}"
  tags = {
    Name = "image-sanitization-bucket"
  }
}

# Output'lar
output "eks_cluster_name" {
  value = aws_eks_cluster.main.name
}

output "db_endpoint" {
  value = aws_db_instance.postgres.endpoint
}

output "s3_bucket_name" {
  value = aws_s3_bucket.images.bucket
}