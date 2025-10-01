# Integrating Task 4 & Task 5

**Do you need Tasks 4 & 5?**
- **Not strictly required**, but **recommended**:
  - Use **Task 5** descriptive stats/plots as the baseline that the LLM narrative (Task 6) referenced.
  - Reuse **Task 4** code/utilities if they include robust descriptive pipelines, seeds, or validation scripts.

## What to copy
- Task 5 summary tables/figures → `results/tables/legacy_*.csv`, `results/figures/legacy_*.*`
- Task 5 narrative/prompts → `prompts/task5_*`
- Task 4 code/notebooks → `archives/task4/` (we won’t run these automatically; keep for audit)
- Document provenance in `data/raw/README.md` and cite in the report appendices.

## How the report uses them
- The **Findings** section cross-references Task 5 baselines and compares to re-created results here.
- The **LLM Narrative** block is from Task 6 interview; we annotate what we verified or corrected.
- The **Appendices** list Task 4/5 artifacts with timestamps.
