
import streamlit as st
import time
import json
# pyrefly: ignore [missing-import]
import plotly.graph_objects as go
from agents.engine import run_multi_agent_debate
from utils.optimization import calculate_architecture_scores
from utils.graph_builder import generate_mermaid_architecture
from utils.exporter import export_blueprint_markdown

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="AetherMind Genesis | Autonomous AI OS",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# High-Precision Design System CSS (Vercel / Linear / Apple Standard)
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    /* Global Background & Base Typography */
    html, body, .stApp {
        background: linear-gradient(135deg, #050816 0%, #0B1220 35%, #111827 70%, #050816 100%) !important;
        background-attachment: fixed !important;
        color: #FFFFFF !important;
        font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif !important;
        line-height: 1.6 !important;
        letter-spacing: -0.01em !important;
    }

    /* Subtle Grid Background Effect */
    .stAppViewContainer::before {
        content: '';
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(rgba(59, 130, 246, 0.12) 1px, transparent 1px),
            radial-gradient(rgba(139, 92, 246, 0.08) 1px, transparent 1px);
        background-size: 32px 32px;
        background-position: 0 0, 16px 16px;
        pointer-events: none;
        z-index: 0;
        opacity: 0.6;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(11, 18, 32, 0.85) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        padding-top: 2rem !important;
    }
    section[data-testid="stSidebar"] label {
        color: #C9D1D9 !important;
        font-size: 15px !important;
        font-weight: 600 !important;
    }

    /* Header Section & Glow */
    .header-container {
        position: relative;
        padding-bottom: 2rem;
        margin-bottom: 2.5rem;
    }
    .status-badge-container {
        display: flex;
        gap: 0.75rem;
        align-items: center;
        margin-bottom: 1.25rem;
    }
    .status-badge {
        background: rgba(34, 211, 238, 0.12);
        border: 1px solid rgba(34, 211, 238, 0.35);
        color: #22D3EE;
        padding: 0.35rem 0.9rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        box-shadow: 0 0 15px rgba(34, 211, 238, 0.2);
    }
    .status-badge-purple {
        background: rgba(139, 92, 246, 0.12);
        border: 1px solid rgba(139, 92, 246, 0.35);
        color: #C084FC;
        box-shadow: 0 0 15px rgba(139, 92, 246, 0.2);
    }

    .brand-title {
        font-size: 52px !important;
        font-weight: 800 !important;
        letter-spacing: -0.035em !important;
        background: linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 40%, #3B82F6 80%, #8B5CF6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.15 !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 0 0 40px rgba(59, 130, 246, 0.25);
    }
    .brand-subtitle {
        color: #C9D1D9 !important;
        font-size: 18px !important;
        font-weight: 400 !important;
        line-height: 1.5 !important;
    }

    /* Input Console */
    .stTextArea textarea {
        background-color: rgba(16, 27, 45, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 18px !important;
        color: #FFFFFF !important;
        font-size: 17px !important;
        line-height: 1.6 !important;
        padding: 1.25rem !important;
        backdrop-filter: blur(16px) !important;
        transition: all 0.25s ease !important;
    }
    .stTextArea textarea::placeholder {
        color: #8B949E !important;
        font-size: 16px !important;
    }
    .stTextArea textarea:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.35) !important;
        background-color: rgba(16, 27, 45, 0.9) !important;
    }

    /* Synthesize Button */
    .stButton>button {
        background: linear-gradient(135deg, #3B82F6 0%, #6366F1 50%, #8B5CF6 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 17px !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 0.85rem 2.5rem !important;
        box-shadow: 0 6px 25px rgba(59, 130, 246, 0.4) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        letter-spacing: -0.01em !important;
    }
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.015) !important;
        box-shadow: 0 12px 35px rgba(139, 92, 246, 0.55) !important;
    }

    /* Premium Metric Card (20px Rounded + Glow) */
    .metric-card {
        background: rgba(16, 27, 45, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 1.6rem 1.2rem;
        text-align: center;
        position: relative;
        backdrop-filter: blur(20px);
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        transition: all 0.25s ease;
    }
    .metric-card:hover {
        border-color: rgba(59, 130, 246, 0.4);
        transform: translateY(-4px);
        box-shadow: 0 15px 35px -5px rgba(59, 130, 246, 0.25);
    }
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0; left: 15%; right: 15%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #3B82F6, #22D3EE, transparent);
    }
    .metric-value {
        font-size: 2.4rem;
        font-weight: 800;
        color: #FFFFFF;
        font-family: 'JetBrains Mono', monospace;
        letter-spacing: -0.03em;
    }
    .metric-label {
        font-size: 14px;
        color: #8B949E;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-top: 0.4rem;
    }

    /* Agent Debate Bubbles */
    .agent-bubble {
        background: rgba(16, 27, 45, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 4px solid #3B82F6;
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.25rem;
        backdrop-filter: blur(16px);
    }
    .agent-bubble-sec { border-left-color: #22D3EE; }
    .agent-bubble-perf { border-left-color: #8B5CF6; }
    .agent-bubble-cost { border-left-color: #10B981; }

    .agent-header {
        font-weight: 700;
        font-size: 17px;
        color: #FFFFFF;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .agent-msg {
        color: #C9D1D9;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Glass Container */
    .glass-card {
        background: rgba(16, 27, 45, 0.55);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 1.75rem;
        backdrop-filter: blur(20px);
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Engine
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h3 style='color:#FFFFFF; font-size:22px;'>⚡ Optimization Matrix</h3>", unsafe_allow_html=True)
    st.caption("Adjust priority weights to balance Pareto constraints:")
    
    sec_weight = st.slider("🛡️ Security (OWASP / Zero-Trust)", 0.0, 1.0, 0.7, 0.1)
    perf_weight = st.slider("⚡ Performance (Low Latency / RPS)", 0.0, 1.0, 0.7, 0.1)
    cost_weight = st.slider("💰 Budget (Cloud Cost Efficiency)", 0.0, 1.0, 0.5, 0.1)
    
    st.divider()
    st.markdown("<h3 style='color:#FFFFFF; font-size:20px;'>📌 Architecture Presets</h3>", unsafe_allow_html=True)
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
# Main UI Header & Input Console
# ---------------------------------------------------------
st.markdown("""
<div class="header-container">
    <div class="status-badge-container">
        <span class="status-badge">⚡ Offline Mode Enabled</span>
        <span class="status-badge status-badge-purple">🔒 API Keyless Runtime</span>
        <span class="status-badge">🧠 Computational Intelligence Engine</span>
    </div>
    <div class="brand-title">AetherMind Genesis</div>
    <div class="brand-subtitle">Autonomous Computational System Architect & Multi-Agent Design Simulator</div>
</div>
""", unsafe_allow_html=True)

# Preset Prompt Handling
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
    height=120
)

col_btn, col_info = st.columns([1, 4])
with col_btn:
    generate_btn = st.button("🌌 Synthesize Blueprint", use_container_width=True)
with col_info:
    st.markdown("<p style='color:#8B949E; font-size:15px; margin-top:0.75rem;'>⚡ Multi-Agent Engine Ready | Zero-Latency Local Synthesis</p>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Execution Logic
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

    st.markdown("<br><hr style='border-color:rgba(255,255,255,0.08);'><br>", unsafe_allow_html=True)

    # 1. Metric Scorecard Row 1
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores.get("overall_score", 80)}/100</div><div class="metric-label">Architecture Score</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores.get("security_score", 85)}</div><div class="metric-label">Security Index</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores.get("performance_score", 75)}</div><div class="metric-label">Performance Index</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores.get("cost_efficiency_score", 70)}</div><div class="metric-label">Cost Efficiency</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 1. Metric Scorecard Row 2
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores.get("scalability_score", 78)}</div><div class="metric-label">Scalability Index</div></div>', unsafe_allow_html=True)
    with c6:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores.get("maintainability_score", 82)}</div><div class="metric-label">Maintainability</div></div>', unsafe_allow_html=True)
    with c7:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores.get("innovation_score", 88)}</div><div class="metric-label">Innovation Score</div></div>', unsafe_allow_html=True)
    with c8:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{scores.get("reliability_score", 90)}</div><div class="metric-label">Reliability Score</div></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 2. Plotly 6-Axis Radar Chart & Recommendation
    col_chart, col_info_box = st.columns([1.2, 1])
    with col_chart:
        st.markdown("<h3 style='font-size:24px; color:#FFFFFF; font-weight:700;'>📊 Architecture Trade-Off Radar</h3>", unsafe_allow_html=True)
        categories = ['Security', 'Performance', 'Cost Efficiency', 'Scalability', 'Maintainability', 'Reliability']
        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=[
                scores.get('security_score', 85), 
                scores.get('performance_score', 75), 
                scores.get('cost_efficiency_score', 70), 
                scores.get('scalability_score', 78), 
                scores.get('maintainability_score', 82), 
                scores.get('reliability_score', 90)
            ],
            theta=categories,
            fill='toself',
            name='Current Blueprint',
            line_color='#3B82F6',
            fillcolor='rgba(59, 130, 246, 0.25)'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], color="#8B949E"),
                angularaxis=dict(color="#FFFFFF")
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#FFFFFF',
            margin=dict(l=40, r=40, t=20, b=20),
            showlegend=False,
            height=340
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_info_box:
        st.markdown("<h3 style='font-size:24px; color:#FFFFFF; font-weight:700;'>🎯 Recommended Tech Stack</h3>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="glass-card">
            <p style="font-size:17px; margin-bottom:0.75rem;"><strong style="color:#C9D1D9;">Architecture Profile:</strong> <span style="color:#22D3EE; font-weight:700;">{scores['architecture_profile']}</span></p>
            <p style="font-size:17px; margin-bottom:0.75rem;"><strong style="color:#C9D1D9;">Est. Cloud Budget:</strong> <span style="color:#10B981; font-weight:700;">{scores['estimated_monthly_cost']}</span></p>
            <p style="font-size:17px; margin-bottom:0.75rem;"><strong style="color:#C9D1D9;">Primary Database:</strong> <span style="color:#C084FC; font-weight:700;">{scores['recommended_db']}</span></p>
            <p style="font-size:15px; color:#8B949E; margin-top:1rem; line-height:1.5;">Synthesized dynamically by balancing Pareto optimization weights across 4 specialized AI agents.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color:rgba(255,255,255,0.08);'><br>", unsafe_allow_html=True)

    # 3. Enterprise Tabs Workbench
    tab_analytics, tab_debate, tab_diagram, tab_db, tab_api, tab_deploy, tab_export = st.tabs([
        "📊 Phase 8: Analytics Dashboard",
        "🗣️ Multi-Agent Debate Console",
        "🗺️ System Topology Diagram",
        "🗄️ Database DDL Schema",
        "🔌 OpenAPI Specification",
        "🚀 Phase 7: Deployment Hub",
        "📥 Phase 9: Export Center"
    ])

    # ---------------------------------------------------------
    # PHASE 8 IMPLEMENTATION: Professional Analytics Dashboard
    # ---------------------------------------------------------
    with tab_analytics:
        st.markdown("<h3 style='font-size:24px; color:#FFFFFF; margin-bottom:0.5rem;'>📊 Phase 8: Interactive Analytics & System Health Gauges</h3>", unsafe_allow_html=True)
        st.caption("Real-time circular progress gauges, trend heatmaps, and metric score breakdowns:")
        
        g1, g2, g3 = st.columns(3)
        with g1:
            fig_g1 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=scores.get('security_score', 85),
                title={'text': "Security Index (OWASP)"},
                gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#22D3EE"}}
            ))
            fig_g1.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='#FFF', height=240, margin=dict(l=20, r=20, t=30, b=20))
            st.plotly_chart(fig_g1, use_container_width=True)

        with g2:
            fig_g2 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=scores.get('performance_score', 75),
                title={'text': "Performance Index (RPS)"},
                gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#8B5CF6"}}
            ))
            fig_g2.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='#FFF', height=240, margin=dict(l=20, r=20, t=30, b=20))
            st.plotly_chart(fig_g2, use_container_width=True)

        with g3:
            fig_g3 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=scores.get('cost_efficiency_score', 70),
                title={'text': "Cost Efficiency Index"},
                gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#10B981"}}
            ))
            fig_g3.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='#FFF', height=240, margin=dict(l=20, r=20, t=30, b=20))
            st.plotly_chart(fig_g3, use_container_width=True)

        # Heatmap Matrix
        st.markdown("<h4 style='font-size:18px; color:#FFFFFF; margin-top:1rem;'>🔥 Sub-System Performance & Vulnerability Heatmap</h4>", unsafe_allow_html=True)
        heatmap_fig = go.Figure(data=go.Heatmap(
            z=[[scores.get('security_score', 85), scores.get('performance_score', 75), scores.get('scalability_score', 78)],
               [scores.get('maintainability_score', 82), scores.get('innovation_score', 88), scores.get('reliability_score', 90)]],
            x=['Security / OWASP', 'Performance / Speed', 'Scalability / Scale'],
            y=['Maintainability Core', 'Reliability Layer'],
            colorscale='Viridis'
        ))
        heatmap_fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#FFF', height=250, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(heatmap_fig, use_container_width=True)

    # ---------------------------------------------------------
    # EXISTING TABS (Preserved 100%)
    # ---------------------------------------------------------
    with tab_debate:
        st.markdown("<h3 style='font-size:24px; color:#FFFFFF; margin-bottom:0.5rem;'>🗣️ Multi-Agent Collaborative Reasoning Stream</h3>", unsafe_allow_html=True)
        st.caption("Threaded discussion among 9 specialized AI Architect personas evaluating system trade-offs:")
        
        for log in results["debate_logs"]:
            role_color = log.get("role_color", "#3B82F6")
            confidence = log.get("confidence", 90)
            
            advantages_html = "".join([f"<li>✅ {adv}</li>" for adv in log.get("advantages", [])])
            disadvantages_html = "".join([f"<li>⚠️ {dis}</li>" for dis in log.get("disadvantages", [])])

            card_html = f"""<div style="background: rgba(16, 27, 45, 0.65); border: 1px solid rgba(255,255,255,0.08); border-left: 5px solid {role_color}; border-radius: 18px; padding: 1.5rem; margin-bottom: 1.5rem; backdrop-filter: blur(20px);"><div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;"><div style="display: flex; align-items: center; gap: 0.6rem;"><span style="font-size: 1.5rem;">{log['avatar']}</span><span style="font-size: 19px; font-weight: 700; color: #FFFFFF;">{log['agent']}</span><span style="background: rgba(255,255,255,0.08); border: 1px solid {role_color}; color: {role_color}; font-size: 12px; font-weight: 600; padding: 0.2rem 0.6rem; border-radius: 9999px;">{log.get('badge', 'Architect Persona')}</span></div><div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); color: #10B981; font-size: 13px; font-weight: 700; padding: 0.3rem 0.75rem; border-radius: 9999px;">Confidence: {confidence}%</div></div><div style="font-size: 16px; color: #FFFFFF; font-weight: 600; margin-bottom: 0.75rem;">💡 <strong>Recommendation:</strong> {log.get('recommendation', '')}</div><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem; font-size: 15px;"><div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.15); border-radius: 12px; padding: 0.85rem 1rem;"><strong style="color: #10B981; font-size: 14px; text-transform: uppercase;">Advantages:</strong><ul style="color: #C9D1D9; margin: 0.4rem 0 0 1.2rem; padding: 0;">{advantages_html}</ul></div><div style="background: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.15); border-radius: 12px; padding: 0.85rem 1rem;"><strong style="color: #EF4444; font-size: 14px; text-transform: uppercase;">Trade-Offs / Disadvantages:</strong><ul style="color: #C9D1D9; margin: 0.4rem 0 0 1.2rem; padding: 0;">{disadvantages_html}</ul></div></div></div>"""
            st.markdown(card_html, unsafe_allow_html=True)

        # Final Consensus Result Card
        consensus = results.get("consensus", {})
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 1.75rem; margin-top: 2rem; backdrop-filter: blur(20px);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.6rem;">
                    <span style="font-size: 1.8rem;">🎯</span>
                    <span style="font-size: 22px; font-weight: 800; color: #FFFFFF;">Final Multi-Agent Consensus Result</span>
                </div>
                <span style="background: rgba(16, 185, 129, 0.2); border: 1px solid #10B981; color: #10B981; font-weight: 700; font-size: 13px; padding: 0.35rem 0.9rem; border-radius: 9999px;">
                    STATUS: {consensus.get('status', 'APPROVED')} ({consensus.get('agreement_rate', 93)}% Agreement)
                </span>
            </div>
            <p style="font-size: 17px; color: #FFFFFF; font-weight: 600; margin-bottom: 0.5rem;">
                {consensus.get('primary_recommendation', '')}
            </p>
            <p style="font-size: 16px; color: #C9D1D9; line-height: 1.6; margin: 0;">
                {consensus.get('summary', '')}
            </p>
        </div>
        """, unsafe_allow_html=True)

    with tab_diagram:
        st.markdown("<h3 style='font-size:24px; color:#FFFFFF;'>🗺️ Visual System Architecture Graph (Mermaid.js)</h3>", unsafe_allow_html=True)
        st.code(mermaid_code, language="mermaid")

    # TAB 3: Database DDL Schema & ER Diagram (Phase 4 Implement)
    with tab_db:
        st.markdown("<h3 style='font-size:24px; color:#FFFFFF; margin-bottom:0.5rem;'>🗄️ Relational Database Schema & ER Diagram</h3>", unsafe_allow_html=True)
        st.caption(f"Target Database Engine: {scores['recommended_db']} | Multi-Table Entity-Relationship Topology")
        
        # Display ER Diagram syntax
        st.markdown("<h4 style='font-size:18px; color:#FFFFFF;'>🌐 Entity-Relationship (ER) Topology Diagram</h4>", unsafe_allow_html=True)
        er_code = results.get("er_diagram_code", "")
        st.code(er_code, language="mermaid")
        
        st.markdown("<br><h4 style='font-size:18px; color:#FFFFFF;'>📄 SQL DDL Schema Code</h4>", unsafe_allow_html=True)
        st.code(results["sql_schema"], language="sql")
        
        st.download_button(
            label="💾 Download DDL SQL Schema (.sql)",
            data=results["sql_schema"],
            file_name="AetherMind_Genesis_Schema.sql",
            mime="text/x-sql"
        )

    # TAB 4: OpenAPI & REST Endpoint Documentation (Phase 5 Implement)
    with tab_api:
        st.markdown("<h3 style='font-size:24px; color:#FFFFFF; margin-bottom:0.5rem;'>🔌 Swagger-Style REST API Documentation Workbench</h3>", unsafe_allow_html=True)
        st.caption("Complete OpenAPI v3 endpoint specifications covering GET, POST, PUT, DELETE methods with sample payloads & error codes:")
        
        endpoints = results.get("api_endpoints_documentation", [])
        for ep in endpoints:
            method = ep["method"]
            method_color = "#10B981" if method == "GET" else ("#3B82F6" if method == "POST" else ("#F59E0B" if method == "PUT" else "#EF4444"))
            
            headers_formatted = json.dumps(ep.get("headers", {}), indent=2)
            req_formatted = json.dumps(ep.get("sample_request", {}), indent=2) if ep.get("sample_request") else "None (No Request Body)"
            resp_formatted = json.dumps(ep.get("sample_response", {}), indent=2)

            errors_html = "".join([f"<li><strong style='color:#EF4444;'>HTTP {err['code']}</strong>: {err['description']}</li>" for err in ep.get("error_codes", [])])

            ep_html = f"""
            <div style="background: rgba(16, 27, 45, 0.7); border: 1px solid rgba(255,255,255,0.08); border-left: 5px solid {method_color}; border-radius: 16px; padding: 1.25rem 1.5rem; margin-bottom: 1.5rem; backdrop-filter: blur(20px);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                    <div style="display: flex; align-items: center; gap: 0.75rem;">
                        <span style="background: {method_color}; color: #FFFFFF; font-weight: 800; font-size: 13px; padding: 0.25rem 0.75rem; border-radius: 6px;">{method}</span>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 17px; font-weight: 700; color: #FFFFFF;">{ep['path']}</span>
                    </div>
                    <span style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #C9D1D9; font-size: 12px; font-weight: 600; padding: 0.2rem 0.6rem; border-radius: 9999px;">
                        Auth: {ep['auth']}
                    </span>
                </div>
                
                <p style="font-size: 15px; color: #C9D1D9; margin-bottom: 1rem;">{ep['summary']}</p>
                
                <details style="color: #8B949E; cursor: pointer;">
                    <summary style="font-weight: 600; color: #3B82F6; margin-bottom: 0.5rem;">🔍 View Headers, Request Payload, Sample Response & Error Codes</summary>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 0.75rem;">
                        <div>
                            <strong style="color: #FFFFFF; font-size: 13px;">Request Headers:</strong>
                            <pre style="background: rgba(5,8,22,0.8); color: #22D3EE; padding: 0.6rem; border-radius: 8px; font-size: 12px;">{headers_formatted}</pre>
                            <strong style="color: #FFFFFF; font-size: 13px;">Sample Request Body:</strong>
                            <pre style="background: rgba(5,8,22,0.8); color: #C084FC; padding: 0.6rem; border-radius: 8px; font-size: 12px;">{req_formatted}</pre>
                        </div>
                        <div>
                            <strong style="color: #FFFFFF; font-size: 13px;">Sample HTTP Response (200 OK):</strong>
                            <pre style="background: rgba(5,8,22,0.8); color: #10B981; padding: 0.6rem; border-radius: 8px; font-size: 12px;">{resp_formatted}</pre>
                            <strong style="color: #FFFFFF; font-size: 13px;">Error Codes:</strong>
                            <ul style="margin: 0.4rem 0 0 1.2rem; padding: 0; font-size: 13px; color: #C9D1D9;">
                                {errors_html}
                            </ul>
                        </div>
                    </div>
                </details>
            </div>
            """
            st.markdown(ep_html, unsafe_allow_html=True)

        st.markdown("<br><h4 style='font-size:18px; color:#FFFFFF;'>📄 OpenAPI v3.0 JSON Specification</h4>", unsafe_allow_html=True)
        st.code(results["api_spec"], language="json")

    # TAB 5: Master Blueprint Export Hub (Phase 6 Implement)
    with tab_export:
        st.markdown("<h3 style='font-size:24px; color:#FFFFFF; margin-bottom:0.5rem;'>📄 Master 12-Section Enterprise Software Blueprint Hub</h3>", unsafe_allow_html=True)
        st.caption("Complete enterprise specification covering Overview, Requirements, Architecture, Database, APIs, Folder Structure, Deployment, Security, Performance, Cost Analysis, Timeline & Risks:")
        
        markdown_doc = export_blueprint_markdown(
            data["prompt"],
            scores,
            results["debate_logs"],
            mermaid_code,
            results["sql_schema"],
            results["api_spec"]
        )

        col_dl1, col_dl2 = st.columns([1, 1])
        with col_dl1:
            st.download_button(
                label="📄 Download Master Blueprint (.md)",
                data=markdown_doc,
                file_name=f"AetherMind_Genesis_Master_Blueprint.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col_dl2:
            st.download_button(
                label="💾 Export Document Spec (.txt)",
                data=markdown_doc,
                file_name=f"AetherMind_Genesis_Blueprint_Spec.txt",
                mime="text/plain",
                use_container_width=True
            )

        st.markdown("<br><h4 style='font-size:18px; color:#FFFFFF;'>🔍 Master Document Preview & Code Output</h4>", unsafe_allow_html=True)
        st.text_area("Complete 12-Section Specification Document", value=markdown_doc, height=450)
