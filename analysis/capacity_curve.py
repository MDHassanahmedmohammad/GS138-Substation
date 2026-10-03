import csv
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader(open(ROOT / "results" / "study_results.csv", encoding="utf-8")))
x = [float(r["growth_pct"]) for r in rows]
y = [float(r["n1_surviving_transformer_loading_pct"]) for r in rows]

fig, ax = plt.subplots(figsize=(9.5, 5.4))
ax.plot(x, y, marker="o", linewidth=2)
ax.axhline(100, linestyle="--", linewidth=1.5, label="50 MVA thermal limit (100%)")
for xi, yi in zip(x, y):
    ax.annotate(f"{yi:.2f}%", (xi, yi), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=9)
ax.set_xlabel("Load growth above 40 MW base case (%)")
ax.set_ylabel("Surviving transformer loading under N-1 (%)")
ax.set_title("GS138 N-1 Capacity Boundary")
ax.grid(True, alpha=0.25)
ax.legend(loc="upper left")
ax.set_ylim(84, 103)
fig.tight_layout()
fig.savefig(ROOT / "figures" / "capacity_curve.png", dpi=220, bbox_inches="tight")
