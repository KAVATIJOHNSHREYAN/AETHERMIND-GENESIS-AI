import math

def calculate_architecture_scores(security_weight: float, perf_weight: float, cost_weight: float, domain_specs: dict) -> dict:
    """
    Multi-Objective Optimization Function (Computational Intelligence):
    Evaluates architecture trade-offs based on user priority weights and domain constraints.
    Returns normalized sub-scores and Pareto trade-off recommendations.
    """
    # Normalize weights so sum = 1.0
    total_w = max(security_weight + perf_weight + cost_weight, 0.001)
    sw = security_weight / total_w
    pw = perf_weight / total_w
    cw = cost_weight / total_w

    # Base scores driven by domain complexity
    base_sec = domain_specs.get("base_security_complexity", 75)
    base_perf = domain_specs.get("base_perf_complexity", 70)
    base_cost_efficiency = domain_specs.get("base_cost_efficiency", 80)

    # Core scores
    sec_score = min(100, round(base_sec * (0.8 + 0.4 * sw)))
    perf_score = min(100, round(base_perf * (0.8 + 0.4 * pw) - (0.1 * sw)))
    cost_score = min(100, round(base_cost_efficiency * (0.7 + 0.5 * cw) - (0.15 * pw) - (0.15 * sw)))

    # Enhanced Sub-Metrics (Scalability, Maintainability, Innovation, Reliability)
    scalability_score = min(100, round(perf_score * 0.9 + sw * 10))
    maintainability_score = min(100, round(cost_score * 0.85 + (1.0 - sw) * 15))
    innovation_score = min(100, round((perf_score + sec_score) / 2.0 * 0.95))
    reliability_score = min(100, round(sec_score * 0.6 + perf_score * 0.4))

    # Overall Weighted Architecture Score
    overall_score = round((sec_score * sw) + (perf_score * pw) + (cost_score * cw))

    # Determine Tech Recommendation Profile
    if cw >= 0.5:
        profile = "Cost-Optimized Serverless / Monolith"
        est_monthly_cost = "$15 - $45 / mo"
        primary_db = "PostgreSQL (Managed Shared) / SQLite"
    elif pw >= 0.5:
        profile = "High-Throughput Microservices & Redis Cluster"
        est_monthly_cost = "$150 - $450 / mo"
        primary_db = "PostgreSQL + Redis Cache + Kafka/RabbitMQ"
    elif sw >= 0.5:
        profile = "Zero-Trust Encrypted Infrastructure (Air-Gapped Vaults)"
        est_monthly_cost = "$200 - $600 / mo"
        primary_db = "PostgreSQL with Field-Level Encryption + Vault"
    else:
        profile = "Balanced Hybrid Cloud Architecture"
        est_monthly_cost = "$50 - $120 / mo"
        primary_db = "PostgreSQL (Supabase/RDS) + Redis Cache"

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
