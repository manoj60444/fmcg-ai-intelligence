"""
Tab renderers – one function per analysis tab.
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

    st.markdown("### 🔎 Root Cause Analysis")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown("**Contributing Factor Weights:**")

    for _key, data in reasoning.items():
        weight_val = int(data['weight'].replace('%', ''))
        st.markdown(f"""
        <div class="weight-container">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
                <span style="color:#e2e8f0;font-weight:500;">{data['label']}</span>
                <span style="color:{data['color']};font-weight:700;">{data['weight']}</span>
            </div>
            <div class="weight-bar-bg">
                <div class="weight-bar-fill"
                     style="width:{weight_val}%;
                            background:linear-gradient(90deg,{data['color']},{data['color']}88);">
                </div>
            </div>
            <div style="color:#94a3b8;font-size:0.8rem;margin-top:4px;">
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
            <div class="prediction-value">3 More</div>
            <div class="prediction-label">Distributors Likely Affected</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("")

    # Plotly chart
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=daily_sales['Date'], y=daily_sales['Sales'],
        mode='lines', name='Historical Sales',
        line=dict(color='#8b5cf6', width=2),
        fill='tozeroy', fillcolor='rgba(139,92,246,0.1)',
    ))

    fig.add_trace(go.Scatter(
        x=forecast_df['Date'], y=forecast_df['Forecast'],
        mode='lines', name='Forecast (No Action)',
        line=dict(color='#ef4444', width=2, dash='dash'),
    ))

    fig.add_trace(go.Scatter(
        x=pd.concat([forecast_df['Date'], forecast_df['Date'][::-1]]),
        y=pd.concat([forecast_df['Upper'], forecast_df['Lower'][::-1]]),
        fill='toself', fillcolor='rgba(239,68,68,0.1)',
        line=dict(color='rgba(239,68,68,0)'),
        name='Confidence Interval',
    ))

    # Anomaly-start marker
    anomaly_start = ops_df['Date'].min() + pd.Timedelta(days=59)
    fig.add_shape(
        type="line",
        x0=anomaly_start.strftime("%Y-%m-%d"),
        x1=anomaly_start.strftime("%Y-%m-%d"),
        y0=0, y1=1, yref="paper",
        line=dict(color="rgba(251,191,36,0.5)", width=2, dash="dot"),
    )
    fig.add_annotation(
        x=anomaly_start.strftime("%Y-%m-%d"), y=1, yref="paper",
        text="Anomaly Start", showarrow=False,
        font=dict(color="#fbbf24", size=12), yshift=10,
    )

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter'),
        height=450,
        margin=dict(l=50, r=30, t=30, b=50),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(gridcolor='rgba(99,102,241,0.1)', title="Date"),
        yaxis=dict(gridcolor='rgba(99,102,241,0.1)', title="Daily Sales (₹)"),
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
    st.markdown("### 💬 Chat Intelligence")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        "*Ask questions about the detected anomaly. "
        "The AI will respond based on the operational data.*"
    )

    demo_responses = get_demo_responses(alert, ops_df.shape[0])

    # Quick-question buttons
    st.markdown("**Suggested Questions:**")
    qc1, qc2, qc3 = st.columns(3)
    with qc1:
        if st.button(f"❓ Why is {alert['Zone']} Zone dropping?", key="q1"):
            _add_chat(
                f"Why is {alert['Zone']} Zone performance dropping?",
                demo_responses, alert,
            )
    with qc2:
        if st.button("❓ What if no action taken?", key="q2"):
            _add_chat(
                "What happens if no action is taken?",
                demo_responses, alert,
            )
    with qc3:
        if st.button("❓ Recommended actions?", key="q3"):
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
        "*Click the button below to trigger automated corrective actions. "
        "The system will generate draft communications and action plans.*"
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
        with st.spinner("Generating corrective actions..."):
            time.sleep(1)

        actions = generate_workflow_actions(alert)

        st.markdown("""
        <div style="background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.3);
             border-radius:12px;padding:1rem;margin:1rem 0;text-align:center;">
            <span style="color:#4ade80;font-weight:700;font-size:1.1rem;">
                ✅ 3 Corrective Actions Generated Successfully
            </span><br>
            <span style="color:#86efac;font-size:0.85rem;">
                Once approved, this can be automated fully.
            </span>
        </div>
        """, unsafe_allow_html=True)

        for action in actions.values():
            with st.expander(f"{action['title']} ({action['type']})", expanded=True):
                st.markdown(action['content'])

        st.markdown("""
        <div style="text-align:center;margin-top:2rem;padding:1.5rem;
             background:rgba(99,102,241,0.1);border:1px solid rgba(99,102,241,0.2);
             border-radius:12px;">
            <p style="color:#a78bfa;font-size:1rem;font-weight:600;margin:0;">
                💡 In production, these actions would be automatically routed
                to approval workflows, email systems, and CRM platforms
                via API integrations.
            </p>
        </div>
        """, unsafe_allow_html=True)
