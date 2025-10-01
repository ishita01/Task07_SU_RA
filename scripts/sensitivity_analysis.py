import pandas as pd, numpy as np, os
from utils import load_config
from pathlib import Path

def remove_top_n(df, by_col, n):
    return df.sort_values(by_col, ascending=False).iloc[n:].copy()

def main():
    cfg = load_config()
    dfs = [pd.read_csv(p) for p in cfg["data"]["raw_paths"] if os.path.exists(p)]
    if not dfs:
        print("[ERROR] No raw data found. Update config/data paths.")
        return 1
    df = pd.concat(dfs, ignore_index=True, sort=False)

    Path("results/tables").mkdir(parents=True, exist_ok=True)

    if {"goals","match_minute"}.issubset(df.columns):
        base_mean = df["goals"].mean()
        n = max(1, int(0.05*len(df)))
        pert = remove_top_n(df, "match_minute", n=n)
        pert_mean = pert["goals"].mean()
        with open("results/tables/sensitivity_goals.txt","w") as f:
            f.write(f"Base mean goals: {base_mean:.3f}\nAfter removing top 5% minutes: {pert_mean:.3f}\n")
        print("[OK] sensitivity_analysis: wrote sensitivity_goals.txt")
    else:
        print("[INFO] Skipped example sensitivity; required columns not present.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
