"""
Layer 5: Automation Layer
Generates corrective-action drafts (emails, proposals, warnings).
"""


def generate_workflow_actions(alert):
    """Return a dict of workflow action drafts keyed by action type."""

    zone = alert['Zone']
    affected = alert['Distributors_Affected']
    drop = alert['Sales_Drop']
    credit = alert['Credit_Increase']
    risk = alert['Projected_Risk']
    cluster = alert['Cluster']

    return {
        "email_regional_manager": {
            "title": "📧 Automated Auditor Notice: Regional Director",
            "type": "Escalation Draft",
            "content": f"""
**To:** Regional Director – {zone} Operations
**Subject:** FINANCIAL RISK ESCALATION: Unmitigated Performance Anomaly – {cluster}

Dear Regional Manager,

Our AI monitoring system has detected a significant performance \
deterioration in the {zone} Zone affecting {affected} distributors.

**Key Metrics:**
• Sales decline: {drop} below 30-day rolling average
• Credit days: Increased from {credit}
• Projected revenue risk: {risk} over 60 days

**Immediate Attention Required:**
1. Schedule review meeting with affected distributors within 48 hours
2. Review competitor pricing strategy in the {zone} Zone
3. Evaluate scheme reactivation feasibility

The system has generated a corrective action plan (attached) for your review.

Best regards,
FMCG Intelligence System
""",
        },
        "scheme_proposal": {
            "title": "📋 Financial Mitigation Proposal",
            "type": "System-Generated Strategy",
            "content": f"""
**CAPITAL & REVENUE MITIGATION STRATEGY**
**Zone:** {zone} | **Cluster:** {cluster}

**Background:**
{affected} distributors showing declining secondary sales ({drop}) \
coinciding with scheme deactivation.

**Proposal:**
1. **Immediate** (Week 1-2): Reactivate 15% trade discount for top 10 \
affected SKUs
2. **Short-term** (Week 3-4): Launch volume-based incentive program \
(Buy 10 Get 1 Free)
3. **Medium-term** (Month 2): Implement competitive pricing adjustment \
on key categories

**Expected Impact:**
• Sales recovery: 8-12% within 30 days
• Full recovery to baseline: 45-60 days
• Investment required: ₹8.5 Lakhs
• ROI: Prevents {risk.replace('₹', '₹')} loss

**Approval Required From:** VP Sales & Marketing
""",
        },
        "credit_warning": {
            "title": "⚠️ Working Capital Exposure Alert",
            "type": "Risk Control Protocol",
            "content": f"""
**CREDIT & WORKING CAPITAL ALERT**
**Control Zone:** {zone} | **Exposure Priority:** CRITICAL

**Summary:**
Credit days for {affected} distributors have increased from {credit}.

**Risk Assessment:**
• Outstanding exposure has increased by approximately 35%
• Working capital impact: Negative
• Projected bad debt risk if uncorrected: Medium-High

**Recommended Actions:**
1. Freeze further credit extension for affected distributors
2. Initiate weekly payment follow-up calls
3. Reduce credit limit by 20% for distributors with Credit Days > 35
4. Escalate to Finance team for portfolio review

**Compliance Note:**
All credit adjustments must be documented as per Policy CR-2024.
""",
        },
    }
