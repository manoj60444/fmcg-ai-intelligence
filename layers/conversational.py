"""
Layer 4: Conversational AI
Provides pre-built intelligent responses for the demo chat interface.
Dynamically generates responses based on the active zone alert.
"""


def get_demo_responses(alert, ops_count):
    """
    Return a dict of keyword-pattern → response for the chat layer.
    Responses are dynamically filled with alert-specific data.
    """

    zone = alert['Zone']

    responses = {
        "why is {zone} zone performance dropping": f"""
**{zone} Zone Performance Analysis:**

The {zone} Zone is experiencing a multi-factor performance decline driven by three interconnected causes:

1. **Scheme Deactivation (40% Impact)**
   - Promotional schemes were deactivated for {alert['Distributors_Affected']} \
distributors starting approximately 30 days ago
   - Without trade incentives, retailer ordering frequency has dropped by ~18%
   - This directly impacted secondary sales by {alert['Sales_Drop']}

2. **Competitive Pressure (35% Impact)**
   - Competitor price index has risen significantly (up from baseline 0.45)
   - Competitors appear to be running aggressive pricing campaigns in the \
{zone} Zone markets
   - Estimated market share erosion: 4-6% in affected territories

3. **Credit Stress (25% Impact)**
   - Average credit days extended from {alert['Credit_Increase']}
   - Working capital squeeze is limiting distributor buying capacity
   - {alert['Distributors_Affected']} distributors are now in the \
"high credit risk" category

**Confidence Level:** {alert['Confidence']}
**Data Points Analyzed:** {ops_count:,}
""",
        "what happens if no action is taken": f"""
**Projected Impact (If No Corrective Action):**

Based on current trend analysis and historical pattern matching:

📉 **30-Day Projection:**
- Revenue decline will accelerate to **18-22%** from current {alert['Sales_Drop']}
- Additional **3 distributors** will likely enter the anomaly zone
- Credit days could extend to **42-45 days** for worst-affected distributors

📉 **60-Day Projection:**
- Projected total revenue loss: **{alert['Projected_Risk']}**
- Margin compression: **3.2%** across {zone} Zone
- Risk of **2 distributor exits** (churn risk above 70%)
- Competitor market share gain: estimated **6-8%**

📉 **90-Day Worst Case:**
- Revenue impact could reach **₹75 Lakhs**
- Permanent loss of **4-5 retail coverage points**
- Recovery timeline extends to **120+ days**

⚠️ **Critical Threshold:** If credit days cross 45 days for any distributor, \
automated credit freeze triggers.
""",
        "what corrective action do you recommend": f"""
**Recommended Corrective Actions (Priority Order):**

🔴 **IMMEDIATE (Week 1-2):**
1. **Reactivate Schemes** – Apply 15% trade discount on top 10 SKUs for \
affected distributors
   - Expected impact: +8% sales recovery within 2 weeks
   - Cost: ₹3.5 Lakhs

2. **Field Force Deployment** – Deploy 5 additional sales reps to {zone} Zone
   - Focus: Top 8 affected territories
   - Expected impact: +5% coverage improvement

🟡 **SHORT-TERM (Week 3-4):**
3. **Volume Incentive Program** – Buy 10 Get 1 Free for retailers
   - Expected impact: +12% order volume
   - Investment: ₹5 Lakhs

4. **Credit Restructuring** – Offer 45-day credit with 2% early payment discount
   - Expected impact: Reduce average credit days by 8 days

🟢 **MEDIUM-TERM (Month 2):**
5. **Competitive Pricing Review** – Adjust MRP for 5 price-sensitive SKUs
   - Expected impact: Neutralize competitor pricing advantage

6. **Distributor Loyalty Program** – Quarterly performance bonuses
   - Expected impact: Long-term churn reduction

**Total Investment Required:** ₹12.5 Lakhs
**Expected Recovery:** Full baseline recovery in 45-60 days
**ROI:** Prevents {alert['Projected_Risk']} loss = **3.4x return**
""",
    }

    # Normalise keys to lowercase
    return {k.format(zone=zone.lower()): v for k, v in responses.items()}


def match_response(user_input, demo_responses, alert):
    """
    Try to match user_input against known demo responses.
    Returns the best matching response or a generic fallback.
    """

    user_lower = user_input.lower()

    for key, response in demo_responses.items():
        keywords = key.split()
        match_count = sum(1 for kw in keywords if kw in user_lower)
        if match_count >= 3:
            return response

    # Fallback
    return f"""
**Analysis Based on Current Data:**

Based on the detected anomaly in the {alert['Zone']} Zone affecting \
{alert['Distributors_Affected']} distributors:

The system has identified a **{alert['Sales_Drop']} sales decline** with \
credit days extending from {alert['Credit_Increase']}.
The projected risk stands at **{alert['Projected_Risk']}** with \
{alert['Confidence']} confidence.

Key factors driving this situation include scheme deactivation, competitive \
pressure, and credit stress.

*For more specific analysis, try asking:*
- "Why is {alert['Zone']} Zone performance dropping?"
- "What happens if no action is taken?"
- "What corrective action do you recommend?"

💡 *Tip: Connect OpenAI API for deeper, context-aware responses.*
"""
