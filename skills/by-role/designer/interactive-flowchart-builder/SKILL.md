---
name: interactive-flowchart-builder
description: >
  Build interactive "living workflow" flowcharts in the visual style of
  https://statuesque-starship-49757d.netlify.app/revenue-engine - vanilla
  HTML/CSS/JS files with a horizontal step bar, a vertical trunk that grows
  per step, tool-to-tool columns with animated payload pills between brand-marked
  tool nodes, alternating left/right step descriptions, and per-step outputs.
  Use whenever the user says "build a flowchart", "interactive flowchart",
  "living workflow", "revenue engine flowchart", "demand gen flowchart", "GTM
  workflow diagram", "process diagram with animations", "Nebor-style flowchart",
  or asks to recreate the workflow visual from the Nebor site. Always asks
  which flowchart to build (Revenue Engine / Demand Gen / CRM & RevOps / Custom)
  and waits for explicit approval of the step + tool + edge table before
  generating any files.
---

## When to invoke

User asks for an interactive multi-step process flowchart with tools, edges, and animated data flow - especially one modeled on the Nebor site's "living workflow" pattern. If the user just wants a static diagram, a Mermaid chart, or a slide-deck flowchart, hand off to a different skill - this one specifically produces the Nebor-style vanilla-JS animated flowchart.

## Reference visual

The output should match the rendering pattern of:
- https://statuesque-starship-49757d.netlify.app/revenue-engine (Sales Engine & GTM)
- https://statuesque-starship-49757d.netlify.app/demand-gen (Demand Gen & ABM)
- https://statuesque-starship-49757d.netlify.app/crm-revops (CRM & RevOps)

All three use the same vanilla-JS engine driven by two globals: `window.NEBOR_TOOLS` and `window.NEBOR_WORKFLOW`. Reproduce that engine.

## Workflow

### Step 1 - Ask which flowchart to build

Print exactly this block and wait:

> Which flowchart would you like me to build?
>
> 1. **Revenue Engine / Sales Engine & GTM** - Identify → Enrich → Personalize → Send → Qualify → Book
> 2. **Demand Gen & ABM** - audience build → signal capture → orchestrated plays → measurement
> 3. **CRM & RevOps** - audit → model → automate → report → govern
> 4. **Custom** - tell me the domain, steps, and tools and I'll design it
>
> Reply with `1`, `2`, `3`, or `4` (with details).

### Step 2 - Draft and confirm the scope

Once the user picks an option, produce a compact markdown table with:

- 4-7 steps (verb-first names, e.g. "Identify", "Enrich")
- One-line `desc` per step
- 3-5 tools per step (real product names, real hex brand colors)
- `roles` map (one sentence per tool, per step)
- `flow` edges - each with `from`, `to`, `proto` (one of `api` / `webhook` / `event` / `sql` / `llm`), `label`
- One-line `output` per step (e.g. "1,284 ranked accounts written to HubSpot - weekly refresh")

End with: *"Approve as-is, or change anything before I generate the files?"*

**Do not generate any files until the user types an approval (yes / approved / ship it / etc.).**

### Step 3 - Generate the files

After approval, write three files into the current working directory (or a path the user specifies):

1. `index.html` - DOM skeleton + inline CSS + script tags
2. `tools.js` - populates `window.NEBOR_TOOLS`
3. `workflow.js` - populates `window.NEBOR_WORKFLOW` + the renderer + animation loop

#### Required DOM skeleton (in index.html)

```html
<section class="workflow">
  <div class="workflow-track"><div class="workflow-track-fill"></div></div>
  <div id="wf-nodes" class="wf-nodes"></div>
  <h3 id="wf-title"></h3>
  <p  id="wf-desc"></p>
  <div id="wf-cumulative" class="wf-cumulative"></div>
  <div id="wf-output" class="wf-output"></div>
</section>
<script src="tools.js"></script>
<script src="workflow.js"></script>
```

#### Required data shape (in tools.js + workflow.js)

```js
window.NEBOR_TOOLS = {
  "<slug>": {
    name: "<Display Name>",
    color: "#HEX",
    cat: "<Category>",          // CRM, Data, Enrichment, LLM, Outreach, Analytics, etc.
    fb:  "Xx",                  // 2-letter fallback mark
    domain: "<example.com>",    // optional
    desc: "<one-sentence why-this-tool>"
  }
};

window.NEBOR_WORKFLOW = [
  {
    step:  "Identify",
    desc:  "TAM mapped from firmographics, tech-stack, and intent.",
    tools: ["apollo", "clay", "builtwith", "hubspot"],
    roles: {
      apollo: "Sources accounts from firmographic + funding filters",
      clay:   "Orchestrates enrichment passes across 50+ providers",
      // one role per tool
    },
    flow: [
      { from: "apollo",    to: "clay",    proto: "api",     label: "POST /accounts" },
      { from: "builtwith", to: "clay",    proto: "api",     label: "tech.signals" },
      { from: "clay",      to: "hubspot", proto: "webhook", label: "ranked.json" }
    ],
    output: "1,284 ranked accounts written to HubSpot - weekly refresh"
  }
];
```

#### Render rules

1. Build a horizontal step bar from `NEBOR_WORKFLOW`. Auto-advance every 4-6s; clicking a step jumps to it.
2. Below the bar, render a vertical "trunk" - one continuous line connecting every step's `root` and `merge` markers.
3. Each step renders a `.tree-section` containing: `.trunk-root` (number + step name) → `.trunk-fork` (horizontal bar) → `.trunk-cols[data-cols=N]` (columns of `from-tool` → animated `.tree-payload` on `.tree-wire` → `to-tool`) → `.trunk-merge`.
4. Alternate the step description side: even index → text right, odd → text left.
5. Animate ALL visible payload pills in sync (not just the current step's) - the "living" quality is the defining feature.
6. Past steps render with class `past` and status pill "wired"; the current step renders with class `current` and pill "live".
7. Tool nodes show: brand-color square mark on the left (inline SVG if available, else the 2-letter `fb` mark) + tool name + hover tooltip with the step-specific `role`.
8. Color-code `.tree-payload` by `proto`:
   - `api` - indigo (`#4F46E5`)
   - `webhook` - teal (`#0D9488`)
   - `event` - amber (`#D97706`)
   - `sql` - violet (`#7C3AED`)
   - `llm` - rose (`#E11D48`)

#### Style targets

- Background: warm off-white `#F5F1EA`. Ink: `#15140F`.
- Serif display for headings (Tiempos, Cormorant, or Playfair Display fallback). Grotesk for body (Inter / system-ui).
- Tool node: rounded rectangle, white fill, 1px ink border, brand mark on the left.
- Payload pill: small pill shape, color per protocol, animated translateX along the wire with CSS keyframes.
- Magazine-grade whitespace. No drop shadows, no glassmorphism, no gradients except subtle.

### Step 4 - Hand off

After writing files, print:

- How to preview: `cd <dir> && python3 -m http.server 8000` then open `http://localhost:8000`.
- How to add a step: append an object to `NEBOR_WORKFLOW` in `workflow.js`.
- How to add a tool: add a slug entry to `NEBOR_TOOLS` in `tools.js`.
- Where to tweak protocol colors / animation speed (note exact CSS class names).

## Anti-Patterns

- Don't reach for React, ReactFlow, Mermaid, or D3. The reference engine is vanilla JS by design - introducing a framework defeats the point.
- Don't generate files before the user approves the scope table. Skipping the confirmation step produces flowcharts the user has to redo.
- Don't invent tools or hex colors. Use real product names and real brand colors. If you don't know a color, ask before guessing.
- Don't drop the animation. A static flowchart fails the brief.
- Don't merge `tools.js` and `workflow.js` into one file unless the user asks - keeping them split is what makes the flowchart editable.
- Don't write a README or extra docs unless the user asks. Three files is the deliverable.

## Quality Checklist

- [ ] User explicitly approved the step + tool + edge table before any file was written.
- [ ] 4-7 steps total, each with `step`, `desc`, `tools`, `roles` (one per tool), `flow`, `output`.
- [ ] Every tool slug referenced in any `flow.from`, `flow.to`, or `tools[]` exists as a key in `NEBOR_TOOLS`.
- [ ] Every edge has a valid `proto` (`api` | `webhook` | `event` | `sql` | `llm`) and a human label.
- [ ] Horizontal step bar + vertical trunk + animated payloads all render from a single `index.html` open in the browser (no build step).
- [ ] Past steps show as "wired", current step shows as "live".
- [ ] Hover on a tool node shows the step-specific role tooltip.
- [ ] Brand-color marks render for every tool (SVG or 2-letter fallback).
