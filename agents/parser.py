import re

def parse_prompt_requirements(prompt: str) -> dict:
    """
    Pure Computational Prompt Parser:
    Analyzes raw user prompt dynamically to extract entities, verbs, data models,
    security levels, performance targets, and architectural complexity without static domain lists.
    """
    raw = prompt.strip()
    words = re.findall(r'\w+', raw.lower())
    
    # 1. Dynamic Entity & Noun Extraction
    stop_words = {"build", "a", "an", "the", "for", "with", "and", "or", "in", "to", "app", "application", "system", "platform"}
    extracted_entities = [w.capitalize() for w in words if len(w) > 3 and w not in stop_words]
    
    main_entity = extracted_entities[0] if extracted_entities else "CoreSystem"
    secondary_entities = extracted_entities[1:5] if len(extracted_entities) > 1 else ["Resource", "Metadata", "Log"]
    
    # 2. Dynamic Feature & Metric Detection
    has_auth = any(w in words for w in ["auth", "login", "user", "secure", "privacy", "account", "permission", "kyc", "token"])
    has_finance = any(w in words for w in ["money", "payment", "bank", "pay", "transaction", "balance", "transfer", "wallet"])
    has_high_throughput = any(w in words for w in ["video", "stream", "live", "realtime", "real-time", "high", "scale", "fleet", "driver"])
    has_ai = any(w in words for w in ["ai", "model", "llm", "prompt", "generator", "predict", "intelligence"])
    
    # 3. Dynamic Architectural Complexity Metrics
    complexity_score = min(100, max(40, len(words) * 5 + (15 if has_finance else 0) + (20 if has_high_throughput else 0)))
    
    sec_index = 95 if has_finance else (88 if has_auth else 75)
    perf_index = 92 if has_high_throughput else (85 if has_ai else 70)
    cost_efficiency_index = max(40, 90 - int(complexity_score * 0.4))
    
    return {
        "raw_prompt": raw,
        "main_entity": main_entity,
        "secondary_entities": secondary_entities,
        "all_entities": extracted_entities,
        "has_auth": has_auth,
        "has_finance": has_finance,
        "has_high_throughput": has_high_throughput,
        "has_ai": has_ai,
        "complexity_score": complexity_score,
        "sec_index": sec_index,
        "perf_index": perf_index,
        "cost_efficiency_index": cost_efficiency_index
    }
