# 🌌 AetherMind Genesis - AI System Architect

> **Transform high-level product ideas into production-ready software architecture blueprints using Multi-Agent Consensus Simulation and Multi-Objective Computational Intelligence.**

---

## 🌟 Overview
**AetherMind Genesis** is an autonomous AI System Architect built with 100% Python and Streamlit. It takes a plain-English application description and orchestrates a debate among specialized AI personas (**Lead Architect**, **Security Architect**, **Performance Architect**, and **Cost Architect**) to generate a comprehensive, Pareto-optimized software blueprint.

### Key Capabilities:
- **🗣️ Multi-Agent Consensus Debate**: Live streaming argument & compromise feed balancing Security vs Latency vs Budget constraints.
- **🗺️ Dynamic System Topology (Mermaid.js)**: Auto-synthesizes visual C4 flowchart architecture diagrams.
- **🗄️ Database DDL Schema Generator**: Generates domain-tailored SQL database schemas (PostgreSQL / SQLite).
- **🔌 OpenAPI Specification Workbench**: Generates structured REST/GraphQL endpoint specs with JSON payloads.
- **📊 Multi-Objective Optimization Engine**: Mathematical fitness function evaluating trade-offs across OWASP security index, latency, and cloud infrastructure budgets.
- **⚡ API-Keyless Runtime**: Runs instantly offline using built-in deterministic rule synthesis.

---

## 🛠️ Project Structure
```
AETHERMIND-GENESIS/
├── app.py                 # Main Streamlit Full-Stack Application & Dashboard
├── requirements.txt       # Dependencies
├── .gitignore             # Git ignore rules
├── agents/
│   ├── __init__.py
│   └── engine.py          # Multi-Agent Debate Simulation & Rule Engine
└── utils/
    ├── __init__.py
    ├── optimization.py    # Multi-Objective Optimization Scoring Engine (CI)
    ├── graph_builder.py   # Mermaid.js Architecture Diagram Builder
    └── exporter.py        # Markdown Blueprint Exporter
```

---

## 🚀 Quick Start & Local Execution

### 1. Clone the Repository
```bash
git clone https://github.com/KAVATIJOHNSHREYAN/AETHERMIND-GENESIS-AI.git
cd AETHERMIND-GENESIS-AI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to use **AetherMind Genesis**.

---

## 🧠 Computational Intelligence Architecture
Unlike simple chatbot prompt wrappers, AetherMind Genesis leverages **Multi-Objective Optimization**:

$$\text{Fitness Score} = (S_{\text{security}} \times w_s) + (S_{\text{perf}} \times w_p) + (S_{\text{cost}} \times w_c)$$

Where weights $w_s, w_p, w_c$ are dynamically set via interactive UI sliders to simulate real-world Pareto trade-off optimization.

---
*Created under the **AetherMind** AI Flagship Suite.*
