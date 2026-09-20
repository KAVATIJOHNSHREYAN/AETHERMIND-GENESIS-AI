def run_multi_agent_debate(prompt: str, sec_weight: float, perf_weight: float, cost_weight: float) -> dict:
    """
    Simulates real-time multi-agent reasoning, debate, and blueprint generation without external API dependencies.
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

    # 1. Multi-Agent Debate Simulation Logs
    debate_logs = [
        {
            "agent": "Lead Architect",
            "avatar": "👑",
            "message": f"Initiating system design synthesis for concept: '{prompt}'. Analyzing core constraints across Security, Latency, and Budget..."
        }
    ]

    # Security Agent perspective
    if sec_weight >= 0.4 or domain in ["fintech", "healthcare"]:
        sec_msg = f"CRITICAL REQUIREMENT ({domain.upper()} domain): Implementing mandatory OAuth2 + PKCE auth, TLS 1.3 in transit, and AES-256 field encryption for sensitive fields. Enforcing Zero-Trust microsegmentation."
    else:
        sec_msg = "Standard Security Profile: JWT Token Authentication with HTTPS endpoint enforcement and OWASP Top 10 automated sanitization."
    debate_logs.append({"agent": "Security Architect", "avatar": "🛡️", "message": sec_msg})

    # Performance Agent perspective
    if perf_weight >= 0.4 or domain in ["ai_media", "fintech"]:
        perf_msg = "HIGH LATENCY THREAT: Enabling Redis cluster caching layer for session state and hot queries. Offloading heavy background computations to async RabbitMQ workers."
    else:
        perf_msg = "Balanced Performance: Standard indexed database queries with simple HTTP response caching. Expected latency < 150ms."
    debate_logs.append({"agent": "Performance Architect", "avatar": "⚡", "message": perf_msg})

    # Cost Agent perspective
    if cost_weight >= 0.4:
        cost_msg = "BUDGET RESTRAINT: Recommending managed Serverless infrastructure (Supabase + Vercel/Cloudflare Workers) to minimize idle server costs below $30/mo."
    else:
        cost_msg = "Infrastructure Investment: Budget permits dedicated containerized services (AWS ECS / Kubernetes) to ensure 99.99% uptime SLA."
    debate_logs.append({"agent": "Cost Architect", "avatar": "💰", "message": cost_msg})

    # Lead Architect Consensus
    debate_logs.append({
        "agent": "Lead Architect",
        "avatar": "👑",
        "message": "Consensus reached among all 4 specialized agents! Synthesizing final relational DB schema, API routes, and C4 architecture graph."
    })

    # 2. Database Schema Generation (SQL)
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

    # 3. API OpenAPI JSON Specification
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
        "sql_schema": sql_schema,
        "api_spec": api_spec,
        "base_security_complexity": 85 if domain in ["fintech", "healthcare"] else 70,
        "base_perf_complexity": 85 if domain == "ai_media" else 75,
        "base_cost_efficiency": 70 if domain == "fintech" else 85
    }
