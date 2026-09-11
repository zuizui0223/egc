# Eco-genetic criticality

A theorem-first research repository for finite-population eco-genetic criticality.

## Questions

- **H1:** When can interaction feedback alter potential high-trait viability?
- **H3:** At fixed total area, when do isolation, migration rescue, and migration erosion produce different trait and genetic outcomes?
- **State separation:** When do potential viability, realised occupancy,
  demographic state, diversity, and allele persistence respond differently to
  the same fragmentation contrast?

## Research architecture

```text
mathematical theorem
-> declared model projection
-> finite-population closure
-> simulation robustness test
-> state-representation boundary
-> empirical measurement design in the extension repository
```

Potential viability, realised trait occupancy, allele persistence, genetic diversity, and realised ecological function are distinct states.

## Final finite-model status

The active H1–H3 finite-model campaign is closed. Its canonical results and limits are recorded in [`docs/final_evidence_ledger.md`](docs/final_evidence_ledger.md).

- **H1:** mutation-conditioned interaction memory is supported as finite Type S evidence in the declared closure.
- **H3 / fragmentation:** conditional on valid H1 full-state transfer, equal isolation lowers interaction, local effective size, and realised high-trait mass before demographic disappearance.
- **H2-A:** fixed absolute diversity thresholds `H_alpha,H_gamma <= 0.20` are not retained as a robust canonical warning rule after the no-resimulation audit found mixed lead/lag ordering.
- **Historical H2-R benchmark:** baseline-relative `H_alpha/H_gamma` erosion preceded observed realised trait loss in the inherited calibrated symmetric domain. This event-conditioned ordering is preserved as parent evidence, but it does not establish discrimination, specificity, event-risk separation, or predictive warning validity.
- **Fragmentation-gradient state separation:** in a preregistered fresh-seed sensitivity, potential high-trait viability was lost at the first subdivision while realised occupancy persisted over the finite endpoint; interaction, local effective size, and realised high-trait mass then followed different gradient shapes.

## State-sufficiency result

Under the declared simulator closure, the complete explicit present state together with future forcing and the stochastic law is Markov/future-sufficient. This is a theorem about the declared model representation, not a claim that any usual ecological summary is sufficient in nature.

A constructive alignment audit shows why the distinction matters. Two states can share census, interaction and allele-frequency marginals, realised trait-bin state, `H_alpha`, `H_gamma`, and `F_ST` while differing in patchwise cross-layer alignment. Their exact next interaction transition can then differ substantially. The fixed long-horizon campaign did not establish a directional loss-incidence effect of alignment, so the result is a **representation boundary**, not a universal alignment-risk rule.

## Submission role

This repository is the **mechanistic evidence parent for Question 1 of the active Nature Ecology & Evolution flagship**. Question 1 asks whether fragmentation produces one biological deterioration state. EGC owns the theorem-guided interaction/fragmentation framework, the closed finite H1/H3 evidence ledger, state-sufficiency certificates, the fresh fragmentation-gradient sensitivity, and the inherited H2-R event-conditioned benchmark. The standalone state-separation manuscript is retained only as provenance/fallback material; it is not a separate active submission while the NEE flagship is the publication route.

The companion repository, [`egwe`](https://github.com/zuizui0223/egwe), owns **Question 2 of the same NEE flagship**: given state separation, what hidden organization and life-cycle operators determine divergent futures, and what continuous reserve carries fate information. The natural measurement/representation programme has moved to the separate [`egwee`](https://github.com/zuizui0223/egwee) repository.

The current reader-facing publication route for these EGC results is the NEE flagship rather than a separate EGC submission. H2-R remains a historical event-conditioned record, while full-denominator warning validity and later fate-ranking belong to EGWE Question 2.

The repositories remain separate computational provenance units. They are integrated at the argument, manuscript, reproducibility-contract, and release-package levels rather than by merging code or evidence ledgers.

## Reproduce and package

Start with [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md). The machine-readable scientific lock is [`reproducibility/release_manifest.json`](reproducibility/release_manifest.json).

A lightweight verification is:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev,reproducibility]'
python -m pytest
python scripts/verify_release_contract.py
python -m build
```

The `Submission reproducibility` workflow additionally smoke-tests the built wheel and uploads a checksummed release bundle. The canonical scientific commit remains `dd8ee379d0d3518194c767d16402042525bc00dc`; later packaging/README maintenance does not revise its scientific evidence.

The package version is currently `0.1.0`, matching the extension repository. Final release/citation metadata are coordinated from the extension release-readiness ledger and require explicit author approval before immutable tags or archive DOI creation.

## Maintenance command surface

The default branch is a maintenance/release surface rather than an active simulation campaign. Historical campaign-specific GitHub Actions workflows remain immutable in the canonical scientific commit instead of staying enabled on current `main`.

After installing the package, use the single `egc` entry point for the retained command-line interfaces:

```bash
egc --list
egc theorem-boundary --help
egc h2r-independent-validation --help
```

The former `scripts/run_*.py` convenience wrappers are intentionally removed from the maintenance head. Historical protocol documents preserve the original commands as provenance; check out the canonical scientific commit when exact historical execution is required. New maintenance work should not add one-off runner wrappers or new campaign workflows to this parent repository.

Only ordinary `CI` and `Submission reproducibility` workflows should remain active on the maintenance head.

## Manuscript synthesis

The retained paper-facing material in [`manuscript/`](manuscript/) preserves exact theorems, closure-conditional results and finite Type S state-separation results as provenance and reusable evidence. The active integrated manuscript is the NEE flagship in `zuizui0223/egwe`; predictive-warning validity is also owned there, while the natural-data measurement/representation synthesis is authoritative in `zuizui0223/egwee`.

## Current model layers

- `canonical_h1_bifurcation.py` gives the specified-system H1 certificate for the one-state logistic reduction: strict bistability, branch stability, and high-trait margin change.
- `first_passage_reporting.py` and `censoring_aware_phase_diagram.py` keep H2 warning lead probabilities, valid-pair denominators, and censored replicates distinct.
- `network_migration_matrix_theory.py` gives H3 allele-floor and focal-rescue bounds for arbitrary network mixing matrices.
- `network_h3_lifecycle.py` and `network_h3_experiments.py` add a separate finite-population H3 closure with individual dispersal, extinction, rescue, recolonisation, realised trait abundance, allele copies, and replicated event summaries.

The H3 lifecycle is a declared stochastic model, not a universal claim that connectivity is beneficial. It can represent migration rescue, migration erosion, or no material effect under different declared kernels and life-cycle parameters. See `docs/h3_extinction_recolonisation_lifecycle.md`.

## Repository ownership boundary

This repository is the sole owner of eco-genetic criticality code and parent evidence. RACH N1–N4 channel identifiability, theorem-to-model projection, and next-observation design remain owned by [`zuizui0223/microdonta`](https://github.com/zuizui0223/microdonta). Cross-program context must use a link or an explicit adapter, not a duplicate implementation.

## Scope and stop rule

This repository closes the active H1–H3 theorem and finite-bin closure programme migrated from `microdonta`. Further biological closures, mutation models, threshold choices, or deterioration schedules must be separately declared extensions rather than silent revisions of the final evidence ledger.

Do not reopen simulator parameter/seed tuning merely to obtain a preferred empirical or warning result. New biological evidence belongs in prospectively declared extension work; parent maintenance should preserve the canonical scientific commit and release provenance.
