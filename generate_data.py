"""
FMCG AI Layers Demo – Data Generation Script
=============================================
Generates 3 CSV files with realistic FMCG distribution data.

Anomaly injection:
  • West Zone (D081-D095): heavy anomaly from Day 60 onward
  • North Zone (D011-D018): lighter anomaly from Day 70 onward
"""

import os
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# ============================================================
# 1. DISTRIBUTOR MASTER – 120 Distributors
# ============================================================

ZONE_CITIES = {
    "North": ["Delhi", "Chandigarh", "Lucknow", "Jaipur",
              "Amritsar", "Noida", "Gurgaon", "Agra"],
    "South": ["Chennai", "Bangalore", "Hyderabad", "Kochi",
              "Coimbatore", "Mysore", "Vizag", "Madurai"],
    "East":  ["Kolkata", "Patna", "Bhubaneswar", "Guwahati",
              "Ranchi", "Siliguri", "Dhanbad", "Rourkela"],
    "West":  ["Mumbai", "Pune", "Ahmedabad", "Surat",
              "Nagpur", "Indore", "Vadodara", "Nashik"],
}

DIST_NAME_BASES = [
    "Star Distributors", "Bright Traders", "Global Supply Co",
    "Metro Distributors", "Prime Trading", "Excel Supply",
    "United Traders", "Royal Distributors", "Diamond Supply",
    "Golden Traders", "Supreme Distributors", "National Supply",
    "Pioneer Traders", "Victory Distributors", "Crystal Trading",
    "Phoenix Supply", "Sunrise Distributors", "Atlas Trading",
    "Omega Distributors", "Summit Supply", "Crown Traders",
    "Empire Distributors", "Fusion Trading", "Genesis Supply",
    "Horizon Distributors", "Impact Traders", "Jupiter Supply",
    "Keystone Distributors", "Liberty Trading", "Momentum Supply",
]

distributors = []
did = 1
for zone, cities in ZONE_CITIES.items():
    for i in range(30):
        distributors.append({
            "Distributor_ID": f"D{did:03d}",
            "Distributor_Name": f"{DIST_NAME_BASES[i % len(DIST_NAME_BASES)]} {cities[i % len(cities)]}",
            "Zone": zone,
            "City": cities[i % len(cities)],
            "Credit_Limit": random.randint(300_000, 800_000),
            "Avg_Monthly_Billing": random.randint(800_000, 2_000_000),
        })
        did += 1

dist_df = pd.DataFrame(distributors)
dist_df.to_csv(f"{DATA_DIR}/distributor_master.csv", index=False)
print(f"✔ distributor_master.csv  → {len(dist_df)} rows")

# ============================================================
# 2. SKU MASTER – 70 SKUs
# ============================================================

SKU_CATALOG = {
    "Haircare": [
        ("Hair Oil 100ml", 120, 18), ("Hair Oil 200ml", 210, 20),
        ("Shampoo 100ml", 150, 22), ("Shampoo 200ml", 250, 24),
        ("Conditioner 100ml", 180, 20), ("Hair Gel 50ml", 90, 25),
        ("Hair Serum 50ml", 280, 30), ("Hair Color Pack", 350, 28),
        ("Anti Dandruff Shampoo 150ml", 220, 22), ("Hair Mask 100g", 160, 18),
    ],
    "Skincare": [
        ("Face Cream 50g", 180, 25), ("Face Wash 100ml", 150, 22),
        ("Body Lotion 200ml", 220, 20), ("Sunscreen 50ml", 280, 28),
        ("Night Cream 50g", 350, 30), ("Moisturizer 100ml", 200, 22),
        ("Face Scrub 50g", 130, 20), ("Aloe Vera Gel 100ml", 160, 24),
        ("Anti Aging Cream 30g", 450, 35), ("BB Cream 30ml", 320, 28),
    ],
    "Oral Care": [
        ("Toothpaste 100g", 80, 15), ("Toothpaste 200g", 140, 18),
        ("Mouthwash 250ml", 180, 22), ("Toothbrush Standard", 40, 30),
        ("Toothbrush Premium", 90, 35), ("Tooth Whitening Gel", 220, 28),
        ("Kids Toothpaste 50g", 60, 20), ("Dental Floss Pack", 110, 25),
        ("Tongue Cleaner", 35, 40), ("Sensitivity Toothpaste 100g", 120, 20),
    ],
    "Home Care": [
        ("Floor Cleaner 500ml", 120, 18), ("Dish Wash 250ml", 80, 20),
        ("Dish Wash 500ml", 140, 22), ("Toilet Cleaner 500ml", 100, 20),
        ("Glass Cleaner 250ml", 110, 22), ("Fabric Softener 500ml", 180, 20),
        ("Detergent 1kg", 200, 15), ("Detergent 500g", 110, 18),
        ("Handwash 200ml", 90, 25), ("Surface Cleaner 500ml", 130, 20),
    ],
    "Personal Care": [
        ("Deo Spray 150ml", 200, 28), ("Body Wash 250ml", 250, 24),
        ("Soap 100g", 40, 20), ("Soap 75g (3-pack)", 100, 22),
        ("Talcum Powder 100g", 80, 18), ("Hand Cream 50ml", 120, 25),
        ("Lip Balm 4g", 80, 35), ("Wet Wipes 30s", 100, 22),
        ("Sanitizer 200ml", 130, 28), ("Baby Powder 100g", 120, 20),
    ],
    "Foods": [
        ("Instant Noodles 70g", 14, 12), ("Biscuits 100g", 30, 15),
        ("Cookie Pack 200g", 80, 18), ("Juice 200ml", 25, 20),
        ("Juice 1L", 100, 18), ("Jam 200g", 90, 22),
        ("Ketchup 200g", 70, 20), ("Peanut Butter 200g", 180, 25),
        ("Cornflakes 250g", 160, 18), ("Oats 500g", 200, 20),
    ],
    "Baby Care": [
        ("Baby Shampoo 200ml", 220, 22), ("Baby Lotion 200ml", 250, 24),
        ("Baby Oil 200ml", 180, 20), ("Baby Soap 75g", 60, 22),
        ("Diaper Pack S", 400, 15), ("Diaper Pack M", 450, 15),
        ("Baby Wipes 80s", 180, 20), ("Baby Cream 50g", 150, 25),
        ("Baby Wash 200ml", 200, 22), ("Baby Powder 200g", 160, 20),
    ],
}

skus = []
sid = 1
for category, products in SKU_CATALOG.items():
    for name, mrp, margin in products:
        skus.append({
            "SKU_ID": f"SKU{sid:02d}",
            "SKU_Name": name,
            "Category": category,
            "MRP": mrp,
            "Margin_Percentage": margin,
        })
        sid += 1

sku_df = pd.DataFrame(skus)
sku_df.to_csv(f"{DATA_DIR}/sku_master.csv", index=False)
print(f"✔ sku_master.csv          → {len(sku_df)} rows")

# ============================================================
# 3. DAILY OPERATIONS – 90 Days
# ============================================================

START_DATE = datetime(2025, 12, 1)
DATES = [START_DATE + timedelta(days=i) for i in range(90)]

# Anomaly groups
WEST_ANOMALY_IDS  = {f"D{i:03d}" for i in range(81, 96)}   # Day 60+
NORTH_ANOMALY_IDS = {f"D{i:03d}" for i in range(11, 19)}    # Day 70+

operations = []
for day_idx, date in enumerate(DATES):
    day_num = day_idx + 1

    for _, dist in dist_df.iterrows():
        dist_id = dist["Distributor_ID"]
        avg_billing = dist["Avg_Monthly_Billing"]
        credit_limit = dist["Credit_Limit"]

        # 1-3 SKUs per distributor per day
        for _, sku in sku_df.sample(n=random.randint(1, 3)).iterrows():
            base_primary = avg_billing / 30 * np.random.uniform(0.7, 1.3)
            base_secondary = base_primary * np.random.uniform(0.85, 1.05)
            base_inv_units = random.randint(200, 800)
            base_inv_days = random.randint(12, 25)
            base_credit_out = credit_limit * np.random.uniform(0.3, 0.7)
            base_credit_days = random.randint(22, 32)
            base_scheme = "Yes" if random.random() > 0.2 else "No"
            base_comp = round(np.random.uniform(0.30, 0.55), 2)
            noise = np.random.normal(1.0, 0.05)

            # ---- WEST ZONE heavy anomaly (Day 60+) ----
            if dist_id in WEST_ANOMALY_IDS and day_num >= 60:
                progress = min((day_num - 60) / 30, 1.0)
                base_secondary *= (1.0 - 0.15 * progress)
                base_credit_days = int(28 + 10 * progress)
                base_inv_days = int(base_inv_days * (1 + 0.20 * progress))
                if progress > 0.3:
                    base_scheme = "No"
                base_comp = round(0.50 + 0.25 * progress, 2)
                base_credit_out *= (1 + 0.15 * progress)

            # ---- NORTH ZONE lighter anomaly (Day 70+) ----
            if dist_id in NORTH_ANOMALY_IDS and day_num >= 70:
                progress = min((day_num - 70) / 20, 1.0)
                base_secondary *= (1.0 - 0.12 * progress)
                base_credit_days = int(28 + 7 * progress)
                base_inv_days = int(base_inv_days * (1 + 0.15 * progress))
                if progress > 0.5:
                    base_scheme = "No"
                base_comp = round(0.45 + 0.20 * progress, 2)
                base_credit_out *= (1 + 0.10 * progress)

            operations.append({
                "Date": date.strftime("%Y-%m-%d"),
                "Distributor_ID": dist_id,
                "SKU_ID": sku["SKU_ID"],
                "Primary_Billing_Value": round(base_primary * noise, 2),
                "Secondary_Sales_Value": round(base_secondary * noise, 2),
                "Inventory_Units": int(base_inv_units * noise),
                "Inventory_Days": base_inv_days,
                "Credit_Outstanding": round(base_credit_out, 2),
                "Credit_Days": base_credit_days,
                "Scheme_Active": base_scheme,
                "Competitor_Price_Index": min(base_comp, 1.0),
            })

ops_df = pd.DataFrame(operations)
ops_df.to_csv(f"{DATA_DIR}/daily_operations.csv", index=False)
print(f"✔ daily_operations.csv    → {len(ops_df):,} rows")
print(f"  Date range  : {ops_df['Date'].min()} – {ops_df['Date'].max()}")
print(f"  Distributors: {ops_df['Distributor_ID'].nunique()}")

# Verify
for label, ids, start_day in [
    ("West", WEST_ANOMALY_IDS, 59),
    ("North", NORTH_ANOMALY_IDS, 69),
]:
    subset = ops_df[ops_df['Distributor_ID'].isin(ids)]
    pre  = subset[subset['Date'] < DATES[start_day].strftime('%Y-%m-%d')]['Secondary_Sales_Value'].mean()
    post = subset[subset['Date'] >= DATES[start_day].strftime('%Y-%m-%d')]['Secondary_Sales_Value'].mean()
    print(f"\n  {label} anomaly check:")
    print(f"    Pre-anomaly avg : ₹{pre:,.0f}")
    print(f"    Post-anomaly avg: ₹{post:,.0f}")
    print(f"    Drop            : {((post - pre) / pre) * 100:.1f}%")

print("\n✅  All data files generated successfully!")
