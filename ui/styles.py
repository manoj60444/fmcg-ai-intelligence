"""
UI Styles – CSS for the FMCG demo.
"""

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #0d1b2a 50%, #1b2838 100%);
        font-family: 'Inter', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ---------- Title ---------- */
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7, #d946ef);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        letter-spacing: -1px;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #94a3b8;
        margin-bottom: 2rem;
        font-weight: 300;
        letter-spacing: 2px;
    }

    /* ---------- Overview Cards ---------- */
    .overview-container {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin: 1.5rem 0;
        flex-wrap: wrap;
    }
    .overview-card {
        background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(139,92,246,0.05));
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 16px;
        padding: 1.2rem 2rem;
        text-align: center;
        min-width: 180px;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    .overview-card:hover {
        border-color: rgba(139,92,246,0.5);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(99,102,241,0.15);
    }
    .overview-number {
        font-size: 2rem;
        font-weight: 700;
        color: #a78bfa;
    }
    .overview-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 4px;
    }

    /* ---------- Alert Card ---------- */
    .alert-card {
        background: linear-gradient(135deg, rgba(239,68,68,0.15), rgba(220,38,38,0.08));
        border: 1px solid rgba(239,68,68,0.4);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 1.5rem auto;
        max-width: 800px;
        position: relative;
        overflow: hidden;
        animation: alertPulse 2s ease-in-out;
    }
    @keyframes alertPulse {
        0% { opacity: 0; transform: scale(0.95); }
        50% { opacity: 0.8; }
        100% { opacity: 1; transform: scale(1); }
    }
    .alert-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 4px; height: 100%;
        background: linear-gradient(180deg, #ef4444, #dc2626);
    }
    .alert-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 0.8rem;
    }
    .alert-badge {
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        animation: blink 1.5s ease-in-out infinite;
    }
    @keyframes blink {
        0%,100% { opacity: 1; }
        50% { opacity: 0.6; }
    }
    .alert-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #fca5a5;
    }
    .alert-details {
        display: flex;
        gap: 2rem;
        margin-top: 1rem;
        flex-wrap: wrap;
    }
    .alert-metric { text-align: center; }
    .alert-metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #f87171;
    }
    .alert-metric-label {
        font-size: 0.8rem;
        color: #fca5a5;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* ---------- Tabs ---------- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(15,23,42,0.5);
        padding: 8px;
        border-radius: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        background: rgba(30,41,59,0.5);
        border-radius: 8px;
        color: #94a3b8;
        font-weight: 500;
        padding: 8px 20px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: white !important;
    }

    /* ---------- Root-cause ---------- */
    .root-cause-card {
        background: linear-gradient(135deg, rgba(251,191,36,0.1), rgba(245,158,11,0.05));
        border: 1px solid rgba(251,191,36,0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .root-cause-header {
        font-size: 1.2rem;
        font-weight: 700;
        color: #fbbf24;
        margin-bottom: 1rem;
    }

    /* ---------- Buttons ---------- */
    div.stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        border: none;
        padding: 1rem 3rem;
        border-radius: 12px;
        font-size: 1.1rem;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99,102,241,0.4);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(99,102,241,0.5);
    }

    /* ---------- Chat ---------- */
    .stChatMessage {
        background: rgba(15,23,42,0.5) !important;
        border: 1px solid rgba(99,102,241,0.15);
        border-radius: 12px !important;
    }

    /* ---------- Scanning ---------- */
    .scanning-text {
        text-align: center;
        font-size: 1.1rem;
        color: #a78bfa;
        animation: fadeInOut 1.5s ease-in-out infinite;
    }
    @keyframes fadeInOut {
        0%,100% { opacity: 0.4; }
        50% { opacity: 1; }
    }

    /* ---------- Weight bars ---------- */
    .weight-container { margin: 0.5rem 0; }
    .weight-bar-bg {
        background: rgba(30,41,59,0.8);
        border-radius: 8px;
        height: 28px;
        overflow: hidden;
    }
    .weight-bar-fill {
        height: 100%;
        border-radius: 8px;
        display: flex;
        align-items: center;
        padding-left: 10px;
        font-size: 0.8rem;
        font-weight: 600;
        color: white;
        transition: width 1s ease;
    }

    /* ---------- Prediction cards ---------- */
    .prediction-card {
        background: linear-gradient(135deg, rgba(239,68,68,0.08), rgba(239,68,68,0.03));
        border: 1px solid rgba(239,68,68,0.25);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
    }
    .prediction-value {
        font-size: 1.6rem;
        font-weight: 700;
        color: #f87171;
    }
    .prediction-label {
        font-size: 0.85rem;
        color: #fca5a5;
    }

    /* ---------- Layer indicator ---------- */
    .layer-indicator {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .layer-active {
        background: rgba(34,197,94,0.15);
        border: 1px solid rgba(34,197,94,0.4);
        color: #4ade80;
    }
    .status-dot {
        width: 8px; height: 8px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow: 0 0 6px rgba(34,197,94,0.6);
    }

    /* ---------- Divider ---------- */
    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(99,102,241,0.3), transparent);
        margin: 2rem 0;
    }

    /* ---------- No-anomaly banner ---------- */
    .no-anomaly-banner {
        background: linear-gradient(135deg, rgba(34,197,94,0.12), rgba(34,197,94,0.04));
        border: 1px solid rgba(34,197,94,0.35);
        border-radius: 14px;
        padding: 1.5rem 2rem;
        margin: 1.5rem auto;
        max-width: 700px;
        text-align: center;
    }
    .no-anomaly-banner .icon { font-size: 2.4rem; }
    .no-anomaly-banner .headline {
        font-size: 1.25rem;
        font-weight: 700;
        color: #4ade80;
        margin-top: 0.5rem;
    }
    .no-anomaly-banner .body {
        font-size: 0.95rem;
        color: #94a3b8;
        margin-top: 0.3rem;
    }

    /* ---------- Zone selector ---------- */
    div[data-testid="stSelectbox"] label {
        color: #a78bfa !important;
        font-weight: 600 !important;
    }
</style>
"""
