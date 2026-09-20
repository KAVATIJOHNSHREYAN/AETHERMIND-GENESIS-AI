from agents.parser import parse_prompt_requirements

def run_multi_agent_debate(prompt: str, sec_weight: float, perf_weight: float, cost_weight: float) -> dict:
    """
    STAGE 3: Multi-Agent Collaboration with 11 Agent Personas & Agent-to-Agent Challenges
    STAGE 4: Architecture Pattern Selection & Justification
    STAGE 5: Technology Stack & Deep Rationale
    STAGE 6: Deliverables (Dynamic DDL & OpenAPI v3.0 Spec)
    STAGE 7: AI Project Intelligence & Pipeline Topology
    """
    reqs = parse_prompt_requirements(prompt)
    main = reqs["main_entity"]
    sec_ents = reqs["secondary_entities"]
    domain = reqs["domain"]
    
    # ---------------------------------------------------------
    # STAGE 4: ARCHITECTURE PATTERN SELECTION
    # ---------------------------------------------------------
    if reqs["has_high_throughput"]:
        arch_pattern = "Event-Driven Async Microservices Topology"
        arch_justification = f"Chosen because high-frequency '{main}' telemetry and streaming require non-blocking event queues to isolate ingestion spikes from core state processors."
    elif reqs["has_finance"]:
        arch_pattern = "Event-Sourced CQRS Modular Hexagonal Architecture"
        arch_justification = f"Chosen because '{main}' ledger balance transitions require an append-only immutable event store paired with strict command-query separation to guarantee financial auditability."
    elif reqs["has_ai"]:
        arch_pattern = "Decoupled Asynchronous Microservices with GPU Inference Workers"
        arch_justification = f"Chosen to segregate web latency-sensitive '{main}' API endpoints from heavy ML model vector embeddings and LLM inference generation pools."
    else:
        arch_pattern = "Modular Hexagonal Monolith"
        arch_justification = f"Chosen to minimize operational friction while strictly enforcing domain boundaries around '{main}' domain logic."

    # ---------------------------------------------------------
    # STAGE 3: 11 AI ARCHITECT AGENT REASONING & CHALLENGES
    # ---------------------------------------------------------
    
    # 1. Lead Architect
    lead_agent = {
        "agent": "Lead Architect", "avatar": "👑", "role_color": "#3B82F6", "badge": "Strategy & Pattern",
        "recommendation": f"Establish {arch_pattern} centered on the primary '{main}' domain entity, segregating bounded contexts for {', '.join(sec_ents[:3])}.",
        "advantages": [f"Isolates core '{main}' state machine from third-party operational noise", f"Allows independent auto-scaling of high-load '{main}' worker pods"],
        "disadvantages": [f"Introduces distributed state consistency management across bounded context boundaries for {main}"],
        "confidence": min(98, 88 + len(reqs["all_entities"])),
        "challenge": "Rejects simple monolith due to long-term domain scaling bottlenecks under peak user load."
    }

    # 2. Security Architect
    sec_auth = "mTLS + OAuth2 Hardware-Backed Tokens & Field-Level AES-256 GCM" if reqs["has_finance"] else ("Zero-Trust OIDC / SAML SSO with Fine-Grained ABAC" if reqs["has_auth"] else "Stateless Asymmetric Ed25519 Signed JWT Tokens")
    sec_agent = {
        "agent": "Security Architect", "avatar": "🛡️", "role_color": "#22D3EE", "badge": "Zero-Trust Compliance",
        "recommendation": f"Enforce {sec_auth} alongside automated WAF rate limiting and strict OWASP Top 10 payload validation on all '{main}' routes.",
        "advantages": [f"Mitigates unauthorized data exfiltration for '{main}' payloads", "Prevents SQL injection and cross-site scripting (XSS) at gateway level"],
        "disadvantages": [f"Adds 8-15ms cryptographic validation overhead per '{main}' inbound request"],
        "confidence": reqs["sec_index"],
        "challenge": "Challenges Lead Architect: Demands payload payload decryption occur inside isolated enclave containers."
    }

    # 3. Backend Architect
    be_tech = "Rust (Axum / Tokio) high-concurrency microservices" if reqs["has_high_throughput"] else ("FastAPI (Python 3.11) with Pydantic v2 & AsyncIO" if reqs["has_ai"] else "Go (Golang 1.22) Fiber REST framework")
    be_queue = "Apache Kafka cluster with distributed consumer groups" if reqs["has_high_throughput"] else "RabbitMQ / Celery async task dispatchers"
    be_agent = {
        "agent": "Backend Architect", "avatar": "⚙️", "role_color": "#8B5CF6", "badge": "Runtime & Execution",
        "recommendation": f"Construct backend using {be_tech} integrated with {be_queue} for processing '{main}' pipelines.",
        "advantages": [f"Achieves non-blocking concurrency exceeding 25,000 RPS for '{main}' transactions", f"Offloads blocking compute tasks asynchronously via {be_queue}"],
        "disadvantages": [f"Requires stringent connection pooling configuration for downstream database services"],
        "confidence": 94,
        "challenge": "Challenges Frontend Architect: Direct GraphQL clients must not issue unbounded N+1 nested queries against the database."
    }

    # 4. Frontend Architect
    fe_tech = "Next.js 14 App Router with React Server Components & Tailwind CSS" if reqs["has_high_throughput"] else "Vite + React 18 SPA with Zustand & TanStack Query"
    fe_agent = {
        "agent": "Frontend Architect", "avatar": "🎨", "role_color": "#EC4899", "badge": "Client UI & Hydration",
        "recommendation": f"Engineer frontend utilizing {fe_tech} with optimistic UI state transitions and web-worker streaming for '{main}' dashboards.",
        "advantages": [f"Delivers sub-80ms First Contentful Paint (FCP) for '{main}' user interfaces", "Optimizes bundle size via modular tree-shaking"],
        "disadvantages": [f"Demands strict hydration synchronization between client state and edge cache"],
        "confidence": 91,
        "challenge": "Challenges Security Architect: OAuth token refreshes must be seamless and never freeze active user sessions."
    }

    # 5. Database Architect
    db_type = "PostgreSQL 16 with TimescaleDB Hyper-tables" if reqs["has_finance"] else ("PostgreSQL 16 + ScyllaDB Distributed NoSQL" if reqs["has_high_throughput"] else "PostgreSQL 16 Relational Database with pgvector Extension")
    db_agent = {
        "agent": "Database Architect", "avatar": "🗄️", "role_color": "#F59E0B", "badge": "Data Schema Topology",
        "recommendation": f"Provision {db_type} with composite B-Tree indexes and JSONB metadata columns optimized for '{main}' primary key lookup queries.",
        "advantages": [f"Guarantees strict ACID transactional guarantees for '{main}' updates", f"Accelerates join performance for related entities ({', '.join(sec_ents[:2])})"],
        "disadvantages": [f"Requires automated VACUUM and WAL log replication management"],
        "confidence": 95,
        "challenge": "Challenges Backend Architect: Unindexed ORM queries against table '{main}' will be killed automatically after 2000ms."
    }

    # 6. Cloud Architect
    cloud_provider = "AWS Enterprise (EKS, Aurora, ElastiCache, S3)" if reqs["has_high_throughput"] else "Google Cloud Platform (GKE, Cloud SQL, Vertex AI, Cloud Storage)"
    cloud_agent = {
        "agent": "Cloud Architect", "avatar": "☁️", "role_color": "#0EA5E9", "badge": "Multi-Region Cloud",
        "recommendation": f"Deploy infrastructure on {cloud_provider} spanning 3 availability zones with automated cross-region replication.",
        "advantages": [f"Provides 99.99% infrastructure uptime SLA for '{main}' endpoints", "Supports automated elastic pod autoscaling (HPA)"],
        "disadvantages": ["Increases cross-region data transfer egress costs under peak load"],
        "confidence": 93,
        "challenge": "Challenges DevOps Engineer: Cloud provision manifests must enforce infrastructure-as-code state immutability via Terraform."
    }

    # 7. DevOps Engineer
    devops_agent = {
        "agent": "DevOps Engineer", "avatar": "🚀", "role_color": "#30E3CA", "badge": "CI/CD & Kubernetes",
        "recommendation": f"Containerize '{main}' services using multi-stage Docker builds and orchestrate deployments via Kubernetes Helm charts & ArgoCD GitOps pipelines.",
        "advantages": [f"Enables zero-downtime blue/green deployments for '{main}' releases", "Provides automated vulnerability scanning on container base images"],
        "disadvantages": ["Requires dedicated Kubernetes control plane management overhead"],
        "confidence": 92,
        "challenge": "Challenges Reliability Engineer: Circuit breakers must automatically trigger container rollbacks upon 2% HTTP 5xx spikes."
    }

    # 8. Performance Engineer
    perf_cdn = "Cloudflare Enterprise Edge Workers + Redis v7 In-Memory Cluster" if reqs["has_high_throughput"] else "Redis v7 Multi-Node In-Memory Cluster"
    perf_agent = {
        "agent": "Performance Engineer", "avatar": "⚡", "role_color": "#10B981", "badge": "Latency & Caching",
        "recommendation": f"Implement {perf_cdn} with write-through cache strategy on '{main}' query paths.",
        "advantages": [f"Achieves P99 read latency under 20ms for '{main}' payloads", "Offloads up to 85% of read queries from primary PostgreSQL storage"],
        "disadvantages": ["Demands rigorous cache invalidation rules to avoid serving stale '{main}' state"],
        "confidence": reqs["perf_index"],
        "challenge": "Challenges Database Architect: Cold cache hits must fallback gracefully without triggering database thread pool starvation."
    }

    # 9. Reliability Engineer
    rel_agent = {
        "agent": "Reliability Engineer", "avatar": "⚓", "role_color": "#6366F1", "badge": "SRE & Resilience",
        "recommendation": f"Establish Prometheus telemetry, OpenTelemetry trace propagation, and chaos engineering drills for '{main}' microservices.",
        "advantages": [f"Enables mean-time-to-detection (MTTD) under 3 minutes for '{main}' anomalies", "Guarantees RPO < 1 minute and RTO < 5 minutes"],
        "disadvantages": ["Consumes storage capacity for high-cardinality distributed tracing telemetry"],
        "confidence": 94,
        "challenge": "Challenges Cost Agent: High availability infrastructure must not compromise failover redundancy for cost savings."
    }

    # 10. Cost Optimization Agent
    cost_agent = {
        "agent": "Cost Optimization Agent", "avatar": "💰", "role_color": "#F43F5E", "badge": "FinOps Guardrails",
        "recommendation": f"Utilize Kubernetes Spot Instances for stateless '{main}' batch processing workers and enforce AWS Savings Plans for database instances.",
        "advantages": [f"Reduces monthly cloud compute expenses for '{main}' cluster by 35-50%", "Implements hard cost alert quotas per cloud environment"],
        "disadvantages": ["Requires handling node termination notices gracefully within worker queues"],
        "confidence": reqs["cost_efficiency_index"],
        "challenge": "Challenges Cloud Architect: Idle container pods in staging environments must scale down to zero replicas during off-peak hours."
    }

    # 11. Innovation Agent
    innov_agent = {
        "agent": "Innovation Agent", "avatar": "🧠", "role_color": "#C084FC", "badge": "AI & Future Scale",
        "recommendation": f"Embed Vector Embeddings (pgvector / Qdrant) and RAG pipeline workflows to power intelligent autonomous reasoning over '{main}' domain records.",
        "advantages": [f"Transforms raw '{main}' data into semantic vector knowledge embeddings for automated insights", "Differentiates product with enterprise generative AI features"],
        "disadvantages": ["Requires GPU infrastructure provisioning and LLM model latency monitoring"],
        "confidence": 93,
        "challenge": "Challenges Lead Architect: Architecture must remain modular to allow drop-in replacement of LLM model inference providers."
    }

    debate_logs = [lead_agent, sec_agent, be_agent, fe_agent, db_agent, cloud_agent, devops_agent, perf_agent, rel_agent, cost_agent, innov_agent]

    consensus = {
        "status": "APPROVED",
        "agreement_rate": round(sum(a["confidence"] for a in debate_logs) / len(debate_logs), 1),
        "summary": f"All 11 AI architects reached consensus for '{domain}'. Synthesized {arch_pattern}, utilizing {be_tech}, {db_type}, and {cloud_provider}.",
        "primary_recommendation": f"Proceed with production build of {main} enterprise blueprint."
    }

    # ---------------------------------------------------------
    # STAGE 6: DYNAMIC REAL DDL & REST API SPECIFICATIONS
    # ---------------------------------------------------------
    sql_schema = f"""-- AetherMind Genesis: Production SQL DDL Schema for {domain}
-- Domain Entity: {main} | Authored for PostgreSQL 16+

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";

CREATE TABLE {main.lower()}_tenants (
    tenant_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_name VARCHAR(255) NOT NULL,
    plan_tier VARCHAR(50) DEFAULT 'ENTERPRISE',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE {main.lower()}_core (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID REFERENCES {main.lower()}_tenants(tenant_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'ACTIVE',
    metadata JSONB DEFAULT '{{}}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_{main.lower()}_tenant ON {main.lower()}_core(tenant_id);
CREATE INDEX idx_{main.lower()}_status ON {main.lower()}_core(status);
CREATE INDEX idx_{main.lower()}_meta ON {main.lower()}_core USING gin (metadata);

"""
    for sec_ent in sec_ents[:3]:
        sql_schema += f"""CREATE TABLE {sec_ent.lower()}_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    {main.lower()}_id UUID REFERENCES {main.lower()}_core(id) ON DELETE CASCADE,
    record_key VARCHAR(100) NOT NULL,
    record_payload JSONB DEFAULT '{{}}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_{sec_ent.lower()}_{main.lower()} ON {sec_ent.lower()}_records({main.lower()}_id);

"""

    api_spec = f"""{{
  "openapi": "3.0.3",
  "info": {{
    "title": "{main} Enterprise API Specification",
    "description": "Production REST API endpoints for {domain} managing {main} domain entities.",
    "version": "1.0.0"
  }},
  "servers": [
    {{ "url": "https://api.enterprise.domain/v1", "description": "Production Cloud Gateway" }}
  ],
  "paths": {{
    "/api/v1/{main.lower()}": {{
      "get": {{
        "summary": "List {main} entities",
        "parameters": [
          {{ "name": "limit", "in": "query", "schema": {{ "type": "integer", "default": 20 }} }},
          {{ "name": "status", "in": "query", "schema": {{ "type": "string" }} }}
        ],
        "responses": {{
          "200": {{ "description": "Successful retrieval of {main} list." }},
          "401": {{ "description": "Unauthorized token error." }}
        }}
      }},
      "post": {{
        "summary": "Create new {main} domain record",
        "requestBody": {{
          "required": true,
          "content": {{
            "application/json": {{
              "schema": {{
                "type": "object",
                "properties": {{
                  "title": {{ "type": "string" }},
                  "metadata": {{ "type": "object" }}
                }},
                "required": ["title"]
              }}
            }}
          }}
        }},
        "responses": {{
          "201": {{ "description": "{main} entity created successfully." }}
        }}
      }}
    }},
    "/api/v1/{main.lower()}/{{id}}": {{
      "get": {{
        "summary": "Retrieve {main} details by UUID",
        "responses": {{ "200": {{ "description": "{main} entity payload." }} }}
      }},
      "delete": {{
        "summary": "Soft delete {main} entity",
        "responses": {{ "200": {{ "description": "{main} entity archived." }} }}
      }}
    }}
  }}
}}"""

    # ---------------------------------------------------------
    # STAGE 7: AI PROJECT INTELLIGENCE PIPELINE
    # ---------------------------------------------------------
    ai_pipeline = {
        "model_selected": "Llama-3-70B-Instruct / Claude 3.5 Sonnet / OpenAI gpt-4o",
        "inference_framework": "vLLM with TensorRT-LLM GPU Acceleration",
        "vector_database": "pgvector (PostgreSQL) / Qdrant Enterprise",
        "embedding_model": "text-embedding-3-large (3072 dimensions)",
        "gpu_requirements": "2x NVIDIA H100 80GB PCIe or 4x NVIDIA A100 40GB",
        "rag_architecture": "Hybrid Sparse-Dense Vector Retrieval with Reciprocal Rank Fusion (RRF)",
        "latency_target": "< 450ms for first token, < 1.2s total completion",
        "safety_pipeline": "Llama Guard 3 Guardrails + OWASP Prompt Injection Sanitizer"
    }

    # ---------------------------------------------------------
    # DYNAMIC MERMAID ER DIAGRAM SYNTHESIS
    # ---------------------------------------------------------
    er_diagram_code = f"""erDiagram
    {main.upper()}_TENANTS ||--o{{ {main.upper()}_CORE : "provisions"
"""
    for sec_ent in sec_ents[:3]:
        er_diagram_code += f'    {main.upper()}_CORE ||--o{{ {sec_ent.upper()}_RECORDS : "contains"\n'

    # ---------------------------------------------------------
    # DYNAMIC API ENDPOINTS WORKBENCH LIST SYNTHESIS
    # ---------------------------------------------------------
    api_endpoints_documentation = [
        {
            "method": "GET",
            "path": f"/api/v1/{main.lower()}",
            "auth": "Bearer OAuth2 JWT",
            "summary": f"List and filter primary '{main}' domain records with pagination.",
            "headers": {"Authorization": "Bearer <token>", "Accept": "application/json"},
            "sample_request": None,
            "sample_response": {"status": "success", "count": 1, "data": [{"id": "uuid-1234", "title": f"Sample {main}", "status": "ACTIVE"}]},
            "error_codes": [{"code": 401, "description": "Unauthorized token claim or expired access token."}, {"code": 429, "description": "Rate limit exceeded (Max 100 req/min)."}]
        },
        {
            "method": "POST",
            "path": f"/api/v1/{main.lower()}",
            "auth": "Bearer OAuth2 JWT",
            "summary": f"Provision a new '{main}' core record and trigger asynchronous workflow queues.",
            "headers": {"Authorization": "Bearer <token>", "Content-Type": "application/json"},
            "sample_request": {"title": f"New {main} Record", "metadata": {"priority": "HIGH", "tags": [domain.lower()]}},
            "sample_response": {"status": "created", "id": "uuid-5678", "created_at": "2026-09-21T00:00:00Z"},
            "error_codes": [{"code": 400, "description": "Validation error in request payload structure."}, {"code": 409, "description": "Duplicate resource key conflict."}]
        },
        {
            "method": "PUT",
            "path": f"/api/v1/{main.lower()}/{{id}}",
            "auth": "Bearer OAuth2 JWT",
            "summary": f"Update metadata parameters and execution state for target '{main}' entity.",
            "headers": {"Authorization": "Bearer <token>", "Content-Type": "application/json"},
            "sample_request": {"status": "PROCESSING", "metadata": {"updated_by": "SystemArchitect"}},
            "sample_response": {"status": "updated", "id": "uuid-5678", "updated_at": "2026-09-21T00:01:00Z"},
            "error_codes": [{"code": 404, "description": "Target entity UUID not found."}]
        },
        {
            "method": "DELETE",
            "path": f"/api/v1/{main.lower()}/{{id}}",
            "auth": "Bearer OAuth2 Admin JWT",
            "summary": f"Archive and soft-delete '{main}' record with cascading child item cleanup.",
            "headers": {"Authorization": "Bearer AdminToken"},
            "sample_request": None,
            "sample_response": {"status": "archived", "id": "uuid-5678"},
            "error_codes": [{"code": 403, "description": "Forbidden: Requires Admin RBAC privilege."}]
        }
    ]

    return {
        "domain": domain,
        "arch_pattern": arch_pattern,
        "arch_justification": arch_justification,
        "debate_logs": debate_logs,
        "consensus": consensus,
        "sql_schema": sql_schema,
        "api_spec": api_spec,
        "api_endpoints_documentation": api_endpoints_documentation,
        "er_diagram_code": er_diagram_code,
        "ai_pipeline": ai_pipeline,
        "base_security_complexity": reqs["sec_index"],
        "base_perf_complexity": reqs["perf_index"],
        "base_cost_efficiency": reqs["cost_efficiency_index"]
    }

