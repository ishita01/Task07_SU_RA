import pandas as pd, numpy as np, os
from scipy import stats
from utils import load_config
from pathlib import Path

def main():
    cfg = load_config()
    dfs = [pd.read_csv(p) for p in cfg["data"]["raw_paths"] if os.path.exists(p)]
    if not dfs:
        print("[ERROR] No raw data found. Update config/data paths.")
        return 1
    df = pd.concat(dfs, ignore_index=True, sort=False)

    Path("results/tables").mkdir(parents=True, exist_ok=True)

    if {"shot_accuracy_first_half","shot_accuracy_second_half"}.issubset(df.columns):
        a = df["shot_accuracy_first_half"].dropna()
        b = df["shot_accuracy_second_half"].dropna()
        if len(a) and len(b):
            t, p = stats.ttest_rel(a, b)
            with open("results/tables/ttest_accuracy_halves.txt","w") as f:
                f.write(f"Paired t-test first vs second half accuracy: t={t:.3f}, p={p:.4f}\n")
            print("[OK] stats_tests: wrote ttest_accuracy_halves.txt")
    else:
        print("[INFO] t-test skipped; accuracy columns not found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
