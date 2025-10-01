import pandas as pd, numpy as np, os
from utils import load_config, ci_bootstrap
from pathlib import Path

def main():
    cfg = load_config()
    dfs = []
    for p in cfg["data"]["raw_paths"]:
        if os.path.exists(p):
            dfs.append(pd.read_csv(p))
    if not dfs:
        print("[ERROR] No raw data found. Update config/data paths.")
        return 1
    df = pd.concat(dfs, ignore_index=True, sort=False)

    Path("results/tables").mkdir(parents=True, exist_ok=True)

    topline = df.describe(include='all').T
    topline.to_csv("results/tables/topline_stats.csv" )

    if "goals" in df.columns:
        ci, _ = ci_bootstrap(df["goals"], n_resamples=2000, ci=0.95, func=np.mean)
        with open("results/tables/ci_goals_mean.txt","w") as f:
            f.write(f"Mean goals 95% CI: {ci[0]:.3f} to {ci[1]:.3f}\n")

    if {"match_minute","shots_on_goal"}.issubset(df.columns):
        # compute minute-level accuracy proxy if accuracy column absent
        minute_shots = df.groupby("match_minute")["shots_on_goal"].mean()
        minute_shots.to_csv("results/tables/minute_shots_on_goal.csv" )

    print("[OK] descriptive_stats: wrote topline & example CIs")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
