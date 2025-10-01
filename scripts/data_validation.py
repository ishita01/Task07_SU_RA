import pandas as pd, numpy as np, os
from utils import load_config
from pathlib import Path

def main():
    cfg = load_config()
    frames = []
    for p in cfg["data"]["raw_paths"]:
        if os.path.exists(p):
            df = pd.read_csv(p)
            df["__source_file"] = p
            frames.append(df)
        else:
            print(f"[WARN] Missing raw file: {p}")
    if not frames:
        print("[ERROR] No raw data found. Update config/data paths.")
        return 1
    df = pd.concat(frames, ignore_index=True, sort=False)

    Path("results/tables").mkdir(parents=True, exist_ok=True)

    # Missingness
    missing = df.isna().mean().sort_values(ascending=False)
    missing.to_csv("results/tables/missingness.csv", header=["missing_rate"])

    # Outliers (z-score > threshold on numeric cols)
    num = df.select_dtypes(include=[np.number]).copy()
    if not num.empty:
        z = (num - num.mean())/num.std(ddof=0)
        outliers = (z.abs() > cfg["analysis"]["outlier_z_threshold"]).sum().sort_values(ascending=False)
        outliers.to_csv("results/tables/outlier_counts.csv", header=["count_over_threshold"])

    print("[OK] data_validation: wrote missingness & outlier_counts")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
