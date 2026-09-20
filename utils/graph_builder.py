def generate_mermaid_architecture(domain: str, tech_profile: str) -> str:
    """
    Generates dynamic Mermaid.js architecture topology featuring all 11 required system components:
    Client, Load Balancer, API Gateway, Auth, Backend Services, AI Engine, Vector DB, SQL DB, Redis, Storage, Monitoring.
    """
    return f"""graph TD
    Client["📱 Client App (Web / Mobile)"] --> LB["🛡️ Load Balancer (NGINX / Envoy)"]
    LB --> Gateway["🚪 API Gateway (Kong / Cloudflare)"]
    
    Gateway --> Auth["🔐 Auth Service (OAuth2 / JWT / KMS)"]
    Gateway --> Backend["⚙️ Backend Services Core (FastAPI / Node)"]
    
    Backend --> AIEngine["🤖 AI Engine (LangChain / Local Embeddings)"]
    Backend --> Cache[("⚡ Redis Memory Cache")]
    
    AIEngine --> VectorDB[("🧠 Vector Database (Chroma / Qdrant)")]
    Backend --> SQLDB[("🗄️ SQL Database (PostgreSQL)")]
    Backend --> Storage["📦 Object Storage (S3 / Cloudflare R2)"]
    
    Backend --> Monitoring["📊 Monitoring & Observability (Prometheus / Grafana)"]
    Gateway --> Monitoring
    AIEngine --> Monitoring

    style Client fill:#1E293B,stroke:#38BDF8,stroke-width:2px,color:#FFF
    style LB fill:#1E293B,stroke:#3B82F6,stroke-width:2px,color:#FFF
    style Gateway fill:#1E293B,stroke:#8B5CF6,stroke-width:2px,color:#FFF
    style Auth fill:#1E293B,stroke:#22D3EE,stroke-width:2px,color:#FFF
    style Backend fill:#1E293B,stroke:#6366F1,stroke-width:2px,color:#FFF
    style AIEngine fill:#1E293B,stroke:#EC4899,stroke-width:2px,color:#FFF
    style VectorDB fill:#1E293B,stroke:#C084FC,stroke-width:2px,color:#FFF
    style SQLDB fill:#1E293B,stroke:#F59E0B,stroke-width:2px,color:#FFF
    style Cache fill:#1E293B,stroke:#EF4444,stroke-width:2px,color:#FFF
    style Storage fill:#1E293B,stroke:#10B981,stroke-width:2px,color:#FFF
    style Monitoring fill:#1E293B,stroke:#30E3CA,stroke-width:2px,color:#FFF
"""

def generate_interactive_3d_topology_graph(domain: str, tech_profile: str) -> str:
    """
    Generates a full 3D WebGL Network Topology Viewer using Three.js & 3D Force Graph.
    Displays glowing 3D nodes, pulsing directional particle light streams, orbital controls,
    node inspection tooltips, and real-time 3D rotation.
    """
    return """
    <div style="background: rgba(16, 27, 45, 0.85); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 1.5rem; backdrop-filter: blur(25px); box-shadow: 0 0 35px rgba(59, 130, 246, 0.15);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
                <span style="font-size: 18px; font-weight: 800; color: #22D3EE; font-family: 'Plus Jakarta Sans', sans-serif;">🌌 3D WebGL System Network Topology Viewer</span>
                <p style="font-size: 12px; color: #8B949E; margin: 0.2rem 0 0 0;">Drag to rotate in 3D • Scroll to zoom • Click node to inspect state</p>
            </div>
            <span style="background: rgba(34, 211, 238, 0.15); border: 1px solid #22D3EE; color: #22D3EE; font-size: 12px; font-weight: 700; padding: 0.3rem 0.8rem; border-radius: 9999px;">
                WebGL 3D Engine Active
            </span>
        </div>

        <div id="3d-graph-container" style="width: 100%; height: 520px; border-radius: 16px; overflow: hidden; background: #050816; position: relative; border: 1px solid rgba(255,255,255,0.08);"></div>

        <script src="https://unpkg.com/3d-force-graph"></script>
        <script>
            (function() {
                const gData = {
                    nodes: [
                        { id: 'client', name: '📱 Client App', group: 1, val: 20, color: '#38BDF8', desc: 'React 18 / Mobile Client' },
                        { id: 'lb', name: '🛡️ Load Balancer', group: 1, val: 24, color: '#3B82F6', desc: 'NGINX / Envoy Ingress' },
                        { id: 'gateway', name: '🚪 API Gateway', group: 2, val: 28, color: '#8B5CF6', desc: 'Kong REST / GraphQL Router' },
                        { id: 'auth', name: '🔐 Auth Service', group: 2, val: 22, color: '#22D3EE', desc: 'OAuth2 / SAML / Ed25519 JWT' },
                        { id: 'backend', name: '⚙️ Core Microservices', group: 3, val: 32, color: '#6366F1', desc: 'Rust Axum / Tokio Runtime' },
                        { id: 'ai', name: '🤖 AI Inference Engine', group: 4, val: 30, color: '#EC4899', desc: 'vLLM / PyTorch GPU Pipeline' },
                        { id: 'vectordb', name: '🧠 Vector Database', group: 4, val: 26, color: '#C084FC', desc: 'pgvector / HNSW Embeddings' },
                        { id: 'sqldb', name: '🗄️ PostgreSQL Database', group: 5, val: 28, color: '#F59E0B', desc: 'PostgreSQL 16 Primary ACID' },
                        { id: 'cache', name: '⚡ Redis Cache', group: 5, val: 24, color: '#EF4444', desc: 'Redis v7 Memory Cluster' },
                        { id: 'storage', name: '📦 S3 Storage', group: 5, val: 22, color: '#10B981', desc: 'AWS S3 / Cloudflare R2' },
                        { id: 'monitoring', name: '📊 Prometheus Monitoring', group: 6, val: 25, color: '#30E3CA', desc: 'Prometheus + Grafana Telemetry' }
                    ],
                    links: [
                        { source: 'client', target: 'lb', name: 'HTTPS / WSS' },
                        { source: 'lb', target: 'gateway', name: 'gRPC Ingress' },
                        { source: 'gateway', target: 'auth', name: 'Token Verification' },
                        { source: 'gateway', target: 'backend', name: 'Proxy Route' },
                        { source: 'backend', target: 'ai', name: 'Async Model Request' },
                        { source: 'ai', target: 'vectordb', name: 'Vector Similarity Query' },
                        { source: 'backend', target: 'sqldb', name: 'ACID Transactions' },
                        { source: 'backend', target: 'cache', name: 'Read-Through Cache' },
                        { source: 'backend', target: 'storage', name: 'Binary Payload Store' },
                        { source: 'backend', target: 'monitoring', name: 'OpenTelemetry Spans' },
                        { source: 'gateway', target: 'monitoring', name: 'Request Metrics' },
                        { source: 'ai', target: 'monitoring', name: 'GPU Latency Telemetry' }
                    ]
                };

                const container = document.getElementById('3d-graph-container');
                if (container && typeof ForceGraph3D !== 'undefined') {
                    const Graph = ForceGraph3D()(container)
                        .graphData(gData)
                        .nodeId('id')
                        .nodeLabel(node => `<div style="background:rgba(16,27,45,0.95); padding:8px 12px; border-radius:8px; border:1px solid ${node.color}; color:#FFF; font-family:sans-serif;"><strong>${node.name}</strong><br><small style="color:#C9D1D9">${node.desc}</small></div>`)
                        .nodeColor(node => node.color)
                        .nodeVal('val')
                        .nodeResolution(16)
                        .linkSource('source')
                        .linkTarget('target')
                        .linkLabel(link => `<span style="color:#38BDF8; font-size:11px; background:#0B1220; padding:2px 6px; border-radius:4px;">${link.name}</span>`)
                        .linkDirectionalParticles(4)
                        .linkDirectionalParticleSpeed(0.008)
                        .linkDirectionalParticleWidth(2.5)
                        .linkDirectionalParticleColor(() => '#38BDF8')
                        .linkColor(() => 'rgba(255,255,255,0.15)')
                        .backgroundColor('#050816');

                    Graph.controls().autoRotate = true;
                    Graph.controls().autoRotateSpeed = 0.8;
                }
            })();
        </script>
    </div>
    """

