"""
Layer 1: Monitoring Intelligence
Detects anomalies using rolling averages and multi-signal analysis.
Supports per-zone and all-zone scanning.
"""

import pandas as pd
import streamlit as st
from config.settings import (
    SALES_DEVIATION_THRESHOLD,
    CREDIT_DAYS_THRESHOLD,
    INVENTORY_DAYS_THRESHOLD,
    ROLLING_WINDOW_DAYS,
    RECENT_DAYS_LOOKBACK,
    RISK_PROJECTION_MONTHS,
)


@st.cache_data
def run_behaviour_scan(ops_data, dist_data, selected_zone="All Zones"):
    """
    Run multi-signal anomaly detection across distributors.

    Returns:
        alerts  : list of alert dicts (one per affected zone)
        anomaly_df : DataFrame of flagged distributors
        daily_agg  : aggregated daily data used for downstream layers
    """

    ops_sorted = ops_data.sort_values(['Distributor_ID', 'Date'])

    # Aggregate daily data per distributor
    daily_agg = ops_sorted.groupby(['Date', 'Distributor_ID']).agg({
        'Secondary_Sales_Value': 'sum',
        'Credit_Days': 'mean',
        'Inventory_Days': 'mean',
        'Scheme_Active': lambda x: (x == 'Yes').mean(),
        'Competitor_Price_Index': 'mean',
    }).reset_index()

    # Rolling window
    daily_agg = daily_agg.sort_values(['Distributor_ID', 'Date'])
    daily_agg['Rolling_Sales'] = daily_agg.groupby('Distributor_ID')[
        'Secondary_Sales_Value'
    ].transform(lambda x: x.rolling(ROLLING_WINDOW_DAYS, min_periods=10).mean())

    # Sales deviation
    daily_agg['Sales_Deviation'] = (
        (daily_agg['Secondary_Sales_Value'] - daily_agg['Rolling_Sales'])
        / daily_agg['Rolling_Sales']
    )

    # Recent window
    max_date = daily_agg['Date'].max()
    cutoff_date = max_date - pd.Timedelta(days=RECENT_DAYS_LOOKBACK)
    recent = daily_agg[daily_agg['Date'] >= cutoff_date]

    # Check each distributor
    anomaly_rows = []
    for dist_id in recent['Distributor_ID'].unique():
        dist_recent = recent[recent['Distributor_ID'] == dist_id]

        avg_deviation = dist_recent['Sales_Deviation'].mean()
        avg_credit = dist_recent['Credit_Days'].mean()
        avg_inventory = dist_recent['Inventory_Days'].mean()

        sales_drop = avg_deviation < SALES_DEVIATION_THRESHOLD
        credit_stress = avg_credit > CREDIT_DAYS_THRESHOLD
        inventory_buildup = avg_inventory > INVENTORY_DAYS_THRESHOLD

        if sales_drop and (credit_stress or inventory_buildup):
            zone = dist_data.loc[
                dist_data['Distributor_ID'] == dist_id, 'Zone'
            ].values[0]
            anomaly_rows.append({
                'Distributor_ID': dist_id,
                'Zone': zone,
                'Sales_Deviation': avg_deviation,
                'Credit_Days': avg_credit,
                'Inventory_Days': avg_inventory,
                'Scheme_Active': dist_recent['Scheme_Active'].mean(),
                'Competitor_Index': dist_recent['Competitor_Price_Index'].mean(),
            })

    anomaly_df = pd.DataFrame(anomaly_rows)

    # Filter by selected zone
    if selected_zone and selected_zone != "All Zones" and len(anomaly_df) > 0:
        anomaly_df = anomaly_df[anomaly_df['Zone'] == selected_zone]

    # Build alerts per zone
    alerts = []
    if len(anomaly_df) > 0:
        for zone in anomaly_df['Zone'].unique():
            zone_anomalies = anomaly_df[anomaly_df['Zone'] == zone]
            affected = len(zone_anomalies)
            avg_drop = zone_anomalies['Sales_Deviation'].mean()

            zone_distributors = dist_data[dist_data['Zone'] == zone]
            avg_billing = zone_distributors['Avg_Monthly_Billing'].mean()
            projected_risk = (
                abs(avg_drop) * avg_billing * affected * RISK_PROJECTION_MONTHS
            )

            avg_credit = zone_anomalies['Credit_Days'].mean()
            baseline_credit = 28  # Known baseline

            alerts.append({
                "Zone": zone,
                "Distributors_Affected": affected,
                "Sales_Drop": f"{abs(avg_drop)*100:.0f}%",
                "Credit_Increase": f"{baseline_credit} to {avg_credit:.0f} days",
                "Projected_Risk": f"₹{projected_risk/100000:.0f} Lakhs",
                "Confidence": f"{min(70 + affected * 4, 95)}%",
                "Cluster": f"Cluster {len(alerts) + 1}",
            })

    return alerts, anomaly_df, daily_agg
