# Skill Versions

This file is the version index for every skill in this repository. It exists so that you, or an
agent acting for you, can compare an installed copy against what is published here and decide
whether an update is worth pulling. Each row names the skill, the role it ships under, its current
version, the date that version was published, and the path to its `SKILL.md`.

Dates are DD-MM-YYYY.

## How versions are bumped

1. **Patch** (1.0.0 to 1.0.1) for wording, typos, formatting, or clarified examples. Behaviour is
   unchanged, so an existing user notices nothing.
2. **Minor** (1.0.0 to 1.1.0) for a new capability: an added step, a new reference file, a wider
   trigger in the `description`. Everything that worked before still works the same way.
3. **Major** (1.0.0 to 2.0.0) for a behaviour change that would surprise someone already using the
   skill: a different output format, a removed step, a rewritten workflow, or a narrowed trigger.

When you change a skill, bump its version here and set the date to the day the change ships. The
plugin version in `.claude-plugin/plugin.json` covers the collection as a whole and is bumped
separately when the published bundle changes.

## Skills

| Skill | Role | Version | Last updated | Path |
| --- | --- | --- | --- | --- |
| audit-workpaper | accountant | 1.0.0 | 09-08-2026 | `skills/by-role/accountant/audit-workpaper` |
| budget-variance-analysis | accountant | 1.0.0 | 09-08-2026 | `skills/by-role/accountant/budget-variance-analysis` |
| financial-statement-review | accountant | 1.0.0 | 09-08-2026 | `skills/by-role/accountant/financial-statement-review` |
| month-end-close | accountant | 1.0.0 | 09-08-2026 | `skills/by-role/accountant/month-end-close` |
| tax-position-memo | accountant | 1.0.0 | 09-08-2026 | `skills/by-role/accountant/tax-position-memo` |
| acceptance-criteria-writer | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/acceptance-criteria-writer` |
| brd-writer | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/brd-writer` |
| cost-benefit-analysis | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/cost-benefit-analysis` |
| data-dictionary | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/data-dictionary` |
| decision-matrix | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/decision-matrix` |
| frd-writer | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/frd-writer` |
| gap-analysis | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/gap-analysis` |
| impact-assessment | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/impact-assessment` |
| process-mapper | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/process-mapper` |
| requirements-elicitation | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/requirements-elicitation` |
| root-cause-analysis | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/root-cause-analysis` |
| stakeholder-map | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/stakeholder-map` |
| traceability-matrix | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/traceability-matrix` |
| uat-plan | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/uat-plan` |
| use-case-writer | business-analyst | 1.0.0 | 09-08-2026 | `skills/by-role/business-analyst/use-case-writer` |
| client-proposal | consultant | 1.0.0 | 09-08-2026 | `skills/by-role/consultant/client-proposal` |
| engagement-scoping | consultant | 1.0.0 | 09-08-2026 | `skills/by-role/consultant/engagement-scoping` |
| exec-summary | consultant | 1.0.0 | 09-08-2026 | `skills/by-role/consultant/exec-summary` |
| findings-presentation | consultant | 1.0.0 | 09-08-2026 | `skills/by-role/consultant/findings-presentation` |
| issue-tree | consultant | 1.0.0 | 09-08-2026 | `skills/by-role/consultant/issue-tree` |
| status-report | consultant | 1.0.0 | 09-08-2026 | `skills/by-role/consultant/status-report` |
| churn-risk-analysis | customer-success | 1.0.0 | 09-08-2026 | `skills/by-role/customer-success/churn-risk-analysis` |
| escalation-playbook | customer-success | 1.0.0 | 09-08-2026 | `skills/by-role/customer-success/escalation-playbook` |
| expansion-discovery | customer-success | 1.0.0 | 09-08-2026 | `skills/by-role/customer-success/expansion-discovery` |
| health-scorecard | customer-success | 1.0.0 | 09-08-2026 | `skills/by-role/customer-success/health-scorecard` |
| onboarding-plan | customer-success | 1.0.0 | 09-08-2026 | `skills/by-role/customer-success/onboarding-plan` |
| qbr-deck | customer-success | 1.0.0 | 09-08-2026 | `skills/by-role/customer-success/qbr-deck` |
| etl-runbook | data-engineer | 1.0.0 | 09-08-2026 | `skills/by-role/data-engineer/etl-runbook` |
| pipeline-design-doc | data-engineer | 1.0.0 | 09-08-2026 | `skills/by-role/data-engineer/pipeline-design-doc` |
| schema-spec | data-engineer | 1.0.0 | 09-08-2026 | `skills/by-role/data-engineer/schema-spec` |
| data-story | data-scientist | 1.0.0 | 09-08-2026 | `skills/by-role/data-scientist/data-story` |
| eda-report | data-scientist | 1.0.0 | 09-08-2026 | `skills/by-role/data-scientist/eda-report` |
| experiment-design | data-scientist | 1.0.0 | 09-08-2026 | `skills/by-role/data-scientist/experiment-design` |
| feature-engineering | data-scientist | 1.0.0 | 09-08-2026 | `skills/by-role/data-scientist/feature-engineering` |
| model-card | data-scientist | 1.0.0 | 09-08-2026 | `skills/by-role/data-scientist/model-card` |
| component-spec | designer | 1.0.0 | 09-08-2026 | `skills/by-role/designer/component-spec` |
| design-critique | designer | 1.0.0 | 09-08-2026 | `skills/by-role/designer/design-critique` |
| design-system-doc | designer | 1.0.0 | 09-08-2026 | `skills/by-role/designer/design-system-doc` |
| figma-copy-rewriter | designer | 1.0.0 | 09-08-2026 | `skills/by-role/designer/figma-copy-rewriter` |
| interactive-flowchart-builder | designer | 1.0.0 | 09-08-2026 | `skills/by-role/designer/interactive-flowchart-builder` |
| ux-audit | designer | 1.0.0 | 09-08-2026 | `skills/by-role/designer/ux-audit` |
| deployment-checklist | devops | 1.0.0 | 09-08-2026 | `skills/by-role/devops/deployment-checklist` |
| incident-response | devops | 1.0.0 | 09-08-2026 | `skills/by-role/devops/incident-response` |
| postmortem | devops | 1.0.0 | 09-08-2026 | `skills/by-role/devops/postmortem` |
| runbook | devops | 1.0.0 | 09-08-2026 | `skills/by-role/devops/runbook` |
| api-design | engineer | 1.0.0 | 09-08-2026 | `skills/by-role/engineer/api-design` |
| code-review | engineer | 1.0.0 | 09-08-2026 | `skills/by-role/engineer/code-review` |
| debug | engineer | 1.0.0 | 09-08-2026 | `skills/by-role/engineer/debug` |
| karpathy-guidelines | engineer | 1.0.0 | 09-08-2026 | `skills/by-role/engineer/karpathy-guidelines` |
| pr-description | engineer | 1.0.0 | 09-08-2026 | `skills/by-role/engineer/pr-description` |
| tech-debt | engineer | 1.0.0 | 09-08-2026 | `skills/by-role/engineer/tech-debt` |
| write-tests | engineer | 1.0.0 | 09-08-2026 | `skills/by-role/engineer/write-tests` |
| business-model-canvas | founder | 1.0.0 | 09-08-2026 | `skills/by-role/founder/business-model-canvas` |
| customer-discovery | founder | 1.0.0 | 09-08-2026 | `skills/by-role/founder/customer-discovery` |
| fundraising-email | founder | 1.0.0 | 09-08-2026 | `skills/by-role/founder/fundraising-email` |
| investor-update | founder | 1.0.0 | 09-08-2026 | `skills/by-role/founder/investor-update` |
| pitch-narrative | founder | 1.0.0 | 09-08-2026 | `skills/by-role/founder/pitch-narrative` |
| feedback-delivery | leadership | 1.0.0 | 09-08-2026 | `skills/by-role/leadership/feedback-delivery` |
| leadership-transition | leadership | 1.0.0 | 09-08-2026 | `skills/by-role/leadership/leadership-transition` |
| one-on-one | leadership | 1.0.0 | 09-08-2026 | `skills/by-role/leadership/one-on-one` |
| psychological-safety | leadership | 1.0.0 | 09-08-2026 | `skills/by-role/leadership/psychological-safety` |
| team-health-check | leadership | 1.0.0 | 09-08-2026 | `skills/by-role/leadership/team-health-check` |
| team-multiplier | leadership | 1.0.0 | 09-08-2026 | `skills/by-role/leadership/team-multiplier` |
| ab-copy-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/ab-copy-writer` |
| ad-campaign-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/ad-campaign-writer` |
| brand-context | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/brand-context` |
| campaign-brief | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/campaign-brief` |
| case-study-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/case-study-writer` |
| competitor-analyst | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/competitor-analyst` |
| content-repurposer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/content-repurposer` |
| content-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/content-writer` |
| copy-review | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/copy-review` |
| customer-persona | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/customer-persona` |
| customer-research | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/customer-research` |
| email-nurture | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/email-nurture` |
| growth-experiment | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/growth-experiment` |
| icp-research | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/icp-research` |
| kpi-review | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/kpi-review` |
| landing-page-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/landing-page-writer` |
| linkedin-post | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/linkedin-post` |
| messaging-framework | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/messaging-framework` |
| newsletter-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/newsletter-writer` |
| page-cro | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/page-cro` |
| positioning-doc | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/positioning-doc` |
| ppt-maker | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/ppt-maker` |
| pr-pitch-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/pr-pitch-writer` |
| press-release-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/press-release-writer` |
| retro | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/retro` |
| seo-article-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/seo-article-writer` |
| social-calendar | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/social-calendar` |
| thought-leadership-writer | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/thought-leadership-writer` |
| webinar-planner | marketing | 2.0.0 | 09-08-2026 | `skills/by-role/marketing/webinar-planner` |
| 11-star-framework | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/11-star-framework` |
| competitive-analysis | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/competitive-analysis` |
| compliance-auditor | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/compliance-auditor` |
| discovery-interview-prep | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/discovery-interview-prep` |
| epic-breakdown | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/epic-breakdown` |
| experiment-design | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/experiment-design` |
| feature-spec | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/feature-spec` |
| go-to-market-checklist | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/go-to-market-checklist` |
| meeting-to-spec-update | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/meeting-to-spec-update` |
| okr-writer | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/okr-writer` |
| opportunity-solution-tree | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/opportunity-solution-tree` |
| outcome-vs-output | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/outcome-vs-output` |
| persona-updater | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/persona-updater` |
| pilot-debrief | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/pilot-debrief` |
| pm-weekly-update | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/pm-weekly-update` |
| prioritization | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/prioritization` |
| product-discovery | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/product-discovery` |
| product-market-fit | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/product-market-fit` |
| product-thinking | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/product-thinking` |
| release-notes-writer | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/release-notes-writer` |
| retention-design | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/retention-design` |
| retro-synthesizer | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/retro-synthesizer` |
| risk-register | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/risk-register` |
| spec-reviewer | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/spec-reviewer` |
| spec-to-ux-tasks | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/spec-to-ux-tasks` |
| stakeholder-update | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/stakeholder-update` |
| team-brief | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/team-brief` |
| write-prd | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/write-prd` |
| write-user-stories | pm | 1.0.0 | 09-08-2026 | `skills/by-role/pm/write-user-stories` |
| delivery-risk-review | program-delivery-manager | 1.0.0 | 09-08-2026 | `skills/by-role/program-delivery-manager/delivery-risk-review` |
| dependency-mapping | program-delivery-manager | 1.0.0 | 09-08-2026 | `skills/by-role/program-delivery-manager/dependency-mapping` |
| flow-metrics-review | program-delivery-manager | 1.0.0 | 09-08-2026 | `skills/by-role/program-delivery-manager/flow-metrics-review` |
| milestone-scoping | program-delivery-manager | 1.0.0 | 09-08-2026 | `skills/by-role/program-delivery-manager/milestone-scoping` |
| program-status-report | program-delivery-manager | 1.0.0 | 09-08-2026 | `skills/by-role/program-delivery-manager/program-status-report` |
| release-planning | program-delivery-manager | 1.0.0 | 09-08-2026 | `skills/by-role/program-delivery-manager/release-planning` |
| exploratory-testing | qa | 1.0.0 | 09-08-2026 | `skills/by-role/qa/exploratory-testing` |
| qa-execution | qa | 1.0.0 | 09-08-2026 | `skills/by-role/qa/qa-execution` |
| qa-metrics | qa | 1.0.0 | 09-08-2026 | `skills/by-role/qa/qa-metrics` |
| qa-release | qa | 1.0.0 | 09-08-2026 | `skills/by-role/qa/qa-release` |
| qa-strategy | qa | 1.0.0 | 09-08-2026 | `skills/by-role/qa/qa-strategy` |
| qa-test-design | qa | 1.0.0 | 09-08-2026 | `skills/by-role/qa/qa-test-design` |
| risk-based-testing | qa | 1.0.0 | 09-08-2026 | `skills/by-role/qa/risk-based-testing` |
| candidate-debrief | recruiter | 1.0.0 | 09-08-2026 | `skills/by-role/recruiter/candidate-debrief` |
| intake-meeting | recruiter | 1.0.0 | 09-08-2026 | `skills/by-role/recruiter/intake-meeting` |
| interview-scorecard | recruiter | 1.0.0 | 09-08-2026 | `skills/by-role/recruiter/interview-scorecard` |
| job-description | recruiter | 1.0.0 | 09-08-2026 | `skills/by-role/recruiter/job-description` |
| offer-letter | recruiter | 1.0.0 | 09-08-2026 | `skills/by-role/recruiter/offer-letter` |
| sourcing-strategy | recruiter | 1.0.0 | 09-08-2026 | `skills/by-role/recruiter/sourcing-strategy` |
| hypothesis-framing | researcher | 1.0.0 | 09-08-2026 | `skills/by-role/researcher/hypothesis-framing` |
| literature-review | researcher | 1.0.0 | 09-08-2026 | `skills/by-role/researcher/literature-review` |
| study-design | researcher | 1.0.0 | 09-08-2026 | `skills/by-role/researcher/study-design` |
| account-plan | sales | 1.0.0 | 09-08-2026 | `skills/by-role/sales/account-plan` |
| deal-qualification | sales | 1.0.0 | 09-08-2026 | `skills/by-role/sales/deal-qualification` |
| discovery-call | sales | 1.0.0 | 09-08-2026 | `skills/by-role/sales/discovery-call` |
| objection-handling | sales | 1.0.0 | 09-08-2026 | `skills/by-role/sales/objection-handling` |
| sales-proposal | sales | 1.0.0 | 09-08-2026 | `skills/by-role/sales/sales-proposal` |
| pentest-scope | security | 1.0.0 | 09-08-2026 | `skills/by-role/security/pentest-scope` |
| threat-model | security | 1.0.0 | 09-08-2026 | `skills/by-role/security/threat-model` |
| vuln-report | security | 1.0.0 | 09-08-2026 | `skills/by-role/security/vuln-report` |
| confluence-to-md | shared | 1.0.0 | 09-08-2026 | `skills/shared/confluence-to-md` |
| diagram-generator | shared | 1.0.0 | 09-08-2026 | `skills/shared/diagram-generator` |
| draft-email | shared | 1.0.0 | 09-08-2026 | `skills/shared/draft-email` |
| jira-ticket-creator | shared | 1.0.0 | 09-08-2026 | `skills/shared/jira-ticket-creator` |
| md-to-confluence | shared | 1.0.0 | 09-08-2026 | `skills/shared/md-to-confluence` |
| presentation-builder | shared | 1.0.0 | 09-08-2026 | `skills/shared/presentation-builder` |
| youtube-transcript | shared | 1.0.0 | 09-08-2026 | `skills/shared/youtube-transcript` |

Total: 163 skills. 134 at 1.0.0, 29 at 2.0.0 (the marketing skills, rebuilt on 09-08-2026).
