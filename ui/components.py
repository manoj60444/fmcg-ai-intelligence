"""
Reusable UI components for the FMCG demo.
"""

import streamlit as st


def render_overview_cards(stats):
    """Render the five KPI cards at the top of the page."""
    st.markdown(f"""
    <div class="overview-container">
        <div class="overview-card">
            <div class="overview-number">{stats['distributors']}</div>
            <div class="overview-label">Active Distributors</div>
        </div>
        <div class="overview-card">
            <div class="overview-number">{stats['zones']}</div>
            <div class="overview-label">Zones Monitored</div>
        </div>
        <div class="overview-card">
            <div class="overview-number">{stats['skus']}</div>
            <div class="overview-label">SKUs Tracked</div>
        </div>
        <div class="overview-card">
            <div class="overview-number">{stats['days']}</div>
            <div class="overview-label">Days of Data</div>
        </div>
        <div class="overview-card">
            <div class="overview-number">{stats['data_points']:,}</div>
            <div class="overview-label">Data Points</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_layer_status():
    """Render the six layer-status badges."""
    from config.settings import LAYERS

    cols = st.columns(len(LAYERS))
    for i, (col, layer) in enumerate(zip(cols, LAYERS)):
        with col:
            st.markdown(f"""
            <div style="text-align:center;">
                <div class="layer-indicator layer-active">
                    <span class="status-dot"></span>
                    Layer {i + 1}: {layer['name']}
                </div>
            </div>
            """, unsafe_allow_html=True)


def render_alert_card(alert):
    """Render a red alert card for a detected anomaly."""
    st.markdown(f"""
    <div class="alert-card">
        <div class="alert-header">
            <span class="alert-badge">🚨 ALERT DETECTED</span>
            <span class="alert-title">{alert['Zone']} Zone – {alert['Cluster']}</span>
        </div>
        <div class="alert-details">
            <div class="alert-metric">
                <div class="alert-metric-value">{alert['Confidence']}</div>
                <div class="alert-metric-label">Confidence Level</div>
            </div>
            <div class="alert-metric">
                <div class="alert-metric-value">{alert['Projected_Risk']}</div>
                <div class="alert-metric-label">Projected Risk</div>
            </div>
            <div class="alert-metric">
                <div class="alert-metric-value">{alert['Distributors_Affected']}</div>
                <div class="alert-metric-label">Distributors Affected</div>
            </div>
            <div class="alert-metric">
                <div class="alert-metric-value">{alert['Sales_Drop']}</div>
                <div class="alert-metric-label">Sales Decline</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_no_anomaly(zone_label):
    """Render a green 'all clear' banner."""
    st.markdown(f"""
    <div class="no-anomaly-banner">
        <div class="icon">✅</div>
        <div class="headline">No Anomalies Detected</div>
        <div class="body">
            {zone_label} operating within normal parameters.
            All distributors are within acceptable thresholds for sales,
            credit, and inventory metrics.
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_divider():
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
