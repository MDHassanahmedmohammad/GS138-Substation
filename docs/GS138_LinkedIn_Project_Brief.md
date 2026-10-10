# 138/34.5-kV Substation Study — Project Brief

## Objective

Evaluate a conceptual two-transformer 138/34.5-kV substation under normal loading, N-1 transformer outages, corrective bus-tie transfer, and future load growth.

## Model

- 2 × 50-MVA, 138/34.5-kV transformers
- Split 34.5-kV Bus A / Bus B
- Normally open bus tie
- Base station load: 40 MW / 13.15 Mvar
- Approximate load power factor: 0.95

## Key results

| Case | Result |
|---|---:|
| Normal transformer loading | 42.80% each |
| Base N-1 surviving transformer | 87.24% |
| +10% load-growth N-1 | 96.36% |
| +13.9% load-growth N-1 | 99.94% |
| +14% load-growth N-1 | 100.04% — overload |
| +15% load-growth N-1 | 100.96% — overload |
| Approximate N-1 capacity boundary | 45.6 MW |
| Post-contingency voltage at 45.56 MW | 0.95967 pu |

## Takeaway

The model remains N-1 capable at the 40-MW base load. Capacity testing indicates that the surviving transformer's 50-MVA thermal rating becomes the limiting factor at approximately 45.6 MW, before the selected 0.95-pu voltage criterion is reached.

**Tools:** PowerWorld Simulator, load flow, contingency analysis, transformer loading, voltage checks, scenario-based capacity planning.

**Scope:** Conceptual training/portfolio study; not for construction.
