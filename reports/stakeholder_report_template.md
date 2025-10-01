Title & Purpose

SU Women’s Lacrosse 2023–2025 — Decision Guidance with Evidence, Uncertainty, and Risks

Executive Summary:
Top recommendation:
Introduce focused endurance-and-shot-selection micro-drills targeting post‑minute‑30 scenarios and instrument practice scrimmages to monitor shot accuracy, shots on goal, and saves. Scale to rotation/lineup changes only if effects persist across scrimmages with 95% CIs excluding 0.

Risk level: Medium
Confidence: Moderate

Rationale (evidence + uncertainty):
Multi‑year period summaries show a second‑half decline in goals and shots on goal in 2025 relative to earlier periods, while saves are comparatively stable. Effects are modest and sensitive to normalization; we report 95% bootstrap CIs and run sensitivity checks (remove top 5% minutes, alternate normalizations). Subgroup counts by position/class year may be uneven; interpret pooled effects cautiously.

Background & Decision Question:
We produced descriptive stats (Task 4/5) and an LLM-assisted sideline interview (Task 6). Task 7 converts that narrative into a stakeholder decision with uncertainty, fairness, and reproducibility, focused on whether to emphasize endurance protocols and rotation adjustments in late‑game scenarios.

Data & Methods (brief)
Source: Official Syracuse Women’s Lacrosse combined team statistics (2023–2025 PDFs).
Processing: period-level extraction; consolidated CSV; schema checks; outlier review.
Inference: non‑parametric bootstrap (seed recorded); paired tests where applicable; subgroup fairness.
Reproducibility: commands and outputs under scripts/ and outputs/; seeds in seeds.json.

Findings (with Uncertainty)
• Second-half shot accuracy/production decline in 2025; 95% CI for the change excludes 0 in our bootstrap runs (magnitude modest).
• Saves show no significant second‑half change in 2025.
• Sensitivity: Results persist after removing top 5% by minutes; effect sizes shrink slightly.

Recommendations (Tiered)
Operational (low risk): endurance micro‑drills; recovery windows; targeted shot‑selection drills after minute 30; instrument practices.
Investigatory (medium): A/B scrimmage protocol for hydration+pacing; pre‑register metrics (SOG, accuracy, RPE, minor injury incidence); 95% CIs per scrimmage block.
High-stakes (needs human/legal): Rotation/lineup changes based on endurance metrics; document decisions; HR/Legal review.

Ethical / Legal Considerations:
LLM content labeled; no PII published; FERPA respected; fairness across subgroups monitored; disclose uncertainty; human‑in‑the‑loop for personnel decisions.

Appendices:
• A. Data lineage (PDFs → CSV) • B. LLM prompts & outputs (Task 6) • C. Scripts & environment • D. Statistical details (bootstrap, sensitivity)
