"""
Layer 3: Predictive Intelligence
Generates trend-based sales forecast for a given zone.
"""

import pandas as pd
import numpy as np
import streamlit as st
from datetime import timedelta

from config.settings import FORECAST_DAYS


@st.cache_data
def generate_forecast(ops_data, dist_df, zone="West"):
    """
    Build a 30-day sales forecast for the given zone using
    linear-trend extrapolation.

    Returns:
        daily_sales     : historical daily sales Series
        forecast_df     : DataFrame with Date, Forecast, Lower, Upper
        projected_loss  : estimated revenue loss (₹)
        margin_compression : estimated margin compression (%)
    """

    # Merge with distributor master to get Zone
    zone_data = ops_data.merge(dist_df[['Distributor_ID', 'Zone']], on='Distributor_ID')
    zone_data = zone_data[zone_data['Zone'] == zone]

    daily_sales = (
        zone_data
        .groupby('Date')['Secondary_Sales_Value']
        .sum()
        .reset_index()
    )
    daily_sales.columns = ['Date', 'Sales']
    daily_sales = daily_sales.sort_values('Date')

    # Linear trend on last 30 days
    last_30 = daily_sales.tail(30)
    x = np.arange(len(last_30))
    y = last_30['Sales'].values

    mask = ~np.isnan(y)
    if mask.sum() > 5:
        coeffs = np.polyfit(x[mask], y[mask], 1)
        trend_slope = coeffs[0]
    else:
        trend_slope = -5000  # default downward

    last_date = daily_sales['Date'].max()
    forecast_dates = [last_date + timedelta(days=i + 1) for i in range(FORECAST_DAYS)]

    base_sales = last_30['Sales'].mean()
    forecast_values, lower_bound, upper_bound = [], [], []

    rng = np.random.RandomState(42)
    for i in range(FORECAST_DAYS):
        predicted = base_sales + trend_slope * (i + len(last_30))
        noise = rng.normal(0, base_sales * 0.05)
        forecast_values.append(max(predicted + noise, base_sales * 0.5))
        lower_bound.append(max(predicted - base_sales * 0.15, base_sales * 0.3))
        upper_bound.append(predicted + base_sales * 0.1)

    forecast_df = pd.DataFrame({
        'Date': forecast_dates,
        'Forecast': forecast_values,
        'Lower': lower_bound,
        'Upper': upper_bound,
    })

    # Projected loss
    first_period_avg = daily_sales.head(30)['Sales'].mean()
    last_period_avg = daily_sales.tail(15)['Sales'].mean()
    projected_loss = (first_period_avg - last_period_avg) * 60
    margin_compression = (
        abs(first_period_avg - last_period_avg) / first_period_avg * 100
        if first_period_avg > 0
        else 0
    )

    return daily_sales, forecast_df, projected_loss, margin_compression
