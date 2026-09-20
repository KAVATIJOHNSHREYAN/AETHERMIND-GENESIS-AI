import io
import zipfile

def generate_deployment_configs(domain: str) -> dict:
    """
    Phase 7: Generates production deployment manifests for Dockerfile, Docker Compose, Nginx,
    GitHub Actions, Kubernetes, Terraform, AWS, Azure, and GCP.
    """
    dockerfile = """# AetherMind Genesis Production Dockerfile
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
"""

    docker_compose = """version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/appdb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: appdb
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pgdata:
"""

    nginx_conf = """events { worker_connections 1024; }

http {
    upstream backend {
        server api:8000;
    }

    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location /health {
            stub_status on;
        }
    }
}
"""

    github_actions = """name: AetherMind Genesis CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run Tests
        run: pytest
      - name: Build Docker Image
        run: docker build -t aethermind-app:${{ github.sha }} .
"""

    kubernetes_yaml = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: aethermind-api
  labels:
    app: aethermind
spec:
  replicas: 3
  selector:
    matchLabels:
      app: aethermind
  template:
    metadata:
      labels:
        app: aethermind
    spec:
      containers:
      - name: api
        image: aethermind-app:latest
        ports:
        - containerPort: 8000
        resources:
          limits:
            cpu: "500m"
            memory: "512Mi"
          requests:
            cpu: "250m"
            memory: "256Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: aethermind-service
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8000
  selector:
    app: aethermind
"""

    terraform_tf = """# Terraform Main Configuration - AWS Provider
provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "aethermind_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = { Name = "aethermind-vpc" }
}

resource "aws_ecs_cluster" "aethermind_cluster" {
  name = "aethermind-genesis-cluster"
}
"""

    aws_config = """# AWS ECS & RDS Multi-AZ Cloud Stack Config
aws ecs create-cluster --cluster-name aethermind-prod
aws rds create-db-instance --db-instance-identifier aethermind-db --db-instance-class db.t4g.micro --engine postgres
"""

    azure_config = """# Azure AKS & Database for PostgreSQL Config
az group create --name aethermind-rg --location eastus
az aks create --resource-group aethermind-rg --name aethermindAKS --node-count 3
"""

    gcp_config = """# GCP GKE Cluster & Cloud SQL Config
gcloud container clusters create aethermind-gke --num-nodes=3 --zone=us-central1-a
gcloud sql instances create aethermind-sql-db --tier=db-f1-micro --region=us-central1
"""

    return {
        "Dockerfile": dockerfile,
        "docker-compose.yml": docker_compose,
        "nginx.conf": nginx_conf,
        "github-actions.yml": github_actions,
        "k8s-deployment.yaml": kubernetes_yaml,
        "main.tf": terraform_tf,
        "aws-setup.sh": aws_config,
        "azure-setup.sh": azure_config,
        "gcp-setup.sh": gcp_config
    }

def create_zip_blueprint(blueprint_md: str, sql_schema: str, api_spec: str, configs: dict) -> bytes:
    """
    Phase 9: Bundles blueprint documents, schemas, specs, and deployment configs into a single downloadable ZIP.
    """
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("AetherMind_Master_Blueprint.md", blueprint_md)
        zf.writestr("schema.sql", sql_schema)
        zf.writestr("openapi_spec.json", api_spec)
        for fname, content in configs.items():
            zf.writestr(f"deployment/{fname}", content)
    buffer.seek(0)
    return buffer.getvalue()
