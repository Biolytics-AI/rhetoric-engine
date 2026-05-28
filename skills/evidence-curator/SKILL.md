---
name: evidence-curator
description: Use after claims and slide theses are known to build a claim-evidence matrix, rank evidence, choose primary and backup evidence, document provenance, and expose evidence gaps.
---

# Evidence Curator

Curate proof so every claim has credible, audience-legible support. Separate primary evidence, backup evidence, provenance, and gaps.

## Inputs

- Approved intent brief, insight artifact, argument spine, and slide thesis map.
- Available sources, data, research, examples, quotations, user notes, and constraints.
- Audience trust standards, domain norms, objections, and source restrictions.
- Visual reasoning or cognitive design notes when evidence must support a specific slide treatment.

## Outputs

Return an `Evidence Dossier` with:

- `claim_evidence_matrix`: each claim, required proof job, available evidence, strength, caveats, and source.
- `per_slide_evidence_choice`: primary evidence selected for each slide thesis and why.
- `source_provenance_notes`: origin, date, author, method, reliability, permissions, and citation needs.
- `backup_evidence`: secondary proof for likely objections, appendix use, or Q&A.
- `evidence_gaps`: missing, weak, stale, disputed, or unsupported claims that need sourcing or revision.

## Workflow

1. List every claim from the argument spine and slide thesis map.
2. Define the proof job for each claim: establish fact, quantify scale, compare options, show trend, validate cause, demonstrate example, or answer objection.
3. Match available evidence to claims and reject evidence that is merely interesting.
4. Rank evidence by relevance, credibility, recency, specificity, audience legibility, and resistance to challenge.
5. Choose one primary evidence item per slide where possible and assign backup evidence for likely objections.
6. Record provenance, caveats, permissions, and citation requirements.
7. Flag evidence gaps and recommend whether to source more, weaken the claim, move material to backup, or ask the user.

## Evaluation Checks

- Every important claim has evidence or an explicit gap.
- Primary evidence directly supports the slide thesis.
- Backup evidence prepares for objections without overloading the main flow.
- Source provenance is sufficient for review and citation.
- Weak, decorative, or irrelevant evidence is rejected.
- Evidence choices do not create new claims beyond the approved argument.

## Failure Modes

- Treating all available sources as equally strong.
- Using evidence because it is impressive but not claim-relevant.
- Hiding uncertainty, outdated sources, or provenance gaps.
- Overloading slides with proof that belongs in backup.
- Inventing evidence or citations.
- Choosing visuals or renderer-specific treatments instead of curating proof.

## Next Route

- If evidence gaps block an important claim: ask the user for sources, source more if tools permit, weaken the claim, or return to `argument-spine-builder` / `slide-thesis-mapper`.
- If the `Evidence Dossier` is complete and evidence affects visual form: load `visual-reasoner`.
- If the dossier is complete and evidence density or legibility is a risk: load `cognitive-designer` or `content-distiller`.
- If proof, design, visual reasoning, and content fit are sufficient: load `deck-compiler`.
- This artifact feeds the whole presentation by deciding what each claim can honestly prove, what belongs in backup, and what must remain caveated or unresolved.

## Handoff

Handoff the `Evidence Dossier` to `visual-reasoner`, `cognitive-designer`, or deck compilation. Include primary and backup evidence, provenance notes, and gaps so downstream work can prove claims without inventing or overstating support.
