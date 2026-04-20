# UX Copy Guidelines

Industry-standard UX writing guidelines for clear, consistent, and inclusive interface copy.

## Source Books & Frameworks

This guide synthesises frameworks from the following books. Each section references the originating book(s) so readers know where to go deeper.

| Code | Book | Author(s) | Core Framework |
|------|------|-----------|----------------|
| **SWU** | *Strategic Writing for UX* | Torrey Podmajersky | Copy purpose matrix: every string maps to a user goal + product voice. Categorises all UI text into 6 types (titles, descriptions, buttons, errors, notifications, confirmations). |
| **WID** | *Writing Is Designing* | Michael J. Metts, Andy Welfle | Words as design material. Collaboration patterns between writers and designers. Content-first design process. |
| **MCG** | *Microcopy: The Complete Guide* | Kinneret Yifrah | Tactical microcopy patterns for every UI element. Voice-and-tone spectrum. Friction reduction through copy. |
| **CDN** | *Content Design* | Sarah Winters (Sarah Richards) | User-need-driven content. Pair writing. Evidence-based content decisions. "Content should be useful, usable, and accessible." |
| **CVD** | *Conversational Design* | Erika Hall | Interaction as conversation. Cooperative principle (Grice's maxims applied to UI). Turn-taking in digital flows. |
| **NCS** | *Nicely Said* | Nicole Fenton, Kate Kiefer Lee | Voice charts with personality traits + do/don't examples. Empathy-first writing. "Treat every message like a conversation with a friend." |
| **EBW** | *Everybody Writes* | Ann Handley | "Utility x Inspiration x Empathy" formula. 12-step writing process. "Write for one person, not an audience." |
| **DMT** | *Don't Make Me Think* | Steve Krug | Cognitive load reduction through self-evident copy. "If a user has to think about it, you've failed." Trunk test for navigation clarity. |
| **LGW** | *Letting Go of the Words* | Janice (Ginny) Redish | Inverted pyramid for screens. Layered information architecture. How people actually read on screens (F-pattern, scanning). |

Additional industry sources: Material Design Writing, Apple HIG, NNG Research, GOV.UK Content Design, Mailchimp Content Style Guide.

---

## 1. Reading Level

> **Books**: LGW (scanning behaviour), CDN (accessible content), DMT (cognitive load)

1. Target grade 6-8 reading level (Flesch-Kincaid). If a 12-year-old cannot understand it, rewrite it.
2. Maximum 25 words per sentence. Break longer sentences into two.
3. Maximum 3 sentences per paragraph in UI copy.
4. One idea per sentence. One purpose per paragraph.
5. Prefer 1-syllable words over 3-syllable words when meaning is identical.
6. **Front-load the key information** in every sentence -- users scan the first 2-3 words, then decide whether to read the rest. *(LGW: inverted pyramid for screens)*
7. **Break walls of text into scannable chunks** -- users don't read on screens, they scan in an F-pattern. Use headings, bullets, and bold keywords to support scanning. *(LGW: how people actually read on screens)*

**Quick test**: Read the copy aloud. If you stumble, it is too complex. *(EBW: "If it sounds like writing, rewrite it.")*

---

## 2. Voice and Tone

> **Books**: SWU (voice chart), NCS (voice attributes), MCG (tone spectrum), CVD (conversational principles)

### Voice (constant across all screens)

Define voice using a **voice chart** with 4-5 personality traits, each with a "this but not that" qualifier *(NCS framework)*:

| Trait | This | Not that |
|-------|------|----------|
| Friendly | Warm, approachable | Slangy, overly casual |
| Clear | Plain, direct | Blunt, cold |
| Encouraging | Supportive, positive | Patronising, fake-cheerful |
| Confident | Certain, trustworthy | Arrogant, dismissive |
| Respectful | Polite, empathetic | Stiff, formal |

### Voice rules

1. **Direct**: Address the user as "you" / "your". Never "the user" or "one". *(SWU: second person creates connection)*
2. **Active**: "We sent you a code" not "A code has been sent". *(EBW: active voice = clarity)*
3. **Present tense**: "Your form is saved" not "Your form has been saved".
4. **Confident**: "This takes 2 minutes" not "This should take about 2 minutes". *(MCG: hedging language erodes trust)*
5. **Honest**: Never overpromise. "We will contact you" not "You will definitely hear from us". *(NCS: empathy-first, always truthful)*

### Tone (varies by context)

Tone shifts along a spectrum from **serious to playful** depending on the user's emotional state in the moment *(MCG: tone spectrum framework)*:

| Context | User's emotional state | Tone | Example |
|---------|----------------------|------|---------|
| Onboarding / Welcome | Curious, cautious | Warm, encouraging | "Let's get started" |
| Form labels | Focused, task-mode | Neutral, precise | "Date of birth" |
| Success | Relieved, happy | Celebratory but brief | "You're all set!" |
| Error | Frustrated, anxious | Calm, helpful | "That number doesn't look right. Check and try again." |
| Blocking / Ineligible | Disappointed | Empathetic, forward-looking | "This feature isn't available for your plan yet. Here are some alternatives." |
| Legal / T&C | Wary, scanning | Clear, no legalese | "We store your data securely and never share it." |

---

## 3. The Copy Purpose Matrix

> **Books**: SWU (copy purpose matrix -- the core framework of the book)

Every piece of UI text must serve exactly ONE purpose. If it serves two, split it into two strings.

| Copy type | Purpose | Max length | Example |
|-----------|---------|------------|---------|
| **Title** | Orient the user -- where am I? | 3-5 words | "Verify your number" |
| **Description** | Explain what's happening or what to do | 1-2 sentences | "We'll send a verification code to your WhatsApp" |
| **Button/CTA** | Name the next action | 1-3 words | "Send code" |
| **Error** | Identify the problem + offer a fix | 2 sentences max | "That number doesn't look right. Enter a 10-digit mobile number." |
| **Confirmation** | Reassure the user the action worked | 1 sentence | "Code sent to +91 98765 43210" |
| **Notification** | Alert about something that needs attention | 1 sentence + action | "Your session expires in 5 minutes. Save your progress." |

**Test**: For every string, ask "What is the user trying to do right now?" If the copy doesn't help them do it, cut or rewrite it. *(SWU: user goal alignment)*

---

## 4. Terminology Consistency (Glossary)

> **Books**: WID (shared vocabulary), SWU (terminology governance)

Use the left column. Never use the right column. *(WID: "Inconsistent terminology is the #1 source of user confusion.")*

| Use this (canonical) | Never use |
|---------------------|-----------|
| Sign in | Log in, Login, Log on |
| Sign out | Log out, Logout |
| Sign up | Register (as button label) |
| Mobile number | Phone number, Cell number, Contact number |
| Verification code | OTP, One-time password, Auth code |
| Email address | Email ID, E-mail, Mail ID |
| Date of birth | DOB, Birth date, Birthday |
| PIN code | Pincode, Zip code, Postal code |
| Password | Passcode (unless numeric-only) |
| Photo | Image, Picture, Pic |
| Upload | Attach (for files) |
| Delete | Remove (for permanent actions) |
| Cancel | Dismiss, Close (for abandoning a flow) |
| Go back | Return, Previous |
| Continue | Proceed, Next (as primary CTA) |
| Try again | Retry, Re-attempt |
| Learn more | Read more, See more, Find out more |
| Saving... | Loading..., Please wait... |
| Something went wrong | An error occurred, System error, Unexpected error |
| Powered by | Built by, Created by (for attribution) |

### Project-Specific Terms

Extend this section per project. Example entries (replace with your own glossary):

| Use this | Never use |
|----------|-----------|
| [canonical term] | [variants to avoid] |

---

## 5. Forbidden Jargon

> **Books**: CDN (plain language mandate), LGW (write for scanning), DMT (self-evident copy)

Replace technical terms with plain alternatives. *(CDN: "If a user wouldn't use this word to search for it, don't use it in the interface.")*

| Jargon | Plain alternative |
|--------|------------------|
| Authenticate | Verify |
| Submit | Send / Continue / Done |
| Invalid | Not recognised / Doesn't look right |
| Mandatory | Required |
| Populate | Fill in |
| Navigate | Go to |
| Initiate | Start |
| Terminate | End / Stop |
| Configure | Set up |
| Execute | Run |
| Parameter | Setting / Option |
| Utilize | Use |
| Facilitate | Help |
| Subsequent | Next |
| Prior to | Before |
| In order to | To |
| Leverage | Use |
| Optimize | Improve |
| Implement | Set up / Add |
| Functionality | Feature |
| Credentials | Sign-in details |
| Propagate | Spread / Send |
| Payload | Data |
| Deprecated | No longer available |
| Regex / Pattern | Format |
| Boolean | Yes / No |

---

## 6. Buttons and CTAs

> **Books**: SWU (button = promise of action), MCG (CTA microcopy patterns), DMT (self-evident navigation)

### Rules

1. **Verb + noun**: "Create account", "Send code", "Check eligibility". *(SWU: a button is a promise -- the label must match the outcome exactly)*
2. **Maximum 3 words** for primary CTAs. 4 words acceptable for secondary.
3. **Never use**: "Click here", "Submit", "OK", "Yes/No" as standalone labels. *(DMT: "Submit" forces the user to think about what they're submitting)*
4. **Sentence case**: "Send code" not "Send Code" or "SEND CODE".
5. **Match the action**: The label must describe what happens next, not what the user wants. *(MCG: "Start free trial" not "I want a free trial")*
6. **Destructive actions**: Use specific language. "Delete account" not "Delete". Add confirmation. *(MCG: friction is good for destructive actions)*

### Patterns

| Action type | Pattern | Examples |
|-------------|---------|----------|
| Primary forward | Verb + context | "Continue to payment", "Send code" |
| Secondary back | "Go back" or context | "Go back", "Choose a different grade" |
| Confirmation | Verb + object | "Delete account", "Cancel registration" |
| Toggle | State description | "Show password", "Hide details" |

### Arrow Usage

1. Right arrow (→) only on primary forward CTAs that navigate to a new screen.
2. Never arrows on secondary buttons or in-page actions.
3. Never left arrow (←) on back buttons -- use text "Go back" or a back icon.

---

## 7. Error Messages

> **Books**: MCG (error microcopy chapter -- most tactical), SWU (error copy framework), CVD (repair turns)

### Structure

Every error message answers two questions *(MCG: the 2-part error formula)*:
1. **What happened?** (one sentence)
2. **What can you do about it?** (one sentence)

### Rules

1. **Never blame the user**: "That number doesn't look right" not "You entered an invalid number". *(MCG: "The system failed, not the user. Write accordingly.")*
2. **Be specific**: "Enter a 10-digit mobile number" not "Invalid input". *(SWU: vague errors create more support tickets than bugs do)*
3. **Suggest a fix**: Always tell the user what to do next.
4. **No error codes**: Never show codes like "ERR_422" or "Error: null".
5. **No technical details**: Never mention server, API, database, timeout, or network.
6. **Positive framing**: "Enter your name" not "Name cannot be empty". *(MCG: tell users what TO do, not what NOT to do)*
7. **Use the conversational repair pattern**: Acknowledge, explain, offer a fix -- like a human would correct a misunderstanding. *(CVD: Grice's maxim of manner -- be clear, be brief, be orderly)*

### Patterns

| Type | Pattern | Example |
|------|---------|---------|
| Missing field | "Enter your [field]" | "Enter your mobile number" |
| Wrong format | "[Field] must be [format]" | "Mobile number must be 10 digits" |
| Out of range | "[Field] must be between [X] and [Y]" | "Age must be between 19 and 28" |
| Not found | "We couldn't find [thing]. [Alternative]." | "We couldn't find that school. Check the spelling or choose from the list." |
| Connection | "Check your internet connection and try again." | -- |
| Generic | "Something went wrong. Try again." | -- |

---

## 8. Form Labels and Helper Text

> **Books**: MCG (form microcopy chapter), LGW (layered information), WID (label as design material)

### Labels

1. **Noun or noun phrase**: "Mobile number" not "Enter your mobile number". *(LGW: labels are scanning anchors -- keep them short)*
2. **Sentence case**: "Annual school fee" not "Annual School Fee".
3. **No colons**: "Mobile number" not "Mobile number:".
4. **Required fields**: Mark optional fields "(optional)" rather than marking required with *. *(MCG: most fields are required -- marking the minority reduces noise)*
5. **Consistent naming**: If label says "Mobile number", use "mobile number" everywhere. *(WID: a label is a contract with the user)*

### Placeholder Text

1. **Show format or example**: "e.g., 9876543210" or "DD/MM/YYYY".
2. **Never repeat the label**: If label is "Mobile number", placeholder is NOT "Enter mobile number". *(MCG: redundant placeholders waste the one chance to show a helpful example)*
3. **Use lowercase**: "e.g., 9876543210" not "E.g., 9876543210".

### Helper Text

1. **Explain why or clarify**: "We will send a verification code to this number". *(MCG: answer the user's unspoken "why do you need this?")*
2. **One line maximum**.
3. **Below the field**: Never above or beside.

---

## 9. Conversational Flow Design

> **Books**: CVD (core framework), SWU (flow-level copy), DMT (don't make me think)

### Grice's Maxims Applied to UI Copy *(CVD framework)*

1. **Quantity**: Say enough to be helpful, but no more. Don't over-explain. Don't under-explain.
2. **Quality**: Only state things that are true. Don't use copy that sounds good but means nothing ("Best-in-class experience!").
3. **Relation**: Every piece of copy must be relevant to what the user is doing right now. No marketing copy on error screens.
4. **Manner**: Be clear, be brief, be orderly. Avoid ambiguity.

### Turn-Taking in Multi-Step Flows *(CVD framework)*

1. Each screen is one "turn" in the conversation. The product speaks (title, description), the user responds (input, selection, button).
2. Don't ask two questions in one turn. One screen = one decision.
3. The button is the user's "reply" -- it must feel like a natural response to what the screen just said.
4. **Acknowledge before advancing**: After the user acts, confirm what happened before asking the next question. ("Code sent. Now enter it below.")

---

## 10. Progress and Status

> **Books**: SWU (notification/confirmation copy types), MCG (loading states), DMT (progress visibility)

### Step Indicators

1. **"Step X of Y"**: Always show total. "Step 2 of 4" not "Step 2". *(DMT: users need to know where they are and how far they have to go)*
2. **Present tense for current step**: "Verify your number" not "Number verification".
3. **Consistent wording**: All step headers must follow the same pattern.

### Loading States

1. **Verb + -ing**: "Checking eligibility...", "Sending code..."
2. **No "please wait"**: The loading indicator already asks them to wait. *(MCG: "please wait" is the verbal equivalent of a spinning wheel on top of a spinning wheel)*
3. **Show progress if possible**: "Uploading 3 of 5 photos" not "Uploading..."

### Success States

1. **Confirm what happened**: "Registration complete" not just "Success!". *(SWU: confirmation copy must name the specific thing that succeeded)*
2. **State next steps**: "We will send your test details to +91 98765 43210".
3. **One exclamation mark maximum**: Never "Congratulations!!!" or "Success!!!".

---

## 11. Empty States and Ineligibility

> **Books**: MCG (empty state microcopy), CDN (dead-end prevention), NCS (empathy-first messaging)

### Empty States *(MCG: the 3-question framework)*

Answer three questions:
1. **What is this?** (what would normally be here)
2. **Why is it empty?** (what is missing)
3. **What to do?** (clear action)

### Ineligibility / Blocking Messages

1. **Lead with empathy**: "This feature isn't available on your plan yet." *(NCS: "Write like a human talking to a human.")*
2. **Explain why briefly**: One sentence maximum.
3. **Offer alternatives**: Resources, links, or next steps. Never leave the user at a dead end. *(CDN: "Every dead end is a failure of content design.")*
4. **No apology overload**: One "sorry" is enough. Never "We're so sorry for the inconvenience." *(MCG: over-apologising signals the product is unreliable)*

---

## 12. Cognitive Load Reduction

> **Books**: DMT (core thesis), LGW (scanning behaviour), CDN (content reduction)

1. **Self-evident over self-explanatory**: If the UI needs copy to explain it, the design needs work first. Copy is a last resort for confusion. *(DMT: "Don't make me think")*
2. **Trunk test for every screen**: Can the user answer "Where am I? What can I do here? Where do I go next?" within 3 seconds of landing? If not, the copy or layout needs simplifying. *(DMT: trunk test)*
3. **Progressive disclosure**: Show only what's needed now. Hide details behind "Learn more" or expandable sections. *(LGW: layered information architecture)*
4. **One primary action per screen**: If there are two equally prominent CTAs, the user must think about which to choose. Reduce to one primary + one secondary. *(DMT: eliminate unnecessary choices)*
5. **Cut ruthlessly**: If removing a sentence doesn't change meaning, remove it. Then cut again. *(CDN: "Content should be as short as it can be, and no shorter.")*

---

## 13. Content-First Design Process

> **Books**: WID (words as design material), CDN (pair writing), EBW (writing process)

When collaborating with designers on new screens:

1. **Write the copy before the layout**: Words determine how much space is needed, not the other way around. Placeholder "Lorem ipsum" creates layouts that don't fit real content. *(WID: "If you design with fake words, you get a fake design.")*
2. **Pair writing**: Writer and designer work on the same screen simultaneously. The designer handles layout, the writer handles every text string. Neither works in isolation. *(CDN: pair writing from GDS)*
3. **Write for the longest realistic string**: If a name field could contain "Raghunathan Subramanian", don't test with "John". *(WID: edge-case content testing)*
4. **Write for multiple languages early**: If the product will be localised, account for text expansion (some languages expand 30-40% vs English). *(WID: internationalisation awareness)*

---

## 14. Inclusive Language

> **Books**: NCS (empathy-first writing), CDN (accessible content), EBW (writing for all)

1. **Gender-neutral by default**: "They/their" not "he/she" or "his/her".
2. **"Prefer not to say"**: Always offer as a gender option. Never "Other" alone.
3. **No idioms or slang**: "Immediately" not "right off the bat". *(NCS: "Write for your global audience, not your local one.")*
4. **No assumptions about ability**: "Check" not "See". "Select" not "Click". *(CDN: accessible content principles)*
5. **No assumptions about age**: Avoid "elderly", "young person". Use specific age ranges.
6. **No assumptions about family**: "Parent or guardian" not "mother/father".
7. **Cultural sensitivity**: Avoid metaphors tied to specific cultures.
8. **Plain language is inclusive language**: The simpler the copy, the more people can understand it -- including non-native speakers, users with cognitive disabilities, and users under stress. *(CDN + EBW)*

---

## 15. Numbers and Formatting

> **Books**: LGW (formatting for scannability), CDN (GOV.UK style)

1. **Spell out 1-9**: "three tracks" not "3 tracks". Exception: data, ages, dates.
2. **Digits for 10+**: "15 languages" not "fifteen languages".
3. **Phone format**: "+91 98765 43210" (spaced groups).
4. **Currency**: "$1,200" or "₹1,200" with locale-appropriate thousand separator. No space between symbol and number.
5. **Dates**: "15 Apr 2026" in display. Use the format hint that matches your locale (e.g., "DD/MM/YYYY" or "MM/DD/YYYY").
6. **Percentages**: "75%" with no space. "75 percent" in running text.
7. **Time**: "2:30 PM" (12-hour with AM/PM).

---

## 16. Capitalisation

1. **Sentence case everywhere**: Headings, buttons, labels, menu items, tab names.
2. **Exceptions**: Proper nouns and brand names, acronyms (OTP, PIN).
3. **Never ALL CAPS**: Not for emphasis, not for labels, not for headings. Use bold instead.
4. **Title Case only for**: Product names, brand names, legal document titles.

---

## 17. Punctuation

1. **No full stops in**: Headings, buttons, labels, placeholder text, list items (unless multi-sentence).
2. **Full stops in**: Body text, helper text, error messages, descriptions.
3. **No exclamation marks in**: Error messages, form labels, helper text.
4. **One exclamation mark maximum per screen**: Reserve for genuine celebration.
5. **Oxford comma**: "red, white, and blue" not "red, white and blue".
6. **En dash for ranges**: "19-28 years" not "19 to 28 years" in compact UI.
7. **Ellipsis for loading**: "Uploading..." Never "Uploading....".

---

## 18. Audit Checklist

When reviewing copy on a Figma screen, check every text node against:

1. **Copy purpose** *(SWU)*: Does every string serve exactly one purpose (title/description/button/error/confirmation/notification)?
2. **Reading level** *(LGW, CDN)*: Would a 12-year-old understand this?
3. **Jargon-free** *(CDN, DMT)*: No terms from the Forbidden Jargon list?
4. **Terminology consistent** *(WID, SWU)*: Same concept uses the same word everywhere?
5. **Voice** *(NCS)*: Active, direct, "you/your" address, matching the voice chart traits?
6. **Tone** *(MCG)*: Does the tone match the user's emotional state in this moment?
7. **Button pattern** *(SWU, DMT)*: Verb + noun, max 3 words, sentence case, matches the outcome?
8. **Error pattern** *(MCG)*: What happened + what to do? No blame?
9. **Label pattern** *(LGW)*: Noun phrase, sentence case, no colon?
10. **Conversational flow** *(CVD)*: One question per screen? Acknowledge before advancing?
11. **Cognitive load** *(DMT)*: Can user answer "where am I, what can I do, where do I go" in 3 seconds?
12. **Inclusive** *(NCS, CDN)*: Gender-neutral, no idioms, no assumptions?
13. **Formatting** *(LGW)*: Numbers, dates, currency follow rules?
14. **Punctuation**: Correct per context (heading vs body vs button)?
15. **Scannability** *(LGW)*: Key info front-loaded? Bold for scanning anchors? No walls of text?
