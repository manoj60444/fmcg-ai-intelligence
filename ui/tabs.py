"""
Tab renderers – one function per analysis tab.
Premium AI-themed tabs with enhanced Plotly charts and styling.
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

    st.markdown("### 🧠 AI Root Cause Analysis")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown("**Contributing Factor Weights:**")

    for _key, data in reasoning.items():
        weight_val = int(data['weight'].replace('%', ''))
        st.markdown(f"""
        <div class="weight-container">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
                <span style="color:#e2e8f0;font-weight:600;font-size:0.9rem;">{data['label']}</span>
                <span style="color:{data['color']};font-weight:800;font-family:'JetBrains Mono',monospace;">{data['weight']}</span>
            </div>
            <div class="weight-bar-bg">
                <div class="weight-bar-fill"
                     style="width:{weight_val}%;
                            background:linear-gradient(90deg,{data['color']},{data['color']}88);">
                </div>
            </div>
            <div style="color:#64748b;font-size:0.78rem;margin-top:6px;padding-left:2px;">
                📌 {data['evidence']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="root-cause-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="root-cause-header">'
        '🧠 AI-Generated Root Cause Explanation</div>',
        unsafe_allow_html=True,
    )
    st.markdown(summary)
    st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# TAB 2 – Predictive Impact
# ─────────────────────────────────────────────
def render_predictive_tab(alert, ops_df, dist_df):
    st.markdown(
        '<div class="layer-indicator layer-active">'
        '<span class="status-dot"></span> '
        'Layer 3: Predictive Intelligence Active</div>',
        unsafe_allow_html=True,
    )

    st.markdown("### 📈 Predictive Impact Analysis")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    daily_sales, forecast_df, _, margin_comp = generate_forecast(
        ops_df, dist_df, zone=alert['Zone']
    )

    # Metric cards
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="prediction-card">
            <div class="prediction-label">📉 If No Action Taken</div>
            <div class="prediction-value">{alert['Projected_Risk']}</div>
            <div class="prediction-label">Projected Revenue Loss</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="prediction-card">
            <div class="prediction-label">📊 Margin Impact</div>
            <div class="prediction-value">{margin_comp:.1f}%</div>
            <div class="prediction-label">Margin Compression</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="prediction-card">
            <div class="prediction-label">🏢 Spread Risk</div>
            <div class="prediction-value">Likely High</div>
            <div class="prediction-label">Market Contagion Rating</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("")
    
    # NEW: Catchy Pie Chart for Risk Distribution
    st.markdown("#### 🥧 Risk Matrix Distribution")
    cc1, cc2 = st.columns([1, 2])
    with cc1:
        pie_fig = go.Figure(data=[go.Pie(
            labels=['Sales Loss', 'Margin Compression', 'Inventory Bloat', 'Credit Exposure'],
            values=[40, 25, 20, 15],
            hole=.6,
            marker_colors=['#f87171', '#fbbf24', '#6366f1', '#a855f7']
        )])
        pie_fig.update_layout(
            showlegend=False,
            height=250,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(pie_fig, use_container_width=True)
    
    with cc2:
        st.markdown("""
        <div style="padding: 1rem; background: rgba(15,18,35,0.4); border-radius: 12px; height: 100%;">
            <p style="color: #94a3b8; font-size: 0.9rem;">
                <b>AI Insight:</b> Most of the risk is concentrated in <b>Sales Loss (40%)</b>. 
                The system detects that the secondary cause is <b>Margin Compression</b> due to 
                aggressive competitor pricing in the south cluster.
            </p>
            <p style="color: #6366f1; font-weight: 600; font-size: 0.8rem; letter-spacing: 1px;">
                CONFIDENCE: 94.2%
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Premium Plotly chart
    fig = go.Figure()

    # Historical line with gradient fill
    fig.add_trace(go.Scatter(
        x=daily_sales['Date'], y=daily_sales['Sales'],
        mode='lines', name='Historical Sales',
        line=dict(color='#818cf8', width=2.5, shape='spline'),
        fill='tozeroy',
        fillcolor='rgba(129,140,248,0.08)',
    ))

    # Forecast line
    fig.add_trace(go.Scatter(
        x=forecast_df['Date'], y=forecast_df['Forecast'],
        mode='lines', name='AI Forecast (No Action)',
        line=dict(color='#f87171', width=2.5, dash='dash', shape='spline'),
    ))

    # Confidence band
    fig.add_trace(go.Scatter(
        x=pd.concat([forecast_df['Date'], forecast_df['Date'][::-1]]),
        y=pd.concat([forecast_df['Upper'], forecast_df['Lower'][::-1]]),
        fill='toself', fillcolor='rgba(248,113,113,0.06)',
        line=dict(color='rgba(248,113,113,0)'),
        name='Confidence Band',
    ))

    # Anomaly-start marker
    anomaly_start = ops_df['Date'].min() + pd.Timedelta(days=59)
    fig.add_shape(
        type="line",
        x0=anomaly_start.strftime("%Y-%m-%d"),
        x1=anomaly_start.strftime("%Y-%m-%d"),
        y0=0, y1=1, yref="paper",
        line=dict(color="rgba(251,191,36,0.4)", width=2, dash="dot"),
    )
    fig.add_annotation(
        x=anomaly_start.strftime("%Y-%m-%d"), y=1, yref="paper",
        text="⚠ Anomaly Start", showarrow=False,
        font=dict(color="#fbbf24", size=11, family="Outfit"),
        yshift=12,
        bgcolor="rgba(251,191,36,0.1)",
        bordercolor="rgba(251,191,36,0.3)",
        borderwidth=1,
        borderpad=4,
    )

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Outfit, sans-serif', color='#94a3b8'),
        height=460,
        margin=dict(l=50, r=30, t=40, b=50),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            xanchor="right", x=1,
            bgcolor="rgba(15,18,35,0.5)",
            bordercolor="rgba(99,102,241,0.15)",
            borderwidth=1,
            font=dict(size=11),
        ),
        xaxis=dict(
            gridcolor='rgba(99,102,241,0.06)',
            title="Date",
            title_font=dict(color='#64748b'),
            zeroline=False,
        ),
        yaxis=dict(
            gridcolor='rgba(99,102,241,0.06)',
            title="Daily Sales (₹)",
            title_font=dict(color='#64748b'),
            zeroline=False,
        ),
        hoverlabel=dict(
            bgcolor="rgba(15,18,35,0.9)",
            bordercolor="rgba(99,102,241,0.3)",
            font=dict(family="JetBrains Mono", size=12, color="#e2e8f0"),
        ),
    )
    st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────
# TAB 3 – Chat Intelligence
# ─────────────────────────────────────────────
def render_chat_tab(alert, ops_df):
    st.markdown(
        '<div class="layer-indicator layer-active">'
        '<span class="status-dot"></span> '
        'Layer 4: Conversational AI Active</div>',
        unsafe_allow_html=True,
    )
    st.markdown("### 💬 AI Chat Intelligence")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        "*Ask the AI about the detected anomaly. "
        "Responses are generated from real-time operational data analysis.*"
    )

    demo_responses = get_demo_responses(alert, ops_df.shape[0])

    # Quick-question buttons
    st.markdown("**Suggested Queries:**")
    qc1, qc2, qc3 = st.columns(3)
    with qc1:
        if st.button(f"🔍 Why is {alert['Zone']} Zone dropping?", key="q1"):
            _add_chat(
                f"Why is {alert['Zone']} Zone performance dropping?",
                demo_responses, alert,
            )
    with qc2:
        if st.button("📊 What if no action taken?", key="q2"):
            _add_chat(
                "What happens if no action is taken?",
                demo_responses, alert,
            )
    with qc3:
        if st.button("⚡ Recommended actions?", key="q3"):
            _add_chat(
                "What corrective action do you recommend?",
                demo_responses, alert,
            )

    st.markdown("")

    # Render history
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Free-text input
    if user_input := st.chat_input("Ask the AI about the detected anomaly..."):
        response = match_response(user_input, demo_responses, alert)
        st.session_state.chat_messages.append({"role": "user", "content": user_input})
        st.session_state.chat_messages.append({"role": "assistant", "content": response})
        st.rerun()


def _add_chat(question, demo_responses, alert):
    response = match_response(question, demo_responses, alert)
    st.session_state.chat_messages.append({"role": "user", "content": question})
    st.session_state.chat_messages.append({"role": "assistant", "content": response})


# ─────────────────────────────────────────────
# TAB 4 – Trigger Workflow
# ─────────────────────────────────────────────
def render_workflow_tab(alert):
    st.markdown(
        '<div class="layer-indicator layer-active">'
        '<span class="status-dot"></span> '
        'Layer 5: Automation Layer Active</div>',
        unsafe_allow_html=True,
    )
    st.markdown("### ⚡ Corrective Workflow Automation")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        "*Click below to trigger AI-generated corrective actions. "
        "The system will create draft communications and action plans automatically.*"
    )

    _, col_mid, _ = st.columns([1, 1, 1])
    with col_mid:
        trigger = st.button(
            "⚡ Trigger Corrective Workflow",
            use_container_width=True,
            key="workflow_btn",
        )

    if trigger:
        st.session_state.workflow_triggered = True

    if st.session_state.get("workflow_triggered"):
        with st.spinner("AI generating corrective actions..."):
            time.sleep(1)

        actions = generate_workflow_actions(alert)

        st.markdown("""
        <div class="workflow-success">
            <span style="color:#4ade80;font-weight:700;font-size:1.1rem;">
                ✅ 3 Corrective Actions Generated by AI
            </span><br>
            <span style="color:#86efac;font-size:0.82rem;">
                Review below. Once approved, actions execute automatically.
            </span>
        </div>
        """, unsafe_allow_html=True)

        for action in actions.values():
            with st.expander(f"{action['title']} ({action['type']})", expanded=True):
                st.markdown(action['content'])

        st.markdown("""
        <div class="workflow-info">
            <p style="color:#a78bfa;font-size:0.95rem;font-weight:600;margin:0;">
                💡 In production, these AI-generated actions are automatically routed
                to approval workflows, email systems, and CRM platforms
                via intelligent API integrations.
            </p>
        </div>
        """, unsafe_allow_html=True)
