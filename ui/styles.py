"""
UI Styles – Clean, Corporate, Operational Intelligence System.
Per PDF requirements:
  ✅ White background, clean alert cards, structured text, simple line charts
  ❌ No dark themes, no animated dashboards, no startup-looking UI, no KPI tiles
"""

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ============================================================
       CORE — Clean White Corporate Background
       ============================================================ */
    .stApp {
        background: #ffffff;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #1a1a2e;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ============================================================
       SIDEBAR — Professional Navy
       ============================================================ */
    [data-testid="stSidebar"] {
        background: #1a1a2e;
        border-right: 1px solid #e5e7eb;
    }
    [data-testid="stSidebar"] .stSelectbox label {
        color: #94a3b8 !important;
    }

    .nav-header {
        text-align: center;
        padding: 2rem 1rem 1.5rem;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 1.5rem;
    }

    /* ============================================================
       HEADER — Corporate, minimal
       ============================================================ */
    .ai-header-container {
        text-align: center;
        padding: 2rem 2rem 1rem;
        margin-bottom: 0.5rem;
        border-bottom: 1px solid #f1f5f9;
    }

    .ai-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-radius: 50px;
        padding: 5px 16px;
        font-size: 0.68rem;
        font-weight: 600;
        color: #166534;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }
    .ai-badge .pulse-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #22c55e;
        animation: dotPulse 2s ease-in-out infinite;
    }
    @keyframes dotPulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.3); opacity: 0.6; }
    }

    .main-title {
        text-align: center;
        font-size: 1.8rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.2rem;
        letter-spacing: -0.5px;
    }

    .sub-title {
        text-align: center;
        font-size: 0.75rem;
        color: #94a3b8;
        margin-bottom: 0.5rem;
        font-weight: 500;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    /* ============================================================
       ALERT CARD — Clean white with red accent (NOT cyberpunk)
       Per PDF: "Clear alert cards"
       ============================================================ */
    .alert-card {
        position: relative;
        background: #ffffff;
        border: 1px solid #fecaca;
        border-left: 4px solid #dc2626;
        border-radius: 8px;
        padding: 1.5rem 1.8rem;
        margin: 1.2rem auto;
        max-width: 850px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
        animation: alertFadeIn 0.5s ease;
    }
    @keyframes alertFadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .alert-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 0.8rem;
    }
    .alert-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #dc2626;
        color: white;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .alert-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #991b1b;
    }
    .alert-details {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
        flex-wrap: wrap;
    }
    .alert-metric {
        text-align: center;
        background: #fef2f2;
        border: 1px solid #fecaca;
        border-radius: 6px;
        padding: 0.8rem 1.2rem;
        min-width: 130px;
        flex: 1;
    }
    .alert-metric-value {
        font-size: 1.3rem;
        font-weight: 800;
        color: #dc2626;
        font-family: 'JetBrains Mono', monospace;
    }
    .alert-metric-label {
        font-size: 0.7rem;
        color: #991b1b;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 2px;
        font-weight: 500;
    }

    /* ============================================================
       DETECTION BANNER — System auto-detected (show FIRST)
       Per PDF: "Behavioural Drift Detected" first
       ============================================================ */
    .detection-banner {
        background: #fffbeb;
        border: 1px solid #fde68a;
        border-left: 4px solid #f59e0b;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin: 1rem auto;
        max-width: 850px;
        animation: alertFadeIn 0.6s ease;
    }
    .detection-banner .detection-title {
        font-size: 1rem;
        font-weight: 700;
        color: #92400e;
        margin-bottom: 0.3rem;
    }
    .detection-banner .detection-body {
        font-size: 0.88rem;
        color: #78350f;
        line-height: 1.6;
    }

    /* ============================================================
       REASONING BLOCK — Structured text, per PDF
       ============================================================ */
    .reasoning-block {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem auto;
        max-width: 850px;
    }
    .reasoning-block .reasoning-header {
        font-size: 0.95rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .reasoning-block p, .reasoning-block li {
        font-size: 0.88rem;
        color: #334155;
        line-height: 1.7;
    }

    /* ============================================================
       FINANCIAL IMPACT CARDS — Per PDF: Revenue, Margin, Working Capital
       ============================================================ */
    .impact-row {
        display: flex;
        gap: 1rem;
        margin: 1rem auto;
        max-width: 850px;
        flex-wrap: wrap;
    }
    .impact-card {
        flex: 1;
        min-width: 200px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    }
    .impact-card .impact-label {
        font-size: 0.7rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.3rem;
    }
    .impact-card .impact-value {
        font-size: 1.4rem;
        font-weight: 800;
        color: #dc2626;
        font-family: 'JetBrains Mono', monospace;
    }
    .impact-card .impact-note {
        font-size: 0.78rem;
        color: #94a3b8;
        margin-top: 0.2rem;
    }

    /* ============================================================
       PREDICTION CARD  — Minimal
       ============================================================ */
    .prediction-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    }
    .prediction-value {
        font-size: 1.4rem;
        font-weight: 800;
        color: #dc2626;
        font-family: 'JetBrains Mono', monospace;
    }
    .prediction-label {
        font-size: 0.78rem;
        color: #64748b;
        font-weight: 500;
    }

    /* ============================================================
       BUTTONS — Corporate, not neon
       ============================================================ */
    div.stButton > button {
        background: #1a1a2e;
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 6px;
        font-size: 0.9rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        letter-spacing: 0.5px;
        transition: all 0.2s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    }
    div.stButton > button:hover {
        background: #2d2d4e;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* ============================================================
       WORKFLOW SECTION
       ============================================================ */
    .workflow-success {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-left: 4px solid #22c55e;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
    }
    .workflow-info {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
    }

    /* ============================================================
       SCANNING STATUS — Simple, corporate
       ============================================================ */
    .scanning-text {
        text-align: center;
        font-size: 0.9rem;
        color: #64748b;
        font-weight: 500;
    }

    /* Progress bar */
    .stProgress > div > div > div > div {
        background: #1a1a2e !important;
        border-radius: 6px;
    }

    /* ============================================================
       LAYER STATUS — Simple corporate badges
       ============================================================ */
    .layer-pipeline {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0;
        margin: 1rem auto;
        padding: 0.8rem;
        max-width: 900px;
    }
    .layer-node {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
        padding: 8px 10px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        min-width: 90px;
    }
    .layer-node-icon { font-size: 1.1rem; }
    .layer-node-name {
        font-size: 0.6rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .layer-node-status {
        display: flex;
        align-items: center;
        gap: 4px;
        font-size: 0.55rem;
        color: #16a34a;
        font-weight: 600;
    }
    .layer-node-status .dot {
        width: 5px; height: 5px;
        border-radius: 50%;
        background: #22c55e;
        animation: dotPulse 2s ease-in-out infinite;
    }
    .layer-connector {
        width: 30px;
        height: 2px;
        background: linear-gradient(90deg, #cbd5e1, #94a3b8, #cbd5e1);
        flex-shrink: 0;
    }

    /* ============================================================
       LAYER INDICATOR (tab headers)
       ============================================================ */
    .layer-indicator {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 14px;
        border-radius: 4px;
        font-size: 0.7rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
        letter-spacing: 0.5px;
    }
    .layer-active {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #166534;
    }
    .status-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #22c55e;
        animation: dotPulse 2s ease-in-out infinite;
    }

    /* ============================================================
       ROOT CAUSE  — Clean
       ============================================================ */
    .root-cause-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .root-cause-header {
        font-size: 1rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* ============================================================
       DIVIDER — Simple
       ============================================================ */
    .custom-divider {
        height: 1px;
        background: #e2e8f0;
        margin: 1.5rem 0;
    }

    /* ============================================================
       NO ANOMALY BANNER
       ============================================================ */
    .no-anomaly-banner {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-radius: 8px;
        padding: 2rem;
        margin: 1.5rem auto;
        max-width: 700px;
        text-align: center;
    }
    .no-anomaly-banner .icon { font-size: 2rem; }
    .no-anomaly-banner .headline {
        font-size: 1.1rem;
        font-weight: 700;
        color: #166534;
        margin-top: 0.5rem;
    }
    .no-anomaly-banner .body {
        font-size: 0.85rem;
        color: #64748b;
        margin-top: 0.4rem;
        line-height: 1.6;
    }

    /* ============================================================
       REDIRECT PANELS — Clean corporate
       ============================================================ */
    .redirect-panel {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.2s ease;
        margin: 0.8rem 0;
    }
    .redirect-panel:hover {
        border-color: #94a3b8;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }
    .panel-icon {
        font-size: 2rem;
        margin-bottom: 0.8rem;
    }
    .panel-title {
        color: #0f172a;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    .panel-desc {
        color: #64748b;
        font-size: 0.85rem;
        line-height: 1.5;
    }

    /* ============================================================
       CHAT — Clean
       ============================================================ */
    .stChatMessage {
        background: #f8fafc !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
    }
    .stChatInput > div {
        border-color: #e2e8f0 !important;
        border-radius: 6px !important;
    }

    /* ============================================================
       FOOTER — Corporate minimal
       ============================================================ */
    .ai-footer {
        text-align: center;
        padding: 1rem;
        margin-top: 1rem;
    }
    .ai-footer-line {
        height: 1px;
        background: #e2e8f0;
        margin-bottom: 0.8rem;
    }
    .ai-footer-text {
        font-size: 0.7rem;
        color: #94a3b8;
        letter-spacing: 1px;
    }

    /* ============================================================
       WEIGHT BARS — Simple clean progress bars
       ============================================================ */
    .weight-container { margin: 0.6rem 0; }
    .weight-bar-bg {
        background: #f1f5f9;
        border: 1px solid #e2e8f0;
        border-radius: 4px;
        height: 28px;
        overflow: hidden;
    }
    .weight-bar-fill {
        height: 100%;
        border-radius: 4px;
        display: flex;
        align-items: center;
        padding-left: 10px;
        font-size: 0.72rem;
        font-weight: 700;
        color: white;
        font-family: 'JetBrains Mono', monospace;
    }

    /* ============================================================
       TABS — Clean corporate
       ============================================================ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: #f8fafc;
        padding: 4px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 6px;
        color: #64748b;
        font-weight: 600;
        font-size: 0.85rem;
        padding: 8px 16px;
        transition: all 0.2s ease;
        border: 1px solid transparent;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #0f172a;
        background: #ffffff;
    }
    .stTabs [aria-selected="true"] {
        background: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    }
</style>
"""
