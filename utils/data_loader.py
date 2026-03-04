"""
FMCG AI Layers Demo - Data Loading Utilities
"""

import pandas as pd
import streamlit as st
from config.settings import DISTRIBUTOR_FILE, SKU_FILE, OPERATIONS_FILE


@st.cache_data
def load_data():
    """Load all 3 CSV datasets and return as DataFrames."""
    dist = pd.read_csv(DISTRIBUTOR_FILE)
    sku = pd.read_csv(SKU_FILE)
    ops = pd.read_csv(OPERATIONS_FILE)
    ops['Date'] = pd.to_datetime(ops['Date'])
    return dist, sku, ops


def get_zone_list(dist_df):
    """Get sorted list of unique zones from distributor data."""
    return sorted(dist_df['Zone'].unique().tolist())


def get_zone_stats(dist_df, sku_df, ops_df, zone=None):
    """Get summary statistics, optionally filtered by zone."""
    if zone and zone != "All Zones":
        zone_dist_ids = dist_df[dist_df['Zone'] == zone]['Distributor_ID'].tolist()
        filtered_ops = ops_df[ops_df['Distributor_ID'].isin(zone_dist_ids)]
        filtered_dist = dist_df[dist_df['Zone'] == zone]
    else:
        filtered_ops = ops_df
        filtered_dist = dist_df

    return {
        "distributors": filtered_dist.shape[0],
        "zones": dist_df['Zone'].nunique(),
        "skus": sku_df.shape[0],
        "days": filtered_ops['Date'].nunique(),
        "data_points": filtered_ops.shape[0],
    }
