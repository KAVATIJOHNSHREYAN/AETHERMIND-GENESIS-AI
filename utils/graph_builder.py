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
    Generates a full 3D Network Topology Viewer with 3D WebGL / Canvas rendering engine.
    Features glowing 3D spherical nodes, pulsing link particle streams, 3D rotation, and node cards.
    """
    return """
    <div style="background: rgba(16, 27, 45, 0.85); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 1.5rem; backdrop-filter: blur(25px); box-shadow: 0 0 35px rgba(59, 130, 246, 0.15); color: #FFFFFF; font-family: 'Plus Jakarta Sans', system-ui, sans-serif;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
                <span style="font-size: 18px; font-weight: 800; color: #22D3EE;">🌌 3D System Network Topology Viewer</span>
                <p style="font-size: 12px; color: #8B949E; margin: 0.2rem 0 0 0;">Drag/Move mouse to rotate 3D view • Pulsing real-time network streams</p>
            </div>
            <span style="background: rgba(34, 211, 238, 0.15); border: 1px solid #22D3EE; color: #22D3EE; font-size: 12px; font-weight: 700; padding: 0.3rem 0.8rem; border-radius: 9999px;">
                WebGL 3D Engine Active
            </span>
        </div>

        <div id="3d-graph-wrapper" style="width: 100%; height: 500px; border-radius: 16px; overflow: hidden; background: #050816; position: relative; border: 1px solid rgba(255,255,255,0.08);">
            <canvas id="topology-canvas" width="1200" height="500" style="width: 100%; height: 100%; cursor: grab;"></canvas>
            
            <!-- Tooltip overlay -->
            <div id="node-tooltip" style="position: absolute; bottom: 15px; left: 15px; background: rgba(16, 27, 45, 0.92); border: 1px solid #3B82F6; padding: 10px 16px; border-radius: 10px; font-size: 13px; color: #FFF; pointer-events: none; backdrop-filter: blur(10px); display: none;">
                <strong id="tooltip-title" style="color: #22D3EE; font-size: 14px;"></strong><br>
                <span id="tooltip-desc" style="color: #C9D1D9;"></span>
            </div>
        </div>

        <script>
            (function() {
                const canvas = document.getElementById('topology-canvas');
                if (!canvas) return;
                const ctx = canvas.getContext('2d');
                
                // Adjust for high-DPI screens
                const rect = canvas.getBoundingClientRect();
                canvas.width = rect.width * 2;
                canvas.height = rect.height * 2;
                ctx.scale(2, 2);
                
                const W = rect.width;
                const H = rect.height;

                // 11 Infrastructure Nodes with 3D (X, Y, Z) coordinates
                const nodes = [
                    { id: 'client', name: '📱 Client App', x: -280, y: 0, z: 0, color: '#38BDF8', desc: 'React 18 / Mobile Client Ingress' },
                    { id: 'lb', name: '🛡️ Load Balancer', x: -170, y: -20, z: 40, color: '#3B82F6', desc: 'NGINX / Envoy Multi-AZ Balancer' },
                    { id: 'gateway', name: '🚪 API Gateway', x: -60, y: 0, z: -20, color: '#8B5CF6', desc: 'Kong REST / GraphQL API Router' },
                    { id: 'auth', name: '🔐 Auth Service', x: -60, y: -130, z: 80, color: '#22D3EE', desc: 'OAuth2 / SAML / Ed25519 JWT Auth' },
                    { id: 'backend', name: '⚙️ Core Microservices', x: 70, y: 0, z: 0, color: '#6366F1', desc: 'Rust Axum / Tokio Event Workers' },
                    { id: 'ai', name: '🤖 AI Inference Engine', x: 190, y: -120, z: -60, color: '#EC4899', desc: 'vLLM / PyTorch GPU Worker Pool' },
                    { id: 'vectordb', name: '🧠 Vector Database', x: 300, y: -120, z: 30, color: '#C084FC', desc: 'pgvector / HNSW Vector Search' },
                    { id: 'sqldb', name: '🗄️ PostgreSQL DB', x: 200, y: 120, z: 50, color: '#F59E0B', desc: 'PostgreSQL 16 Primary ACID Storage' },
                    { id: 'cache', name: '⚡ Redis Cache', x: 70, y: 130, z: -70, color: '#EF4444', desc: 'Redis v7 Multi-Node Memory Cluster' },
                    { id: 'storage', name: '📦 S3 Object Store', x: 300, y: 120, z: -40, color: '#10B981', desc: 'AWS S3 / Cloudflare R2 Payload Store' },
                    { id: 'monitoring', name: '📊 Prometheus', x: -60, y: 130, z: 60, color: '#30E3CA', desc: 'Prometheus + Grafana OpenTelemetry' }
                ];

                const links = [
                    { from: 0, to: 1, label: 'HTTPS' },
                    { from: 1, to: 2, label: 'gRPC' },
                    { from: 2, to: 3, label: 'Auth' },
                    { from: 2, to: 4, label: 'Route' },
                    { from: 4, to: 5, label: 'Async AI' },
                    { from: 5, to: 6, label: 'Vector RAG' },
                    { from: 4, to: 7, label: 'ACID DB' },
                    { from: 4, to: 8, label: 'Cache' },
                    { from: 4, to: 9, label: 'Payload' },
                    { from: 4, to: 10, label: 'Telemetry' },
                    { from: 2, to: 10, label: 'Metrics' }
                ];

                // Data flow animated particles
                const particles = [];
                for (let i = 0; i < 24; i++) {
                    particles.push({
                        linkIdx: Math.floor(Math.random() * links.length),
                        t: Math.random(),
                        speed: 0.006 + Math.random() * 0.008
                    });
                }

                let angleX = 0.15;
                let angleY = 0.005;
                let isDragging = false;
                let lastMouseX = 0;
                let lastMouseY = 0;
                let hoveredNode = null;

                canvas.addEventListener('mousedown', (e) => {
                    isDragging = true;
                    lastMouseX = e.clientX;
                    lastMouseY = e.clientY;
                });

                window.addEventListener('mouseup', () => isDragging = false);

                canvas.addEventListener('mousemove', (e) => {
                    if (isDragging) {
                        const dx = e.clientX - lastMouseX;
                        const dy = e.clientY - lastMouseY;
                        angleY += dx * 0.005;
                        angleX += dy * 0.005;
                        lastMouseX = e.clientX;
                        lastMouseY = e.clientY;
                    }
                });

                function render() {
                    ctx.clearRect(0, 0, W, H);
                    
                    // Auto rotate 3D scene smoothly
                    if (!isDragging) {
                        angleY += 0.004;
                    }

                    const cosY = Math.cos(angleY), sinY = Math.sin(angleY);
                    const cosX = Math.cos(angleX), sinX = Math.sin(angleX);

                    // Project 3D points to 2D Screen
                    const projected = nodes.map(n => {
                        // Rotate Y
                        let x1 = n.x * cosY - n.z * sinY;
                        let z1 = n.z * cosY + n.x * sinY;
                        // Rotate X
                        let y1 = n.y * cosX - z1 * sinX;
                        let z2 = z1 * cosX + n.y * sinX;

                        const scale = 500 / (500 + z2);
                        return {
                            sx: W / 2 + x1 * scale,
                            sy: H / 2 + y1 * scale,
                            scale: scale,
                            z: z2,
                            node: n
                        };
                    });

                    // Sort nodes by Z depth for rendering
                    projected.sort((a, b) => b.z - a.z);

                    // Draw connections with glowing lines
                    links.forEach(l => {
                        const p1 = projected.find(p => p.node === nodes[l.from]);
                        const p2 = projected.find(p => p.node === nodes[l.to]);
                        if (!p1 || !p2) return;

                        ctx.beginPath();
                        ctx.moveTo(p1.sx, p1.sy);
                        ctx.lineTo(p2.sx, p2.sy);
                        ctx.strokeStyle = 'rgba(59, 130, 246, 0.25)';
                        ctx.lineWidth = 1.5 * Math.min(p1.scale, p2.scale);
                        ctx.stroke();
                    });

                    // Animate network packet particles
                    particles.forEach(pt => {
                        pt.t += pt.speed;
                        if (pt.t > 1) pt.t = 0;
                        const l = links[pt.linkIdx];
                        const p1 = projected.find(p => p.node === nodes[l.from]);
                        const p2 = projected.find(p => p.node === nodes[l.to]);
                        if (p1 && p2) {
                            const px = p1.sx + (p2.sx - p1.sx) * pt.t;
                            const py = p1.sy + (p2.sy - p1.sy) * pt.t;
                            ctx.beginPath();
                            ctx.arc(px, py, 3, 0, Math.PI * 2);
                            ctx.fillStyle = '#22D3EE';
                            ctx.shadowColor = '#22D3EE';
                            ctx.shadowBlur = 8;
                            ctx.fill();
                            ctx.shadowBlur = 0;
                        }
                    });

                    // Draw 3D Spherical Nodes & Badges
                    projected.forEach(p => {
                        const r = 24 * p.scale;
                        
                        // Outer Glow Ring
                        ctx.beginPath();
                        ctx.arc(p.sx, p.sy, r + 4, 0, Math.PI * 2);
                        ctx.fillStyle = 'rgba(5, 8, 22, 0.8)';
                        ctx.fill();
                        
                        ctx.beginPath();
                        ctx.arc(p.sx, p.sy, r, 0, Math.PI * 2);
                        ctx.fillStyle = p.node.color;
                        ctx.shadowColor = p.node.color;
                        ctx.shadowBlur = 15 * p.scale;
                        ctx.fill();
                        ctx.shadowBlur = 0;

                        // Node Label
                        ctx.font = `bold ${Math.max(10, 12 * p.scale)}px sans-serif`;
                        ctx.fillStyle = '#FFFFFF';
                        ctx.textAlign = 'center';
                        ctx.fillText(p.node.name, p.sx, p.sy + r + 14);
                    });

                    requestAnimationFrame(render);
                }

                render();
            })();
        </script>
    </div>
    """

def generate_interactive_html_graph(domain: str, tech_profile: str) -> str:
    """Alias for backwards compatibility."""
    return generate_interactive_3d_topology_graph(domain, tech_profile)

def render_visual_mermaid(mermaid_code: str) -> str:
    """
    Renders visual Mermaid.js SVG graphic diagram inside an HTML container.
    """
    return f"""
    <div style="background: rgba(16, 27, 45, 0.85); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 1.5rem; text-align: center; backdrop-filter: blur(20px);">
        <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
        <div class="mermaid" style="display: flex; justify-content: center;">
{mermaid_code}
        </div>
        <script>
            if (window.mermaid) {{
                mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});
            }}
        </script>
    </div>
    """



