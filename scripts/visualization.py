import pandas as pd, numpy as np, os
import matplotlib.pyplot as plt
from utils import load_config
from pathlib import Path

def main():
    cfg = load_config()
    dfs = [pd.read_csv(p) for p in cfg["data"]["raw_paths"] if os.path.exists(p)]
    if not dfs:
        print("[ERROR] No raw data found. Update config/data paths.")
        return 1
    df = pd.concat(dfs, ignore_index=True, sort=False)

    Path("results/figures").mkdir(parents=True, exist_ok=True)

    if {"match_minute","shots_on_goal"}.issubset(df.columns):
        plt.figure()
        df.groupby("match_minute")["shots_on_goal"].mean().plot()
        plt.title("Avg Shots on Goal by Match Minute")
        plt.xlabel("Minute"); plt.ylabel("Avg Shots on Goal")
        plt.savefig("results/figures/shots_over_time.png", bbox_inches="tight")
        plt.close()

    print("[OK] visualization: wrote figures (if data available)" )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
