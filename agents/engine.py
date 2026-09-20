def run_multi_agent_debate(prompt: str, sec_weight: float, perf_weight: float, cost_weight: float) -> dict:
    """
    Simulates real-time multi-agent reasoning, debate, and blueprint generation across 9 specialized AI Architect personas.
    Returns structured recommendations, pros/cons, confidence scores, and consensus results.
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
            "role_color": "#3B82F6", # Electric Blue
            "badge": "Strategy & Synthesis",
            "recommendation": f"Adopt a modular component architecture tailored for {domain.upper()} domain requirements.",
            "advantages": ["Clear separation of concerns", "High maintainability", "Flexible scaling path"],
            "disadvantages": ["Slightly higher initial setup complexity"],
            "confidence": 96
        },
        {
            "agent": "Security Architect",
            "avatar": "🛡️",
            "role_color": "#22D3EE", # Cyan
            "badge": "Zero-Trust & OWASP",
            "recommendation": f"Enforce mandatory OAuth2 + PKCE authentication, AES-256 field encryption, and TLS 1.3.",
            "advantages": ["Prevents unauthorized access", "Compliant with industry regulations"],
            "disadvantages": ["Adds encryption overhead on database I/O"],
            "confidence": 94 if sec_weight >= 0.5 else 88
        },
        {
            "agent": "Backend Architect",
            "avatar": "⚙️",
            "role_color": "#8B5CF6", # Purple
            "badge": "API & Runtime Core",
            "recommendation": "Deploy an asynchronous REST/GraphQL gateway with rate-limiting and connection pooling.",
            "advantages": ["Prevents server overload", "High throughput handling"],
            "disadvantages": ["Requires connection pool tuning"],
            "confidence": 92
        },
        {
            "agent": "Frontend Architect",
            "avatar": "🎨",
            "role_color": "#EC4899", # Pink
            "badge": "UI/UX & Client State",
            "recommendation": "Build a responsive single-page client with optimistic UI updates and server-side rendering (SSR).",
            "advantages": ["Sub-second page loads", "Seamless user feedback"],
            "disadvantages": ["Higher client bundle size"],
            "confidence": 90
        },
        {
            "agent": "Database Architect",
            "avatar": "🗄️",
            "role_color": "#F59E0B", # Amber
            "badge": "Data Topology & DDL",
            "recommendation": "Use relational PostgreSQL with composite indexes on high-frequency query columns.",
            "advantages": ["ACID compliance guarantees", "Fast lookup performance"],
            "disadvantages": ["Requires schema migration management"],
            "confidence": 95
        },
        {
            "agent": "Cloud Architect",
            "avatar": "☁️",
            "role_color": "#30E3CA", # Teal
            "badge": "Infrastructure & Cost",
            "recommendation": "Deploy on managed serverless nodes (Vercel/Supabase or AWS ECS) with auto-scaling triggers.",
            "advantages": ["Pay-per-use cost efficiency", "Zero server maintenance"],
            "disadvantages": ["Potential cold-start latency spikes"],
            "confidence": 89 if cost_weight >= 0.5 else 93
        },
        {
            "agent": "DevOps Architect",
            "avatar": "🚀",
            "role_color": "#10B981", # Emerald
            "badge": "CI/CD & Observability",
            "recommendation": "Implement automated GitHub Actions CI/CD pipelines with Prometheus metrics & OpenTelemetry logging.",
            "advantages": ["Automated zero-downtime deployments", "Real-time error tracking"],
            "disadvantages": ["Requires pipeline setup time"],
            "confidence": 91
        },
        {
            "agent": "AI Engineer",
            "avatar": "🤖",
            "role_color": "#6366F1", # Indigo
            "badge": "Model & Context Pipeline",
            "recommendation": "Integrate local vector embeddings (Chroma/FAISS) with streaming token inference.",
            "advantages": ["Fast response latency", "Rich contextual search"],
            "disadvantages": ["Vector memory index overhead"],
            "confidence": 93
        },
        {
            "agent": "QA Engineer",
            "avatar": "🧪",
            "role_color": "#EF4444", # Red
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

    # SQL Schema DDL
    if domain == "fintech":
        sql_schema = """-- AetherMind Genesis: FinTech DB Schema
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
CREATE INDEX idx_tx_sender ON transactions(sender_account_id);
"""
    elif domain == "healthcare":
        sql_schema = """-- AetherMind Genesis: Healthcare DB Schema (HIPAA Compliant)
CREATE TABLE patients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    encrypted_dob BYTEA NOT NULL,
    encrypted_name BYTEA NOT NULL,
    medical_record_number VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE appointments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    patient_id UUID REFERENCES patients(id),
    doctor_id UUID NOT NULL,
    appointment_date TIMESTAMP NOT NULL,
    status VARCHAR(50) DEFAULT 'SCHEDULED'
);
"""
    else:
        sql_schema = """-- AetherMind Genesis: Core SaaS DB Schema
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
"""

    # OpenAPI JSON Specification
    api_spec = f"""{{
  "openapi": "3.0.0",
  "info": {{
    "title": "{prompt.capitalize()} API",
    "version": "1.0.0"
  }},
  "paths": {{
    "/api/v1/auth/login": {{
      "post": {{
        "summary": "Authenticate User",
        "responses": {{ "200": {{ "description": "Returns JWT Access Token" }} }}
      }}
    }},
    "/api/v1/data": {{
      "get": {{
        "summary": "Fetch Main Resource List",
        "responses": {{ "200": {{ "description": "Returns Array of Objects" }} }}
      }},
      "post": {{
        "summary": "Create Resource Item",
        "responses": {{ "201": {{ "description": "Item Created Successfully" }} }}
      }}
    }},
    "/api/v1/health": {{
      "get": {{
        "summary": "System Health Status",
        "responses": {{ "200": {{ "description": "Status OK" }} }}
      }}
    }}
  }}
}}"""

    return {
        "domain": domain,
        "debate_logs": debate_logs,
        "consensus": consensus,
        "sql_schema": sql_schema,
        "api_spec": api_spec,
        "base_security_complexity": 85 if domain in ["fintech", "healthcare"] else 70,
        "base_perf_complexity": 85 if domain == "ai_media" else 75,
        "base_cost_efficiency": 70 if domain == "fintech" else 85
    }
