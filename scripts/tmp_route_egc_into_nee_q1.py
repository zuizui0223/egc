from pathlib import Path

p = Path('README.md')
text = p.read_text(encoding='utf-8')

def rep(old, new):
    global text
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'anchor count {n}: {old[:100]!r}')
    text = text.replace(old, new, 1)

rep(
"This repository is the **mechanistic parent** of the integrated Letter manuscript and the source of a standalone state-separation manuscript. It owns the theorem-guided interaction/fragmentation framework, the closed finite H1/H3 evidence ledger, state-sufficiency certificates, the fresh fragmentation-gradient sensitivity, and the inherited H2-R event-conditioned benchmark.",
"This repository is the **mechanistic evidence parent for Question 1 of the active Nature Ecology & Evolution flagship**. Question 1 asks whether fragmentation produces one biological deterioration state. EGC owns the theorem-guided interaction/fragmentation framework, the closed finite H1/H3 evidence ledger, state-sufficiency certificates, the fresh fragmentation-gradient sensitivity, and the inherited H2-R event-conditioned benchmark. The standalone state-separation manuscript is retained only as provenance/fallback material; it is not a separate active submission while the NEE flagship is the publication route."
)
rep(
"The companion repository, [`eco-genetic-warning-extensions`](https://github.com/zuizui0223/eco-genetic-warning-extensions), is now the **condition-recovery, warning-replication/portability, state-representation, natural state-sufficiency, integrated-manuscript, and submission-bundle repository**. Its empirical programme tests whether candidate ecological state variables predict their downstream endpoints before asking whether geography or fragmentation history adds residual information.",
"The companion repository, [`egwe`](https://github.com/zuizui0223/egwe), owns **Question 2 of the same NEE flagship**: given state separation, what hidden organization and life-cycle operators determine divergent futures, and what continuous reserve carries fate information. The natural measurement/representation programme has moved to the separate [`egwee`](https://github.com/zuizui0223/egwee) repository."
)
rep(
"The standalone parent submission does **not** use H2-R as a headline or\npredictive-validity claim. Its active claim set is interaction bistability,\nmigration bounds, finite fragmentation effects, and explicit separation of\npotential viability, realised occupancy, demographic state, diversity, and\nallele persistence. H2-R remains a historical event-conditioned record.\nFull-denominator warning validity belongs to the extension repository.",
"The current reader-facing publication route for these EGC results is the NEE flagship rather than a separate EGC submission. H2-R remains a historical event-conditioned record, while full-denominator warning validity and later fate-ranking belong to EGWE Question 2."
)
rep(
"The standalone parent paper-facing material is in [`manuscript/`](manuscript/).\nIt separates exact theorems, closure-conditional results, and finite Type S\nstate-separation results. The H2-R ordering remains available in the historical\nledger and supplement but is outside the standalone headline claim set. The\nintegrated manuscript, predictive-warning validity audit, and current\nnatural-data synthesis live in the extension repository.",
"The retained paper-facing material in [`manuscript/`](manuscript/) preserves exact theorems, closure-conditional results and finite Type S state-separation results as provenance and reusable evidence. The active integrated manuscript is the NEE flagship in `zuizui0223/egwe`; predictive-warning validity is also owned there, while the natural-data measurement/representation synthesis is authoritative in `zuizui0223/egwee`."
)
p.write_text(text, encoding='utf-8')
print('routed EGC into NEE Question 1')
