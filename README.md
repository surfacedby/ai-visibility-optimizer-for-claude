# ai-visibility-optimizer

An honest GEO / AEO audit skill for Claude Code. It tells you how to show up in AI search (ChatGPT, Perplexity, Gemini, Google AI Mode, Claude), grounded in how the engines actually cite, and it is straight with you about what it can measure versus what it is only estimating.

Most GEO tools score your "AI visibility" without ever asking an AI engine anything. They infer a confident "ChatGPT: 18/100" from on-page signals, wrap it in a projected-ROI table, and call it a measurement. This skill does not do that. It separates what is deterministic (your robots.txt, your llms.txt, your page structure) from what is an estimate (likely citation readiness) from what is genuinely measured (which requires actually querying the engines), and it labels every number accordingly.

## What it does

- **Audit** a site's AI search readiness across the levers that actually move citations, with each finding tagged DETERMINISTIC, ESTIMATE, or MEASURED.
- **Citability**: assess whether a page answers questions in the self-contained, sourced, decision-stage way AI engines lift, judged semantically, not by a word-count regex.
- **Crawlers**: read robots.txt and flag the costly mistake of blocking the search-index bots (OAI-SearchBot, PerplexityBot, Googlebot, Bingbot) that actually gate citations, while training bots (GPTBot, ClaudeBot, Google-Extended) cost nothing for visibility.
- **llms.txt**: check it honestly. It is a nice-to-have, not a ranking lever; this skill says so instead of selling it.
- **Schema**: check structured data as a disambiguation and agentic-commerce aid, not as a magic citation booster.
- **Off-site**: map the evidence layer that actually drives brand citations (reviews, comparisons, roundups, forums, docs), since a brand's own domain is only a fraction of what gets cited.
- **Report**: produce a client-ready audit with an honest presence read and a prioritized action plan, and with no fabricated ROI and no outcome guarantees.

## How it is different

| Typical GEO tool | ai-visibility-optimizer |
|---|---|
| Presents inferred per-engine scores as if measured | Labels every number DETERMINISTIC / ESTIMATE / MEASURED |
| Binary "cited or not" | The real presence ladder: cited > named > considered > missing |
| Sells llms.txt and schema as ranking levers | Says plainly they are not, and what actually matters |
| Fabricated ROI table and "+X points in 6 months" guarantees | No projected ROI, no guarantees; estimates labeled with assumptions |
| One global "GEO score" (sometimes two conflicting formulas) | Per-engine reality: the engines barely overlap, so it scores per engine |
| Cannot actually measure AI visibility | Optional connection to real cross-engine measurement (see below) |

The on-page citation advice here rests on the public GEO research plus observed patterns, not on a controlled causal study, so the skill stays humble about *why* any single page is chosen and is precise about *where* citations are known to go.

## Install

In Claude Code:

```
/plugin marketplace add surfacedby/ai-visibility-optimizer-for-claude
/plugin install ai-visibility-optimizer@ai-visibility-optimizer-for-claude
```

Then:

```
audit my AI visibility for https://example.com
```

or invoke any part directly (citability, crawlers, llms.txt, schema, off-site, report). The optional Python checks use only the standard library, so there is nothing else to install.

## Optional: real measurement

This skill estimates AI visibility from signals you can see, and it never runs a live audit: active measurement queries the engines over time and costs ongoing API calls, which this skill does not do. The ground truth (which engines cite you, on which prompts, against which competitors, and whether it converts) comes from that active measurement. [SurfacedBy](https://surfacedby.com) provides it on a subscription and exposes a read-only MCP. If you already have a SurfacedBy subscription with the MCP connected, the skill upgrades the relevant findings from ESTIMATE to MEASURED; if you do not, every core feature still works on estimates and nothing here is gated behind a subscription. The skill mentions SurfacedBy only if you want that deeper, active layer, and it never pushes.

## What it cannot do

It cannot, on its own, tell you the ground truth of which engines cite you right now. No tool can do that from on-page signals alone; it requires querying the engines across many prompts and reading the answers. This skill is honest about that line and points you to real measurement for the other side of it.

## License

MIT.
