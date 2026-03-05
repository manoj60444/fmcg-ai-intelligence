"""
FMCG Operational Intelligence System
=====================================
AI-Powered Real-time Monitoring & Analysis Platform
Main Streamlit entry-point.
"""

import time
import streamlit as st

from config.settings import APP_TITLE, APP_ICON, APP_SUBTITLE, ZONES, DEFAULT_ZONE
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
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ──────────────────────────────────────
# Load data
# ──────────────────────────────────────
try:
    dist_df, sku_df, ops_df = load_data()
except FileNotFoundError:
    st.error("⚠️ Data files not found. Run `python generate_data.py` first!")
    st.stop()

# ──────────────────────────────────────
# Session state defaults
# ──────────────────────────────────────
if "scan_complete" not in st.session_state:
    st.session_state.scan_complete = False
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
if "workflow_triggered" not in st.session_state:
    st.session_state.workflow_triggered = False
if "selected_zone" not in st.session_state:
    st.session_state.selected_zone = DEFAULT_ZONE

# ──────────────────────────────────────
# AI Header
# ──────────────────────────────────────
render_ai_header(APP_TITLE, APP_SUBTITLE)

# ──────────────────────────────────────
# Zone selector + Overview cards
# ──────────────────────────────────────
zone_col, spacer = st.columns([1, 3])
with zone_col:
    selected_zone = st.selectbox(
        "🌍 Select Zone",
        options=ZONES,
        index=ZONES.index(st.session_state.selected_zone),
        key="zone_picker",
    )
    # Reset scan on zone change
    if selected_zone != st.session_state.selected_zone:
        st.session_state.selected_zone = selected_zone
        st.session_state.scan_complete = False
        st.session_state.chat_messages = []
        st.session_state.workflow_triggered = False

zone_label = selected_zone if selected_zone != "All Zones" else "All Zones"
stats = get_zone_stats(dist_df, sku_df, ops_df, selected_zone)
render_overview_cards(stats)

# Layer status pipeline
render_layer_status()
render_divider()

# ──────────────────────────────────────
# Scan button
# ──────────────────────────────────────
_, btn_col, _ = st.columns([1, 1, 1])
with btn_col:
    scan_clicked = st.button(
        "🔍  Run AI Behaviour Scan",
        use_container_width=True,
        key="scan_btn",
    )

if scan_clicked:
    st.session_state.scan_complete = False
    st.session_state.chat_messages = []
    st.session_state.workflow_triggered = False

    progress = st.progress(0)
    status = st.empty()
    steps = [
        "Initializing neural monitoring engine…",
        f"Loading operational data for {zone_label}…",
        "Computing rolling averages per distributor node…",
        "Running multi-signal anomaly detection algorithm…",
        "Cross-referencing credit & inventory patterns…",
        "AI calculating confidence scores…",
        "Generating intelligent alert objects…",
        "Anomaly detection complete.",
    ]
    for i, step in enumerate(steps):
        status.markdown(
            f'<div class="scanning-text">⟳ {step}</div>',
            unsafe_allow_html=True,
        )
        progress.progress((i + 1) / len(steps))
        time.sleep(0.4)

    status.markdown(
        '<div class="scanning-text">✅ AI Behaviour scan complete.</div>',
        unsafe_allow_html=True,
    )
    time.sleep(0.4)
    progress.empty()
    status.empty()
    st.session_state.scan_complete = True

# ──────────────────────────────────────
# Results
# ──────────────────────────────────────
if st.session_state.scan_complete:
    alerts, anomaly_df, _daily_agg = run_behaviour_scan(
        ops_df, dist_df, selected_zone
    )

    if not alerts:
        render_no_anomaly(zone_label)
    else:
        # Show each alert card
        for alert in alerts:
            render_alert_card(alert)

        st.markdown("")

        # Pick the first alert for tab drill-down (or let user choose)
        if len(alerts) > 1:
            alert_labels = [
                f"{a['Zone']} Zone – {a['Cluster']}" for a in alerts
            ]
            chosen_idx = st.radio(
                "Drill into alert:",
                range(len(alert_labels)),
                format_func=lambda x: alert_labels[x],
                horizontal=True,
            )
            active_alert = alerts[chosen_idx]
        else:
            active_alert = alerts[0]

        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "🔎 Root Cause Analysis",
            "📈 Predictive Impact",
            "💬 Chat Intelligence",
            "⚡ Trigger Workflow",
        ])

        with tab1:
            render_root_cause_tab(active_alert, anomaly_df)
        with tab2:
            render_predictive_tab(active_alert, ops_df, dist_df)
        with tab3:
            render_chat_tab(active_alert, ops_df)
        with tab4:
            render_workflow_tab(active_alert)

# ──────────────────────────────────────
# Footer
# ──────────────────────────────────────
st.markdown("")
render_ai_footer()
