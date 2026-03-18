"""
Tab renderers – one function per analysis layer.
Per PDF requirements:
  ✅ Simple line chart for prediction, structured text, bullet format, business-focused
  ❌ No multiple bar charts, no pie charts, no heat maps, no KPI boxes
"""

import time
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from layers.decision import generate_root_cause
from layers.predictive import generate_forecast
from layers.conversational import get_demo_responses, match_response
from layers.automation import generate_workflow_actions


# ─────────────────────────────────────────────
# TAB 1 – Root Cause Analysis
# ─────────────────────────────────────────────
def render_root_cause_tab(alert, anomaly_df):
    st.markdown(
        '<div class="layer-indicator layer-active">'
        '<span class="status-dot"></span> '
        'Layer 2: Decision Intelligence Active</div>',
        unsafe_allow_html=True,
    )

    reasoning, summary = generate_root_cause(alert, anomaly_df)

    # Per PDF: "Explain reasoning" — structured text, not chart-heavy
    st.markdown("#### How Did the System Detect This?")
    st.markdown(
        '<div class="reasoning-block">'
        '<div class="reasoning-header">🔍 Detection Logic</div>'
        f'<p>The system compares current behaviour with <strong>30-day normal patterns</strong>. '
        f'When multiple stress indicators — sales deviation ({alert["Sales_Drop"]} drop), '
        f'credit days increase ({alert["Credit_Increase"]}), and inventory buildup '
        f'— moved together across {alert["Distributors_Affected"]} distributors in the '
        f'{alert["Zone"]} zone, the system flagged a <strong>behavioural deviation</strong>.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Root-cause contribution — simple weight bars (NOT pie chart per PDF)
    st.markdown("#### Contributing Factors")
    factors = [
        ("Stockout / Logistics Delay", 45, "#dc2626"),
        ("Competitive Pricing Pressure", 25, "#f59e0b"),
        ("Scheme Inactivity", 20, "#6366f1"),
        ("Credit Hold / Settlement Delay", 10, "#64748b"),
    ]
    for label, pct, color in factors:
        st.markdown(
            f'<div class="weight-container">'
            f'<div style="display:flex;justify-content:space-between;margin-bottom:4px;">'
            f'<span style="font-size:0.82rem;color:#334155;font-weight:500;">{label}</span>'
            f'<span style="font-size:0.82rem;color:#64748b;font-family:JetBrains Mono,monospace;">{pct}%</span>'
            f'</div>'
            f'<div class="weight-bar-bg">'
            f'<div class="weight-bar-fill" style="width:{pct}%;background:{color};"></div>'
            f'</div></div>',
            unsafe_allow_html=True,
        )

    # AI-generated root cause summary
    st.markdown("")
    st.markdown(
        '<div class="root-cause-card">'
        '<div class="root-cause-header">AI-Generated Root Cause Explanation</div>',
        unsafe_allow_html=True,
    )
    st.markdown(summary)
    st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# TAB 2 – Predictive Impact (Risk Projection)
# ─────────────────────────────────────────────
def render_predictive_tab(alert, ops_df, dist_df):
    st.markdown(
        '<div class="layer-indicator layer-active">'
        '<span class="status-dot"></span> '
        'Layer 3: Predictive Intelligence Active</div>',
        unsafe_allow_html=True,
    )

    # Per PDF: "Show Forecast as Risk Projection"
    st.markdown("#### Risk Projection — If No Action Taken")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    daily_sales, forecast_df, _, margin_comp = generate_forecast(
        ops_df, dist_df, zone=alert['Zone']
    )

    # Financial impact cards — Per PDF: Revenue, Margin, Working Capital
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="prediction-card">
            <div class="prediction-label">📉 Revenue Risk (60-Day)</div>
            <div class="prediction-value">{alert['Projected_Risk']}</div>
            <div class="prediction-label">Projected sales erosion if no corrective action</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="prediction-card">
            <div class="prediction-label">📊 Margin Compression</div>
            <div class="prediction-value">{margin_comp:.1f}%</div>
            <div class="prediction-label">Impact on operating margin</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="prediction-card">
            <div class="prediction-label">💰 Working Capital Impact</div>
            <div class="prediction-value">{alert['Credit_Increase']}</div>
            <div class="prediction-label">Credit days deterioration trend</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("")

    # Per PDF: "Simple line chart for prediction" — ONLY one chart, clean
    fig = go.Figure()

    # Historical line
    fig.add_trace(go.Scatter(
        x=daily_sales['Date'], y=daily_sales['Sales'],
        mode='lines', name='Historical Sales',
        line=dict(color='#1a1a2e', width=2, shape='spline'),
        fill='tozeroy',
        fillcolor='rgba(26,26,46,0.04)',
    ))

    # Forecast line
    fig.add_trace(go.Scatter(
        x=forecast_df['Date'], y=forecast_df['Forecast'],
        mode='lines', name='Projected Trajectory (No Action)',
        line=dict(color='#dc2626', width=2, dash='dash', shape='spline'),
    ))

    # Confidence band
    fig.add_trace(go.Scatter(
        x=pd.concat([forecast_df['Date'], forecast_df['Date'][::-1]]),
        y=pd.concat([forecast_df['Upper'], forecast_df['Lower'][::-1]]),
        fill='toself', fillcolor='rgba(220,38,38,0.05)',
        line=dict(color='rgba(220,38,38,0)'),
        name='Confidence Band',
    ))

    # Anomaly start marker
    anomaly_start = ops_df['Date'].min() + pd.Timedelta(days=59)
    fig.add_shape(
        type="line",
        x0=anomaly_start.strftime("%Y-%m-%d"),
        x1=anomaly_start.strftime("%Y-%m-%d"),
        y0=0, y1=1, yref="paper",
        line=dict(color="rgba(245,158,11,0.5)", width=1.5, dash="dot"),
    )
    fig.add_annotation(
        x=anomaly_start.strftime("%Y-%m-%d"), y=1, yref="paper",
        text="⚠ Deviation Start", showarrow=False,
        font=dict(color="#92400e", size=10, family="Inter"),
        yshift=12,
        bgcolor="rgba(254,243,199,0.8)",
        bordercolor="#fde68a",
        borderwidth=1,
        borderpad=4,
    )

    # Clean chart layout — Per PDF: white, corporate, minimal
    fig.update_layout(
        template='plotly_white',
        paper_bgcolor='rgba(255,255,255,0)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(family='Inter, sans-serif', color='#334155', size=12),
        height=400,
        margin=dict(l=50, r=30, t=40, b=50),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            xanchor="right", x=1,
            bgcolor="rgba(248,250,252,0.9)",
            bordercolor="#e2e8f0",
            borderwidth=1,
            font=dict(size=11),
        ),
        xaxis=dict(
            gridcolor='#f1f5f9',
            title="Date",
            title_font=dict(color='#64748b'),
            zeroline=False,
        ),
        yaxis=dict(
            gridcolor='#f1f5f9',
            title="Daily Sales (₹)",
            title_font=dict(color='#64748b'),
            zeroline=False,
        ),
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#e2e8f0",
            font=dict(family="JetBrains Mono", size=11, color="#0f172a"),
        ),
    )
    st.plotly_chart(fig, use_container_width=True)

    # Risk narrative — structured text block
    st.markdown(
        '<div class="reasoning-block">'
        '<div class="reasoning-header">📋 Risk Narrative</div>'
        f'<p>Based on the current deviation trajectory in <strong>{alert["Zone"]} Zone</strong>, '
        f'the system projects a revenue erosion of <strong>{alert["Projected_Risk"]}</strong> over '
        f'the next 60 days if no corrective action is taken. '
        f'Margin compression is estimated at <strong>{margin_comp:.1f}%</strong> due to '
        f'combined effects of sales decline and increased credit exposure.</p>'
        f'<p>Working capital is being affected as credit days have increased from '
        f'<strong>{alert["Credit_Increase"]}</strong>, indicating distributor financial stress.</p>'
        '</div>',
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────
# TAB 3 – Chat Intelligence
# ─────────────────────────────────────────────
def render_chat_tab(alert, ops_df):
    st.markdown(
        '<div class="layer-indicator layer-active">'
        '<span class="status-dot"></span> '
        'Layer 4: Conversational Intelligence Active</div>',
        unsafe_allow_html=True,
    )
    st.markdown("#### Operational Intelligence Chat")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        "*Ask the system about the detected anomaly. "
        "Responses are contextual — generated from real-time operational data analysis.*"
    )

    demo_responses = get_demo_responses(alert, ops_df.shape[0])

    # Quick-question buttons — Per PDF: business-focused, contextual
    st.markdown("**Suggested Questions:**")
    qc1, qc2, qc3 = st.columns(3)
    with qc1:
        if st.button("🔍 What is driving this deviation?", key="q1"):
            _add_chat(
                f"What are the primary drivers causing the deviation in {alert['Zone']} Zone?",
                demo_responses, alert,
            )
    with qc2:
        if st.button("📊 What is the financial exposure?", key="q2"):
            _add_chat(
                "What happens if no action is taken?",
                demo_responses, alert,
            )
    with qc3:
        if st.button("⚡ Provide containment strategy", key="q3"):
            _add_chat(
                "What containment strategies do you recommend to limit exposure?",
                demo_responses, alert,
            )

    st.markdown("")

    # Render history
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Free-text input
    if user_input := st.chat_input("Ask about the detected anomaly..."):
        response = match_response(user_input, demo_responses, alert)
        st.session_state.chat_messages.append({"role": "user", "content": user_input})
        st.session_state.chat_messages.append({"role": "assistant", "content": response})
        st.rerun()


def _add_chat(question, demo_responses, alert):
    response = match_response(question, demo_responses, alert)
    st.session_state.chat_messages.append({"role": "user", "content": question})
    st.session_state.chat_messages.append({"role": "assistant", "content": response})


# ─────────────────────────────────────────────
# TAB 4 – Trigger Workflow (Automation)
# Per PDF: "Position Automation as Next Phase"
# "Corrective workflow can be triggered automatically"
# ─────────────────────────────────────────────
def render_workflow_tab(alert):
    st.markdown(
        '<div class="layer-indicator layer-active">'
        '<span class="status-dot"></span> '
        'Layer 5: Automation Layer Active</div>',
        unsafe_allow_html=True,
    )
    st.markdown("#### Corrective Workflow Automation")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        "*The system can trigger corrective workflows automatically based on detected anomalies. "
        "Review and approve the generated action plans below.*"
    )

    _, col_mid, _ = st.columns([1, 1, 1])
    with col_mid:
        trigger = st.button(
            "⚡ Yes, Generate Mitigation Plans",
            use_container_width=True,
            key="workflow_btn",
        )

    if trigger:
        st.session_state.workflow_triggered = True

    if st.session_state.get("workflow_triggered"):
        with st.spinner("Generating corrective actions..."):
            time.sleep(1)

        actions = generate_workflow_actions(alert)

        st.markdown("""
        <div class="workflow-success">
            <span style="color:#166534;font-weight:700;font-size:1rem;">
                ✅ 3 Corrective Actions Generated
            </span><br>
            <span style="color:#15803d;font-size:0.82rem;">
                Review below. Once approved, actions execute automatically.
            </span>
        </div>
        """, unsafe_allow_html=True)

        for action in actions.values():
            with st.expander(f"{action['title']} ({action['type']})", expanded=True):
                st.markdown(action['content'])

        st.markdown("""
        <div class="workflow-info">
            <p style="color:#334155;font-size:0.9rem;font-weight:500;margin:0;">
                💡 In production, these corrective actions are automatically routed
                to approval workflows, email systems, and CRM platforms
                via API integrations.
            </p>
        </div>
        """, unsafe_allow_html=True)
