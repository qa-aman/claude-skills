---
name: sourcing-strategy
description: >
  Build a candidate sourcing strategy and outreach pipeline. Use when the user says
  "where do I find candidates for this role", "build a sourcing plan", "write a
  cold outreach message", "we're not getting enough applicants", "our pipeline is
  dry", "help me find passive candidates", "write a LinkedIn message", or wants to
  increase the volume or quality of candidates in the funnel - even if they don't
  explicitly say "sourcing strategy". Also use when a recruiter needs to go beyond
  job postings to find talent.
---

## Overview

Based on **Recruiting in the Age of Googlization** (Wolfe) and **Who: The A Method for Hiring** (Smart & Street). Most A players are not applying to job postings - they're employed, performing well, and selectively available. Passive sourcing (outbound) is required to access that pool. The sourcing strategy defines which channels to use, how to find candidates in each, and what to say to get a response.

## Workflow

### Step 1: Define the Ideal Candidate Profile (ICP)

Before sourcing, know exactly who you're looking for. Pull this from the scorecard or intake meeting:
- Role: [role title]
- Level: [seniority]
- Must-have background: [specific experience, domain, or capability]
- Nice-to-have signals: [adjacent experience or company backgrounds]
- Geographic constraint: [remote / hybrid / on-site in X]
- Timeline: [when do you need them in seat?]

The tighter the ICP, the better your outbound conversion rate. Broad ICPs produce volume, not quality.

### Step 2: Choose Sourcing Channels

Select 2-3 primary channels based on the role type. Running too many channels simultaneously splits focus and reduces quality.

| Role Type | Primary Channels |
|-----------|-----------------|
| Software Engineers | LinkedIn, GitHub, conference speaker lists, open source contributors |
| Designers | LinkedIn, Dribbble, Behance, portfolio sites |
| Data / ML | LinkedIn, Kaggle, academic papers, arXiv |
| GTM (Sales, Marketing) | LinkedIn, revenue event communities, company alumni networks |
| Executives | LinkedIn, referral networks, executive search firms |
| Generalist / Operations | LinkedIn, Indeed, industry Slack communities |

### Step 3: Build Boolean Search Strings

Boolean search finds candidates who match specific criteria on LinkedIn or GitHub.

LinkedIn search formula:
```
"[job title 1]" OR "[job title 2]" AND "[skill or domain]" AND "[geography]"
NOT "[company to exclude]"
```

Examples:
```
"Senior Product Manager" OR "Group Product Manager" AND "B2B SaaS" AND "New York"

"Staff Engineer" OR "Principal Engineer" AND "distributed systems" NOT "recruiting"

"Director of Marketing" AND ("demand generation" OR "growth marketing") AND "Series B" OR "Series C"
```

Tips:
- Use title variations - "Software Engineer" vs "Software Developer" vs "SWE"
- Filter by "Current company size" to target right-stage candidates
- Use "Past company" filter to find alumni of companies known for talent density (relevant to your stage and domain)

### Step 4: Write Outbound Messages That Get Responses

The most common failure in sourcing: generic messages that could apply to anyone.

**The Mom Test applied to outreach** (Fitzpatrick): don't lead with what you want. Open with specific recognition of their work.

Message framework (LinkedIn InMail or email):
```
Subject line or opening: [Specific observation about their work or background]
Line 1: Why them specifically - reference something real
Line 2: What the role is and why it's interesting (the mission hook from the JD)
Line 3: Low-friction ask - not "are you interested?" but "worth a 20-minute chat?"
```

Template (edit for each candidate - do not send verbatim):
```
Subject: [Specific thing you noticed] - [Role] at [Your Company]

Hi [Name],

I came across your work on [specific project, article, talk, or GitHub repo] -
[one sentence on why it caught my attention].

I'm building out [your company]'s [function] and have an opening for a [role title].
The core problem we're solving: [one sentence on the mission]. In the first year,
this person will [specific outcome from the JD].

Given your background in [specific domain or skill], I think it could be worth a
conversation - even if you're not actively looking. Would a 20-minute call be
worthwhile?

[Your name]
```

What makes this work:
- The subject line is specific, not "Exciting opportunity!"
- The opening references something real, not "I saw your impressive profile"
- The role has a clear mission - not a job title and a list of perks
- The ask is low-commitment ("20-minute call", not "are you ready to make a move?")

### Step 5: Run Referral Campaigns

Referrals are the highest-quality, lowest-cost sourcing channel. From **Who**: A players know A players. The problem is most referral programs are passive ("Submit a referral in the system").

Active referral campaign:
1. Send a direct message to 5-10 high-performers at [your company]: "I'm hiring a [role]. Here's what I'm looking for: [3-bullet ICP]. Can you think of 1-2 people from past companies who'd be worth a conversation?"
2. Ask specifically - "Do you know anyone from [Company X] who was doing [type of work]?"
3. Make it easy: "Just send me their LinkedIn or email - I'll take it from there."
4. Close the loop: update the referrer on outcome (builds trust and future referrals)

### Step 6: Track Pipeline Health

Source tracking tells you where your best candidates come from. Without it, you can't optimize.

Weekly sourcing metrics:
```
Channel | Messages Sent | Replies | Screen Calls | Offers | Hires
LinkedIn outbound | XX | XX (X%) | XX (X%) | ... | ...
Referrals | XX | XX (X%) | XX (X%) | ... | ...
Inbound (job board) | XX | XX (X%) | XX (X%) | ... | ...
```

Benchmark conversion rates:
- LinkedIn cold outreach: 15-30% reply rate if personalized, 2-5% if generic
- Referrals: 50%+ reply rate, highest hire rate per screen
- Inbound: high volume, lower quality-per-screen than outbound or referral

If reply rates drop below 10% on outbound, the message needs to change - not the volume.

## Anti-Patterns

**1. Spray-and-pray outreach**
Bad: Send 100 generic InMails. Expect volume to compensate for poor conversion.
Good: Send 20 personalized messages to candidates who specifically match the ICP. Expect 30-40% reply rate.

**2. Relying on job postings alone**
Bad: Post the JD on LinkedIn and Indeed, then wait.
Good: Inbound fills the funnel with active job seekers. A players are not actively looking. Outbound is required to access them.

**3. Message that leads with your company**
Bad: "[Your company] is a fast-growing SaaS platform helping teams collaborate better. We're looking for a Senior Engineer to join our talented team..."
Good: Start with them. Reference their specific work. The company pitch comes second.

**4. Using "open to opportunities" as the only filter**
Bad: Filter LinkedIn search for candidates with "open to work" badge only.
Good: Most high-performers don't signal availability publicly. Reach out regardless - the worst outcome is no reply.

**5. Not tracking source quality**
Bad: Running 5 channels with no data on which produces hires.
Good: Track every candidate's source. Cut channels with <5% screen-to-offer conversion after 4+ weeks.

## Quality Checklist

- [ ] Ideal Candidate Profile is defined before sourcing begins
- [ ] 2-3 primary channels selected based on role type (not all channels at once)
- [ ] Boolean search strings written with title variations
- [ ] Outbound messages reference something specific about the candidate
- [ ] Message ask is low-friction ("20-minute chat" not "are you interested in a change?")
- [ ] Active referral campaign run with specific asks to internal high-performers
- [ ] Pipeline tracked by source with reply rate, screen rate, and offer rate
