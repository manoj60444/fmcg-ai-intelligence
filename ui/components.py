"""
Reusable UI components for the FMCG Operational Intelligence System.
Per PDF: Clean, minimal, corporate. No KPI tiles. Show detection first.
"""

import streamlit as st


def render_ai_header(title, subtitle):
    """Render clean corporate header with status badge."""
    html = (
        f'<div class="ai-header-container">'
        f'<div class="ai-badge"><span class="pulse-dot"></span> SYSTEM ACTIVE — MONITORING OPERATIONS</div>'
        f'<div class="main-title">{title}</div>'
        f'<div class="sub-title">{subtitle}</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_detection_banner(alert):
    """
    Render automatic detection banner — this is shown FIRST per PDF:
    'When demo starts, first show: Behavioural Drift Detected'
    """
    html = (
        f'<div class="detection-banner">'
        f'<div class="detection-title">🚨 Behavioural Drift Detected — {alert["Zone"]} Zone</div>'
        f'<div class="detection-body">'
        f'The system identified an operational deviation in {alert["Zone"]} {alert["Cluster"]} '
        f'<strong>before manual review</strong>. It compares current behaviour with 30-day normal '
        f'patterns. When multiple stress indicators moved together, it flagged a behavioural deviation.'
        f'</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_financial_impact(alert):
    """
    Render financial impact cards — Per PDF:
    'Every output must include: Revenue loss estimate, Margin impact, Working capital impact'
    """
    html = (
        f'<div class="impact-row">'
        f'<div class="impact-card">'
        f'<div class="impact-label">Revenue Risk (60-Day Projection)</div>'
        f'<div class="impact-value">{alert["Projected_Risk"]}</div>'
        f'<div class="impact-note">If no corrective action is taken</div>'
        f'</div>'
        f'<div class="impact-card">'
        f'<div class="impact-label">Margin Impact</div>'
        f'<div class="impact-value">7.2%</div>'
        f'<div class="impact-note">Compression from current deviation</div>'
        f'</div>'
        f'<div class="impact-card">'
        f'<div class="impact-label">Working Capital Impact</div>'
        f'<div class="impact-value">{alert["Credit_Increase"]}</div>'
        f'<div class="impact-note">Credit days deterioration</div>'
        f'</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_layer_status():
    """Render simple layer pipeline — corporate style."""
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
    """Render clean alert card for a detected anomaly — corporate style."""
    html = (
        f'<div class="alert-card">'
        f'<div class="alert-header">'
        f'<span class="alert-badge">⚠ OPERATIONAL RISK DETECTED</span>'
        f'<span class="alert-title">{alert["Zone"]} Zone — {alert["Cluster"]}</span>'
        f'</div>'
        f'<div style="color: #475569; font-size: 0.88rem; margin-bottom: 0.8rem; line-height: 1.6;">'
        f'The system detected a behaviour anomaly in the {alert["Zone"]} cluster. '
        f'{alert["Distributors_Affected"]} distributors show synchronized deviation '
        f'from normal operational patterns. Corrective action is recommended to prevent revenue erosion.'
        f'</div>'
        f'<div class="alert-details">'
        f'<div class="alert-metric"><div class="alert-metric-value">{alert["Projected_Risk"]}</div><div class="alert-metric-label">Revenue Risk</div></div>'
        f'<div class="alert-metric"><div class="alert-metric-value">7.2%</div><div class="alert-metric-label">Margin Impact</div></div>'
        f'<div class="alert-metric"><div class="alert-metric-value">{alert["Distributors_Affected"]}</div><div class="alert-metric-label">Affected Distributors</div></div>'
        f'<div class="alert-metric"><div class="alert-metric-value">{alert["Confidence"]}</div><div class="alert-metric-label">Confidence</div></div>'
        f'</div></div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_no_anomaly(zone_label):
    """Render a green 'all clear' banner."""
    html = (
        f'<div class="no-anomaly-banner">'
        f'<div class="icon">✅</div>'
        f'<div class="headline">All Operations Within Normal Parameters</div>'
        f'<div class="body">{zone_label} operations are within normal parameters. '
        f'The system has been continuously monitoring distributor metrics across '
        f'sales, credit, and inventory signals — no behavioural drift detected.</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_divider():
    """Render a simple divider line."""
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)


def render_ai_footer():
    """Render the corporate footer."""
    html = (
        '<div class="ai-footer">'
        '<div class="ai-footer-line"></div>'
        '<div class="ai-footer-text">'
        'FMCG Operational Intelligence · '
        'Continuous Monitoring · '
        '5 Active Intelligence Layers'
        '</div></div>'
    )
    st.markdown(html, unsafe_allow_html=True)
