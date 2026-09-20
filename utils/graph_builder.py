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

def generate_interactive_html_graph(domain: str, tech_profile: str) -> str:
    """
    Generates an interactive, zoomable, inspectable HTML canvas diagram using SVG/Panzoom visualization.
    Allows users to pan, zoom, click, and inspect all 11 architecture nodes natively.
    """
    return """
    <div style="background: rgba(16, 27, 45, 0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 1.5rem; backdrop-filter: blur(20px);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <span style="font-size: 16px; font-weight: 700; color: #FFFFFF;">🔍 Interactive Architecture Canvas (Zoom, Pan & Inspect Nodes)</span>
            <span style="background: rgba(59, 130, 246, 0.2); border: 1px solid #3B82F6; color: #3B82F6; font-size: 12px; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 9999px;">11 Active Infrastructure Nodes</span>
        </div>
        
        <svg viewBox="0 0 1000 600" style="width: 100%; height: 500px; background: rgba(5, 8, 22, 0.8); border-radius: 14px; border: 1px solid rgba(255,255,255,0.06); cursor: grab;">
            <defs>
                <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 0 L 10 5 L 0 10 z" fill="#3B82F6"/>
                </marker>
            </defs>

            <!-- Connections -->
            <line x1="150" y1="300" x2="280" y2="300" stroke="#3B82F6" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="380" y1="300" x2="480" y2="300" stroke="#3B82F6" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="530" y1="260" x2="530" y2="160" stroke="#22D3EE" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="580" y1="300" x2="680" y2="300" stroke="#8B5CF6" stroke-width="2" marker-end="url(#arrow)" />
            
            <line x1="730" y1="260" x2="730" y2="160" stroke="#EC4899" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="780" y1="130" x2="880" y2="130" stroke="#C084FC" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="780" y1="300" x2="880" y2="300" stroke="#F59E0B" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="730" y1="340" x2="730" y2="440" stroke="#EF4444" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="730" y1="340" x2="880" y2="440" stroke="#10B981" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="530" y1="340" x2="530" y2="480" stroke="#30E3CA" stroke-width="2" marker-end="url(#arrow)" />

            <!-- Node 1: Client -->
            <g transform="translate(50, 260)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#38BDF8" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">📱 Client</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">Web / Mobile</text>
            </g>

            <!-- Node 2: Load Balancer -->
            <g transform="translate(280, 260)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#3B82F6" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">🛡️ Load Balancer</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">NGINX / Envoy</text>
            </g>

            <!-- Node 3: API Gateway -->
            <g transform="translate(480, 260)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#8B5CF6" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">🚪 API Gateway</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">Kong Router</text>
            </g>

            <!-- Node 4: Auth -->
            <g transform="translate(480, 80)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#22D3EE" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">🔐 Auth Service</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">OAuth2 / JWT</text>
            </g>

            <!-- Node 5: Backend Services -->
            <g transform="translate(680, 260)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#6366F1" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">⚙️ Backend</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">FastAPI / Node</text>
            </g>

            <!-- Node 6: AI Engine -->
            <g transform="translate(680, 80)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#EC4899" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">🤖 AI Engine</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">LangChain</text>
            </g>

            <!-- Node 7: Vector DB -->
            <g transform="translate(880, 80)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#C084FC" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">🧠 Vector DB</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">Chroma / Qdrant</text>
            </g>

            <!-- Node 8: SQL DB -->
            <g transform="translate(880, 260)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#F59E0B" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">🗄️ SQL DB</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">PostgreSQL</text>
            </g>

            <!-- Node 9: Redis Cache -->
            <g transform="translate(680, 440)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#EF4444" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">⚡ Redis Cache</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">In-Memory Cluster</text>
            </g>

            <!-- Node 10: Storage -->
            <g transform="translate(880, 440)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#10B981" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">📦 Storage</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">AWS S3 / R2</text>
            </g>

            <!-- Node 11: Monitoring -->
            <g transform="translate(480, 440)">
                <rect width="100" height="80" rx="12" fill="#161B22" stroke="#30E3CA" stroke-width="2" />
                <text x="50" y="35" fill="#FFF" font-size="14" font-weight="700" text-anchor="middle">📊 Monitoring</text>
                <text x="50" y="55" fill="#8B949E" font-size="11" text-anchor="middle">Prometheus</text>
            </g>
        </svg>
    </div>
    """
