# Citability: what actually earns a citation

How to judge whether a page is the kind AI answers lift, and what to change. Judge this semantically by reading the page, never by a word-count regex. Label the output an ESTIMATE: these are well-reasoned, externally-supported levers, not a causal score.

## The honesty line (state it in every citability finding)

Where citations go is observable; WHY a single page was chosen is not settled. The levers below come from a controlled public study (Princeton-led GEO research) plus observed patterns, not from a controlled page-feature join. Present them as strong, evidence-backed guidance, and do not claim a given edit will cause a citation. If a page cannot be fetched, say so and do not score it from a cache snippet.

## Verified / research-backed levers

- Statistics, authoritative sourcing, and direct quotations: the Princeton GEO study found these lifted visibility in AI answers by up to roughly 40%. Keyword stuffing underperformed the baseline. This is the strongest evidence-backed lever.
- Answer-first structure: front-load a direct answer (about 40-60 words) before the narrative; a short "key takeaways" or "fast facts" block helps.
- Self-contained, extractable chunks: write facts in small, liftable segments and tables so a chunk still makes sense quoted in isolation.
- Question-based headings that mirror real queries ("What is X?", "How much does X cost?") rather than label nouns; each section answers its heading completely.
- Numerical precision with attribution: exact figures ("a 15 to 25 dollar fee") beat vague claims; vague claims do not get cited.
- Inline sourcing: a page that cites its sources becomes a page worth citing.
- Comparison tables that include an honest weaknesses or limitations column (one cited page literally used a column titled "honest limitations"); even-handed comparisons get pulled.
- Surface E-E-A-T signals: a named author with a credential, a visible "updated on" date, and firsthand evidence ("I tested this for fifty days").

## Page type matters more than most tools admit

On a measured cited corpus, decision-stage pages earned citations at far higher rates than blog posts (integration pages and pricing/comparison pages well above generic blog content). Listicles with the year in the title saw near-universal adoption among cited sources. Implication: for citations, prioritize use-case, comparison, integration, and pricing pages with clear claims over yet another blog post.

## Folklore to skip (do not recommend these as citation levers)

- Schema as a magic citation shortcut (see schema.md). It is disambiguation, not a booster.
- llms.txt as a ranking lever (see llms-txt.md). It is not.
- Keyword stuffing and hidden brand text: underperformed baseline in the study.
- Mass fan-out page multiplication: do not generate hundreds of thin pages for every possible sub-query. Use fan-out analysis to find coverage gaps, then write a few strong pages.
- Seeding fake Reddit or community threads: rejected; it is a trust and policy risk, not a tactic.
- Generic informational content as a differentiator: it is cheap to produce now, which is exactly why it no longer differentiates.

## How the engine shows the source, and why a ranking page still fails

Citation logic operates partly independently of ranking: roughly 30% of domains cited in Google AI Overviews do not rank on organic page one for the same query (measured, external study). Four reasons a page that ranks still does not get cited: answer fit (the AI answers a narrower sub-question than the page targets), claim support (the citation backs a specific fact or step, not a general topic), source type (for some queries docs, forums, reviews, and comparisons are preferred), and freshness (newer or clearly dated wins). Presentation varies by engine and is worth knowing: Google AI Overviews embeds source links inline in the answer text; ChatGPT Search shows inline links plus a Sources sidebar; Google surfaces a Highly Cited badge on frequently-cited links. Do not assume the engines use the same source cues.

## Video as a citation surface

AI also cites video, and most GEO tools miss it. Video functions as evidence in an answer (the AI summarizes a tutorial, compares products from a review, or pulls a claim from a transcript), and YouTube's Ask YouTube compiles videos into generated answers. Levers for video citability: a transcript (gives the AI quotable text), chapters (locate topics in long video), VideoObject structured data (the Google video baseline), an on-page embed tying the video to the surrounding text and product, a clear description, and a credible channel. If a brand's best evidence lives in video, audit the video too, not only the pages.

## The brand-understanding audit (is the AI confused, and why)

AI builds its model of a brand from direct page access (crawlable HTML), consistency across third-party sources, structured clarity (schema that MATCHES visible content), and plain-language signals (category, audience, use case stated in visible HTML). When the AI describes a brand wrong, pinpoint the cause: MISSING facts, BURIED facts (trapped in gated PDFs, sales decks, or form-hidden content), or STALE external sources. Fix in priority order: rewrite core pages with a plain "helps [audience] do [job] through [mechanism]" line; move trapped facts into public crawlable HTML; align drifted third-party sources; add schema only where it matches visible content (never to smuggle unsupported claims); treat llms.txt as a navigation map, not a strategy.

## How to deliver a citability finding

For each key page: state whether it is answer-first, self-contained, sourced, decision-stage, and E-E-A-T-signalled; show the specific gap; recommend the concrete edit; and label the whole thing ESTIMATE (citation readiness), not a measured citation rate. The only way to know if the page is actually cited is to measure (see measurement.md).
