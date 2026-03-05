"""
Reusable UI components for the FMCG AI Intelligence System.
Premium AI-themed components with glassmorphism, glow effects, and animations.
"""

import streamlit as st


def render_ai_header(title, subtitle):
    """Render the premium animated AI header with badge and neural line."""
    html = (
        f'<div class="ai-header-container">'
        f'<div class="ai-badge"><span class="pulse-dot"></span> AI SYSTEM ONLINE</div>'
        f'<div class="main-title">{title}</div>'
        f'<div class="sub-title">{subtitle}</div>'
        f'<div class="neural-line"></div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_overview_cards(stats):
    """Render the five KPI cards with glassmorphism and icons."""
    cards = [
        ("🏢", stats['distributors'], "Active Distributors"),
        ("🌍", stats['zones'], "Zones Monitored"),
        ("📦", stats['skus'], "SKUs Tracked"),
        ("📅", stats['days'], "Days of Data"),
        ("📊", f"{stats['data_points']:,}", "Data Points"),
    ]
    cards_html = ""
    for icon, value, label in cards:
        cards_html += (
            f'<div class="overview-card">'
            f'<div class="overview-icon">{icon}</div>'
            f'<div class="overview-number">{value}</div>'
            f'<div class="overview-label">{label}</div>'
            f'</div>'
        )
    st.markdown(
        f'<div class="overview-container">{cards_html}</div>',
        unsafe_allow_html=True,
    )


def render_layer_status():
    """Render the AI layer pipeline with connectors."""
    from config.settings import LAYERS

    nodes_html = ""
    for i, layer in enumerate(LAYERS):
        nodes_html += (
            f'<div class="layer-node">'
            f'<div class="layer-node-icon">{layer["icon"]}</div>'
            f'<div class="layer-node-name">{layer["name"]}</div>'
            f'<div class="layer-node-status"><span class="dot"></span> ACTIVE</div>'
            f'</div>'
        )
        if i < len(LAYERS) - 1:
            nodes_html += '<div class="layer-connector"></div>'

    st.markdown(
        f'<div class="layer-pipeline">{nodes_html}</div>',
        unsafe_allow_html=True,
    )


def render_alert_card(alert):
    """Render a cyberpunk-style red alert card for a detected anomaly."""
    html = (
        f'<div class="alert-card">'
        f'<div class="alert-header">'
        f'<span class="alert-badge">⚠ ANOMALY DETECTED</span>'
        f'<span class="alert-title">{alert["Zone"]} Zone – {alert["Cluster"]}</span>'
        f'</div>'
        f'<div class="alert-details">'
        f'<div class="alert-metric"><div class="alert-metric-value">{alert["Confidence"]}</div><div class="alert-metric-label">Confidence</div></div>'
        f'<div class="alert-metric"><div class="alert-metric-value">{alert["Projected_Risk"]}</div><div class="alert-metric-label">Projected Risk</div></div>'
        f'<div class="alert-metric"><div class="alert-metric-value">{alert["Distributors_Affected"]}</div><div class="alert-metric-label">Affected Nodes</div></div>'
        f'<div class="alert-metric"><div class="alert-metric-value">{alert["Sales_Drop"]}</div><div class="alert-metric-label">Sales Decline</div></div>'
        f'</div></div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_no_anomaly(zone_label):
    """Render a green 'all clear' banner."""
    html = (
        f'<div class="no-anomaly-banner">'
        f'<div class="icon">✅</div>'
        f'<div class="headline">All Systems Nominal</div>'
        f'<div class="body">{zone_label} operations are within normal parameters. '
        f'AI monitoring confirms all distributor metrics are within '
        f'acceptable thresholds across sales, credit, and inventory signals.</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_divider():
    """Render a gradient divider line."""
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)


def render_ai_footer():
    """Render the premium AI footer."""
    html = (
        '<div class="ai-footer">'
        '<div class="ai-footer-line"></div>'
        '<div class="ai-footer-text">'
        '<span>FMCG Operational Intelligence</span> · '
        'Powered by <span>Artificial Intelligence</span> · '
        '6 Active Neural Layers · Real-time Monitoring'
        '</div></div>'
    )
    st.markdown(html, unsafe_allow_html=True)
