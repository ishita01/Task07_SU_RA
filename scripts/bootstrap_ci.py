import argparse, json, os
import pandas as pd
import numpy as np
from pathlib import Path

def bootstrap_diff_mean(a, b, iters=5000, seed=0):
    rng = np.random.default_rng(seed)
    n1, n2 = len(a), len(b)
    diffs = np.empty(iters, dtype=float)
    for i in range(iters):
        s1 = rng.choice(a, size=n1, replace=True)
        s2 = rng.choice(b, size=n2, replace=True)
        diffs[i] = s1.mean() - s2.mean()
    return diffs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--col", required=True, help="numeric column")
    ap.add_argument("--by", required=True, help="binary grouping column")
    ap.add_argument("--diff", default="", help="format: A-B where A and B are levels in --by")
    ap.add_argument("--iters", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=20250924)
    ap.add_argument("--out", required=True)
    ap.add_argument("--encoding", default="utf-8")
    args = ap.parse_args()

    df = pd.read_csv(args.data, encoding=args.encoding)

    # Ensure numeric target (handles commas/currency)
    df[args.col] = pd.to_numeric(df[args.col].astype(str).str.replace(r"[^\d\.\-eE]", "", regex=True), errors="coerce")

    if args.diff:
        a_label, b_label = args.diff.split("-", 1)
    else:
        levels = df[args.by].dropna().unique()
        if len(levels) != 2:
            raise ValueError("Provide --diff=A-B when the grouping has more than two levels.")
        a_label, b_label = levels[0], levels[1]

    # Validate labels
    levels_set = set(map(str, df[args.by].dropna().unique()))
    if a_label not in levels_set or b_label not in levels_set:
        raise ValueError(f"Levels not found in '{args.by}'. Found: {sorted(levels_set)}; wanted: {a_label}, {b_label}")

    a = df.loc[df[args.by] == a_label, args.col].dropna().to_numpy()
    b = df.loc[df[args.by] == b_label, args.col].dropna().to_numpy()
    if len(a) == 0 or len(b) == 0:
        raise ValueError("One of the groups has no numeric data after cleaning.")

    boot = bootstrap_diff_mean(a, b, iters=args.iters, seed=args.seed)
    ci_low, ci_high = np.percentile(boot, [2.5, 97.5])
    est = float(a.mean() - b.mean())

    Path(os.path.dirname(args.out)).mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{
        "metric": f"mean({args.col})[{a_label}] - mean({args.col})[{b_label}]",
        "estimate": est, "ci_low": float(ci_low), "ci_high": float(ci_high),
        "iters": args.iters, "seed": args.seed
    }]).to_csv(args.out, index=False)

    print(f"[OK] Bootstrap CI -> {args.out}  est={est:.3f}  CI=({ci_low:.3f}, {ci_high:.3f})")

if __name__ == "__main__":
    main()
