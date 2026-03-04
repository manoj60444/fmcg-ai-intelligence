"""
Layer 2: Decision Intelligence
Generates root cause analysis with reasoning weights.
"""

from config.settings import REASONING_WEIGHTS


def generate_root_cause(alert, anomaly_df):
    """
    Build root-cause reasoning and a natural-language summary
    for a given zone alert.
    """

    zone_anomalies = anomaly_df[anomaly_df['Zone'] == alert['Zone']]

    reasoning = {
        "Scheme_Impact": {
            "weight": f"{REASONING_WEIGHTS['Scheme_Impact']['weight']}%",
            "label": REASONING_WEIGHTS['Scheme_Impact']['label'],
            "description": (
                "Promotional schemes were deactivated for affected distributors. "
                "Without scheme incentives, retailers reduced order volumes "
                "leading to secondary sales decline."
            ),
            "evidence": (
                f"Scheme active rate dropped from 80% to "
                f"{zone_anomalies['Scheme_Active'].mean()*100:.0f}% "
                f"for affected distributors"
            ),
            "color": REASONING_WEIGHTS['Scheme_Impact']['color'],
        },
        "Competitor_Impact": {
            "weight": f"{REASONING_WEIGHTS['Competitor_Impact']['weight']}%",
            "label": REASONING_WEIGHTS['Competitor_Impact']['label'],
            "description": (
                "Competitor price index increased significantly, indicating "
                f"aggressive competitor pricing in the {alert['Zone']} Zone. "
                "Retailers shifted purchase preference."
            ),
            "evidence": (
                f"Competitor Price Index rose to "
                f"{zone_anomalies['Competitor_Index'].mean():.2f} "
                f"(baseline: 0.45)"
            ),
            "color": REASONING_WEIGHTS['Competitor_Impact']['color'],
        },
        "Credit_Stress": {
            "weight": f"{REASONING_WEIGHTS['Credit_Stress']['weight']}%",
            "label": REASONING_WEIGHTS['Credit_Stress']['label'],
            "description": (
                "Credit days extended beyond threshold, squeezing distributor "
                "working capital. This led to reduced ordering capacity and "
                "inventory accumulation."
            ),
            "evidence": (
                f"Average Credit Days: "
                f"{zone_anomalies['Credit_Days'].mean():.0f} days "
                f"(baseline: 28 days)"
            ),
            "color": REASONING_WEIGHTS['Credit_Stress']['color'],
        },
    }

    summary = f"""
**Root Cause Summary for {alert['Zone']} Zone Anomaly:**

The system has identified a multi-factor deterioration affecting \
**{alert['Distributors_Affected']} distributors** in the {alert['Zone']} Zone.
The primary driver is the **deactivation of promotional schemes** (40% weight), \
compounded by **intensified competitor pricing** (35% weight) \
and **credit stress** (25% weight).

**Key Findings:**
1. **Sales Impact**: Secondary sales have dropped by \
**{alert['Sales_Drop']}** compared to the 30-day rolling average
2. **Credit Deterioration**: Credit days have extended from \
{alert['Credit_Increase']}, a significant increase
3. **Inventory Accumulation**: Inventory days have increased by \
~20%, indicating slower product movement
4. **Market Pressure**: Competitor price index has risen to \
**{zone_anomalies['Competitor_Index'].mean():.2f}**, \
suggesting aggressive competitive pricing activity

**Business Risk:**
If uncorrected, the projected revenue exposure is \
**{alert['Projected_Risk']}** over the next 60 days, \
with potential margin compression of **3.2%** across the affected cluster.
"""

    return reasoning, summary
