"""
FMCG Operational Intelligence System
=====================================
Per PDF Requirements:
  ✅ Detection-first approach (not dashboard)
  ✅ Clean & minimal white background
  ✅ Automatic detection shown BEFORE data
  ✅ Financial terms in every output
  ❌ No KPI tiles, no dashboard feel
"""

import time
import streamlit as st

from config.settings import APP_TITLE, APP_ICON, APP_SUBTITLE, ZONES, DEFAULT_ZONE, LAYERS
from utils.data_loader import load_data, get_zone_stats
from layers.monitoring import run_behaviour_scan
from ui.styles import CUSTOM_CSS
from ui.components import (
    render_ai_header,
    render_detection_banner,
    render_financial_impact,
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
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ──────────────────────────────────────
# Session state & Navigation
# ──────────────────────────────────────
if "active_page" not in st.session_state:
    st.session_state.active_page = "Detection"
if "scan_complete" not in st.session_state:
    st.session_state.scan_complete = False
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
if "workflow_triggered" not in st.session_state:
    st.session_state.workflow_triggered = False
if "selected_zone" not in st.session_state:
    st.session_state.selected_zone = DEFAULT_ZONE

# ──────────────────────────────────────
# Sidebar Navigation
# ──────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="nav-header">', unsafe_allow_html=True)
    st.markdown(
        '<div style="font-size: 2rem; margin-bottom: 0.5rem;">🏢</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="color:#e2e8f0; font-weight:700; font-size:1rem; letter-spacing:1px;">'
        'OPERATIONAL INTELLIGENCE</div>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Navigation pages — progressive unlocking
    # Per PDF: Detection first, then Analysis, then Prediction, then Automation, then Chat
    all_pages = [
        {"name": "Detection",  "icon": "🚨", "unlocked": True},
        {"name": "Analysis",   "icon": "🔍", "unlocked": "scan_complete"},
        {"name": "Prediction", "icon": "📈", "unlocked": "scan_complete"},
        {"name": "Automation", "icon": "⚡", "unlocked": "prediction_viewed"},
        {"name": "Intelligence", "icon": "💬", "unlocked": "workflow_triggered"},
    ]

    for p in all_pages:
        unlocked = True
        if isinstance(p["unlocked"], str):
            unlocked = st.session_state.get(p["unlocked"], False)

        if unlocked:
            if st.button(
                f"{p['icon']} {p['name']}",
                key=f"nav_{p['name']}",
                use_container_width=True,
            ):
                st.session_state.active_page = p["name"]
                st.rerun()
        else:
            st.button(
                f"🔒 {p['name']}",
                key=f"nav_locked_{p['name']}",
                use_container_width=True,
                disabled=True,
            )

    st.sidebar.divider()
    selected_zone = st.selectbox(
        "🌍 Zone",
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

if st.session_state.active_page == "Detection":
    # ═══════════════════════════════════════════════
    # DETECTION PAGE — Per PDF: Show Detection FIRST
    # "When demo starts, first show:
    #  🚨 Behavioural Drift Detected"
    # ═══════════════════════════════════════════════
    render_layer_status()
    render_divider()

    # Run scan immediately and show detection
    if not st.session_state.scan_complete:
        progress_bar = st.progress(0)
        status_text = st.empty()
        scan_steps = [
            "Scanning distributor behaviour patterns...",
            "Comparing against 30-day baselines...",
            "Evaluating credit and inventory signals...",
            "Identifying behavioural deviations...",
        ]
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
            if i % 25 == 0:
                status_text.markdown(
                    f'<div class="scanning-text">{scan_steps[i // 25]}</div>',
                    unsafe_allow_html=True,
                )
        st.session_state.scan_complete = True
        status_text.empty()
        progress_bar.empty()

    alerts, anomaly_df, _ = run_behaviour_scan(
        ops_df, dist_df, st.session_state.selected_zone
    )

    if not alerts:
        render_no_anomaly(st.session_state.selected_zone)
    else:
        # Per PDF: Show detection banner FIRST — "System identified issue BEFORE human asked"
        render_detection_banner(alerts[0])

        # Then the alert card with core metrics
        render_alert_card(alerts[0])

        # Financial impact — Per PDF: Revenue, Margin, Working Capital
        render_financial_impact(alerts[0])

        render_divider()

        # Guide to deeper analysis
        st.markdown(
            f"""
            <div class="redirect-panel">
                <div class="panel-icon">🔍</div>
                <div class="panel-title">Root Cause Analysis</div>
                <div class="panel-desc">
                    Understand why this deviation occurred. The system has identified
                    contributing factors across logistics, competition, and credit signals.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("🔍 Investigate System Drivers", use_container_width=True, key="btn_analyse"):
            st.session_state.active_page = "Analysis"
            st.rerun()


elif st.session_state.active_page == "Analysis":
    # ═══════════════════════════════════════════════
    # ANALYSIS PAGE — Root Cause
    # ═══════════════════════════════════════════════
    st.markdown("#### Root Cause Analysis")

    alerts, anomaly_df, _ = run_behaviour_scan(
        ops_df, dist_df, st.session_state.selected_zone
    )
    if not alerts:
        render_no_anomaly(st.session_state.selected_zone)
    else:
        render_root_cause_tab(alerts[0], anomaly_df)

        render_divider()

        # Guide to prediction
        st.markdown(
            f"""
            <div class="redirect-panel">
                <div class="panel-icon">📈</div>
                <div class="panel-title">Risk Projection</div>
                <div class="panel-desc">
                    Model the impact of this {st.session_state.selected_zone} anomaly
                    over the next 30-60 days. See projected revenue loss and margin compression.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("📈 Project Revenue Risk", use_container_width=True):
            st.session_state.active_page = "Prediction"
            st.session_state.prediction_viewed = True
            st.rerun()


elif st.session_state.active_page == "Prediction":
    # ═══════════════════════════════════════════════
    # PREDICTION PAGE — Risk Projection
    # Per PDF: "Show Forecast as Risk Projection"
    # ═══════════════════════════════════════════════
    st.session_state.prediction_viewed = True
    alerts, _, _ = run_behaviour_scan(
        ops_df, dist_df, st.session_state.selected_zone
    )
    if alerts:
        render_predictive_tab(alerts[0], ops_df, dist_df)

        render_divider()

        # Per PDF: "Position Automation as Next Phase"
        st.markdown(
            """
            <div class="redirect-panel">
                <div class="panel-icon">⚡</div>
                <div class="panel-title">Corrective Automation</div>
                <div class="panel-desc">
                    Corrective workflow can be triggered automatically.
                    The system generates targeted action plans for the identified risk areas.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("⚡ Yes, Limit Exposure Automatically", use_container_width=True):
            st.session_state.active_page = "Automation"
            st.rerun()
    else:
        st.info("No active anomalies detected in current zone.")


elif st.session_state.active_page == "Automation":
    # ═══════════════════════════════════════════════
    # AUTOMATION PAGE
    # Per PDF: "Corrective workflow can be triggered automatically"
    # ═══════════════════════════════════════════════
    alerts, _, _ = run_behaviour_scan(
        ops_df, dist_df, st.session_state.selected_zone
    )
    if alerts:
        render_workflow_tab(alerts[0])
        st.session_state.workflow_triggered = True

        render_divider()

        st.markdown(
            """
            <div class="redirect-panel">
                <div class="panel-icon">💬</div>
                <div class="panel-title">Ask the System</div>
                <div class="panel-desc">
                    Interact with the operational intelligence system.
                    Ask specific questions about the detected anomaly and corrective strategy.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("💬 Consult the Business Controller", use_container_width=True):
            st.session_state.active_page = "Intelligence"
            st.rerun()
    else:
        st.success("All operations within normal parameters. No workflows pending.")


elif st.session_state.active_page == "Intelligence":
    # ═══════════════════════════════════════════════
    # CHAT PAGE — Conversational AI
    # Per PDF: "Make Conversational AI Look Intelligent"
    #   ❌ No hallucination, no generic answers
    #   ✅ Structured, bullet format, business-focused
    # ═══════════════════════════════════════════════
    alerts, _, _ = run_behaviour_scan(
        ops_df, dist_df, st.session_state.selected_zone
    )
    if alerts:
        render_chat_tab(alerts[0], ops_df)
    else:
        st.info("No active anomalies. The system is monitoring operations.")


render_divider()
render_ai_footer()
