import streamlit as st
import time
import json
from agents.engine import run_multi_agent_debate
from utils.optimization import calculate_architecture_scores
from utils.graph_builder import generate_mermaid_architecture
from utils.exporter import export_blueprint_markdown

# ---------------------------------------------------------
# Page Configuration & Dark Cyber Design System
# ---------------------------------------------------------
st.set_page_config(
    page_title="AetherMind Genesis | AI System Architect",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Glassmorphism & Cyberpunk Styling
st.markdown("""
<style>
    /* Global Theme Overrides */
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 50%, #070a12 100%);
        color: #e2e8f0;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Header Styling */
    .brand-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .brand-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Card Containers */
    .glass-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    /* Metric Card Styling */
    .metric-box {
        text-align: center;
        padding: 1rem;
        background: rgba(15, 23, 42, 0.6);
        border-radius: 10px;
        border: 1px solid rgba(56, 189, 248, 0.2);
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #38bdf8;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Chat/Debate Log Styling */
    .debate-bubble {
        padding: 0.9rem 1.2rem;
        border-radius: 10px;
        margin-bottom: 0.8rem;
        border-left: 4px solid #38bdf8;
        background: rgba(15, 23, 42, 0.5);
    }
    
    /* Button Customization */
    .stButton>button {
        background: linear-gradient(90deg, #0284c7 0%, #4f46e5 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar: Optimization Controls (Computational Intelligence)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### ⚙️ Optimization Weights")
    st.caption("Adjust priority weights to trigger Multi-Objective Optimization trade-offs:")
    
    sec_weight = st.slider("🛡️ Security Priority (OWASP/Zero-Trust)", 0.0, 1.0, 0.7, 0.1)
    perf_weight = st.slider("⚡ Performance Priority (Low Latency)", 0.0, 1.0, 0.7, 0.1)
    cost_weight = st.slider("💰 Budget Priority (Cost Minimization)", 0.0, 1.0, 0.5, 0.1)
    
    st.divider()
    st.markdown("### 📌 Presets")
    preset_choice = st.selectbox(
        "Choose an example app template:",
        [
            "Custom Prompt",
            "Scalable FinTech Payment Gateway",
            "HIPAA Telehealth Patient Portal",
            "Real-Time AI Video Generator",
            "High-Volume E-Commerce Platform"
        ]
    )

# ---------------------------------------------------------
# Main UI Layout
# ---------------------------------------------------------
st.markdown('<div class="brand-title">AetherMind Genesis</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-subtitle">Autonomous AI System Architect & Multi-Agent Design Simulator</div>', unsafe_allow_html=True)

# Input Console
default_prompt = ""
if preset_choice == "Scalable FinTech Payment Gateway":
    default_prompt = "Build a high-security scalable FinTech payment gateway with transaction tracking and account balances."
elif preset_choice == "HIPAA Telehealth Patient Portal":
    default_prompt = "Build a HIPAA-compliant telehealth application for patient records, appointments, and encrypted doctor chats."
elif preset_choice == "Real-Time AI Video Generator":
    default_prompt = "Build a high-performance AI video generation app with real-time prompt rendering and async background workers."
elif preset_choice == "High-Volume E-Commerce Platform":
    default_prompt = "Build an e-commerce platform with flash sale support, product catalog, user shopping carts, and order processing."

prompt_input = st.text_area(
    "💡 Describe your software idea in plain English:",
    value=default_prompt,
    placeholder="e.g. Build an AI-powered fitness tracking app with real-time analytics, user profiles, and workout history...",
    height=100
)

col_btn, col_info = st.columns([1, 4])
with col_btn:
    generate_btn = st.button("🌌 Synthesize Blueprint", use_container_width=True)
with col_info:
    st.caption("⚡ Powered by AetherMind API-Keyless Multi-Agent Reasoning Engine")

# ---------------------------------------------------------
# Execution & Blueprint Generation
# ---------------------------------------------------------
if generate_btn and prompt_input.strip():
    with st.spinner("🚀 Launching Multi-Agent Architectural Debate..."):
        # Run agent reasoning engine
        results = run_multi_agent_debate(prompt_input, sec_weight, perf_weight, cost_weight)
        
        # Calculate computational optimization scores
        scores = calculate_architecture_scores(sec_weight, perf_weight, cost_weight, results)
        
        # Build Mermaid graph syntax
        mermaid_code = generate_mermaid_architecture(results["domain"], scores["architecture_profile"])
        
        # Store in session state
        st.session_state["blueprint_data"] = {
            "prompt": prompt_input,
            "results": results,
            "scores": scores,
            "mermaid_code": mermaid_code
        }

# Render Results if available in state
if "blueprint_data" in st.session_state:
    data = st.session_state["blueprint_data"]
    results = data["results"]
    scores = data["scores"]
    mermaid_code = data["mermaid_code"]

    st.divider()

    # 1. Metric Scoreboard Cards
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{scores["overall_score"]}/100</div><div class="metric-label">Architecture Score</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{scores["security_score"]}</div><div class="metric-label">Security Index</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{scores["performance_score"]}</div><div class="metric-label">Performance Index</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{scores["cost_efficiency_score"]}</div><div class="metric-label">Cost Efficiency</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. Main Tabbed Workbench
    tab_debate, tab_diagram, tab_db, tab_api, tab_export = st.tabs([
        "🗣️ Multi-Agent Debate",
        "🗺️ System Topology Diagram",
        "🗄️ Database Schema",
        "🔌 API Endpoints Spec",
        "📥 Export Blueprint"
    ])

    # TAB 1: Multi-Agent Debate Console
    with tab_debate:
        st.markdown("### 💬 Multi-Agent Consensus Stream")
        st.caption("Observe specialized AI architect agents debating trade-offs in real time:")
        for log in results["debate_logs"]:
            st.markdown(f"""
            <div class="debate-bubble">
                <strong>{log['avatar']} {log['agent']}</strong><br>
                <span style="color: #cbd5e1;">{log['message']}</span>
            </div>
            """, unsafe_allow_html=True)

    # TAB 2: System Architecture Diagram (Mermaid)
    with tab_diagram:
        st.markdown("### 🗺️ Dynamic C4 System Architecture Diagram")
        st.caption(f"Profile: **{scores['architecture_profile']}** | Est. Cost: **{scores['estimated_monthly_cost']}**")
        
        # Display Mermaid diagram code block
        st.code(mermaid_code, language="mermaid")
        st.info("💡 Tip: Copy the block above into any Mermaid viewer or GitHub README to render the visual graph live!")

    # TAB 3: Database Schema (SQL)
    with tab_db:
        st.markdown(f"### 🗄️ Relational DDL Database Schema ({scores['recommended_db']})")
        st.code(results["sql_schema"], language="sql")

    # TAB 4: API OpenAPI Specs
    with tab_api:
        st.markdown("### 🔌 Generated OpenAPI / REST Specification")
        st.code(results["api_spec"], language="json")

    # TAB 5: Blueprint Export
    with tab_export:
        st.markdown("### 📥 Download Complete Architecture Blueprint")
        markdown_doc = export_blueprint_markdown(
            data["prompt"],
            scores,
            results["debate_logs"],
            mermaid_code,
            results["sql_schema"],
            results["api_spec"]
        )
        
        st.download_button(
            label="📄 Download Blueprint (.md)",
            data=markdown_doc,
            file_name="AetherMind_Genesis_Blueprint.md",
            mime="text/markdown",
            use_container_width=True
        )
        
        st.markdown("#### Markdown Preview:")
        st.text_area("Blueprint Raw Output", value=markdown_doc, height=250)
