def calculate_architecture_scores(security_weight: float, perf_weight: float, cost_weight: float, domain_specs: dict) -> dict:
    """
    STAGE 8: Dynamic Scoring Engine (Calculated metrics + deduction explanations)
    STAGE 9: Architecture Radar Axes & Metrics
    STAGE 10: Cost Analysis Breakdown (Dev, Cloud, GPU, Storage, Per-Request, Per-Inference)
    STAGE 11: Comprehensive Risk Matrix & Mitigation Strategies
    """
    total_w = max(security_weight + perf_weight + cost_weight, 0.001)
    sw = security_weight / total_w
    pw = perf_weight / total_w
    cw = cost_weight / total_w

    base_sec = domain_specs.get("base_security_complexity", 85)
    base_perf = domain_specs.get("base_perf_complexity", 80)
    base_cost_efficiency = domain_specs.get("base_cost_efficiency", 75)

    # 1. Calculated Metrics (STAGE 8)
    sec_score = min(99, max(60, round(base_sec * (0.82 + 0.35 * sw))))
    perf_score = min(98, max(55, round(base_perf * (0.82 + 0.35 * pw) - (0.04 * sw))))
    cost_score = min(98, max(45, round(base_cost_efficiency * (0.75 + 0.45 * cw) - (0.08 * pw))))

    scalability_score = min(98, round(perf_score * 0.88 + pw * 12))
    maintainability_score = min(96, round(cost_score * 0.82 + cw * 18))
    reliability_score = min(99, round(sec_score * 0.52 + perf_score * 0.48))
    innovation_score = min(95, round((perf_score + sec_score) / 2.0 + 3))

    overall_score = round((sec_score * sw) + (perf_score * pw) + (cost_score * cw))

    # Explicit Point Deduction Explanations (STAGE 8)
    score_explanations = {
        "security": {
            "score": sec_score,
            "deductions": f"-{100 - sec_score} pts due to payload encryption/decryption CPU latency overhead and token validation round-trips.",
            "improvement": "Deploy hardware-accelerated AES-NI modules and cache validated token claims in local memory."
        },
        "performance": {
            "score": perf_score,
            "deductions": f"-{100 - perf_score} pts due to database read-replica propagation delay under peak concurrent traffic spikes.",
            "improvement": "Introduce edge proxy caching with stale-while-revalidate headers for hot query paths."
        },
        "cost_efficiency": {
            "score": cost_score,
            "deductions": f"-{100 - cost_score} pts due to multi-AZ redundant database standby instances and high-memory caching nodes.",
            "improvement": "Adopt Kubernetes Spot instance node pools for asynchronous background batch processing."
        },
        "scalability": {
            "score": scalability_score,
            "deductions": f"-{100 - scalability_score} pts due to state synchronization locking during horizontal database partition sharding.",
            "improvement": "Transition high-velocity time-series events to partitioned ScyllaDB / Cassandra clusters."
        }
    }

    # 2. Granular Cost Breakdown (STAGE 10)
    domain_name = domain_specs.get("domain", "System Platform")
    if cw >= 0.5:
        profile = f"Cost-Optimized Auto-Scaled Architecture ({domain_name})"
        est_monthly = "$120 - $350 / mo"
        cost_breakdown = {
            "development_cost": "$25,000 - $45,000 (One-Time)",
            "cloud_compute": "$60 / mo (Serverless Container Pods)",
            "gpu_compute": "$0 / mo (CPU Quantized Models)",
            "storage_cost": "$25 / mo (PostgreSQL RDS 100GB + S3)",
            "bandwidth_cost": "$35 / mo (Cloudflare CDN)",
            "cost_per_user": "$0.0012 / user / mo",
            "cost_per_api_request": "$0.000004 / request",
            "cost_per_inference": "$0.0008 / inference call"
        }
    elif pw >= 0.5:
        profile = f"High-Throughput Microservices Cluster ({domain_name})"
        est_monthly = "$650 - $1,850 / mo"
        cost_breakdown = {
            "development_cost": "$50,000 - $90,000 (One-Time)",
            "cloud_compute": "$450 / mo (AWS EKS 6-Node Cluster)",
            "gpu_compute": "$800 / mo (1x NVIDIA A10G Instance)",
            "storage_cost": "$200 / mo (Aurora PostgreSQL + Redis)",
            "bandwidth_cost": "$150 / mo (Global CDN Egress)",
            "cost_per_user": "$0.0045 / user / mo",
            "cost_per_api_request": "$0.000012 / request",
            "cost_per_inference": "$0.0042 / inference call"
        }
    else:
        profile = f"Enterprise Multi-Region Hybrid Cloud ({domain_name})"
        est_monthly = "$350 - $950 / mo"
        cost_breakdown = {
            "development_cost": "$35,000 - $65,000 (One-Time)",
            "cloud_compute": "$220 / mo (Kubernetes Managed Nodes)",
            "gpu_compute": "$350 / mo (Shared GPU Serverless Pool)",
            "storage_cost": "$110 / mo (PostgreSQL + ScyllaDB)",
            "bandwidth_cost": "$80 / mo (Cloudflare Enterprise)",
            "cost_per_user": "$0.0028 / user / mo",
            "cost_per_api_request": "$0.000008 / request",
            "cost_per_inference": "$0.0021 / inference call"
        }

    # 3. Comprehensive Risk Analysis (STAGE 11)
    risk_analysis = [
        {
            "category": "Technical Risk",
            "risk": "Database I/O serialization bottlenecks under peak concurrent update writes.",
            "impact": "HIGH",
            "mitigation": "Enforce write-ahead event streaming queues and separate read-replica pools."
        },
        {
            "category": "Security Risk",
            "risk": "OAuth2 JWT token replay attacks or compromised client state storage.",
            "impact": "CRITICAL",
            "mitigation": "Short-lived access tokens (15 mins), HTTP-only encrypted cookies, and automated IP rate throttling."
        },
        {
            "category": "Scaling Risk",
            "risk": "Cold-start latency spikes when serverless container worker pods auto-scale from zero.",
            "impact": "MEDIUM",
            "mitigation": "Maintain warm provisioned concurrency instances during peak business hours."
        },
        {
            "category": "Operational Risk",
            "risk": "Cascading microservice failure due to unhandled downstream third-party API outages.",
            "impact": "HIGH",
            "mitigation": "Implement Resilience4j circuit breakers, automated fallbacks, and retry exponential backoffs."
        }
    ]

    return {
        "overall_score": overall_score,
        "security_score": sec_score,
        "performance_score": perf_score,
        "cost_efficiency_score": cost_score,
        "scalability_score": scalability_score,
        "maintainability_score": maintainability_score,
        "innovation_score": innovation_score,
        "reliability_score": reliability_score,
        "score_explanations": score_explanations,
        "architecture_profile": profile,
        "estimated_monthly_cost": est_monthly,
        "cost_breakdown": cost_breakdown,
        "risk_analysis": risk_analysis,
        "recommended_db": domain_specs.get("sql_schema", "").split("CREATE TABLE")[1].split("(")[0].strip() if "CREATE TABLE" in domain_specs.get("sql_schema", "") else "PostgreSQL 16 Enterprise",
        "weights": {"security": round(sw, 2), "performance": round(pw, 2), "cost": round(cw, 2)}
    }

