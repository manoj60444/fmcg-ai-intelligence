"""
FMCG Operational Intelligence System
=====================================
Senior Developer Edition: High-End Professional UI.
"""

import streamlit as st
from streamlit_option_menu import option_menu
import time

from config.settings import APP_TITLE, APP_SUBTITLE, ZONES, DEFAULT_ZONE
from utils.data_loader import load_data, get_zone_stats
from layers.monitoring import run_behaviour_scan
from ui.styles import CUSTOM_CSS
from ui.components import (
    render_ai_header,
    render_overview_cards,
    render_sentiment_feed,
    render_kpi,
    render_status_indicator,
    render_divider,
    render_ai_footer,
    render_alert_card,
    render_no_anomaly,
)

# ──────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ──────────────────────────────────────
# Session State Management
# ──────────────────────────────────────
if "active_page" not in st.session_state:
    st.session_state.active_page = "Dashboard"
if "scan_complete" not in st.session_state:
    st.session_state.scan_complete = False
if "selected_zone" not in st.session_state:
    st.session_state.selected_zone = DEFAULT_ZONE
if "prediction_unlocked" not in st.session_state:
    st.session_state.prediction_unlocked = False

# ──────────────────────────────────────
# Data Loading
# ──────────────────────────────────────
try:
    dist_df, sku_df, ops_df = load_data()
except FileNotFoundError:
    st.error("⚠️ Data files not found. Run `python generate_data.py` first!")
    st.stop()

# ──────────────────────────────────────
# Sidebar Navigation (Professional Style)
# ──────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 1rem 0; text-align:center; margin-bottom: 2rem;">
        <span style="font-size: 3rem;">🧠</span>
        <h2 style="color:white; font-weight:300; letter-spacing: 0.1em; font-size: 1.1rem; margin-top:1rem;">CORE AI ENGINE</h2>
    </div>
    """, unsafe_allow_html=True)
    
    selected_page = option_menu(
        menu_title=None,
        options=["Dashboard", "Inventory", "Supply Chain", "Sentiment"],
        icons=["columns-gap", "box-seam", "truck", "chat-square-text"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0F172A"},
            "icon": {"color": "#64748B", "font-size": "1.1rem"}, 
            "nav-link": {
                "font-size": "0.95rem", 
                "text-align": "left", 
                "margin": "0px", 
                "color": "#94A3B8",
                "padding": "12px 20px",
                "font-family": "'Inter', sans-serif"
            },
            "nav-link-selected": {"background-color": "#1E293B", "color": "#10B981", "font-weight": "600"},
        }
    )
    
    st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
    st.sidebar.markdown(f'<p style="color:#64748B; font-size:0.7rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; padding-left:20px;">Cluster Node</p>', unsafe_allow_html=True)
    
    selected_zone = st.sidebar.selectbox(
        "Cluster",
        options=ZONES,
        index=ZONES.index(st.session_state.selected_zone),
        label_visibility="collapsed"
    )
    if selected_zone != st.session_state.selected_zone:
        st.session_state.selected_zone = selected_zone
        st.session_state.scan_complete = False
        st.rerun()

# ──────────────────────────────────────
# Main Application Layout (1-3-1 Density)
# ──────────────────────────────────────
_, main_col, _ = st.columns([1, 3, 1])

with main_col:
    render_ai_header(APP_TITLE, APP_SUBTITLE)
    
    if selected_page == "Dashboard":
        # --- DASHBOARD PAGE ---
        stats = get_zone_stats(dist_df, sku_df, ops_df, st.session_state.selected_zone)
        render_overview_cards(stats)
        
        c1, c2 = st.columns([2, 1])
        
        with c1:
            st.markdown("### 📊 Behaviour Monitor")
            if not st.session_state.scan_complete:
                st.info("System is ready. Initiate neural scan to begin analysis.")
                if st.button("🚀 INITIATE NEURAL SCAN"):
                    with st.spinner("Processing Neural Layers..."):
                        time.sleep(1.5)
                    st.session_state.scan_complete = True
                    st.rerun()
            
            if st.session_state.scan_complete:
                alerts, anomaly_df, _ = run_behaviour_scan(ops_df, dist_df, st.session_state.selected_zone)
                if not alerts:
                    render_no_anomaly(st.session_state.selected_zone)
                else:
                    for alert in alerts:
                        render_alert_card(alert)
                    st.session_state.prediction_unlocked = True
            
        with c2:
            st.markdown("### 🧠 Live Intelligence")
            intelligence_news = [
                {"icon": "📈", "title": f"{st.session_state.selected_zone} Sales Drift", "desc": "Secondary sales show 4% volatility", "status": "Warning"},
                {"icon": "📦", "title": "Stock Reliability", "desc": "South Hub inventory at 98%", "status": "Optimal"},
                {"icon": "🌍", "title": "Market Sentiment", "desc": "Competitor pricing pressure detected", "status": "Risk"},
                {"icon": "⚡", "title": "System Latency", "desc": "Data ingestion node: 24ms", "status": "Optimal"}
            ]
            render_sentiment_feed(intelligence_news)

        if st.session_state.get("prediction_unlocked", False):
            render_divider()
            st.markdown("### 🔮 Risk Prediction Projection")
            # Logic for prediction charts goes here (Enterprise style transitions)
            st.info("Predictive models show potential recovery in 14 days if workflows are triggered.")
            if st.button("🛠 TRIGGER MITIGATION"):
                st.success("Workflows deployed. Access 'Supply Chain' for delivery tracking.")

    elif selected_page == "Inventory":
        st.markdown("### 📦 Inventory Intelligence")
        st.write("Production-ready inventory tables and SKU tracking models...")
        st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
        st.dataframe(sku_df.head(10), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif selected_page == "Supply Chain":
        st.markdown("### 🚚 Supply Chain Node Tracking")
        st.write("Active node management and logistics latency analysis...")
        st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
        st.dataframe(dist_df.head(10), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif selected_page == "Sentiment":
        st.markdown("### 💬 Market Sentiment Interface")
        st.write("AI-Generated news feeds and external signal monitoring...")
        render_sentiment_feed([
            {"icon": "🐦", "title": "Cluster Social Signal", "desc": "High distributor engagement in North sector", "status": "Optimal"},
            {"icon": "📉", "title": "Competitor Price Index", "desc": "Dropped by 8% in competitor cluster", "status": "Risk"}
        ] * 3)

    render_ai_footer()
