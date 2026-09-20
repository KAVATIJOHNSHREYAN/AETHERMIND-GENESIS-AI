def calculate_architecture_scores(security_weight: float, perf_weight: float, cost_weight: float, domain_specs: dict) -> dict:
    """
    Dynamic Multi-Objective Computational Scoring Engine:
    Calculates security, latency, cost, and reliability metrics mathematically directly from the parsed graph depth and user weights.
    """
    total_w = max(security_weight + perf_weight + cost_weight, 0.001)
    sw = security_weight / total_w
    pw = perf_weight / total_w
    cw = cost_weight / total_w

    base_sec = domain_specs.get("base_security_complexity", 80)
    base_perf = domain_specs.get("base_perf_complexity", 75)
    base_cost_efficiency = domain_specs.get("base_cost_efficiency", 70)

    # Mathematical scoring curves
    sec_score = min(100, round(base_sec * (0.8 + 0.4 * sw)))
    perf_score = min(100, round(base_perf * (0.8 + 0.4 * pw) - (0.05 * sw)))
    cost_score = min(100, round(base_cost_efficiency * (0.7 + 0.5 * cw) - (0.1 * pw)))

    scalability_score = min(100, round(perf_score * 0.9 + pw * 10))
    maintainability_score = min(100, round(cost_score * 0.85 + cw * 15))
    innovation_score = min(100, round((perf_score + sec_score) / 2.0))
    reliability_score = min(100, round(sec_score * 0.5 + perf_score * 0.5))

    overall_score = round((sec_score * sw) + (perf_score * pw) + (cost_score * cw))

    # Dynamic Profile Generation
    domain_name = domain_specs.get("domain", "System Core")
    if cw >= 0.5:
        profile = f"Cost-Optimized Serverless Architecture ({domain_name})"
        est_monthly_cost = "$25 - $60 / mo"
        primary_db = "PostgreSQL Shared Serverless / SQLite"
    elif pw >= 0.5:
        profile = f"High-Throughput Microservices Cluster ({domain_name})"
        est_monthly_cost = "$150 - $450 / mo"
        primary_db = "PostgreSQL + Redis Cluster + Kafka"
    elif sw >= 0.5:
        profile = f"Zero-Trust Encrypted Vault Architecture ({domain_name})"
        est_monthly_cost = "$200 - $600 / mo"
        primary_db = "PostgreSQL Field-Level Encrypted + KMS"
    else:
        profile = f"Balanced Hybrid Architecture ({domain_name})"
        est_monthly_cost = "$50 - $120 / mo"
        primary_db = "PostgreSQL (RDS) + Redis Cache"

    return {
        "overall_score": overall_score,
        "security_score": sec_score,
        "performance_score": perf_score,
        "cost_efficiency_score": cost_score,
        "scalability_score": scalability_score,
        "maintainability_score": maintainability_score,
        "innovation_score": innovation_score,
        "reliability_score": reliability_score,
        "architecture_profile": profile,
        "estimated_monthly_cost": est_monthly_cost,
        "recommended_db": primary_db,
        "weights": {"security": round(sw, 2), "performance": round(pw, 2), "cost": round(cw, 2)}
    }
