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
# Sidebar Navigation
# ──────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="nav-header">', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size: 3rem; margin-bottom: 0.5rem;">🧠</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color:#e2e8f0; font-weight:700; font-size:1.2rem;">{APP_TITLE}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    pages = ["Dashboard", "Analytics", "Prediction", "Intelligence", "Automation"]
    icons = ["📊", "🔍", "📈", "💬", "⚡"]
    
    for page, icon in zip(pages, icons):
        is_active = "nav-item-active" if st.session_state.active_page == page else ""
        if st.button(f"{icon} {page}", key=f"nav_{page}", use_container_width=True):
            navigate_to(page)
    
    st.sidebar.divider()
    selected_zone = st.selectbox(
        "🌍 Global Zone Filter",
        options=ZONES,
        index=ZONES.index(st.session_state.selected_zone),
        key="zone_picker",
    )
    if selected_zone != st.session_state.selected_zone:
        st.session_state.selected_zone = selected_zone
        st.session_state.scan_complete = False

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
    
    # Scan trigger cards (Redirecting to Analytics)
    st.markdown("### 🛠 Operational Actions")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="overview-card redirect-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔍</div>
            <div class="overview-number">Run Multi-Layer Scan</div>
            <div class="overview-label">Analyze all zones for anomalies</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Start Intelligence Scan", use_container_width=True):
            navigate_to("Analytics")
            st.rerun()
            
    with c2:
        st.markdown("""
        <div class="overview-card redirect-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⚡</div>
            <div class="overview-number">Automation Layer</div>
            <div class="overview-label">Review pending corrective workflows</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔧 Access Automation", use_container_width=True):
            navigate_to("Automation")
            st.rerun()

elif st.session_state.active_page == "Analytics":
    # --- ANALYTICS / MONITORING PAGE ---
    st.markdown("### 🔍 Real-time Monitoring Scan")
    scan_clicked = st.button("🔍  Reload AI Behaviour Scan", use_container_width=True)
    
    if scan_clicked or not st.session_state.scan_complete:
        progress = st.progress(0)
        status = st.empty()
        steps = ["Initializing Neural Network...", "Loading Data Pipeline...", "Analyzing Signal Noise...", "Identifying Patterns...", "Scan Complete"]
        for i, step in enumerate(steps):
            status.markdown(f'<div class="scanning-text">🔄 {step}</div>', unsafe_allow_html=True)
            progress.progress((i + 1) / len(steps))
            time.sleep(0.3)
        st.session_state.scan_complete = True
        status.empty()
        progress.empty()

    alerts, anomaly_df, _ = run_behaviour_scan(ops_df, dist_df, st.session_state.selected_zone)
    
    if not alerts:
        render_no_anomaly(st.session_state.selected_zone)
    else:
        for alert in alerts:
            render_alert_card(alert)
        
        # New: Analytics Deep Dive Section
        st.markdown("### 📊 Anomaly Root Cause Charts")
        render_root_cause_tab(alerts[0], anomaly_df)

elif st.session_state.active_page == "Prediction":
    # --- PREDICTION PAGE ---
    st.markdown("### 📈 Predictive Intelligence")
    alerts, _, _ = run_behaviour_scan(ops_df, dist_df, st.session_state.selected_zone)
    if alerts:
        render_predictive_tab(alerts[0], ops_df, dist_df)
    else:
        st.info("No active anomalies to predict. Run a scan from the Analytics page.")

elif st.session_state.active_page == "Intelligence":
    # --- CHAT PAGE ---
    st.markdown("### 💬 Central Intelligence Interface")
    alerts, _, _ = run_behaviour_scan(ops_df, dist_df, st.session_state.selected_zone)
    if alerts:
        render_chat_tab(alerts[0], ops_df)
    else:
        st.info("Central Intelligence is idle. Please select a zone with active alerts.")

elif st.session_state.active_page == "Automation":
    # --- AUTOMATION PAGE ---
    st.markdown("### ⚡ Automation & Workflows")
    alerts, _, _ = run_behaviour_scan(ops_df, dist_df, st.session_state.selected_zone)
    if alerts:
        render_workflow_tab(alerts[0])
    else:
        st.success("All workflows are cleared. System status: Optimal.")

render_divider()
render_ai_footer()
