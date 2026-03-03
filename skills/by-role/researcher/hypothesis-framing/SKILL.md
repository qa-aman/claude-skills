---
name: hypothesis-framing
description: >
  Write or refine a research hypothesis. Use when the user says "write a hypothesis",
  "frame my hypothesis", "is my hypothesis testable", "null and alternative hypothesis",
  "research hypothesis", "refine my hypothesis", "hypothesis statement", "H0 and H1",
  "operationalize my hypothesis", "turn my research question into a hypothesis",
  or needs to convert a research question or intuition into a falsifiable, testable
  hypothesis with clear variables and predictions - even if they don't explicitly say "hypothesis".
---

## Overview

Based on **Research Design** (Creswell & Creswell) and **Research Methodology: A Step-by-Step Guide** (Ranjit Kumar). A hypothesis is a falsifiable prediction about the relationship between variables. Kumar's rule: a hypothesis that cannot be proven wrong is not a hypothesis - it is a belief. Creswell's standard: every hypothesis must specify the population, the variables, and the predicted direction of the relationship.

The test: can a different researcher, given only the hypothesis, design a study to test it?

## Workflow

### Step 1: Identify the research question

Start with the question before writing the hypothesis. The hypothesis is the answer you predict the study will find.

```
Research question: [what are you trying to find out?]
Domain: [field of study]
Context: [setting, population, conditions]
Prior evidence: [what makes this prediction plausible? what is it based on?]
```

A good research question has:
- A specific population (not "people" but "adults over 65 with Type 2 diabetes")
- A specific phenomenon or variable being studied
- A clear "compared to what" or "under what conditions"

### Step 2: Identify and operationalize variables

Variables must be measurable. For each variable, define how it is measured:

```
Independent variable (IV): [what you manipulate or group by]
  Operationalization: [how exactly it is measured or defined]
  Levels/values: [if categorical: list levels. if continuous: range and units]

Dependent variable (DV): [what you measure as an outcome]
  Operationalization: [specific measure, scale, or instrument]
  Units: [e.g. seconds, score 1-7 on Likert scale, binary yes/no]

Control variables: [variables held constant or statistically controlled]
  [variable]: [how controlled]

Potential confounds: [variables that could explain results without being your IV]
  [confound]: [how you plan to address it]
```

### Step 3: Write the directional hypothesis

A well-formed hypothesis has three components:
1. **Population**: who or what
2. **Predicted relationship**: direction and nature
3. **Variables**: IV and DV named precisely

Format: "In [population], [IV manipulation or condition] will result in [predicted change in DV direction] compared to [control or comparison condition]."

Examples:
- "Participants who receive spaced-repetition training will score significantly higher on a 30-item vocabulary test at 2-week follow-up than participants who receive massed-practice training."
- "Remote engineering teams using structured async standup tools will report lower meeting fatigue (measured by the Meeting Load Index) than teams using synchronous daily standups."

### Step 4: Write null and alternative hypotheses

```
H₀ (Null hypothesis): There is no significant difference/relationship between [IV] and [DV]
in [population].

H₁ (Alternative hypothesis - directional): [IV] is associated with [higher/lower/more/less]
[DV] in [population].

Or (non-directional):
H₁ (Alternative hypothesis): There is a significant difference in [DV] between [IV
conditions] in [population].

Use directional H₁ when: prior theory or evidence strongly predicts the direction
Use non-directional H₁ when: this is exploratory or direction is genuinely uncertain
```

### Step 5: State the theoretical basis

Explain what mechanism you expect to be driving the predicted effect:

```
Theoretical basis: [What theory or prior finding predicts this result?]
Mechanism: [Why would X cause Y? What is the causal pathway?]
Prior evidence: [1-3 citations showing related findings that support this prediction]
Boundary conditions: [Under what conditions do you expect this to hold? Under what conditions might it not?]
```

### Step 6: Check falsifiability and precision

Run through these questions before finalizing:

1. **Falsifiable**: What result would prove this hypothesis wrong? (If you can't answer, it's not falsifiable)
2. **Specific**: Does it name the population, IV, DV, and direction?
3. **Testable**: Can the variables be measured with available instruments?
4. **Grounded**: Is there a theoretical or empirical reason to predict this relationship?
5. **Appropriately scoped**: Is it narrow enough to test in one study?

If any answer is "no" or "I'm not sure," revise before proceeding to study design.

## Anti-Patterns

**1. Research question disguised as hypothesis**
Bad: "Does social media use affect mental health?"
Good: "Adolescents aged 13-17 who use social media for more than 3 hours/day will report significantly higher levels of anxiety (GAD-7 scale) than those who use social media for less than 1 hour/day."

**2. Unmeasurable variables**
Bad: "Students who feel more motivated will learn better."
Good: "Students in the gamified learning condition (IV) will score higher on the Unit 4 end-of-module test (DV, 20 items, % correct) than students in the standard condition."

**3. No stated direction**
Bad: "There will be a relationship between exercise and mood."
Good: "Adults who engage in 30 minutes of aerobic exercise 5 days per week will report lower depressive symptoms (PHQ-9) than sedentary controls after 8 weeks."

**4. Hypothesis without mechanism**
Bad: Hypothesis states a prediction with no theory behind it.
Good: Include the theoretical mechanism (e.g., cognitive load theory predicts..., self-determination theory suggests...) so reviewers can evaluate the rationale.

## Quality Checklist

- [ ] Research question is specific (named population, phenomenon, comparison)
- [ ] IV and DV are both operationalized with specific measurement definitions
- [ ] Control variables and potential confounds are listed
- [ ] H₀ and H₁ are both stated explicitly
- [ ] H₁ is directional when prior evidence supports a direction
- [ ] Hypothesis names population, IV, DV, and predicted direction
- [ ] Theoretical basis and causal mechanism are stated
- [ ] Hypothesis is falsifiable (can state what would disprove it)
- [ ] Variables are measurable with available instruments
