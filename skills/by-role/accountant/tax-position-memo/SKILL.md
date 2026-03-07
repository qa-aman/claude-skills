---
name: tax-position-memo
description: >
  Write a technical tax position memo that documents a tax filing position with
  authorities, facts, analysis, and conclusion. Use when a tax professional says
  "write a tax memo", "document this tax position", "research memo for the partner",
  "we need to support this deduction", "document the tax treatment", "write up the
  authority for this position", "technical memo on [tax issue]", "MLTN analysis",
  "reasonable basis memo", "document the IRC section that supports this", or needs
  to formally document a tax conclusion. Also trigger when someone has a tax
  question that needs a written conclusion backed by legal authority - even if they
  don't use the words "tax memo" or "tax position".
---

## Reference Files

- `references/authority-hierarchy.md` - Complete federal tax authority hierarchy (IRC through treatises), confidence thresholds (MLTN, substantial authority, reasonable basis), penalty exposure by level, and disclosure form guidance. Read this in Step 3 when compiling authorities and in Step 5 when stating the confidence level and disclosure requirement.

## Overview

Based on **"Federal Tax Research"** by Sawyers and Gill - the standard reference for tax research methodology. A tax position memo is the written record that a tax position meets the applicable confidence standard: substantial authority, more-likely-than-not (MLTN), or reasonable basis. If the IRS examines the return, the memo is the evidence that the position was not taken recklessly.

The FIRAC structure (Facts, Issue, Rule/Authority, Analysis, Conclusion) is the professional standard for tax memos. The analysis section is the most important: it applies the authority to the specific facts. A memo that cites authority without applying it to the facts is not a tax memo - it is a list of citations.

## Workflow

### Step 1: State the facts

Write a precise, complete statement of the relevant facts. Do not include irrelevant facts. Do not omit facts that are unfavorable to the position.

```
FACTS

[Client / entity name and entity type (LLC, S-Corp, C-Corp, individual)]
[Tax year(s) at issue]
[Transaction description: what happened, when, who was involved, amounts]
[Relevant background: industry, prior treatment of similar items, elections in effect]
[Unfavorable facts that must be addressed: any facts that cut against the position]
```

Rules for the facts section:
- State facts, not conclusions. "The company paid $500K to a related party" is a fact. "The payment was an arm's-length royalty" is a conclusion.
- Include dollar amounts and dates. Vague facts produce vulnerable positions.
- Disclose unfavorable facts. A memo that omits contrary facts will not withstand scrutiny.

### Step 2: State the issue

Write the tax question as a single, precise sentence. The conclusion will directly answer this question.

```
ISSUE
Whether [the $500K payment / the loss deduction / the exclusion / etc.] qualifies
as [deductible / excludable / capitalizable / etc.] under [IRC section or applicable authority]
for the [year] tax year.
```

One issue per memo. If there are two issues, write two memos (or two separate FIRAC sections). Conflating issues muddies the analysis and makes the memo harder to defend.

### Step 3: Compile the authorities

List the primary and secondary authorities in priority order. Apply them in the analysis section - do not mix authority listing with application.

```
AUTHORITIES

Primary (binding or highly persuasive):
- Internal Revenue Code: section [X] - [brief description of what it covers]
- Treasury Regulations: section [X] - [brief description]
- Revenue Rulings: Rev. Rul. [year-number] - [brief description, holding relevant to this issue]
- Court cases: [Case name], [citation] ([court, year]) - [holding and relevance]

Secondary (persuasive, not binding):
- IRS Notices / Announcements: Notice [year-number] - [description]
- PLRs / CCAs (not precedent, but evidence of IRS thinking): PLR [number] - [description]
- Legislative history: [committee report, if relevant]
```

Note the confidence level each authority supports:
- Substantial authority (>40% chance of being sustained if challenged): requires primary sources
- More-likely-than-not (>50%): requires authorities that directly support the position on these facts
- Reasonable basis (>25%): lower bar; broader range of authorities

### Step 4: Write the analysis

Apply each authority to the specific facts. This is the substance of the memo.

```
ANALYSIS

[Start with the controlling authority and state what it requires]

Under IRC section [X], [quote or paraphrase the relevant operative language]. The
regulations under section [X] define [key term] as [definition]. [Cite: Treas. Reg. X.X-X(a)]

[Apply the authority to the facts]

In the present case, [specific facts] satisfy [statutory/regulatory requirement] because
[reason]. Specifically, [fact 1] establishes [element 1] and [fact 2] demonstrates
[element 2]. [Cite the supporting case or ruling if applicable]

[Address contrary authorities or unfavorable facts]

The IRS argued in [contrary case] that [contrary position]. However, [distinguishing
factor]: unlike the taxpayer in [case], [client] [specific distinguishing fact]. Therefore,
[case] does not control.

[Address the most significant unfavorable fact directly]

The most significant risk to this position is [unfavorable fact]. [Regulation / case]
is unfavorable on this point. However, [mitigating argument]. This risk [is/is not]
sufficient to reduce the confidence level below [substantial authority / MLTN].
```

The analysis must address every unfavorable authority or fact raised in the authorities section. A memo that ignores contrary authority is not credible.

### Step 5: Write the conclusion

The conclusion directly answers the issue. State the confidence level and the specific basis for it.

```
CONCLUSION

Based on the foregoing analysis, it is our conclusion that [restate the position -
e.g., "the $500K payment is deductible as a business expense under IRC section 162"].

Confidence level: [Substantial authority / More-likely-than-not / Reasonable basis]

This conclusion is supported by [IRC section X], [Treas. Reg. X.X-X], and [case / ruling].
The primary risk is [specific risk]. In our judgment, this risk does not reduce the
confidence level below [threshold] because [brief reason].

Disclosure: [Required / Not required] - [If substantial authority but below MLTN,
Form 8275 or 8275-R disclosure may be required. If MLTN, no disclosure required for
non-tax shelter positions.]

Prepared by: [name]   Date: [date]
Reviewed by: [name]   Date: [date]
```

## Anti-Patterns

**1. Analysis that lists authority without applying it**
Bad: "IRC section 162 allows deductions for ordinary and necessary business expenses. Rev. Rul. 79-24 addresses related-party payments."
Good: "IRC section 162 requires that a deductible expense be ordinary and necessary. The payment to [related party] meets this standard because [specific facts demonstrating the payment was customary and appropriate]. Rev. Rul. 79-24 held that related-party payments are deductible where arm's-length pricing is established - here, [client] obtained an independent valuation supporting the $500K amount."

**2. Omitting unfavorable authority**
Bad: Citing only the cases and rulings that support the position.
Good: A defensible memo identifies the most significant contrary authorities and explains why they are distinguishable. Omitting a directly contrary Revenue Ruling exposes the firm to malpractice risk.

**3. Conclusion without a confidence level**
Bad: "Based on the foregoing, we believe this position is supportable."
Good: State the specific confidence standard (substantial authority, MLTN, reasonable basis) and the basis for reaching it. "Supportable" is not a professional standard.

**4. Facts that are actually conclusions**
Bad: "The management fees paid to the parent were reasonable."
Good: "The company paid $2M in management fees to its parent in [year]. An independent benchmarking study obtained in [year] concluded that management fees of $1.8M-$2.2M were consistent with arm's-length pricing for comparable services."

**5. Missing disclosure analysis**
Bad: Concluding the memo without noting whether disclosure is required.
Good: Every tax memo should note the applicable confidence level and whether Form 8275 (non-tax shelter) or 8275-R (tax shelter) disclosure is required. Failure to disclose when required compounds penalty exposure.

## Quality Checklist

- [ ] Facts are complete, specific, and include unfavorable facts
- [ ] Issue is stated as a single, precise question
- [ ] Authorities listed in priority order (primary before secondary)
- [ ] Confidence level noted for each authority category
- [ ] Analysis applies authority to specific facts (not just summarizes authority)
- [ ] Contrary authorities identified and distinguished
- [ ] Most significant unfavorable fact addressed directly in the analysis
- [ ] Conclusion directly answers the issue
- [ ] Confidence level stated explicitly (substantial authority / MLTN / reasonable basis)
- [ ] Disclosure requirement addressed (Form 8275 / 8275-R / none required)
- [ ] Preparer and reviewer signatures documented
