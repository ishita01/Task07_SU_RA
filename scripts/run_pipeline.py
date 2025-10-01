import subprocess, sys

steps = [
    "scripts/data_validation.py",
    "scripts/descriptive_stats.py",
    "scripts/fairness_checks.py",
    "scripts/sensitivity_analysis.py",
    "scripts/visualization.py",
    "scripts/stats_tests.py"
]

def main():
    ok = True
    for s in steps:
        print(f"\n=== Running {s} ===")
        ret = subprocess.run([sys.executable, s])
        if ret.returncode != 0:
            ok = False
            print(f"[WARN] Step failed: {s} (continuing)")
    if ok:
        print("\n[OK] All steps finished. See results/tables and results/figures.")
    else:
        print("\n[PARTIAL] Some steps failed. Check warnings above.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
