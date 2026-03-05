"""
Professional FMCG AI Components
===============================
Senior Developer UI: Glassmorphism, Status Indicators, Sentiment Feeds.
"""

import streamlit as st

def render_ai_header(title, subtitle):
    """Render the professional thin-weight header with letter spacing."""
    st.markdown(f"""
    <div class="main-header">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def render_kpi(label, value, change, icon, is_up=True):
    """Render a custom HTML/CSS glassmorphism KPI card."""
    change_class = "change-up" if is_up else "change-down"
    change_sign = "↑" if is_up else "↓"
    
    return f"""
    <div class="kpi-card">
        <div class="kpi-icon">{icon}</div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-change {change_class}">
            {change_sign} {change} <span>vs last month</span>
        </div>
    </div>
    """

def render_overview_cards(stats):
    """Render the glassmorphism KPI card row with correct data."""
    # Build 1-3-1 spacing using columns if needed, but flexbox is better for this
    # Flexible row of cards
    cards = [
        {"icon": "🏢", "label": "Active Distributors", "value": stats['distributors'], "change": "4.2%", "up": True},
        {"icon": "🌍", "label": "Zones Monitored", "value": stats['zones'], "change": "0%", "up": True},
        {"icon": "📦", "label": "SKUs Tracked", "value": stats['skus'], "change": "12", "up": True},
        {"icon": "📅", "label": "Operational Days", "value": stats['days'], "change": "30", "up": True},
    ]
    
    cols = st.columns(len(cards))
    for i, col in enumerate(cols):
        with col:
            st.markdown(render_kpi(
                cards[i]['label'], 
                cards[i]['value'], 
                cards[i]['change'], 
                cards[i]['icon'], 
                cards[i]['up']
            ), unsafe_allow_html=True)

def render_status_indicator(status_type):
    """Render a professional dot status indicator: optimal, warning, risk."""
    status_map = {
        "Optimal": "dot-optimal",
        "Warning": "dot-warning",
        "Risk": "dot-risk"
    }
    class_name = status_map.get(status_type, "dot-optimal")
    return f'<span class="status-dot {class_name}"></span>'

def render_sentiment_feed(news_items):
    """Render a professional scrollable news/intelligence feed."""
    items_html = ""
    for item in news_items:
        items_html += f"""
        <div class="sentiment-item">
            <div style="font-size:1.5rem;">{item['icon']}</div>
            <div style="flex:1;">
                <div style="font-weight:600; color:#0F172A; font-size:0.9rem;">{item['title']}</div>
                <div style="color:#64748B; font-size:0.8rem; margin-top:2px;">{item['desc']}</div>
            </div>
            {render_status_indicator(item['status'])}
        </div>
        """
    
    st.markdown(f"""
    <div class="sentiment-container">
        {items_html}
    </div>
    """, unsafe_allow_html=True)

def render_divider():
    """Simple subtle divider."""
    st.markdown('<hr style="border: 0; height: 1px; background: #E2E8F0; margin: 2rem 0;">', unsafe_allow_html=True)

def render_ai_footer():
    """Professional minimalist footer."""
    st.markdown("""
    <div style="text-align:center; padding: 4rem 0; color:#94A3B8; font-size:0.8rem; font-weight:500; letter-spacing:0.05em;">
        FMCG OPERATIONAL INTELLIGENCE LAYER — PRODUCTION CLUSTER V4.2
    </div>
    """, unsafe_allow_html=True)

def render_alert_card(alert):
    """Professional alert card with status dot."""
    st.markdown(f"""
    <div class="sentiment-item" style="border-left: 4px solid #EF4444; border-radius: 12px; background:white; padding: 1.5rem;">
        <div style="font-size:2rem; margin-right: 1rem;">🚨</div>
        <div style="flex:1;">
            <div style="text-transform:uppercase; font-size:0.75rem; font-weight:700; color:#EF4444; letter-spacing:0.1em;">ANOMALY DETECTED</div>
            <div style="font-size:1.1rem; font-weight:700; color:#0F172A; margin: 4px 0;">{alert['Zone']} Zone: {alert['Cluster']} Cluster</div>
            <div style="color:#64748B; font-size:0.9rem;">Confidence: <b>{alert['Confidence']}</b> | Risk: <b>{alert['Projected_Risk']}</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_no_anomaly(zone):
    """Professional 'all clear' state."""
    st.markdown(f"""
    <div class="sentiment-item" style="border-left: 4px solid #10B981; border-radius: 12px; background:white; padding: 1.5rem;">
        <div style="font-size:2rem; margin-right: 1rem;">✅</div>
        <div style="flex:1;">
            <div style="text-transform:uppercase; font-size:0.75rem; font-weight:700; color:#10B981; letter-spacing:0.1em;">All Systems Optimal</div>
            <div style="font-size:1.1rem; font-weight:700; color:#0F172A; margin: 4px 0;">Cluster {zone} is stable</div>
            <div style="color:#64748B; font-size:0.9rem;">No behavioural drift detected in secondary distributor signals.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
