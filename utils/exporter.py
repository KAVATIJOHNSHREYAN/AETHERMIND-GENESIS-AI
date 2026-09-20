import json

def export_blueprint_markdown(idea_title: str, scores: dict, debate_logs: list, mermaid_code: str, sql_schema: str, api_spec: str) -> str:
    """
    Synthesizes the complete architecture blueprint into an enterprise Markdown document.
    """
    debate_formatted = "\n".join([f"- **[{log['agent']}]**: {log['message']}" for log in debate_logs])
    
    return f"""# 🚀 AetherMind Genesis - Software Blueprint
**Project Concept:** {idea_title}
**Architecture Profile:** {scores['architecture_profile']}
**Overall System Score:** {scores['overall_score']}/100

---

## 📊 Optimization & Fitness Metrics
- **Security Score:** {scores['security_score']}/100
- **Performance Score:** {scores['performance_score']}/100
- **Cost Efficiency Score:** {scores['cost_efficiency_score']}/100
- **Estimated Cloud Budget:** {scores['estimated_monthly_cost']}
- **Recommended Database:** {scores['recommended_db']}

---

## 🗣️ Multi-Agent Architecture Consensus Debate
{debate_formatted}

---

## 🗺️ System Architecture Topology (Mermaid.js)
```mermaid
{mermaid_code}
```

---

## 🗄️ Database Schema DDL (SQL)
```sql
{sql_schema}
```

---

## 🔌 API Endpoint Specification
```json
{api_spec}
```

---
*Generated autonomously by **AetherMind Genesis - AI System Architect***
"""
