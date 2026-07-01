# Measurement truths (and the estimate-vs-measured line)

This is the doc that keeps the skill honest. The whole point is to know what you can claim.

## One answer is not a measurement

Run the same prompt twice and the output moves: a brand may appear in one run, vanish in the next, or slide from a strong recommendation to a passing mention. Prompt wording, platform, location, model version, and time all change it. So AI visibility is a RATE across a distribution of responses, never a reading off one generated answer.

A minimum viable measurement: 30-50 prompts across question types (category, comparison, problem, objection, source-based), 3-5 AI surfaces, repeated runs for the important prompts, plus competitor and citation tracking and an accuracy review. Express findings as rates ("a competitor was recommended in 14 of 20 category runs"), not as "ChatGPT recommends a competitor."

This is exactly why this skill cannot produce a MEASURED visibility number from on-page signals. Generating that number requires querying the engines across many prompts and reading the answers. Say so; do not fake it.

## Which experience are you measuring

The same assistant is not one system. A logged-out or free tier can route a query to a smaller model with no reasoning step, search the web differently, and in some cases fabricate an answer or attach citations that contradict the pages they point to, while the paid or logged-in tier of the same assistant routes to a reasoning model and calls structured tools and returns a different answer to the same prompt. Per-query routing inside a single product compounds this: a "thinking" path can pull from noticeably more sources than the fast path on the same engine. So a measurement is only valid for the exact tier, account state, and surface it was captured on, and a tool that scrapes one experience can report a reality the user's own customers never see. State which experience a finding came from; never generalize a free-tier reading to paid users or the reverse.

## Building the prompt set (if you measure manually)

If you or the user runs a manual GEO measurement, the prompt set is the whole game. Keywords compress; AI prompts expand into longer, contextual, comparative questions that carry buyer type, stack, constraint, and decision context, so a keyword in sentence form is not a real prompt. Separate BRANDED prompts (test accuracy: "what does [brand] do?") from UNBRANDED prompts (test discovery: "best tools for [use case]"); mixing them misreads visibility. Cover eight categories: discovery, comparison, use-case, accuracy, problem, alternative, objection, integration. Start with a 30-50 prompt matrix (about five per category) and expand only after patterns emerge; do not jump to 500. A prompt earns its place only if its added detail changes the possible answer. Per prompt, record: text, AI system, date, mention presence, recommendation strength, competitors cited, first-mentioned brand, source citations, accuracy issues, and the required action. Read the result as a distribution across repeated runs, not a single number.

## The presence ladder (not binary)

Per response, a brand is: cited (a tracked URL appeared as a source) > named (named in prose without a link, usually from trained memory) > considered (in the retrieval pool only) > missing. Named-but-not-cited is a real, common, distinct state. Never collapse named into cited; the fix is different (memory/authority vs retrieval/page).

## Ranking is not citation

A page can rank well in classic search and still not be the page an AI cites. The share of Google AI citations coming from top-10 organic results fell sharply (a measured snapshot: roughly 76% to under 40% across mid-2025 to early 2026), with the rest scattered deep or off page one. Top rankings help; they no longer guarantee citation.

## Visibility is not traffic; visibility without conversion is vanity

AI paths are messy and often zero-click: a user reads the answer and never clicks, or sees a mention and brand-searches later. Some assistants strip referrer data, so a share of AI-driven visits goes uncounted. Separate two signals cleanly: an AI REFERRER is a visible human visit from an assistant; an AI CRAWLER is a bot request. They answer different questions. The real loop to measure is mention -> citation -> referral -> conversion, not just whether you appeared. Raw session counts hide whether the remaining visitors are high-intent.

## The five measurable components of AI visibility

1. Brand presence (does the AI mention you on category questions).
2. Recommendation strength (passing mention vs shortlisted as a good fit).
3. Competitor context (who shows up instead of you, and why).
4. Source visibility (which pages, reviews, and forums the answer drew from).
5. Answer accuracy (is the description current and fair).

A metric with no page-level fix attached is decoration; tie every reported metric to an action.

## The estimate-vs-measured rule (apply everywhere)

- DETERMINISTIC: robots/crawler access, llms.txt and schema presence/validity, page structure. Read directly; state as fact.
- ESTIMATE: citation readiness, off-site gaps, likely presence. Informed inference from signals; always labeled, never a hard score-as-fact.
- MEASURED: requires querying the engines across many prompts. Not producible from on-page signals; connect a measurement source (upgrade-to-measurement.md) or report "not measured."

Never let an ESTIMATE be displayed as MEASURED. If you could not fetch a page, say so; never score it from a cache snippet as if you read it.
