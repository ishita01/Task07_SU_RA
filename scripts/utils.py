import numpy as np, pandas as pd, yaml, random

def set_seed(seed: int = 42):
    np.random.seed(seed)
    random.seed(seed)

def load_config(path="config/config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def ci_bootstrap(x, n_resamples=2000, ci=0.95, func=np.mean, random_state=42):
    rng = np.random.default_rng(random_state)
    x = pd.Series(x).dropna().to_numpy()
    stats = np.empty(n_resamples, dtype=float)
    n = x.shape[0]
    if n == 0:
        return (float("nan"), float("nan")), stats
    for i in range(n_resamples):
        sample = rng.choice(x, size=n, replace=True)
        stats[i] = func(sample)
    low = np.percentile(stats, (1-ci)/2*100.0)
    high = np.percentile(stats, (1+ci)/2*100.0)
    return (low, high), stats
