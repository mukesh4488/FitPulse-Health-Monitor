"""
=============================================================
FitPulse — Health Anomaly Detection (Main Runner)
=============================================================
Runs all 4 milestones end-to-end.

Usage:
    python mainpage.py              # Run all milestones
    python mainpage.py --m1         # Only Milestone 1
    python mainpage.py --m1 --m2    # Milestones 1 & 2
    
Launch dashboard:
    streamlit run modules/milestone4_dashboard.py
=============================================================
"""

import argparse
import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.milestone1_preprocessing import run_milestone1
from modules.milestone2_modeling import run_milestone2
from modules.milestone3_anomaly import run_milestone3

def main():
    parser = argparse.ArgumentParser(description="FitPulse Anomaly Detection Pipeline")
    parser.add_argument("--m1", action="store_true", help="Run Milestone 1: Preprocessing")
    parser.add_argument("--m2", action="store_true", help="Run Milestone 2: Modeling")
    parser.add_argument("--m3", action="store_true", help="Run Milestone 3: Anomaly Detection")
    args = parser.parse_args()

    # If no specific flags are passed, run everything
    run_all = not any([args.m1, args.m2, args.m3])

    print("\n╔══════════════════════════════════════════════════════╗")
    print("║   FitPulse — Health Anomaly Detection System         ║")
    print("╚══════════════════════════════════════════════════════╝")

    # Ensure directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    # Check if data exists
    data_path = "data/fitness_data_raw.csv"
    if not os.path.exists(data_path):
        print(f"\n❌ Error: Could not find '{data_path}'.")
        print("Please make sure your CSV files are inside the 'data' folder.")
        return
    else:
        print(f"\n📂 Using dataset: {data_path}")

    # ── Milestone 1 ──
    df_clean = None
    if run_all or args.m1:
        print("\n🚀 Starting Milestone 1...")
        df_clean = run_milestone1(data_path)

    # ── Milestone 2 ──
    m2_results = None
    if run_all or args.m2:
        print("\n🚀 Starting Milestone 2...")
        import pandas as pd
        if df_clean is None:
            try:
                df_clean = pd.read_csv("outputs/cleaned_data.csv", index_col=0, parse_dates=True)
            except FileNotFoundError:
                print("❌ Error: outputs/cleaned_data.csv not found. Please run Milestone 1 first using: python mainpage.py --m1")
                return
        m2_results = run_milestone2(df_clean)

    # ── Milestone 3 ──
    if run_all or args.m3:
        print("\n🚀 Starting Milestone 3...")
        import pandas as pd
        if df_clean is None:
            try:
                df_clean = pd.read_csv("outputs/cleaned_data.csv", index_col=0, parse_dates=True)
            except FileNotFoundError:
                print("❌ Error: outputs/cleaned_data.csv not found. Run Milestone 1 first.")
                return
        
        feat_df = m2_results["features"] if m2_results else None
        prophet = m2_results["prophet"] if m2_results else None
        
        # If we skip M2 but run M3, we should try to load M2 features
        if feat_df is None and os.path.exists("outputs/feature_matrix.csv"):
            feat_df = pd.read_csv("outputs/feature_matrix.csv", index_col=0, parse_dates=True)
            
        df_anomaly = run_milestone3(df_clean, feat_df=feat_df, prophet_results=prophet)

    # ── Summary ──
    print("\n╔══════════════════════════════════════════════════════╗")
    print("║   ✅ EXECUTION COMPLETE                              ║")
    print("╚══════════════════════════════════════════════════════╝\n")

if __name__ == "__main__":
    main()