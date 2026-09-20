import streamlit as st
import time
import json
import plotly.graph_objects as go
from agents.engine import run_multi_agent_debate
from utils.optimization import calculate_architecture_scores
from utils.graph_builder import generate_mermaid_architecture
from utils.exporter import export_blueprint_markdown

# ---------------------------------------------------------
# Page Configuration & Dark Cyber Design System (Vercel/Linear/Apple Style)
# ---------------------------------------------------------
st.set_page_config(
    page_title="AetherMind Genesis | Autonomous AI OS",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Dark Glassmorphism CSS Inject (Color Theme: #07090F, #10131A, #161B22, #3B82F6, #22D3EE, #8B5CF6)
st.markdown("""
<style>
    /* Global Background & Typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    html, body, .stApp {
        background-color: #07090F !important;
        background-image: 
            radial-gradient(circle at 15% 15%, rgba(59, 130, 246, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 85% 85%, rgba(139, 92, 246, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 50% 50%, rgba(34, 211, 238, 0.04) 0%, transparent 60%);
        color: #F8FAFC !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #10131A !important;
        border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
    }
    
    /* Premium Header Badge */
    .status-badge-container {
        display: flex;
        gap: 0.6rem;
        align-items: center;
        margin-bottom: 0.8rem;
    }
    .status-badge {
        background: rgba(34, 211, 238, 0.1);
        border: 1px solid rgba(34, 211, 238, 0.3);
        color: #22D3EE;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
    }
    .status-badge-purple {
        background: rgba(139, 92, 246, 0.1);
        border: 1px solid rgba(139, 92, 246, 0.3);
        color: #C084FC;
    }

    /* Header Title */
    .brand-title {
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #FFFFFF 0%, #94A3B8 50%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        line-height: 1.1;
    }
    .brand-subtitle {
        color: #94A3B8;
        font-size: 1.15rem;
        font-weight: 400;
        margin-bottom: 2rem;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: #161B22;
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(16px);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .glass-card:hover {
        border-color: rgba(59, 130, 246, 0.3);
        transform: translateY(-2px);
    }

    /* Metric Stat Card */
    .metric-card {
        background: #10131A;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 1.2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, #3B82F6, #22D3EE);
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.02em;
        font-family: 'JetBrains Mono', monospace;
    }
    .metric-label {
        font-size: 0.8rem;
        color: #94A3B8;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.08em;
        margin-top: 0.3rem;
    }

    /* Agent Debate Bubble Styling */
    .agent-bubble {
        background: #10131A;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-left: 4px solid #3B82F6;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
    }
    .agent-bubble-sec { border-left-color: #22D3EE; }
    .agent-bubble-perf { border-left-color: #8B5CF6; }
    .agent-bubble-cost { border-left-color: #10B981; }

    .agent-header {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-weight: 700;
        font-size: 0.95rem;
        color: #F8FAFC;
        margin-bottom: 0.4rem;
    }
    .agent-msg {
        color: #CBD5E1;
        font-size: 0.92rem;
        line-height: 1.5;
    }

    /* Synthesize Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 50%, #1D4ED8 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.35) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) scale(1.01) !important;
        box-shadow: 0 8px 30px rgba(59, 130, 246, 0.5) !important;
    }

    /* Text Area Styling */
    .stTextArea textarea {
        background-color: #10131A !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #F8FAFC !important;
        font-size: 0.95rem !important;
    }
    .stTextArea textarea:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar: Optimization Controls & Presets
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### ⚡ Optimization Matrix")
    st.caption("Adjust priority weights to balance Pareto constraints:")
    
    sec_weight = st.slider("🛡️ Security (OWASP / Zero-Trust)", 0.0, 1.0, 0.7, 0.1)
    perf_weight = st.slider("⚡ Performance (Low Latency / RPS)", 0.0, 1.0, 0.7, 0.1)
    cost_weight = st.slider("💰 Budget (Cloud Cost Efficiency)", 0.0, 1.0, 0.5, 0.1)
    
    st.divider()
    st.markdown("### 📌 Architecture Presets")
    preset_choice = st.selectbox(
        "Load example blueprint archetype:",
        [
            "Custom Prompt",
            "Scalable FinTech Payment Gateway",
            "HIPAA Telehealth Patient Portal",
            "Real-Time AI Video Generator",
            "High-Volume E-Commerce Platform"
        ]
    )

# ---------------------------------------------------------
# Main UI Header & Input Engine
# ---------------------------------------------------------
st.markdown("""
<div class="status-badge-container">
    <span class="status-badge">⚡ Offline Mode Enabled</span>
    <span class="status-badge status-badge-purple">🔒 API Keyless Runtime</span>
    <span class="status-badge">🧠 Computational Intelligence Engine</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="brand-title">AetherMind Genesis</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-subtitle">Autonomous Computational System Architect & Multi-Agent Design Simulator</div>', unsafe_allow_html=True)

# Input Bar with Auto-fill Presets
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
    "💡 Describe your software system concept in plain English:",
    value=default_prompt,
    placeholder="e.g. Build an AI-powered fitness tracking platform with real-time biometric analytics...",
    height=100
)

col_btn, col_info = st.columns([1, 4])
with col_btn:
    generate_btn = st.button("🌌 Synthesize Blueprint", use_container_width=True)
with col_info:
    st.caption("⚡ Multi-Agent Engine ready | Zero-Latency Local Synthesis")

# ---------------------------------------------------------
# Execution & State Handler
# ---------------------------------------------------------
if generate_btn and prompt_input.strip():
    with st.spinner("🚀 Simulating Multi-Agent Consensus & Generating Pareto Graph..."):
        results = run_multi_agent_debate(prompt_input, sec_weight, perf_weight, cost_weight)
        scores = calculate_architecture_scores(sec_weight, perf_weight, cost_weight, results)
        mermaid_code = generate_mermaid_architecture(results["domain"], scores["architecture_profile"])
        
        st.session_state["blueprint_data"] = {
            "prompt": prompt_input,
            "results": results,
            "scores": scores,
            "mermaid_code": mermaid_code
        }

# ---------------------------------------------------------
# Render Results & Visual Analytics Dashboard
# ---------------------------------------------------------
if "blueprint_data" in st.session_state:
    data = st.session_state["blueprint_data"]
    results = data["results"]
    scores = data["scores"]
    mermaid_code = data["mermaid_code"]

    st.divider()

    # 1. Primary Analytics Cards (8 Metric Indicators)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores["overall_score"]}/100</div><div class="metric-label">Architecture Score</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores["security_score"]}</div><div class="metric-label">Security Index</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores["performance_score"]}</div><div class="metric-label">Performance Index</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores["cost_efficiency_score"]}</div><div class="metric-label">Cost Efficiency</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores["scalability_score"]}</div><div class="metric-label">Scalability Index</div></div>', unsafe_allow_html=True)
    with c6:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores["maintainability_score"]}</div><div class="metric-label">Maintainability</div></div>', unsafe_allow_html=True)
    with c7:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores["innovation_score"]}</div><div class="metric-label">Innovation Score</div></div>', unsafe_allow_html=True)
    with c8:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores["reliability_score"]}</div><div class="metric-label">Reliability Score</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. Interactive Plotly Radar Chart (Trade-Off Analytics)
    col_chart, col_info_box = st.columns([1.2, 1])
    with col_chart:
        st.markdown("#### 📊 Architecture Trade-Off Radar (Computational Analysis)")
        categories = ['Security', 'Performance', 'Cost Efficiency', 'Scalability', 'Maintainability', 'Reliability']
        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=[scores['security_score'], scores['performance_score'], scores['cost_efficiency_score'], 
               scores['scalability_score'], scores['maintainability_score'], scores['reliability_score']],
            theta=categories,
            fill='toself',
            name='Current Blueprint',
            line_color='#3B82F6',
            fillcolor='rgba(59, 130, 246, 0.25)'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], color="#94A3B8"),
                angularaxis=dict(color="#F8FAFC")
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#F8FAFC',
            margin=dict(l=40, r=40, t=20, b=20),
            showlegend=False,
            height=320
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_info_box:
        st.markdown("#### 🎯 Recommended Tech Stack & Profile")
        st.markdown(f"""
        <div class="glass-card">
            <p><strong>Architecture Profile:</strong> <span style="color:#22D3EE;">{scores['architecture_profile']}</span></p>
            <p><strong>Est. Monthly Cloud Budget:</strong> <span style="color:#10B981;">{scores['estimated_monthly_cost']}</span></p>
            <p><strong>Primary Database:</strong> <span style="color:#C084FC;">{scores['recommended_db']}</span></p>
            <p style="font-size:0.85rem; color:#94A3B8;">Synthesized dynamically by balancing Pareto optimization weights across 4 specialized agents.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # 3. Enterprise Tabbed Workbench
    tab_debate, tab_diagram, tab_db, tab_api, tab_export = st.tabs([
        "🗣️ Multi-Agent Debate Console",
        "🗺️ System Topology Diagram",
        "🗄️ Database DDL Schema",
        "🔌 OpenAPI Specification",
        "📥 Blueprint Export Hub"
    ])

    # TAB 1: Multi-Agent Collaboration View
    with tab_debate:
        st.markdown("### 🗣️ Multi-Agent Collaborative Reasoning Log")
        st.caption("Real-time argumentation stream between specialized AI architects:")
        
        for log in results["debate_logs"]:
            agent_class = "agent-bubble"
            if "Security" in log["agent"]: agent_class += " agent-bubble-sec"
            elif "Performance" in log["agent"]: agent_class += " agent-bubble-perf"
            elif "Cost" in log["agent"]: agent_class += " agent-bubble-cost"

            st.markdown(f"""
            <div class="{agent_class}">
                <div class="agent-header">{log['avatar']} {log['agent']}</div>
                <div class="agent-msg">{log['message']}</div>
            </div>
            """, unsafe_allow_html=True)

    # TAB 2: Architecture Diagram (Mermaid)
    with tab_diagram:
        st.markdown("### 🗺️ Visual System Architecture Graph (Mermaid.js)")
        st.caption("Copy code below to render interactively in GitHub or Mermaid Live Editor:")
        st.code(mermaid_code, language="mermaid")

    # TAB 3: Database DDL Schema
    with tab_db:
        st.markdown(f"### 🗄️ Relational DDL Database Schema ({scores['recommended_db']})")
        st.code(results["sql_schema"], language="sql")

    # TAB 4: API OpenAPI JSON Specs
    with tab_api:
        st.markdown("### 🔌 Generated OpenAPI / REST Endpoint Specification")
        st.code(results["api_spec"], language="json")

    # TAB 5: Blueprint Export
    with tab_export:
        st.markdown("### 📥 Download Blueprint Specification")
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
        st.text_area("Raw Blueprint Preview", value=markdown_doc, height=250)
