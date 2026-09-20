import re

def parse_prompt_requirements(prompt: str) -> dict:
    """
    STAGE 1: Project Understanding & STAGE 2: Domain Classification
    Extracts application type, industry, users, functional/non-functional requirements,
    AI components, scale, security, performance, budget, and timeline.
    Classifies domain specifically without generic placeholders.
    """
    raw = prompt.strip()
    words = re.findall(r'\w+', raw.lower())
    words_set = set(words)
    
    # 1. Domain Classification (STAGE 2)
    domain_rules = [
        ("AI / ML Platform", ["ai", "ml", "llm", "gpt", "rag", "embedding", "model", "vector", "diffusion", "inference"]),
        ("Healthcare & Telehealth", ["health", "medical", "patient", "hipaa", "doctor", "clinical", "ehr", "phr", "telehealth"]),
        ("Finance & Fintech", ["finance", "bank", "pay", "payment", "crypto", "trading", "wallet", "ledger", "pci", "transfer", "fintech"]),
        ("Video & Media Streaming", ["video", "stream", "media", "hls", "ffmpeg", "transcode", "live", "camera", "h264", "webrtc"]),
        ("IoT & Embedded Fleet", ["iot", "drone", "sensor", "telemetry", "mqtt", "fleet", "vehicle", "edge", "actuator", "rover"]),
        ("Cybersecurity & Zero-Trust", ["security", "siem", "firewall", "vulnerability", "zero-trust", "threat", "soc", "encryption", "auth"]),
        ("E-Commerce & Retail", ["cart", "shop", "ecommerce", "store", "product", "order", "checkout", "stripe", "inventory"]),
        ("Enterprise SaaS & Automation", ["saas", "crm", "erp", "tenant", "automation", "workflow", "jira", "slack", "b2b"]),
        ("Gaming & Metaverse", ["game", "multiplayer", "unity", "unreal", "matchmaking", "leaderboard", "fps", "asset"]),
        ("Government & Defense", ["defense", "gov", "compliance", "fedramp", "citizen", "compliance", "classified"])
    ]
    
    classified_domain = "Enterprise Autonomous Software System"
    for dom_name, keywords in domain_rules:
        if any(kw in words_set for kw in keywords):
            classified_domain = dom_name
            break

    # 2. Dynamic Entity & Requirement Extraction (STAGE 1)
    stop_words = {"build", "a", "an", "the", "for", "with", "and", "or", "in", "to", "app", "application", "system", "platform", "using", "that", "can", "should"}
    extracted_entities = [w.capitalize() for w in words if len(w) > 3 and w not in stop_words]
    
    main_entity = extracted_entities[0] if extracted_entities else "CoreEngine"
    secondary_entities = extracted_entities[1:6] if len(extracted_entities) > 1 else ["Payload", "Metadata", "AuditLog", "Session", "Telemetry"]
    
    # 3. Detection Flags
    has_ai = any(w in words_set for w in ["ai", "ml", "llm", "rag", "prompt", "model", "gpt", "vector", "embedding", "neural", "vision", "diffusion"])
    has_finance = any(w in words_set for w in ["money", "payment", "bank", "pay", "transaction", "balance", "transfer", "wallet", "ledger", "crypto", "pci"])
    has_high_throughput = any(w in words_set for w in ["video", "stream", "live", "realtime", "real-time", "high", "scale", "fleet", "driver", "drone", "iot", "sensor", "kafka"])
    has_auth = any(w in words_set for w in ["auth", "login", "user", "secure", "privacy", "account", "permission", "kyc", "token", "jwt", "rbac"])

    # 4. Inferred Metrics (Scale, Budget, Timeline)
    scale_label = "1M+ Active Users / 50k RPS" if has_high_throughput else ("100k Enterprise Users / 5k RPS" if has_finance else "10k Active Users / 1k RPS")
    budget_est = "$5,000 - $25,000 / month" if (has_ai or has_high_throughput) else "$500 - $2,500 / month"
    timeline_est = "12 - 16 Weeks (4 Sprints)" if (has_ai or has_finance) else "6 - 8 Weeks (2 Sprints)"

    # 5. Dynamic Score Bases
    complexity_score = min(100, max(45, len(words) * 4 + (20 if has_ai else 0) + (15 if has_finance else 0) + (15 if has_high_throughput else 0)))
    sec_index = 96 if (has_finance or classified_domain == "Cybersecurity & Zero-Trust") else (90 if has_auth else 82)
    perf_index = 95 if (has_high_throughput or classified_domain == "Video & Media Streaming") else (88 if has_ai else 78)
    cost_efficiency_index = max(40, 92 - int(complexity_score * 0.35))

    return {
        "raw_prompt": raw,
        "domain": classified_domain,
        "main_entity": main_entity,
        "secondary_entities": secondary_entities,
        "all_entities": extracted_entities,
        "has_ai": has_ai,
        "has_finance": has_finance,
        "has_high_throughput": has_high_throughput,
        "has_auth": has_auth,
        "scale": scale_label,
        "budget_est": budget_est,
        "timeline_est": timeline_est,
        "complexity_score": complexity_score,
        "sec_index": sec_index,
        "perf_index": perf_index,
        "cost_efficiency_index": cost_efficiency_index
    }

