# Marketing skills

29 skills for marketing teams. Writing, planning, positioning, research and review.

Every skill is grounded in a named book, and every skill is built to refuse to make things up.

## What makes these different

1. **They will not invent your numbers.** No skill here will write a statistic, a customer quote, a price, a competitor claim, or a benchmark it was not given. Where a fact is missing you get `[NEEDS INPUT: ...]` or `[PROOF NEEDED: ...]` in the draft, not a plausible-looking figure. This is the failure that makes marketing teams distrust AI output, and it is the thing these skills are most carefully built against.
2. **They get smarter about your business.** `/retro` writes evidence-tagged learnings into `knowledge/learnings.md` after each campaign, and six other skills read that file. Run it and the toolkit compounds. Skip it and the skills stay generic.
3. **They tell you what they cannot know.** Most skills end with a section naming what is outside their reach: current platform specs, whether a customer consented, whether a metric is still accurate, what needs legal review.
4. **They are grounded in named sources.** Dunford, Schwartz, Caples, Cialdini, Christensen, Minto, Ogilvy, Krug, Fitzpatrick, Knaflic, Berger, Chaffey, Heath, Miller, Zinsser and others. Each skill declares its source in frontmatter and works the method in the body, rather than name-dropping it.

## Start here, once per company or client

```
/brand-context
```

About ten minutes. It interviews you about voice, audience, positioning and targets, and writes the answers into a `knowledge/` folder. **Every other skill reads that folder.** Skip it and the output is competent but generic.

If you already have a website or a deck, say so and it will draft from those instead of asking you everything.

## Then just describe what you want

The right skill fires on its own. "Write a LinkedIn post about our new batch." "Plan next month's content." "Why isn't this page converting?" You can also invoke any skill directly with `/skill-name`.

Every skill saves a dated file under `output/<skill>/`, so work accumulates instead of scrolling away in chat.

## The 29 skills

**Set-up and research**
| Skill | What it produces |
|---|---|
| `brand-context` | The `knowledge/` files everything else reads. Run first. |
| `customer-research` | Verbatim customer quotes, pains, objections, and a they-say/we-say vocabulary table |
| `customer-persona` | One buyer persona, JTBD structure |
| `icp-research` | Segment and firmographic definition |
| `competitor-analyst` | ERRC grid and strategy canvas, where we win and where we lose |

**Positioning and message**
| Skill | What it produces |
|---|---|
| `positioning-doc` | Positioning statement via Dunford's five-step sequence |
| `messaging-framework` | Brand script and message hierarchy (StoryBrand SB7) |

**Plan**
| Skill | What it produces |
|---|---|
| `campaign-brief` | One campaign: phase, primary KPI, channels, timeline |
| `social-calendar` | A month of posts, quadrant-balanced, with an asset production queue |
| `growth-experiment` | A channel test with pre-committed thresholds |
| `webinar-planner` | End-to-end webinar plan |
| `kpi-review` | Period numbers turned into three ranked actions |
| `retro` | Five Whys on what missed or beat, appended to `knowledge/learnings.md` |

**Write**
| Skill | What it produces |
|---|---|
| `content-writer` | General marketing content, PAS or AIDA by awareness level |
| `landing-page-writer` | Full landing page, section by section |
| `linkedin-post` | One post, named hook formula, gap closed |
| `newsletter-writer` | One newsletter issue |
| `thought-leadership-writer` | Long-form POV essay (SUCCESs) |
| `seo-article-writer` | SEO long-form on a target keyword |
| `email-nurture` | Multi-email sequence with a named cadence |
| `ad-campaign-writer` | Paid ad copy by platform and awareness stage |
| `ab-copy-writer` | Copy variants with a hypothesis each |
| `case-study-writer` | Customer story, SCR structure |
| `press-release-writer` | AP-style release |
| `pr-pitch-writer` | Journalist pitch with a news peg |
| `content-repurposer` | One anchor asset into a multi-channel pack |
| `ppt-maker` | An actual `.pptx` off your brand template |

**Improve what exists**
| Skill | What it produces |
|---|---|
| `copy-review` | Six-pass edit with before and after scores |
| `page-cro` | Conversion diagnosis, ranked fixes, test plan |

## Two habits worth forming

1. **Run `/retro` after every campaign.** It writes what worked into `knowledge/learnings.md`, and six other skills read that file. The toolkit gets more accurate about your business every time you use it.
2. **Never let a skill invent a number or a customer quote.** They are built to tag gaps as `[NEEDS INPUT]` instead. If you see a suspiciously specific statistic, check it.

## Install

**As a plugin (recommended).** Inside Claude Code:

```shell
/plugin marketplace add qa-aman/claude-skills
/plugin install claude-skills@claude-skills
```

If the summary says `Run /reload-plugins to activate.`, run that. Updates later come from
`/plugin marketplace update claude-skills`, so there is no re-cloning. Note that plugin skills are
namespaced, so you invoke them as `/claude-skills:brand-context` rather than `/brand-context`.

This installs all 163 skills in the collection, not only marketing. There is currently no way to
install one role through the plugin system.

**Marketing only, via the script.** Use this if you want just these 29 and nothing else:

```bash
git clone https://github.com/qa-aman/claude-skills
cd claude-skills
bash scripts/install.sh --role marketing
```

That installs these 29 plus 7 shared skills (Confluence import and export, Jira tickets, email drafting, presentation builder, diagram generator, YouTube transcript) into `~/.claude/skills/`, available in every project on that machine. Add `--project` instead to scope them to one folder. Skill names are not namespaced this way, so `/brand-context` works directly. Updating means pulling the repo and re-running the script.

## Quality

Each skill declares its source in `metadata.grounded_in` and ships eval cases in `evals/evals.json`
that specify the behaviour it must produce, including the refusals. Run them with:

```bash
python3 scripts/run_evals.py --role marketing --estimate   # count the calls first
python3 scripts/run_evals.py --skill retro                 # one skill
python3 scripts/run_evals.py --role marketing              # all 29
```

The judge never sees the skill, only the response and the required behaviour, and it must quote a
verbatim span to award a pass. Structural checks are separate:

```bash
python3 scripts/validate_skill.py
python3 scripts/skill_quality.py skills/by-role/marketing
```

Treat `skill_quality.py` as a completeness check rather than a quality score. Its correlation with
blind human review was measured at 0.17, and it says so in its own header. The eval run is the
number that means something.

Versions for every skill are tracked in `VERSIONS.md` at the repo root.

