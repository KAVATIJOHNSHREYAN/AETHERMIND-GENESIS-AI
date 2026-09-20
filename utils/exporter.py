import json

def export_blueprint_markdown(idea_title: str, scores: dict, debate_logs: list, mermaid_code: str, sql_schema: str, api_spec: str, ai_pipeline: dict = None) -> str:
    """
    STAGE 12: Production Blueprint Exporter
    Synthesizes all 12 reasoning stages into an implementation-ready enterprise blueprint.
    """
    domain = scores.get("architecture_profile", "Enterprise Multi-Region System")
    explanations = scores.get("score_explanations", {})
    cost_data = scores.get("cost_breakdown", {})
    risks = scores.get("risk_analysis", [])

    debate_formatted = []
    for log in debate_logs:
        challenge_str = f"  \n  *Challenge:* {log.get('challenge', '')}" if log.get('challenge') else ""
        debate_formatted.append(f"### {log.get('avatar', '👤')} {log['agent']} (`{log.get('badge', 'Architect')}`)\n"
                                f"- **Recommendation:** {log.get('recommendation', '')}\n"
                                f"- **Key Advantage:** {', '.join(log.get('advantages', []))}\n"
                                f"- **Trade-off:** {', '.join(log.get('disadvantages', []))}"
                                f"{challenge_str}\n")
    debate_summary = "\n".join(debate_formatted)

    ai_section = ""
    if ai_pipeline:
        ai_section = f"""---

## 7. 🧠 STAGE 7 — AI Project Intelligence & Pipeline Topology
- **Model Selected:** {ai_pipeline.get('model_selected', 'N/A')}
- **Inference Engine:** {ai_pipeline.get('inference_framework', 'N/A')}
- **Vector Database:** {ai_pipeline.get('vector_database', 'N/A')}
- **Embedding Model:** {ai_pipeline.get('embedding_model', 'N/A')}
- **Hardware/GPU Specs:** {ai_pipeline.get('gpu_requirements', 'N/A')}
- **RAG Architecture:** {ai_pipeline.get('rag_architecture', 'N/A')}
- **Target Latency:** {ai_pipeline.get('latency_target', 'N/A')}
- **Safety & Guardrails:** {ai_pipeline.get('safety_pipeline', 'N/A')}
"""

    return f"""# 🌌 AetherMind Genesis — Master Enterprise Software Blueprint
**Project Title:** {idea_title}  
**Architecture Profile:** {scores.get('architecture_profile', 'Balanced Hybrid Cloud')}  
**Overall System Fitness Score:** {scores.get('overall_score', 92)}/100  
**Domain Classification:** {domain}  
**Author:** *AetherMind Genesis — Autonomous Enterprise AI Software Architect*  

---

## 1. 📋 STAGE 1 — Project Requirements & Scope
- **Application Type:** Enterprise Scalable Platform
- **Target Audience:** High-Concurrency End-Users & Automated API Consumers
- **Functional Requirements:** Real-time state synchronization, RBAC authorization, transactional data processing, telemetry logging.
- **Non-Functional Requirements:** 99.99% Availability, P99 Latency < 150ms, Zero-Trust compliance.

---

## 2. 🏷️ STAGE 2 — Domain Classification
- **Primary Domain:** {domain}
- **Security Envelope:** Zero-Trust TLS 1.3 / mTLS & AES-256 Field Encryption
- **Target Scale:** 1,000,000+ Active Users / 25,000+ Peak Requests Per Second

---

## 3. 👥 STAGE 3 — Multi-Agent Collaboration & Agent Debates
{debate_summary}

---

## 4. 📐 STAGE 4 — Architecture Selection & System Topology
```mermaid
{mermaid_code}
```

---

## 5. 🗄️ STAGE 5 & 6 — Production SQL DDL Schema & Data Design
```sql
{sql_schema}
```

---

## 6. 🔌 STAGE 6 — REST API Specification (OpenAPI v3.0)
```json
{api_spec}
```

{ai_section}

---

## 8. 📊 STAGE 8 & 9 — Dynamic Scoring & Radar Analysis
- **Security Score:** {scores.get('security_score', 90)}/100  
  *{explanations.get('security', {}).get('deductions', '')}*  
  **Action:** {explanations.get('security', {}).get('improvement', '')}
- **Performance Score:** {scores.get('performance_score', 88)}/100  
  *{explanations.get('performance', {}).get('deductions', '')}*  
  **Action:** {explanations.get('performance', {}).get('improvement', '')}
- **Cost Efficiency Score:** {scores.get('cost_efficiency_score', 80)}/100  
  *{explanations.get('cost_efficiency', {}).get('deductions', '')}*  
  **Action:** {explanations.get('cost_efficiency', {}).get('improvement', '')}
- **Scalability Score:** {scores.get('scalability_score', 90)}/100  
  *{explanations.get('scalability', {}).get('deductions', '')}*  
  **Action:** {explanations.get('scalability', {}).get('improvement', '')}

---

## 9. 💰 STAGE 10 — Comprehensive Cost Analysis
- **Estimated Monthly Cloud Expense:** `{scores.get('estimated_monthly_cost', '$350 - $950 / mo')}`
- **One-Time Development Estimation:** `{cost_data.get('development_cost', '$35,000 - $65,000')}`
- **Cloud Compute Pods:** `{cost_data.get('cloud_compute', '$220 / mo')}`
- **GPU Inference Infrastructure:** `{cost_data.get('gpu_compute', '$350 / mo')}`
- **Storage & Database Hosting:** `{cost_data.get('storage_cost', '$110 / mo')}`
- **Network & CDN Bandwidth:** `{cost_data.get('bandwidth_cost', '$80 / mo')}`
- **Granular Cost Metrics:**
  - Cost Per Active User: `{cost_data.get('cost_per_user', '$0.0028')}`
  - Cost Per API Request: `{cost_data.get('cost_per_api_request', '$0.000008')}`
  - Cost Per AI Inference Call: `{cost_data.get('cost_per_inference', '$0.0021')}`

---

## 10. ⚠️ STAGE 11 — Risk Analysis & Mitigation Matrix
""" + "\n".join([f"- **[{r['category']}] ({r['impact']} Impact)**: {r['risk']}\n  *Mitigation:* {r['mitigation']}" for r in risks]) + """

---

## 11. 🚀 STAGE 12 — Production Blueprint & Deployment Pipeline
```
app-root/
├── .github/workflows/ci-cd.yml      # CI/CD Automated Build & Deploy Pipeline
├── src/
│   ├── api/                         # REST & GraphQL Route Controllers
│   ├── core/                        # Business Domain Engine Services
│   ├── db/                          # SQL Migrations & ORM Schema Models
│   ├── security/                    # Zero-Trust Middleware & KMS Encryption
│   └── utils/                       # Shared Helper Modules
├── infra/
│   ├── terraform/                   # Infrastructure-as-Code Terraform Manifests
│   └── k8s/                         # Kubernetes Helm Charts & Pod Specs
├── tests/                           # E2E Playwright & Integration Test Suite
├── Dockerfile                       # Multi-stage Containerization Spec
└── requirements.txt                 # Dependencies Manifest
```

---
*Synthesized autonomously by **AetherMind Genesis — Autonomous Enterprise AI Software Architect***  
*Copyright © 2026 KAVATI JOHN SHREYAN. All Rights Reserved.*
"""

