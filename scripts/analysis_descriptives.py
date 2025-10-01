import argparse, os, re
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

def flatten_columns(cols):
    out = []
    for c in cols:
        if isinstance(c, tuple):
            out.append("_".join([str(x) for x in c if x != ""]))
        else:
            out.append(str(c))
    return out

def safe_filename(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", str(name).strip())
    return s.strip("._") or "col"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--group-cols", default="")
    ap.add_argument("--out", default="outputs")
    ap.add_argument("--seed", type=int, default=1337)
    ap.add_argument("--encoding", default="utf-8")
    args = ap.parse_args()

    np.random.seed(args.seed)
    df = pd.read_csv(args.data, encoding=args.encoding)

    tables_dir = os.path.join(args.out, "tables")
    figs_dir = os.path.join(args.out, "figures")
    Path(tables_dir).mkdir(parents=True, exist_ok=True)
    Path(figs_dir).mkdir(parents=True, exist_ok=True)

    group_cols = [c.strip() for c in args.group_cols.split(",") if c.strip()]
    num_cols = [c for c in df.columns if np.issubdtype(df[c].dtype, np.number)]
    cat_cols = [c for c in df.columns if df[c].dtype == "object" or str(df[c].dtype) == "category"]

    # === Describe ===
    if group_cols:
        if num_cols:
            desc = df.groupby(group_cols, dropna=False)[num_cols].describe()
            desc = desc.reset_index()
            desc.columns = flatten_columns(desc.columns)
            desc.to_csv(os.path.join(tables_dir, "describe.csv"), index=False)
        else:
            counts = df.groupby(group_cols, dropna=False).size().reset_index(name="count")
            counts.to_csv(os.path.join(tables_dir, "describe.csv"), index=False)
    else:
        overall = df.describe(include="all")
        overall.to_csv(os.path.join(tables_dir, "describe.csv"))

    # === Value counts for a few categorical columns ===
    for c in cat_cols[:5]:
        # If c is already in group-cols, skip to avoid duplicate keys
        if c in group_cols:
            continue
        safe_c = safe_filename(c)
        if group_cols:
            # De-duplicate keys while preserving order
            group_keys = []
            for k in group_cols + [c]:
                if k not in group_keys:
                    group_keys.append(k)
            vc = df.groupby(group_keys, dropna=False).size().reset_index(name="count")
            outname = f"value_counts_{safe_c}_by__{'__'.join([safe_filename(k) for k in group_cols])}.csv"
        else:
            vc = df[c].value_counts(dropna=False).reset_index().rename(columns={"index": c, c: "count"})
            outname = f"value_counts_{safe_c}.csv"
        vc.to_csv(os.path.join(tables_dir, outname), index=False)

    # === Histograms for a couple of numeric columns ===
    for col in num_cols[:2]:
        plt.figure()
        df[col].dropna().plot(kind="hist", bins=30, edgecolor="black")
        plt.title(f"Histogram — {col}")
        plt.tight_layout()
        plt.savefig(os.path.join(figs_dir, f"hist_{safe_filename(col)}.png"), dpi=150)
        plt.close()

    print(f"[OK] Wrote describe + value_counts + histograms to {args.out}. Seed={args.seed}")

if __name__ == "__main__":
    main()
