import json

def export_blueprint_markdown(idea_title: str, scores: dict, debate_logs: list, mermaid_code: str, sql_schema: str, api_spec: str) -> str:
    """
    Phase 6: Synthesizes a comprehensive 12-Section Enterprise Software Blueprint Document.
    """
    domain = "FINTECH / GENERAL SAAS"
    if "fintech" in idea_title.lower(): domain = "FINTECH PLATFORM"
    elif "health" in idea_title.lower(): domain = "HEALTHCARE TELEHEALTH"
    elif "video" in idea_title.lower() or "ai" in idea_title.lower(): domain = "AI MEDIA GENERATION ENGINE"

    debate_summary = "\n".join([f"- **[{log['agent']}]** ({log.get('badge', 'Architect')}): {log.get('recommendation', '')}" for log in debate_logs])

    return f"""# 🌌 AetherMind Genesis - Master Enterprise Software Blueprint
**Project Title:** {idea_title}  
**Architecture Profile:** {scores.get('architecture_profile', 'Balanced Hybrid Cloud')}  
**Overall System Fitness Score:** {scores.get('overall_score', 85)}/100  
**Generated Date:** September 20, 2026 | *Autonomous AI System Architect*

---

## 1. 📌 Project Overview
The proposed software system **"{idea_title}"** is engineered as a high-availability, scalable solution in the **{domain}** space. This master technical specification synthesizes system topology, relational schemas, REST API endpoints, security compliance, deployment infrastructure, cost projections, development timelines, and risk mitigation strategies into a unified production blueprint.

---

## 2. 🎯 Core System Requirements
- **Functional Requirements**:
  - Secure User Authentication & Session Management (OAuth2 + PKCE / JWT).
  - High-throughput core transaction & application data processing.
  - Real-Time observability, logging, and status metric endpoints.
- **Non-Functional Requirements**:
  - **Security Index:** {scores.get('security_score', 85)}/100 (Zero-Trust Access, OWASP Top 10 Mitigation, TLS 1.3).
  - **Performance Index:** {scores.get('performance_score', 75)}/100 (Target Latency < 150ms, Sub-second response times).
  - **Scalability Index:** {scores.get('scalability_score', 78)}/100 (Horizontal container auto-scaling up to 10,000 RPS).

---

## 3. 🗺️ System Architecture & Topology
The architecture leverages a multi-tier decoupled topology connecting **Client Apps**, **Load Balancers**, **API Gateways**, **Auth Nodes**, **Backend Services Core**, **AI Engines**, **Vector Databases**, **SQL Databases**, **Redis Caches**, **Object Storage**, and **Observability Modules**.

```mermaid
{mermaid_code}
```

---

## 4. 🗄️ Database Architecture & DDL Schema
**Primary Database Engine:** {scores.get('recommended_db', 'PostgreSQL (RDS / Supabase)')}

```sql
{sql_schema}
```

---

## 5. 🔌 API Endpoint Specification (OpenAPI v3.0)
The backend exposes RESTful HTTPS endpoints with structured JSON request/response contracts and error handlers:

```json
{api_spec}
```

---

## 6. 📁 Recommended Production Folder Structure
```
app-root/
├── .github/workflows/ci-cd.yml    # CI/CD Automated Build & Deploy Pipeline
├── src/
│   ├── api/                       # REST/GraphQL Controllers & Route Handlers
│   ├── core/                      # Business Logic Engine & Services
│   ├── db/                        # DDL Migrations & ORM Schema Models
│   ├── security/                  # Encryption, Auth & OWASP Middleware
│   └── utils/                     # Shared Helper Utilities
├── tests/                         # E2E Playwright & Unit Test Suite
├── Dockerfile                     # Containerization Image Spec
├── docker-compose.yml             # Local Multi-Container Runtime
└── requirements.txt               # Dependencies Manifest
```

---

## 7. 🚀 Infrastructure & Deployment Strategy
- **Containerization:** Docker container images optimized with multi-stage builds.
- **Orchestration:** Managed Kubernetes (EKS / GKE) or Serverless Cloud Nodes (Vercel / Supabase / AWS ECS).
- **CI/CD Pipeline:** Automated GitHub Actions pipeline executing unit tests, security scans, and zero-downtime rolling deployments.

---

## 8. 🛡️ Security & Zero-Trust Compliance
- Mandatory TLS 1.3 encryption in transit; AES-256 field-level encryption for sensitive database storage.
- OAuth2 + PKCE authentication tokens with automated rotation.
- Web Application Firewall (WAF) rate-limiting against DDoS attacks and OWASP input sanitization.

---

## 9. ⚡ Performance & Optimization Strategy
- **Caching Layer:** In-memory Redis cluster for session states and high-frequency database queries.
- **Async Execution:** Asynchronous worker queues (Celery / RabbitMQ) for background tasks and AI model inference.
- **CDN Edge Acceleration:** Static assets cached on Cloudflare / Fastly CDN nodes.

---

## 10. 💰 Cost & Infrastructure Analysis
- **Estimated Cloud Budget:** `{scores.get('estimated_monthly_cost', '$50 - $120 / mo')}`
- **Cost Efficiency Score:** `{scores.get('cost_efficiency_score', 70)}/100`
- **Cost Allocation Breakdown:**
  - Database Hosting (Managed PostgreSQL): ~40%
  - Compute Nodes (Serverless / Containers): ~35%
  - Redis Memory Cache & CDN Storage: ~15%
  - Logging & Observability (Prometheus): ~10%

---

## 11. 📅 Development Roadmap & Timeline
```mermaid
gantt
    title System Development Execution Schedule
    dateFormat  YYYY-MM-DD
    section Phase 1: Foundation
    Requirements & DB Schema Setup    :a1, 2026-10-01, 10d
    Auth & API Gateway Core          :a2, after a1, 12d
    section Phase 2: Core Build
    Backend Services & AI Integration :b1, after a2, 20d
    Frontend UI & State Management    :b2, after a2, 18d
    section Phase 3: Launch
    Security Audit & E2E QA Testing  :c1, after b1, 10d
    Production Cloud Deployment       :c2, after c1, 5d
```

---

## 12. ⚠️ Risk Assessment & Mitigation
- **Risk 1: Database I/O Bottlenecks under peak loads.**  
  *Mitigation:* Implement read-replicas and aggressive Redis query caching.
- **Risk 2: Unauthorized API access attempts.**  
  *Mitigation:* Enforce strict OAuth2 token verification, WAF rate-limiting, and IP throttling.
- **Risk 3: Unexpected cloud compute cost overruns.**  
  *Mitigation:* Configure hard budget alerts and auto-scaling upper limits on cloud worker pools.

---
*Synthesized autonomously by **AetherMind Genesis - Enterprise AI System Architect***
"""
