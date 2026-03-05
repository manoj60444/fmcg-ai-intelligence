"""
UI Styles – Premium AI-powered CSS for the FMCG Intelligence System.
Features: animated neural particles, glassmorphism, neon glow effects,
futuristic typography, cyber-grid backgrounds, and premium micro-animations.
"""

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ============================================================
       CORE APP & BACKGROUND
       ============================================================ */
    .stApp {
        background: #050510;
        font-family: 'Outfit', sans-serif;
        overflow-x: hidden;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ---------- Sidebar Styling ---------- */
    [data-testid="stSidebar"] {
        background: rgba(10, 10, 20, 0.95);
        border-right: 1px solid rgba(99, 102, 241, 0.2);
        backdrop-filter: blur(20px);
    }
    [data-testid="stSidebar"] .stSelectbox {
        margin-top: 2rem;
    }
    
    .nav-header {
        text-align: center;
        padding: 2rem 0;
        border-bottom: 1px solid rgba(99, 102, 241, 0.1);
        margin-bottom: 2rem;
    }
    .nav-item {
        padding: 12px 20px;
        margin: 8px 12px;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 12px;
        color: #94a3b8;
        font-weight: 500;
        text-decoration: none;
    }
    .nav-item:hover {
        background: rgba(99, 102, 241, 0.1);
        color: #a78bfa;
        transform: translateX(5px);
    }
    .nav-item-active {
        background: linear-gradient(90deg, rgba(99,102,241,0.2), transparent);
        border-left: 3px solid #6366f1;
        color: #e2e8f0;
    }

    /* Animated cyber-grid overlay */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background:
            linear-gradient(rgba(99,102,241,0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(99,102,241,0.03) 1px, transparent 1px);
        background-size: 60px 60px;
        pointer-events: none;
        z-index: 0;
        animation: gridPulse 8s ease-in-out infinite;
    }
    @keyframes gridPulse {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.7; }
    }

    /* ============================================================
       ANIMATED HEADER SECTION
       ============================================================ */
    .ai-header-container {
        position: relative;
        text-align: center;
        padding: 2.5rem 2rem 1.5rem;
        margin-bottom: 1rem;
        overflow: hidden;
    }
    .ai-header-container::before {
        content: '';
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: radial-gradient(ellipse at center, rgba(99,102,241,0.08) 0%, transparent 60%);
        animation: headerGlow 6s ease-in-out infinite;
        pointer-events: none;
    }
    @keyframes headerGlow {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 1; }
    }

    /* AI Badge */
    .ai-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(135deg, rgba(99,102,241,0.15), rgba(168,85,247,0.15));
        border: 1px solid rgba(139,92,246,0.3);
        border-radius: 50px;
        padding: 6px 18px;
        font-size: 0.7rem;
        font-weight: 600;
        color: #a78bfa;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
        animation: badgeFloat 3s ease-in-out infinite;
    }
    .ai-badge .pulse-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow: 0 0 8px rgba(34,197,94,0.8);
        animation: dotPulse 1.5s ease-in-out infinite;
    }
    @keyframes dotPulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.4); opacity: 0.6; }
    }
    @keyframes badgeFloat {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-3px); }
    }

    /* Main Title */
    .main-title {
        position: relative;
        text-align: center;
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(135deg, #818cf8 0%, #a78bfa 25%, #c084fc 50%, #e879f9 75%, #818cf8 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.3rem;
        letter-spacing: -1.5px;
        animation: titleShimmer 4s ease-in-out infinite;
        text-shadow: none;
    }
    @keyframes titleShimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .sub-title {
        text-align: center;
        font-size: 0.9rem;
        color: #64748b;
        margin-bottom: 0.5rem;
        font-weight: 400;
        letter-spacing: 4px;
        text-transform: uppercase;
    }

    /* Neural network line under header */
    .neural-line {
        width: 200px;
        height: 2px;
        margin: 1rem auto;
        background: linear-gradient(90deg, transparent, #6366f1, #a855f7, #6366f1, transparent);
        border-radius: 2px;
        animation: neuralPulse 3s ease-in-out infinite;
    }
    @keyframes neuralPulse {
        0%, 100% { opacity: 0.4; width: 200px; }
        50% { opacity: 1; width: 300px; }
    }

    /* ============================================================
       OVERVIEW KPI CARDS – Glassmorphism
       ============================================================ */
    .overview-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 1.5rem 0;
        flex-wrap: wrap;
        padding: 0 1rem;
    }
    .overview-card {
        position: relative;
        background: rgba(15, 18, 35, 0.6);
        border: 1px solid rgba(99,102,241,0.15);
        border-radius: 20px;
        padding: 1.4rem 1.8rem;
        text-align: center;
        min-width: 170px;
        flex: 1;
        max-width: 220px;
        backdrop-filter: blur(20px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        overflow: hidden;
    }
    .overview-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(135deg, rgba(99,102,241,0.05), transparent);
        border-radius: 20px;
        pointer-events: none;
    }
    .overview-card::after {
        content: '';
        position: absolute;
        top: -1px; left: -1px;
        right: -1px; bottom: -1px;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(99,102,241,0.3), transparent, rgba(168,85,247,0.3));
        z-index: -1;
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    .overview-card:hover {
        transform: translateY(-6px);
        border-color: rgba(139,92,246,0.4);
        box-shadow:
            0 12px 40px rgba(99,102,241,0.2),
            0 0 30px rgba(139,92,246,0.1),
            inset 0 1px 0 rgba(255,255,255,0.05);
    }
    .overview-card:hover::after { opacity: 1; }
    
    .overview-icon {
        font-size: 1.4rem;
        margin-bottom: 0.3rem;
        filter: drop-shadow(0 0 8px rgba(139,92,246,0.5));
    }
    .overview-number {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #c084fc, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
    }
    .overview-label {
        font-size: 0.72rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 6px;
        font-weight: 500;
    }

    /* ============================================================
       AI LAYER STATUS PIPELINE
       ============================================================ */
    .layer-pipeline {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0;
        margin: 1.5rem auto;
        padding: 1rem;
        max-width: 900px;
        flex-wrap: wrap;
    }
    .layer-node {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 6px;
        padding: 10px 14px;
        background: rgba(15,18,35,0.7);
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 14px;
        min-width: 110px;
        transition: all 0.3s ease;
        position: relative;
        cursor: default;
    }
    .layer-node:hover {
        border-color: rgba(139,92,246,0.5);
        background: rgba(99,102,241,0.08);
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(99,102,241,0.15);
    }
    .layer-node-icon { font-size: 1.3rem; }
    .layer-node-name {
        font-size: 0.65rem;
        color: #94a3b8;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .layer-node-status {
        display: flex;
        align-items: center;
        gap: 4px;
        font-size: 0.6rem;
        color: #4ade80;
        font-weight: 600;
    }
    .layer-node-status .dot {
        width: 5px; height: 5px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow: 0 0 6px rgba(34,197,94,0.8);
        animation: dotPulse 2s ease-in-out infinite;
    }
    .layer-connector {
        width: 30px;
        height: 2px;
        background: linear-gradient(90deg, rgba(99,102,241,0.4), rgba(168,85,247,0.4));
        position: relative;
        flex-shrink: 0;
    }
    .layer-connector::after {
        content: '';
        position: absolute;
        right: -3px; top: -3px;
        width: 8px; height: 8px;
        border-top: 2px solid rgba(139,92,246,0.5);
        border-right: 2px solid rgba(139,92,246,0.5);
        transform: rotate(45deg);
    }

    /* ============================================================
       ALERT CARD – cyberpunk style
       ============================================================ */
    .alert-card {
        position: relative;
        background: rgba(239,68,68,0.04);
        border: 1px solid rgba(239,68,68,0.2);
        border-radius: 20px;
        padding: 1.8rem 2rem;
        margin: 1.5rem auto;
        max-width: 850px;
        overflow: hidden;
        animation: alertSlideIn 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(15px);
    }
    @keyframes alertSlideIn {
        0% { opacity: 0; transform: translateY(20px) scale(0.98); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    .alert-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 3px; height: 100%;
        background: linear-gradient(180deg, #ef4444, #f97316, #ef4444);
        animation: alertBarPulse 2s ease-in-out infinite;
    }
    @keyframes alertBarPulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    .alert-card::after {
        content: '';
        position: absolute;
        top: -50%; right: -20%;
        width: 60%; height: 200%;
        background: radial-gradient(ellipse, rgba(239,68,68,0.05), transparent 70%);
        pointer-events: none;
    }

    .alert-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 1rem;
    }
    .alert-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: linear-gradient(135deg, #dc2626, #ef4444);
        color: white;
        padding: 5px 14px;
        border-radius: 30px;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        animation: alertBlink 2s ease-in-out infinite;
        box-shadow: 0 0 20px rgba(239,68,68,0.3);
    }
    @keyframes alertBlink {
        0%, 100% { opacity: 1; box-shadow: 0 0 20px rgba(239,68,68,0.3); }
        50% { opacity: 0.8; box-shadow: 0 0 30px rgba(239,68,68,0.5); }
    }
    .alert-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #fca5a5;
        letter-spacing: -0.3px;
    }
    .alert-details {
        display: flex;
        gap: 1.2rem;
        margin-top: 1.2rem;
        flex-wrap: wrap;
    }
    .alert-metric {
        text-align: center;
        background: rgba(239,68,68,0.06);
        border: 1px solid rgba(239,68,68,0.12);
        border-radius: 14px;
        padding: 0.8rem 1.2rem;
        min-width: 130px;
        flex: 1;
        transition: all 0.3s ease;
    }
    .alert-metric:hover {
        background: rgba(239,68,68,0.1);
        border-color: rgba(239,68,68,0.3);
        transform: translateY(-2px);
    }
    .alert-metric-value {
        font-size: 1.5rem;
        font-weight: 800;
        color: #f87171;
        font-family: 'JetBrains Mono', monospace;
    }
    .alert-metric-label {
        font-size: 0.7rem;
        color: #fca5a5;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 4px;
        font-weight: 500;
    }

    /* ============================================================
       TABS – glowing neon style
       ============================================================ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: rgba(10, 12, 25, 0.7);
        padding: 6px;
        border-radius: 16px;
        border: 1px solid rgba(99,102,241,0.1);
        backdrop-filter: blur(10px);
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        color: #64748b;
        font-weight: 600;
        font-size: 0.85rem;
        padding: 10px 20px;
        transition: all 0.3s ease;
        border: 1px solid transparent;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #a78bfa;
        background: rgba(99,102,241,0.05);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(168,85,247,0.2)) !important;
        color: #c4b5fd !important;
        border: 1px solid rgba(139,92,246,0.3) !important;
        box-shadow: 0 0 20px rgba(99,102,241,0.15);
    }

    /* ============================================================
       ROOT CAUSE SECTION
       ============================================================ */
    .root-cause-card {
        background: rgba(15,18,35,0.6);
        border: 1px solid rgba(251,191,36,0.2);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(15px);
        position: relative;
        overflow: hidden;
    }
    .root-cause-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, #fbbf24, transparent);
    }
    .root-cause-header {
        font-size: 1.15rem;
        font-weight: 700;
        color: #fbbf24;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* ============================================================
       BUTTONS – neon glow
       ============================================================ */
    div.stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7);
        color: white;
        border: none;
        padding: 1rem 3rem;
        border-radius: 14px;
        font-size: 1rem;
        font-weight: 700;
        font-family: 'Outfit', sans-serif;
        letter-spacing: 1px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow:
            0 4px 15px rgba(99,102,241,0.4),
            0 0 30px rgba(139,92,246,0.15);
        position: relative;
        overflow: hidden;
    }
    div.stButton > button::before {
        content: '';
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.6s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow:
            0 8px 30px rgba(99,102,241,0.5),
            0 0 50px rgba(139,92,246,0.2);
    }
    div.stButton > button:hover::before {
        left: 150%;
    }

    /* ============================================================
       WEIGHT BARS – animated gradient
       ============================================================ */
    .weight-container { margin: 0.8rem 0; }
    .weight-bar-bg {
        background: rgba(15,18,35,0.8);
        border: 1px solid rgba(99,102,241,0.08);
        border-radius: 10px;
        height: 32px;
        overflow: hidden;
    }
    .weight-bar-fill {
        height: 100%;
        border-radius: 10px;
        display: flex;
        align-items: center;
        padding-left: 12px;
        font-size: 0.75rem;
        font-weight: 700;
        color: white;
        font-family: 'JetBrains Mono', monospace;
        animation: barFillIn 1.2s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    .weight-bar-fill::after {
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
        animation: barShine 3s ease-in-out infinite;
    }
    @keyframes barFillIn {
        0% { width: 0 !important; opacity: 0; }
        100% { opacity: 1; }
    }
    @keyframes barShine {
        0% { left: -100%; }
        100% { left: 200%; }
    }

    /* ============================================================
       PREDICTION CARDS
       ============================================================ */
    .prediction-card {
        background: rgba(15,18,35,0.6);
        border: 1px solid rgba(239,68,68,0.15);
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        margin: 0.5rem 0;
        backdrop-filter: blur(15px);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .prediction-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, #ef4444, transparent);
        opacity: 0.5;
    }
    .prediction-card:hover {
        border-color: rgba(239,68,68,0.3);
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(239,68,68,0.1);
    }
    .prediction-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #f87171;
        font-family: 'JetBrains Mono', monospace;
    }
    .prediction-label {
        font-size: 0.78rem;
        color: #94a3b8;
        font-weight: 500;
    }

    /* ============================================================
       CHAT
       ============================================================ */
    .stChatMessage {
        background: rgba(15,18,35,0.5) !important;
        border: 1px solid rgba(99,102,241,0.12) !important;
        border-radius: 16px !important;
        backdrop-filter: blur(10px);
    }
    .stChatInput > div {
        border-color: rgba(99,102,241,0.2) !important;
        border-radius: 14px !important;
    }

    /* ============================================================
       SCANNING STATUS
       ============================================================ */
    .scanning-text {
        text-align: center;
        font-size: 1rem;
        color: #a78bfa;
        font-weight: 500;
        animation: scanPulse 1.5s ease-in-out infinite;
    }
    @keyframes scanPulse {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 1; }
    }

    /* Progress bar custom */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899) !important;
        border-radius: 10px;
    }

    /* ============================================================
       LAYER INDICATOR (in tabs)
       ============================================================ */
    .layer-indicator {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 0.72rem;
        font-weight: 600;
        margin-bottom: 1rem;
        letter-spacing: 0.5px;
    }
    .layer-active {
        background: rgba(34,197,94,0.08);
        border: 1px solid rgba(34,197,94,0.25);
        color: #4ade80;
    }
    .status-dot {
        width: 7px; height: 7px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow: 0 0 8px rgba(34,197,94,0.8);
        animation: dotPulse 2s ease-in-out infinite;
    }

    /* ============================================================
       DIVIDER – animated gradient line
       ============================================================ */
    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(99,102,241,0.25), rgba(168,85,247,0.25), transparent);
        margin: 2rem 0;
        position: relative;
    }

    /* ============================================================
       NO-ANOMALY BANNER
       ============================================================ */
    .no-anomaly-banner {
        background: rgba(34,197,94,0.05);
        border: 1px solid rgba(34,197,94,0.2);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem auto;
        max-width: 700px;
        text-align: center;
        backdrop-filter: blur(15px);
        position: relative;
        overflow: hidden;
    }
    .no-anomaly-banner::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, #22c55e, transparent);
    }
    .no-anomaly-banner .icon { font-size: 2.5rem; }
    .no-anomaly-banner .headline {
        font-size: 1.3rem;
        font-weight: 700;
        color: #4ade80;
        margin-top: 0.5rem;
    }
    .no-anomaly-banner .body {
        font-size: 0.9rem;
        color: #64748b;
        margin-top: 0.5rem;
    }

    /* ============================================================
       PREMIUM AI BACKGROUND & GRID
       ============================================================ */
    .stApp {
        background-color: #03030b;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(99, 102, 241, 0.05) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, rgba(168, 85, 247, 0.05) 0%, transparent 40%),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        font-family: 'Outfit', sans-serif;
        overflow-x: hidden;
    }

    /* Neural Network Background Pattern */
    .stApp::after {
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background-image: url('https://user-images.githubusercontent.com/11252171/200147913-c977926b-d336-417c-a4d1-8d26f634dba9.png');
        background-size: cover;
        opacity: 0.03;
        pointer-events: none;
        z-index: -1;
    }

    /* ---------- Sidebar: AI Command Center ---------- */
    [data-testid="stSidebar"] {
        background: rgba(10, 10, 20, 0.9);
        border-right: 1px solid rgba(99, 102, 241, 0.15);
        backdrop-filter: blur(25px);
        box-shadow: 10px 0 30px rgba(0,0,0,0.5);
    }
    
    .nav-item {
        margin: 10px 15px;
        padding: 15px;
        border-radius: 15px;
        background: rgba(30, 41, 59, 0.3);
        border: 1px solid rgba(99, 102, 241, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        align-items: center;
        gap: 15px;
        color: #94a3b8;
    }
    .nav-item:hover {
        background: rgba(99, 102, 241, 0.1);
        border-color: #6366f1;
        color: #e2e8f0;
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.2);
    }

    /* ---------- Premium Cards: Glass & Glow ---------- */
    .overview-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 24px;
        padding: 2rem;
        backdrop-filter: blur(20px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    .overview-card::before {
        content: "";
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: conic-gradient(transparent, rgba(99, 102, 241, 0.2), transparent 30%);
        animation: rotate 6s linear infinite;
        pointer-events: none;
    }
    @keyframes rotate {
        100% { transform: rotate(360deg); }
    }
    
    .overview-number {
        font-family: 'JetBrains Mono', monospace;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #fff 0%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* ---------- Alerts: High-Impact ---------- */
    .alert-card {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.08), rgba(0, 0, 0, 0.4));
        border: 2px solid rgba(239, 68, 68, 0.4);
        box-shadow: 0 0 30px rgba(239, 68, 68, 0.15);
    }
    .alert-badge {
        background: #ef4444;
        box-shadow: 0 0 15px #ef4444;
    }

    /* Custom Animation for Redirection */
    .redirect-click {
        animation: pulseEffect 0.5s ease;
    }
    @keyframes pulseEffect {
        0% { transform: scale(1); }
        50% { transform: scale(0.95); opacity: 0.8; }
        100% { transform: scale(1); }
    }
</style>
"""
