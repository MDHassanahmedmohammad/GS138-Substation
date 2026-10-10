# GS138 138/34.5-kV Substation Technical Report

**Author:** Hassan Ahmed Mohammad  
**Study type:** Conceptual portfolio / academic engineering study  
**Primary software:** PowerWorld Simulator

## 1. Objective

Develop a conceptual 138/34.5-kV two-transformer substation model and evaluate performance under normal operation, single-transformer contingencies, corrective bus-tie transfer, and future load growth. The study focuses on transformer utilization, service continuity, voltage performance, and the approximate N-1 capacity limit.

## 2. Modeled system

- Two 138/34.5-kV transformers, T1 and T2, rated 50 MVA each.
- Two 34.5-kV bus sections, Bus A and Bus B.
- Normally open 34.5-kV bus tie.
- Three loads connected to each bus section.
- Base station load: 40.00 MW / 13.15 Mvar at approximately 0.95 power factor.
- Normal topology: both transformers in service; bus tie open.
- Corrective N-1 topology: one transformer open; bus tie closed.

## 3. Base-case power flow

| Quantity | Result |
|---|---:|
| Total station load | 40.00 MW |
| Total reactive load | 13.15 Mvar |
| Power factor | ~0.95 |
| T1 loading | 42.80% |
| T2 loading | 42.80% |
| Bus A voltage | ~0.9838 pu |
| Bus B voltage | ~0.9838 pu |
| Bus tie | Open |

The base case shows balanced loading between the two transformers and acceptable modeled voltage.

## 4. N-1 contingency analysis

Two symmetrical contingencies were evaluated:

1. **T1_Out_TIE_CLOSE** — open T1 and close the Bus A-B tie.
2. **T2_Out_TIE_CLOSE** — open T2 and close the Bus A-B tie.

At the 40-MW base load, either contingency increases the surviving transformer loading to approximately **87.24%**, or about **43.62 MVA**, while maintaining service to both bus sections.

| Contingency | Surviving transformer | Loading | Result |
|---|---|---:|---|
| T1 out + tie closed | T2 | 87.24% | Pass |
| T2 out + tie closed | T1 | 87.24% | Pass |

## 5. Load-growth analysis

Loads were increased while maintaining approximately the same P/Q ratio, and the two transformer-out contingencies were repeated.

| Growth | Total MW | N-1 transformer loading | Result |
|---|---:|---:|---|
| 0% | 40.00 | 87.24% | Pass |
| +10% | 44.00 | 96.36% | Pass |
| +13.9% | 45.56 | 99.94% | Pass / boundary |
| +14.0% | 45.60 | 100.04% | Fail |
| +15.0% | 46.00 | 100.96% | Fail |

The modeled N-1 thermal boundary is therefore approximately **45.6 MW**, or about **14% above the 40-MW base load**.

## 6. Voltage check at the boundary

At approximately +13.9% load growth with one transformer out and the bus tie closed, the surviving transformer carried approximately **49.97 MVA (99.94%)** and the 34.5-kV bus voltage was approximately **0.95967 pu**.

Equivalent line-to-line voltage:

```
34.5 kV × 0.95967 ≈ 33.11 kV
```

Using 0.95 pu as the selected study criterion, the modeled voltage remains above the criterion. Therefore, in this simplified study, the transformer thermal rating becomes limiting before the 0.95-pu voltage criterion is reached.

## 7. Engineering conclusion

The modeled substation operates comfortably at the 40-MW base loading condition. Under loss of either transformer, closing the normally open 34.5-kV bus tie allows the surviving transformer to supply both bus sections at approximately 87.24% loading. Load-growth testing places the approximate N-1 thermal capacity boundary near 45.6 MW. At 45.56 MW, the surviving transformer reaches 99.94% loading while the post-contingency bus voltage remains approximately 0.9597 pu. At 45.60 MW, the transformer exceeds its 50-MVA limit.

## 8. Scope and limitations

This is a conceptual portfolio/training study, not an issued-for-construction design. It does not include short-circuit duty, protection coordination, relay settings, grounding, arc-flash, insulation coordination, equipment procurement specifications, physical layout, cable ampacity, transient/dynamic stability, or a verified automatic transfer scheme.

The 0.95-pu voltage threshold is a selected study criterion and is not presented as a utility-specific requirement.
