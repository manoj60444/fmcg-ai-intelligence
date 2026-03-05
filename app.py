"""
FMCG Operational Intelligence System
=====================================
Multi-page AI-Powered Infrastructure.
"""

import time
import streamlit as st

from config.settings import APP_TITLE, APP_ICON, APP_SUBTITLE, ZONES, DEFAULT_ZONE, LAYERS
from utils.data_loader import load_data, get_zone_stats
from layers.monitoring import run_behaviour_scan
from ui.styles import CUSTOM_CSS
from ui.components import (
    render_ai_header,
    render_overview_cards,
    render_layer_status,
    render_alert_card,
    render_no_anomaly,
    render_divider,
    render_ai_footer,
)
from ui.tabs import (
    render_root_cause_tab,
    render_predictive_tab,
    render_chat_tab,
    render_workflow_tab,
)

# ──────────────────────────────────────
# Page config
# ──────────────────────────────────────
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ──────────────────────────────────────
# Session state & Navigation
# ──────────────────────────────────────
if "active_page" not in st.session_state:
    st.session_state.active_page = "Dashboard"
if "scan_complete" not in st.session_state:
    st.session_state.scan_complete = False
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
if "workflow_triggered" not in st.session_state:
    st.session_state.workflow_triggered = False
if "selected_zone" not in st.session_state:
    st.session_state.selected_zone = DEFAULT_ZONE

# Helper to change pages
def navigate_to(page_name):
    st.session_state.active_page = page_name

# ──────────────────────────────────────
# Sidebar Navigation (UNLOCKABLE)
# ──────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="nav-header">', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size: 3.5rem; margin-bottom: 0.5rem; filter: drop-shadow(0 0 15px #6366f1);">🧠</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color:#e2e8f0; font-weight:800; font-size:1.4rem; letter-spacing:1px;">CORE ENGINE</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Define pages and their required states
    all_pages = [
        {"name": "Dashboard", "icon": "📊", "unlocked": True},
        {"name": "Analytics", "icon": "🔍", "unlocked": True},
        {"name": "Prediction", "icon": "📈", "unlocked": "scan_complete"},
        {"name": "Automation", "icon": "⚡", "unlocked": "prediction_viewed"},
        {"name": "Intelligence", "icon": "💬", "unlocked": "workflow_triggered"}
    ]
    
    for p in all_pages:
        unlocked = True
        if isinstance(p["unlocked"], str):
            unlocked = st.session_state.get(p["unlocked"], False)
        
        if unlocked:
            is_active = "nav-item-active" if st.session_state.active_page == p["name"] else ""
            if st.button(f"{p['icon']} {p['name']}", key=f"nav_{p['name']}", use_container_width=True):
                st.session_state.active_page = p["name"]
                st.rerun()
        else:
            st.button(f"🔒 {p['name']}", key=f"nav_locked_{p['name']}", use_container_width=True, disabled=True)
    
    st.sidebar.divider()
    selected_zone = st.selectbox(
        "🌍 Analysis Cluster",
        options=ZONES,
        index=ZONES.index(st.session_state.selected_zone),
        key="zone_picker",
    )
    if selected_zone != st.session_state.selected_zone:
        st.session_state.selected_zone = selected_zone
        st.session_state.scan_complete = False
        st.session_state.prediction_viewed = False
        st.session_state.workflow_triggered = False

# ──────────────────────────────────────
# Data Loading
# ──────────────────────────────────────
try:
    dist_df, sku_df, ops_df = load_data()
except FileNotFoundError:
    st.error("⚠️ Data files not found. Run `python generate_data.py` first!")
    st.stop()

# ──────────────────────────────────────
# Page Router
# ──────────────────────────────────────
render_ai_header(APP_TITLE, APP_SUBTITLE)

if st.session_state.active_page == "Dashboard":
    # --- DASHBOARD PAGE ---
    stats = get_zone_stats(dist_df, sku_df, ops_df, st.session_state.selected_zone)
    render_overview_cards(stats)
    render_layer_status()
    render_divider()
    
    # Premium Operational Panels (MATCHING USER SCREENSHOT STYLE)
    st.markdown("<h3 style='margin-bottom: 2rem;'>🛠 OPERATIONAL CONTROL PANELS</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown(f"""
        <div class="redirect-panel">
            <div class="panel-icon">🔍</div>
            <div class="panel-title">Neural Behaviour Scan</div>
            <div class="panel-desc">Execute multi-layer audit of {st.session_state.selected_zone} cluster across 12,000+ data points.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 INITIATE SYSTEM SCAN", use_container_width=True, key="btn_scan"):
            st.session_state.active_page = "Analytics"
            st.rerun()
            
    with c2:
        st.markdown("""
        <div class="redirect-panel">
            <div class="panel-icon">⚡</div>
            <div class="panel-title">Automation Stack</div>
            <div class="panel-desc">Access corrective execution layer. Reserved for high-confidence anomalies.</div>
        </div>
        """, unsafe_allow_html=True)
        automation_unlocked = st.session_state.get("prediction_viewed", False)
        if st.button("🔧 OPEN AUTOMATION LAYER" if automation_unlocked else "🔒 LAYER LOCKED", 
                     use_container_width=True, key="btn_auto", disabled=not automation_unlocked):
            st.session_state.active_page = "Automation"
            st.rerun()

elif st.session_state.active_page == "Analytics":
    # --- ANALYTICS / MONITORING PAGE ---
    st.markdown("### 🔍 Cluster Behaviour Analysis")
    
    if not st.session_state.scan_complete:
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
            if i % 25 == 0:
                status_text.markdown(f'<div class="scanning-text">🔄 Processing Neural Layer {i//25 + 1}...</div>', unsafe_allow_html=True)
        st.session_state.scan_complete = True
        status_text.empty()
        progress_bar.empty()

    alerts, anomaly_df, _ = run_behaviour_scan(ops_df, dist_df, st.session_state.selected_zone)
    if not alerts:
        render_no_anomaly(st.session_state.selected_zone)
    else:
        for alert in alerts:
            render_alert_card(alert)
        st.markdown("### 📊 Anomaly Root Cause Charts")
        render_root_cause_tab(alerts[0], anomaly_df)
        
        # REDIRECTION TO PREDICTION
        st.markdown(f"""
        <div class="redirect-panel" style="border-color: #8b5cf6;">
            <div class="panel-icon">📈</div>
            <div class="panel-title">Prediction Intelligence</div>
            <div class="panel-desc">Model the ripple effect of this {st.session_state.selected_zone} anomaly over the next 30 days.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔮 GENERATE RISK FORECAST", use_container_width=True):
            st.session_state.active_page = "Prediction"
            st.session_state.prediction_viewed = True
            st.rerun()

elif st.session_state.active_page == "Prediction":
    # --- PREDICTION PAGE ---
    st.markdown("### 📈 Predictive Intelligence Output")
    st.session_state.prediction_viewed = True
    alerts, _, _ = run_behaviour_scan(ops_df, dist_df, st.session_state.selected_zone)
    if alerts:
        render_predictive_tab(alerts[0], ops_df, dist_df)
        
        # REDIRECTION TO AUTOMATION
        st.markdown(f"""
        <div class="redirect-panel" style="border-color: #ec4899;">
            <div class="panel-icon">⚡</div>
            <div class="panel-title">Corrective Automation</div>
            <div class="panel-desc">Trigger AI-led workflows to mitigate the predicted 7.2% margin impact.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🛠 TRIGGER MITIGATION WORKFLOW", use_container_width=True):
            st.session_state.active_page = "Automation"
            st.rerun()
    else:
        st.info("No active anomalies detected in current cluster.")

elif st.session_state.active_page == "Intelligence":
    # --- CHAT PAGE ---
    st.markdown("### 💬 Neural Chat Interface")
    alerts, _, _ = run_behaviour_scan(ops_df, dist_df, st.session_state.selected_zone)
    if alerts:
        render_chat_tab(alerts[0], ops_df)
    else:
        st.info("Central Intelligence is idle.")

elif st.session_state.active_page == "Automation":
    # --- AUTOMATION PAGE ---
    st.markdown("### ⚡ Execution & Strategy Layer")
    alerts, _, _ = run_behaviour_scan(ops_df, dist_df, st.session_state.selected_zone)
    if alerts:
        render_workflow_tab(alerts[0])
        st.session_state.workflow_triggered = True
        
        # REDIRECTION TO AI CHAT
        st.markdown(f"""
        <div class="redirect-panel" style="border-color: #10b981;">
            <div class="panel-icon">💬</div>
            <div class="panel-title">AI Intelligence Oracle</div>
            <div class="panel-desc">Connect with the Neural Oracle to ask specific questions about the automated strategy.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🧠 CONSULT NEURAL ORACLE", use_container_width=True):
            st.session_state.active_page = "Intelligence"
            st.rerun()
    else:
        st.success("Operational thresholds optimal. No workflows pending.")

render_divider()
render_ai_footer()

render_divider()
render_ai_footer()
