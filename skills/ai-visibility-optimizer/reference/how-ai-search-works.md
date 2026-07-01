# How AI search actually retrieves and cites

Read this first. The mechanisms here are what every other part of the skill rests on. Figures are measured snapshots (roughly mid-2026); treat the DIRECTION as durable and re-verify a number before quoting it.

## Trained memory vs live retrieval (the core split)

Two different sources feed an AI answer:

- TRAINED MEMORY: what the model already knows. It lags the live web by months, sends no traffic, and usually produces a bare NAMED mention with no link.
- LIVE RETRIEVAL: at answer time the system fetches and selects actual pages. This is what produces a clickable CITATION.

A named mention with no source attached typically came from trained memory; a cited mention means the live retrieval step lifted your page. This distinction is the spine of honest measurement, and it is why this skill uses the presence ladder (cited > named > considered > missing) instead of a yes/no.

## There is no unified AI index

Every assistant runs retrieval against its own index with distinct submission paths. Being in the index is the price of entry, but indexed is necessary, not sufficient, for a citation.

- ChatGPT Search: Bing index plus OpenAI's own crawl (OAI-SearchBot).
- Microsoft Copilot: Bing index.
- Claude: Brave Search index (no submission tool; you earn Brave ranking).
- Perplexity: its own index (PerplexityBot).
- Gemini and Google AI surfaces: the Google Search index.

Cross-dependency trap: if robots.txt blocks Googlebot, Brave skips you too, so Claude's retrieval can depend on Googlebot access even though Claude uses Brave's index. A block in one place can remove you from a surface you did not expect.

## Google decomposes the query (fan-out)

Google's AI does not answer the literal query. It breaks it into sub-questions, runs a separate search per sub-question, and synthesizes. Pages that show up across several sub-results get pulled in. Being the best answer to a specific sub-question beats dominating one broad head term.

## Google is three systems, not one

AI Overviews (the answer box), AI Mode (the conversational tab), and Gemini (the standalone app) are functionally independent and cite different sources, even for semantically identical queries. Treat and measure them separately; do not roll them into one "Google" number.

## The engines barely overlap (so GEO is per-engine)

In a measured corpus of ~127,000 citations across five engines, about 70% of cited domains were cited by only one engine and under 3% by all five. Winning one engine barely carries to the others. Always assess and report per engine; a single global "GEO score" hides this and misleads.

Engines also differ in how many sources they cite per answer (Gemini cites the most, ChatGPT the fewest, with Perplexity, Google AI Mode, and Claude in between) and in whether they attach a clickable source at all (Perplexity almost always cites; ChatGPT leaves roughly a third as bare names; Google surfaces often name without a link). Source-type preferences diverge too (live-results Google surfaces lean on YouTube heavily; model-grounded Gemini and Claude barely touch it).

## What this means for the audit

- Assess each engine separately and say so.
- Separate named from cited; a brand that is named everywhere but cited nowhere has a retrieval problem, not a memory problem.
- Getting indexed (crawler access) is step one, not the finish line.
- The on-page work changes WHICH page gets cited; the off-site evidence layer changes WHETHER your brand shows up at all (see off-site.md). Both matter.
