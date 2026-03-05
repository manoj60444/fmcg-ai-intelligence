"""
Professional FMCG AI Dashboard - Custom CSS System
==================================================
Senior Front-End Style: Glassmorphism, Inter Font, Subtle Gradients.
"""

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Global Transitions & Typography */
    * { transition: all 0.2s ease-in-out; }
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #F8FAFC 0%, #F1F5F9 100%);
        font-family: 'Inter', sans-serif;
        color: #0F172A;
    }

    /* Remove Streamlit Defaults */
    header, footer, #MainMenu { visibility: hidden; }
    .stDeployButton { display: none; }

    /* Centered Header & Premium Spacing */
    .main-header {
        text-align: center;
        padding: 3rem 0;
        letter-spacing: -0.05em;
    }
    .main-header h1 {
        font-weight: 300;
        font-size: 2.8rem;
        color: #0F172A;
        margin-bottom: 0.5rem;
    }
    .main-header p {
        font-weight: 400;
        font-size: 1.1rem;
        color: #64748B;
        opacity: 0.8;
    }

    /* Glassmorphism KPI Cards */
    .kpi-container {
        display: flex;
        justify-content: space-between;
        gap: 1.5rem;
        margin-bottom: 3rem;
    }
    
    .kpi-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 20px;
        padding: 1.5rem;
        flex: 1;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .kpi-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        background: rgba(255, 255, 255, 0.9);
    }
    
    .kpi-icon {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: #10B981;
    }
    .kpi-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .kpi-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        margin: 0.2rem 0;
    }
    .kpi-change {
        font-size: 0.85rem;
        font-weight: 700;
    }
    .change-up { color: #10B981; }
    .change-down { color: #EF4444; }

    /* Side-bar Overhaul */
    [data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid #1E293B;
    }
    [data-testid="stSidebar"] section {
        padding-top: 2rem;
    }

    /* Sentiment Feed */
    .sentiment-container {
        max-height: 400px;
        overflow-y: auto;
        padding-right: 10px;
    }
    .sentiment-item {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid #E2E8F0;
        display: flex;
        gap: 1rem;
        align-items: center;
    }
    .sentiment-item:hover {
        border-color: #10B981;
    }
    .status-dot {
        height: 10px;
        width: 10px;
        border-radius: 50%;
        display: inline-block;
    }
    .dot-optimal { background: #10B981; box-shadow: 0 0 8px #10B981; }
    .dot-warning { background: #FBBF24; box-shadow: 0 0 8px #FBBF24; }
    .dot-risk { background: #EF4444; box-shadow: 0 0 8px #EF4444; }

    /* Buttons */
    .stButton > button {
        border-radius: 20px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        border: none !important;
        background: #0F172A !important;
        color: white !important;
        box-shadow: 0 4px 6px rgba(15, 23, 42, 0.2) !important;
    }
    .stButton > button:hover {
        background: #1E293B !important;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px rgba(15, 23, 42, 0.1) !important;
    }

    /* Dataframe padding */
    .dataframe-container {
        padding: 1rem;
        background: white;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
    }

    /* Sidebar option menu custom hover */
    .nav-link:hover {
        background: rgba(255,255,255,0.05) !important;
    }
</style>
"""
