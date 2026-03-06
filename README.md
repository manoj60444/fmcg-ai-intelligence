# FMCG Operational Intelligence Engine

This repository contains the **FMCG Operational Intelligence Engine**, a high-end AI-driven system for monitoring, predicting, and automating responses to supply chain and distribution anomalies.

---

## 🛠 Prerequisites & Setup

### 1. API Credentials & Configuration
The system requires a Google Gemini API key for the **Conversational Intelligence** and **Root Cause Explanation** layers. 

> [!IMPORTANT]
> To keep the system secure, provide your API key via **Streamlit Secrets** or an environment variable.

**How to add your key:**
1. **Local Development**: Create a `.streamlit/secrets.toml` file in the root directory and add:
   ```toml
   GEMINI_API_KEY = "AIzaSy... (your key)"
   ```
2. **Cloud Deployment**: Go to your Streamlit Cloud dashboard → **Settings** → **Secrets** and add the key there.

---

### 2. Dependencies
To run the server, install the following packages:

```bash
# Install all required packages
pip install -r requirements.txt
```

**Core Packages:**
* `streamlit`: Main application framework.
* `pandas`: Data processing and manipulation.
* `numpy`: Mathematical operations.
* `plotly`: High-end interactive data visualizations.
* `streamlit-option-menu`: Custom sidebar navigation.

---

### 3. Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/manoj60444/fmcg-ai-intelligence.git
   cd fmcg-ai-intelligence
   ```

2. **Generate Mock Data:**
   The application requires a base dataset. Run the data generation script before starting:
   ```bash
   python generate_data.py
   ```

3. **Run the Application:**
   Execute the Streamlit server:
   ```bash
   streamlit run app.py
   ```

---

## 🚀 Key Modules & Architecture

* **Dashboard Layer**: Global distribution overview.
* **Analytics Layer**: Real-time behaviour scan for anomalies.
* **Prediction Layer**: AI-driven risk forecasting (unlocked after scan).
* **Automation Layer**: Workflow trigger system (unlocked after prediction).
* **Intelligence Layer**: Neural chat interface for deep insights.

---

## ⚙️ Configuration Details

| Resource | Value |
| --- | --- |
| **Model** | GPT-4o / GPT-4 (Recommended) |
| **Language** | Python 3.10+ |
| **Theme** | Custom Deep Obsidian (UI/Styles.py) |
| **Port** | 8501 (Default) |

---
*Created by the FMCG AI Development Team.*
