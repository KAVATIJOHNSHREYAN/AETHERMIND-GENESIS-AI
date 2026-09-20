def generate_mermaid_architecture(domain: str, tech_profile: str) -> str:
    """
    Generates dynamic Mermaid.js C4 / Flowchart syntax based on detected domain and tech profile.
    """
    if "Serverless" in tech_profile:
        return """graph TD
    Client["📱 Client App / Web Interface"] --> CDN["⚡ Cloudflare / Fastly CDN"]
    CDN --> Gateway["🚪 API Gateway (Cloudflare Workers / AWS Lambda)"]
    Gateway --> Auth["🔐 OAuth2 / JWT Auth Service"]
    Gateway --> MainApp["⚙️ Serverless Function Core"]
    MainApp --> DB[("🗄️ Shared Managed PostgreSQL")]
    MainApp --> Storage["📦 S3 Object Storage"]
"""
    elif "Microservices" in tech_profile:
        return """graph TD
    Client["📱 Client Dashboard"] --> NGINX["🛡️ NGINX / Envoy Load Balancer"]
    NGINX --> Gateway["🚪 API Gateway Router"]
    Gateway --> AuthSvc["🔐 Auth Service"]
    Gateway --> CoreSvc["⚙️ Business Logic Microservice"]
    Gateway --> AnalyticsSvc["📊 Real-Time Analytics Engine"]
    
    CoreSvc --> Cache[("⚡ Redis Cluster Cache")]
    CoreSvc --> Queue["📩 RabbitMQ / Kafka Queue"]
    Queue --> Worker["👷 Async Background Workers"]
    
    CoreSvc --> DB[("🗄️ Primary PostgreSQL Cluster")]
    AnalyticsSvc --> DB
"""
    elif "Zero-Trust" in tech_profile:
        return """graph TD
    Client["📱 Encrypted Client Session"] --> Firewall["🛡️ Web Application Firewall (WAF)"]
    Firewall --> Proxy["🔒 Reverse Proxy (Zero-Trust Enforcer)"]
    Proxy --> KMS["🔑 Key Management Service (AWS KMS / Vault)"]
    Proxy --> AppCore["⚙️ Isolated App Runtime"]
    AppCore --> EncryptedDB[("🔏 Field-Level Encrypted DB")]
    AppCore --> AuditLogs["📝 Immutable Audit Log Stream"]
"""
    else:
        return """graph TD
    User["👤 End User / Web Browser"] --> Frontend["🌐 React / Streamlit Frontend"]
    Frontend --> API["🔌 REST / GraphQL API Gateway"]
    API --> Auth["🔐 Authentication & Authorization Module"]
    API --> Controller["⚙️ Application Logic Core"]
    Controller --> Cache[("⚡ Redis Memory Cache")]
    Controller --> MainDB[("🗄️ PostgreSQL Database")]
    Controller --> Tasks["⏳ Celery Async Task Queue"]
"""
