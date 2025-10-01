import argparse, os
import pandas as pd
import numpy as np
from pathlib import Path

def summarize_by_groups(df, group_cols, target):
    grp = df.groupby(group_cols, dropna=False)[target]
    out = grp.agg(['count','mean','median','std']).reset_index()
    return out

def disparity_table(df, group_cols, target):
    tbl = summarize_by_groups(df, group_cols, target)
    global_mean = df[target].mean()
    tbl['diff_vs_global_mean'] = tbl['mean'] - global_mean
    return tbl, global_mean

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--group-cols", required=True, help="comma-separated")
    ap.add_argument("--target", required=True, help="numeric metric to compare")
    ap.add_argument("--out", required=True)
    ap.add_argument("--encoding", default="utf-8")
    args = ap.parse_args()

    df = pd.read_csv(args.data, encoding=args.encoding)

    # Coerce numeric target (handles commas/currency)
    df[args.target] = pd.to_numeric(df[args.target].astype(str).str.replace(r"[^\d\.\-eE]", "", regex=True), errors="coerce")

    group_cols = [c.strip() for c in args.group_cols.split(",") if c.strip()]
    tbl, gmean = disparity_table(df, group_cols, args.target)
    Path(os.path.dirname(args.out)).mkdir(parents=True, exist_ok=True)
    tbl.to_csv(args.out, index=False)
    print(f"[OK] Fairness summary -> {args.out}. Global mean of {args.target}={gmean:.3f}")

if __name__ == "__main__":
    main()
