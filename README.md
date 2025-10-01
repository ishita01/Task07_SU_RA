# 🧭 Task_07_Decision_Making — SU Women’s Lacrosse (2023–2025)

**Goal:** Transform the Task 06 LLM-generated *sideline interview* into a decision-making report for stakeholders, with strong emphasis on **ethics, reproducibility, and reliability**.  
**Source context:** Builds upon **Task 04** (descriptive statistics), **Task 05** (LLM queries on dataset), and **Task 06** (deep-fake demonstration).  
**Status:** Ready-to-submit framework developed using official SU Women’s Lacrosse statistics from 2023–2025.  

---

## 📦 Repository Structure

```
Task_07_Decision_Making/
├── archives/
│   ├── task4/                      # Carried over files from Task 4 (audit reference)
│   └── task5/                      # Carried over files from Task 5 (audit reference)
├── config/
│   ├── config.example.yaml          # Duplicate and adjust as needed
│   └── config.yaml                  # Points to data/raw/lacrosse_stats.csv
├── data/
│   ├── raw/
│   │   └── lacrosse_stats.csv       # Period-level compiled dataset (2023–2025)
│   └── processed/                   # Outputs created by scripts (if generated)
├── ethics/
│   └── ETHICS_CHECKLIST.md
├── logs/
│   └── llm_prompt_log.md            # All prompts, raw LLM output, and revision notes
├── outputs/                         # Mirrors results/ for consistency
│   ├── figures/
│   └── tables/
├── prompts/
│   └── decision_prompt_template.txt
├── reports/
│   ├── stakeholder_report.md        # Primary stakeholder document
│   └── stakeholder_report_template.md
├── results/
│   ├── figures/
│   ├── report/
│   │   ├── APPENDIX_TASK4_TASK5.md  # Listing of Task 4/5 references
│   │   └── stakeholder_report.md    # Copy of main report for grading
│   └── tables/
├── scripts/
│   ├── analysis_descriptives.py     # Basic profiling (describe, counts, histograms)
│   ├── bootstrap_ci.py              # Bootstrap CI for mean differences
│   ├── fairness_checks.py           # Generates subgroup disparity table
│   ├── data_validation.py           # Missing data & outlier overview
│   ├── descriptive_stats.py         # Core stats + illustrative CIs
│   ├── sensitivity_analysis.py      # Perturbation tests (top-N, normalization)
│   ├── stats_tests.py               # Paired comparisons (e.g., 1st vs 2nd half)
│   ├── visualization.py             # Period/minute trend visualizations
│   └── run_pipeline.py              # Master pipeline script
├── seeds.json                       # Standardized seeds and metadata
├── requirements.txt
├── .gitignore
└── LICENSE
```

> **Note:** `outputs/` is a direct mirror of `results/` so figures/tables can be referenced seamlessly in reports.  

---

## 🚀 Quickstart

1) (Optional) Create a virtual environment and install required packages:  
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```  

2) **Dataset already configured**: `data/raw/lacrosse_stats.csv` (period-level stats, 2023–2025).  
Update `config/config.yaml` if you swap or extend data.  

3) **Run the complete pipeline** (produces outputs in `results/` and mirrors them in `outputs/`):  
```bash
python scripts/run_pipeline.py
```  

4) **Run specific analyses** if desired:  

- Descriptive profile (summary, counts, histograms):  
```bash
python scripts/analysis_descriptives.py   --data data/raw/lacrosse_stats.csv   --out outputs   --seed 42
```  

- Bootstrap CI for mean difference (e.g., 1st vs 2nd half goals):  
```bash
python scripts/bootstrap_ci.py   --data data/raw/lacrosse_stats.csv   --col goals   --by period   --diff "2nd-1st"   --iters 5000   --out outputs/tables/goals_diff_ci.csv   --seed 4242
```  

- Fairness/disparity check (example: grouping by year):  
```bash
python scripts/fairness_checks.py   --data data/raw/lacrosse_stats.csv   --group-cols year   --target goals   --out outputs/tables/fairness_summary.csv
```  

---

## 🧪 What’s Inside the Report

The stakeholder report (`reports/stakeholder_report.md`) provides:  

- **Executive summary with tiered recommendations:**  
  - **Operational (low risk):** Micro-drills for endurance and shot selection after minute 30; track in practice.  
  - **Investigatory (medium risk):** Controlled scrimmages with hydration/pacing interventions; preregistered metrics; 95% CIs.  
  - **High-stakes (high risk):** Potential lineup adjustments based on endurance metrics (requires HR/legal/human oversight).  

- **Uncertainty:** 95% bootstrap intervals; sensitivity tests (removing top 5%; normalization).  
- **Fairness:** Coverage and subgroup disparity summary.  
- **Ethics/Legal:** FERPA, data privacy; explicit labeling of LLM text; mandatory human review for personnel actions.  
- **Appendix:** Catalog of imported Task 4/5 files; prompts and raw model outputs preserved in `logs/llm_prompt_log.md`.  

---

## 🛡️ Reproducibility

- Every script supports `--seed` and logs the value used.  
- Master seeds and metadata are captured in `seeds.json`.  
- **Tables and figures** are created in `results/` and replicated in `outputs/`.  

To snapshot the environment:  
```bash
pip freeze > requirements.txt
```  

---

## 📬 Submission

1) Push the repository to GitHub with the name **Task_07_Decision_Making** (omit large/raw data if necessary).  
2) Send the GitHub link to **jrstrome@syr.edu** (⚠️ not Dr. Stromer-Galley).  
3) Complete the required **Qualtrics check-in** by **October 1**.  

---

## ✅ Notes

- LLM text from **Task 06** (sideline interview) is clearly flagged and validated against stats.  
- Dataset is a consolidation of official SU Women’s Lacrosse performance (2023–2025), including Goals, Shots on Goal, Saves, and OT where applicable.  
- High-stakes recommendations (e.g., personnel or lineup changes) must go through **human validation** and may need **HR/legal approval**.  

## 👩‍💻 Author

**Ishita Ajay Trivedi**  
Master’s in Information Systems  
Syracuse University