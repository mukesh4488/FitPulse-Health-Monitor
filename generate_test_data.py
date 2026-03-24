import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("🚀 Generating EXTREME Overlap Dataset (Scores 1-5)...")

periods = 1000 
start_date = datetime(2024, 6, 1)
timestamps = [start_date + timedelta(minutes=5*i) for i in range(periods)]
df = pd.DataFrame({"timestamp": timestamps})

# BASELINE (Score 0)
df["heart_rate_bpm"] = 70.0
df["spo2_pct"] = 98.0
df["steps"] = 0
df["sleeping"] = 0
df["calories_burned"] = 1.0

# --- SCORE 1: Single Rule (Tachycardia only) ---
df.loc[100:110, "heart_rate_bpm"] = 130.0 

# --- SCORE 2: Double Rule (High HR + Low SpO2) ---
df.loc[200:210, "heart_rate_bpm"] = 140.0
df.loc[200:210, "spo2_pct"] = 92.0

# --- SCORE 3: Triple Rule (High HR + Low SpO2 + Active while Sleeping) ---
df.loc[300:310, "heart_rate_bpm"] = 150.0
df.loc[300:310, "spo2_pct"] = 90.0
df.loc[300:310, "sleeping"] = 1
df.loc[300:310, "steps"] = 60 # Above 50 threshold

# --- SCORE 5+: THE "MAX" SCORE (Extreme values + Sleep Conflict) ---
# This hits Tachycardia, Low SpO2, Sleep-Steps, and Sleep-HR rules all at once
df.loc[400:410, "heart_rate_bpm"] = 180.0
df.loc[400:410, "spo2_pct"] = 85.0
df.loc[400:410, "sleeping"] = 1
df.loc[400:410, "steps"] = 200

df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
df.to_csv("extreme_test.csv", index=False)
print("✅ Success! 'extreme_test.csv' created.")