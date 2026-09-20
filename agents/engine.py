def run_multi_agent_debate(prompt: str, sec_weight: float, perf_weight: float, cost_weight: float) -> dict:
    """
    Simulates real-time multi-agent reasoning, debate, and blueprint generation across 9 specialized AI Architect personas.
    Generates ER diagrams, DDL SQL schemas, and Swagger-style REST API specs (GET, POST, PUT, DELETE, Headers, Payload, Error Codes).
    """
    prompt_lower = prompt.lower()

    # Domain classification
    if any(k in prompt_lower for k in ["money", "bank", "pay", "finance", "crypto", "trading", "wallet"]):
        domain = "fintech"
    elif any(k in prompt_lower for k in ["health", "medical", "patient", "doctor", "clinic", "hospital"]):
        domain = "healthcare"
    elif any(k in prompt_lower for k in ["shop", "store", "e-commerce", "buy", "sell", "cart", "product"]):
        domain = "ecommerce"
    elif any(k in prompt_lower for k in ["video", "image", "media", "stream", "ai", "generator", "chat"]):
        domain = "ai_media"
    else:
        domain = "general_saas"

    # ---------------------------------------------------------
    # 9 Specialized AI Architect Personas Structured Output
    # ---------------------------------------------------------
    debate_logs = [
        {
            "agent": "Lead Architect",
            "avatar": "👑",
            "role_color": "#3B82F6",
            "badge": "Strategy & Synthesis",
            "recommendation": f"Adopt a modular component architecture tailored for {domain.upper()} domain requirements.",
            "advantages": ["Clear separation of concerns", "High maintainability", "Flexible scaling path"],
            "disadvantages": ["Slightly higher initial setup complexity"],
            "confidence": 96
        },
        {
            "agent": "Security Architect",
            "avatar": "🛡️",
            "role_color": "#22D3EE",
            "badge": "Zero-Trust & OWASP",
            "recommendation": f"Enforce mandatory OAuth2 + PKCE authentication, AES-256 field encryption, and TLS 1.3.",
            "advantages": ["Prevents unauthorized access", "Compliant with industry regulations"],
            "disadvantages": ["Adds encryption overhead on database I/O"],
            "confidence": 94 if sec_weight >= 0.5 else 88
        },
        {
            "agent": "Backend Architect",
            "avatar": "⚙️",
            "role_color": "#8B5CF6",
            "badge": "API & Runtime Core",
            "recommendation": "Deploy an asynchronous REST/GraphQL gateway with rate-limiting and connection pooling.",
            "advantages": ["Prevents server overload", "High throughput handling"],
            "disadvantages": ["Requires connection pool tuning"],
            "confidence": 92
        },
        {
            "agent": "Frontend Architect",
            "avatar": "🎨",
            "role_color": "#EC4899",
            "badge": "UI/UX & Client State",
            "recommendation": "Build a responsive single-page client with optimistic UI updates and server-side rendering (SSR).",
            "advantages": ["Sub-second page loads", "Seamless user feedback"],
            "disadvantages": ["Higher client bundle size"],
            "confidence": 90
        },
        {
            "agent": "Database Architect",
            "avatar": "🗄️",
            "role_color": "#F59E0B",
            "badge": "Data Topology & DDL",
            "recommendation": "Use relational PostgreSQL with composite indexes on high-frequency query columns.",
            "advantages": ["ACID compliance guarantees", "Fast lookup performance"],
            "disadvantages": ["Requires schema migration management"],
            "confidence": 95
        },
        {
            "agent": "Cloud Architect",
            "avatar": "☁️",
            "role_color": "#30E3CA",
            "badge": "Infrastructure & Cost",
            "recommendation": "Deploy on managed serverless nodes (Vercel/Supabase or AWS ECS) with auto-scaling triggers.",
            "advantages": ["Pay-per-use cost efficiency", "Zero server maintenance"],
            "disadvantages": ["Potential cold-start latency spikes"],
            "confidence": 89 if cost_weight >= 0.5 else 93
        },
        {
            "agent": "DevOps Architect",
            "avatar": "🚀",
            "role_color": "#10B981",
            "badge": "CI/CD & Observability",
            "recommendation": "Implement automated GitHub Actions CI/CD pipelines with Prometheus metrics & OpenTelemetry logging.",
            "advantages": ["Automated zero-downtime deployments", "Real-time error tracking"],
            "disadvantages": ["Requires pipeline setup time"],
            "confidence": 91
        },
        {
            "agent": "AI Engineer",
            "avatar": "🤖",
            "role_color": "#6366F1",
            "badge": "Model & Context Pipeline",
            "recommendation": "Integrate local vector embeddings (Chroma/FAISS) with streaming token inference.",
            "advantages": ["Fast response latency", "Rich contextual search"],
            "disadvantages": ["Vector memory index overhead"],
            "confidence": 93
        },
        {
            "agent": "QA Engineer",
            "avatar": "🧪",
            "role_color": "#EF4444",
            "badge": "Testing & Resilience",
            "recommendation": "Enforce mandatory E2E Playwright tests and automated API load testing (k6).",
            "advantages": ["High regression prevention", "Verified stress tolerance"],
            "disadvantages": ["Increases build step duration"],
            "confidence": 95
        }
    ]

    # Consensus Synthesis
    consensus = {
        "status": "APPROVED",
        "agreement_rate": 93.2,
        "summary": f"All 9 specialized AI architects have reached consensus for the {domain.upper()} blueprint. The architecture synthesizes Zero-Trust security, PostgreSQL data integrity, async API layers, and auto-scaling cloud infrastructure.",
        "primary_recommendation": f"Proceed with {domain.upper()} Modular Architecture Blueprint."
    }

    # ---------------------------------------------------------
    # PHASE 4: Database ER Diagram & DDL Schema
    # ---------------------------------------------------------
    er_diagram_code = f"""erDiagram
    USERS ||--o{{ PROJECTS : owns
    USERS ||--o{{ ACCOUNTS : possesses
    ACCOUNTS ||--o{{ TRANSACTIONS : initiates
    PROJECTS ||--o{{ SYSTEM_LOGS : records

    USERS {{
        uuid id PK
        string email UK
        string password_hash
        string kyc_status
        timestamp created_at
    }}

    ACCOUNTS {{
        uuid id PK
        uuid user_id FK
        decimal balance
        string currency
        timestamp updated_at
    }}

    TRANSACTIONS {{
        uuid id PK
        uuid sender_account_id FK
        uuid receiver_account_id FK
        decimal amount
        string status
        timestamp timestamp
    }}

    PROJECTS {{
        uuid id PK
        uuid user_id FK
        string name
        boolean is_active
        timestamp created_at
    }}

    SYSTEM_LOGS {{
        int id PK
        uuid project_id FK
        string action
        timestamp created_at
    }}
"""

    if domain == "fintech":
        sql_schema = """-- AetherMind Genesis: FinTech DDL Schema (PostgreSQL)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    kyc_status VARCHAR(50) DEFAULT 'PENDING',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    balance NUMERIC(15, 2) NOT NULL DEFAULT 0.00,
    currency VARCHAR(3) DEFAULT 'USD',
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sender_account_id UUID REFERENCES accounts(id),
    receiver_account_id UUID REFERENCES accounts(id),
    amount NUMERIC(15, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'COMPLETED',
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Primary & Foreign Key Indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_accounts_user_id ON accounts(user_id);
CREATE INDEX idx_tx_sender ON transactions(sender_account_id);
CREATE INDEX idx_tx_receiver ON transactions(receiver_account_id);
"""
    else:
        sql_schema = """-- AetherMind Genesis: Core SaaS DDL Schema (PostgreSQL)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE system_logs (
    id SERIAL PRIMARY KEY,
    project_id UUID REFERENCES projects(id),
    action VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_projects_user_id ON projects(user_id);
CREATE INDEX idx_logs_project_id ON system_logs(project_id);
"""

    # ---------------------------------------------------------
    # PHASE 5: Comprehensive Swagger-Style REST API Documentation
    # ---------------------------------------------------------
    api_endpoints_documentation = [
        {
            "method": "POST",
            "path": "/api/v1/auth/login",
            "summary": "Authenticate User & Obtain JWT Token",
            "auth": "Public / None",
            "headers": {"Content-Type": "application/json", "Accept": "application/json"},
            "sample_request": {
                "email": "user@aethermind.ai",
                "password": "SecurePassword123!"
            },
            "sample_response": {
                "status": 200,
                "message": "Authentication successful",
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "Bearer",
                "expires_in": 3600
            },
            "error_codes": [
                {"code": 400, "description": "Invalid payload parameters"},
                {"code": 401, "description": "Unauthorized: Invalid credentials"}
            ]
        },
        {
            "method": "GET",
            "path": "/api/v1/projects",
            "summary": "Fetch List of User Projects",
            "auth": "Bearer JWT Token",
            "headers": {"Authorization": "Bearer <access_token>", "Accept": "application/json"},
            "sample_request": None,
            "sample_response": {
                "status": 200,
                "total_items": 2,
                "projects": [
                    {"id": "c1f7a2b9-...", "name": "FinTech Gateway", "is_active": True},
                    {"id": "d2e8b3c0-...", "name": "AI Video Engine", "is_active": True}
                ]
            },
            "error_codes": [
                {"code": 401, "description": "Unauthorized: Token missing or expired"},
                {"code": 403, "description": "Forbidden: Insufficient permissions"}
            ]
        },
        {
            "method": "POST",
            "path": "/api/v1/projects",
            "summary": "Create New System Architecture Blueprint Project",
            "auth": "Bearer JWT Token",
            "headers": {"Authorization": "Bearer <access_token>", "Content-Type": "application/json"},
            "sample_request": {
                "name": "E-Commerce Microservice Platform",
                "description": "High-throughput microservices architecture with Redis cache"
            },
            "sample_response": {
                "status": 201,
                "id": "e3f9c4d1-...",
                "name": "E-Commerce Microservice Platform",
                "created_at": "2026-09-20T22:00:00Z"
            },
            "error_codes": [
                {"code": 400, "description": "Validation error: Name is required"},
                {"code": 409, "description": "Conflict: Project name already exists"}
            ]
        },
        {
            "method": "PUT",
            "path": "/api/v1/projects/{id}",
            "summary": "Update Existing Project Settings",
            "auth": "Bearer JWT Token",
            "headers": {"Authorization": "Bearer <access_token>", "Content-Type": "application/json"},
            "sample_request": {
                "is_active": False,
                "description": "Archived system configuration"
            },
            "sample_response": {
                "status": 200,
                "id": "e3f9c4d1-...",
                "updated": True,
                "timestamp": "2026-09-20T22:05:00Z"
            },
            "error_codes": [
                {"code": 404, "description": "Not Found: Project ID does not exist"},
                {"code": 400, "description": "Bad Request: Invalid update properties"}
            ]
        },
        {
            "method": "DELETE",
            "path": "/api/v1/projects/{id}",
            "summary": "Delete System Architecture Blueprint Project",
            "auth": "Bearer JWT Token",
            "headers": {"Authorization": "Bearer <access_token>"},
            "sample_request": None,
            "sample_response": {
                "status": 200,
                "message": "Project e3f9c4d1-... successfully deleted"
            },
            "error_codes": [
                {"code": 404, "description": "Not Found: Project ID does not exist"},
                {"code": 500, "description": "Internal Server Error"}
            ]
        }
    ]

    api_spec = f"""{{
  "openapi": "3.0.0",
  "info": {{
    "title": "{prompt.capitalize()} API",
    "version": "1.0.0"
  }},
  "paths": {{
    "/api/v1/auth/login": {{
      "post": {{ "summary": "Authenticate User", "responses": {{ "200": {{ "description": "Returns JWT Access Token" }} }} }}
    }},
    "/api/v1/projects": {{
      "get": {{ "summary": "Fetch List of User Projects", "responses": {{ "200": {{ "description": "Returns Array of Objects" }} }} }},
      "post": {{ "summary": "Create New Project Blueprint", "responses": {{ "201": {{ "description": "Item Created Successfully" }} }} }}
    }},
    "/api/v1/projects/{{id}}": {{
      "put": {{ "summary": "Update Project Settings", "responses": {{ "200": {{ "description": "Project Updated" }} }} }},
      "delete": {{ "summary": "Delete Project Blueprint", "responses": {{ "200": {{ "description": "Project Deleted" }} }} }}
    }}
  }}
}}"""

    return {
        "domain": domain,
        "debate_logs": debate_logs,
        "consensus": consensus,
        "er_diagram_code": er_diagram_code,
        "sql_schema": sql_schema,
        "api_endpoints_documentation": api_endpoints_documentation,
        "api_spec": api_spec,
        "base_security_complexity": 85 if domain in ["fintech", "healthcare"] else 70,
        "base_perf_complexity": 85 if domain == "ai_media" else 75,
        "base_cost_efficiency": 70 if domain == "fintech" else 85
    }
