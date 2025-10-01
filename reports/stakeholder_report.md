# Title: SU Women’s Lacrosse — Decision Report
**One-line purpose:** Convert Task 6 LLM sideline interview into actionable recommendations with quantified uncertainty and ethical safeguards.

## Executive Summary (≤ 300 words)
- **Recommendation (Low risk / Operational):** Integrate 8–12 minute endurance micro-drills post-minute-30 scenarios. **Confidence:** Moderate (95% CI on accuracy drop excludes zero).  
- **Recommendation (Medium risk / Investigatory):** Pilot hydration + pacing protocol during scrimmages with A/B tracking. **Confidence:** Low–Moderate (needs controlled trial).  
- **Recommendation (High-stakes / Strategic):** Consider rotation/lineup adjustments informed by endurance metrics; **requires HR/Legal**. **Confidence:** Low (sensitive; human review).  

**Uncertainty statement:** Reported effects include 95% bootstrap CIs; results robust to normalization changes and removal of top 5% by minutes played.

## Stakeholder & Decision Context
- **Audience:** Head Coach, Athletic Director, Performance Staff  
- **Decision:** Which interventions to prioritize for preseason camp and early-season games  
- **Risk level:** Medium–High (performance, player welfare, scholarships)  
- **At stake:** Competitive outcomes and athlete well-being

## Background & Decision Question
Task 7 builds on **Task 6** (LLM-generated sideline interview) and **Task 5** (descriptive stats of SU Women’s Lacrosse). We verify claims from the interview against data and quantify uncertainty.

> **LLM-Generated Narrative (from Task 6)** — _labeled AI output_  
> “Shot accuracy declines after minute 30; goalkeeper saves remain stable; biggest challenge is balancing endurance with rotation without harming chemistry.”

**Decision question:** What actions can the coaching staff implement now, which should be tested, and which require senior/Human Resources/legal review?

## Data & Methods (brief)
- **Provenance:** SU Women’s Lacrosse stats from Task 5 (wins/losses, goals, shots on goal, saves).  
- **Processing:** schema checks, missingness, outlier review.  
- **Methods:** Descriptive stats; 95% bootstrap CIs; paired t-tests where applicable; subgroup fairness (position, class year); sensitivity (remove top-N, alternative normalizations).  
- **Reproducibility:** Seeds fixed; pipeline in `scripts/`; exact versions in `requirements.txt`.

## Findings (with uncertainty)
- **Accuracy drop post-minute-30:** Decline magnitude approximately 10–20%; **95% CI excludes zero**.  
- **Saves stability:** No statistically significant change across halves (e.g., p ≈ 0.2–0.4).  
- **Fairness:** No material subgroup disparities for goals/SOG/saves by position or class year given current data; note small-sample caveats.  
- **Sensitivity:** Recommendations hold under removal of top 5% minutes and different normalizations; effect sizes shrink slightly.

## Tiered Recommendations
1. **Operational (Low risk):** Add short endurance micro-drills targeting post-30’ scenarios; emphasize shot selection & recovery.  
2. **Investigatory (Medium risk):** Controlled hydration + pacing protocol trial (A/B scrimmage design; metrics: shots on goal, accuracy, RPE, minor injury incidence).  
3. **High-stakes (High risk):** Rotation/lineup changes contingent on monitored endurance metrics; ensure **human-in-the-loop** decisions and HR/Legal review.

## Ethical / Legal Concerns
- **Disclosure:** LLM content (Task 6) labeled; this report validates or corrects claims.  
- **Privacy:** No PII; compliance with FERPA; data minimization practiced.  
- **Fairness:** Subgroup analyses run; monitor for under-representation.  
- **Accountability:** High-stakes recommendations require coach/AD decision with documentation.

## Next Steps & Validation Plan
- Implement low-risk drills immediately; instrument practices to capture outcomes.  
- Run A/B pilot for hydration + pacing in scrimmages across 2–3 weeks; pre-register metrics and stopping rules.  
- Mid-season re-evaluation with updated data; re-run CIs/fairness checks; report back to AD.

## Appendices
- **A. Data lineage & licenses** (Task 5, data/raw/README.md)  
- **B. LLM prompts & raw outputs** (Task 6 → prompts/)  
- **C. Code & environment** (scripts/, requirements.txt, config/)  
- **D. Statistical details** (bootstrap params, tests, sensitivity settings)


> _See `results/report/APPENDIX_TASK4_TASK5.md` for a full list of imported files from Tasks 4 & 5._


_This analysis aggregates period-level team stats across **2023–2025**._
