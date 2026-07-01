# Producing an honest report

The deliverable is where most GEO tools lose their integrity: they wrap an estimate in a fabricated ROI table and a guarantee. This skill refuses that. An honest report is more persuasive to a real buyer, not less.

## The prioritized action order (use this as the report spine)

1. MEASURE current AI visibility first across the surfaces (the most commonly skipped step; optimizing before measuring is the classic mistake). If real measurement is not connected, say the report's visibility section is an ESTIMATE and recommend measuring.
2. CLARIFY positioning: category, audience, problems, use cases, differentiation. The brand should be explainable in three sentences without "AI-powered," "platform," or "solution."
3. FIX crawlability: robots.txt, WAF/CDN bot rules, server errors, JS rendering, internal linking. Confirm what an external fetch shows (200 vs 403 for the retriever user-agents); recommend the owner confirm via their server logs that search-index crawlers get 200s, or ask them to export the logs if you need to check directly. (DETERMINISTIC; highest-certainty section.)
4. AUDIT the off-site evidence layer: reviews, comparisons, roundups, partner pages, forums. Improve existing sources, not just publish new ones.
5. CREATE decision-stage content: use-case, comparison, integration, and pricing pages with clear claims, statistics, and quotable sourced sentences.
6. TRACK ongoing signals (presence, citations, referral, conversion) on roughly a monthly re-measure cadence as models update.
7. AVOID the hacks: schema-as-magic, llms.txt reliance, fan-out padding, hidden text, fake community seeding.

## What the report must NOT contain (the anti-patterns to refuse)

- A fabricated ROI table or projected revenue. If a projection is shown at all, label it illustrative and state every assumption; never present it as a forecast.
- Outcome guarantees ("+N points in 6 months," "page-one in X weeks"). AI visibility is volatile and model-dependent; guarantees are dishonest.
- A single global score presented as measured truth. Report per engine; if one headline number is shown, label it an ESTIMATE and show its inputs.
- Pricing or tier recommendations driven by the score. Decouple any service tier from the diagnosis so the tool has no incentive to manufacture a "critical" finding. A worse score must never auto-route to a higher price.
- A score for a page that could not be fetched. If fetch failed, the report says "could not read this page," not a number from a cache snippet.

## What GSC and GA4 do and do not show (state this in any traffic section)

If the report touches traffic or analytics, be honest about the tooling limits, or it will mislead:

- Google Search Console does NOT cleanly show AI impressions. Google's AI answers ground on the same index as classic Search, so AI-driven impressions blend into ordinary Search data. Never imply GSC reports AI Overview or AI Mode performance.
- GA4 added an `ai-assistant` medium that auto-groups traffic from referrers on its AI-assistant list, but referral counts undercount AI influence by design: mobile browsers strip or alter the referrer, client-side scripts can be blocked, and assistants often answer with no click at all. The visible click is one layer only.
- Keep crawler fetches and human visits in separate counts; conflating a bot fetch with a human visit distorts the metric.
- Keep paid and earned AI placements in separate buckets. A sponsored result in an AI surface is not evidence about how the organic answer was generated; track earned mentions, citations, sponsored placements, referrals, and conversions as distinct events.
- Attribution is multi-touch and correlational: when citations rise alongside AI-referred visits, that is a relationship worth watching, not proof one caused the other. Do not claim causation.

## The structure of an honest report

- An executive summary that states what was measured vs estimated up front.
- Per-engine presence read using the ladder (cited > named > considered > missing), labeled MEASURED or ESTIMATE.
- DETERMINISTIC findings (crawler access, llms.txt, schema) stated as fact.
- ESTIMATE findings (citability, off-site gaps) clearly labeled with their basis.
- A prioritized action plan following the order above, each action tied to a specific page, source, or platform.
- A "what we could not measure" section naming the limits and pointing to real measurement.

An honest report that says "here is what is certain, here is what we estimate, and here is what only real measurement can tell you" out-converts a fabricated one with senior buyers, and it does not blow up on contact with reality.
