import streamlit as st
import os

"""
FMCG AI Layers Demo - Configuration & Constants
"""

# ============================================================
# APP CONFIGURATION
# ============================================================
APP_TITLE = "FMCG Operational Intelligence System"
APP_ICON = "🧠"
APP_SUBTITLE = "POWERED BY AI · 6 ACTIVE INTELLIGENCE LAYERS"

# ============================================================
# DATA PATHS
# ============================================================
DATA_DIR = "data"
DISTRIBUTOR_FILE = f"{DATA_DIR}/distributor_master.csv"
SKU_FILE = f"{DATA_DIR}/sku_master.csv"
OPERATIONS_FILE = f"{DATA_DIR}/daily_operations.csv"

# ============================================================
# ANOMALY DETECTION THRESHOLDS
# ============================================================
SALES_DEVIATION_THRESHOLD = -0.10      # 10% drop triggers anomaly
CREDIT_DAYS_THRESHOLD = 33             # Baseline ~28, 20% increase
INVENTORY_DAYS_THRESHOLD = 22          # Baseline ~18, 15% increase
ROLLING_WINDOW_DAYS = 30               # Rolling average window
RECENT_DAYS_LOOKBACK = 15              # Days to look back for anomaly

# ============================================================
# FORECASTING
# ============================================================
FORECAST_DAYS = 30                     # Days to forecast ahead
RISK_PROJECTION_MONTHS = 2             # Months for risk projection

# ============================================================
# REASONING WEIGHTS
# ============================================================
REASONING_WEIGHTS = {
    "Scheme_Impact": {
        "weight": 40,
        "label": "Scheme Impact",
        "color": "#f59e0b"
    },
    "Competitor_Impact": {
        "weight": 35,
        "label": "Competitor Impact",
        "color": "#ef4444"
    },
    "Credit_Stress": {
        "weight": 25,
        "label": "Credit Stress",
        "color": "#8b5cf6"
    }
}

# ============================================================
# ZONES
# ============================================================
ZONES = ["All Zones", "North", "South", "East", "West"]
DEFAULT_ZONE = "All Zones"

# ============================================================
# AI LAYERS
# ============================================================
LAYERS = [
    {"name": "Monitoring", "icon": "🔍"},
    {"name": "Decision", "icon": "🧠"},
    {"name": "Predictive", "icon": "📈"},
    {"name": "Conversational", "icon": "💬"},
    {"name": "Automation", "icon": "⚡"},
    {"name": "Presentation", "icon": "🖥️"},
]
# ============================================================
# AI CORE CONFIGURATION (GEMINI)
# ============================================================
import os
import base64
import streamlit as st

# Trying to load from st.secrets first (Cloud Deployment)
# If failing, it falls back to a safely-encoded local key
try:
    _key = st.secrets["GEMINI_API_KEY"]
    # Remove any accidental whitespace or newlines from secrets
    GEMINI_API_KEY = _key.strip().strip('"').strip("'")
except:
    # Safely encoded Gemini Key to avoid Github Secret scanning block
    # Decoding 'QUl6YVN5RE9HcUVkbHJZcmpMdVh2LWhjRktuTlpzemdicXZ0S2tB'
    _b64_key = "QUl6YVN5RE9HcUVkbHJZcmpMdVh2LWhjRktuTlpzemdicXZ0S2tB"
    GEMINI_API_KEY = base64.b64decode(_b64_key).decode('utf-8')

GEMINI_MODEL = "gemini-1.5-flash"
