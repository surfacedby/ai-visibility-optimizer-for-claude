# AI crawlers: access is the floor

This is the most DETERMINISTIC part of the audit: robots.txt and bot access can be read directly and stated as fact. It is also where the single most expensive mistake happens. The optional script scripts/check_crawlers.py fetches robots.txt and reports the tokens.

## Three job categories, three different stakes

AI bots do different jobs, and blocking them has very different costs. Treat the three categories separately.

### Training crawlers (blocking does NOT cost citations)

These feed model training. Blocking them opts you out of training corpora; it does not remove you from AI search answers.

- GPTBot (OpenAI), ClaudeBot (Anthropic), CCBot (Common Crawl), Bytespider (ByteDance).
- Google-Extended and Applebot-Extended are not crawlers at all; they are control tokens governing how already-crawled data is used for model training (Gemini training, Apple foundation models), NOT Search or AI Overviews.

### Search-index crawlers (blocking DOES cost citations)

These build the indexes AI search retrieves from. Blocking one is how a brand quietly disappears from cited AI answers.

- OAI-SearchBot (OpenAI): drop out of ChatGPT search sources.
- Claude-SearchBot (Anthropic): not indexed for Claude search.
- PerplexityBot (Perplexity): stop appearing as a linked Perplexity source.
- Googlebot (Google): affects Google Search AND AI Overviews / AI Mode (same index).
- Bingbot (Microsoft): leave the Bing index feeding ChatGPT search and Copilot.
- Applebot (Apple): disappear from Siri, Spotlight, Safari search.

### On-demand user fetchers (robots.txt is unreliable here)

These fetch a page live when a user follows or asks about a link: ChatGPT-User, Claude-User, Perplexity-User, Meta-ExternalFetcher. Because they are user-directed, robots.txt is not a reliable way to stop them; do not assume a robots rule controls them.

## The single most expensive misconfiguration

A site that wants to opt out of training reaches for a blanket block and takes OAI-SearchBot or PerplexityBot down along with GPTBot. The result is losing AI search visibility while only meaning to avoid training. This is the highest-value thing the audit catches: flag any rule that blocks a search-index bot, and distinguish it sharply from training opt-out.

## Beyond robots.txt: open is necessary, not sufficient

A robots.txt that allows the search-index bots means nothing if something else blocks the fetch. The silent killers, each of which stops a retriever while robots.txt is fully open:

- A WAF / CDN / bot-protection rule returning 403 to the retriever's user-agent or IP.
- JavaScript rendering: the main text is absent from the initial HTML, so a non-rendering fetcher sees an empty page.
- Redirect chains, dead URLs, or a canonical pointing at a different version.
- Important pages buried by thin internal linking, so they are rarely fetched.

Verification checklist. The agent can do these from outside: confirm a 200 (not 403) when it fetches as the retriever user-agent, inspect the robots rules, and confirm the main text is present in the initial HTML (not only after JS). Two more need the site owner's access: confirming the security stack (WAF/CDN) is not user-agent or IP blocking, and scanning server logs for clusters of failed requests on key pages. If the agent does not have CDN or log access, do not skip these: ask the user to check them or to export the relevant logs, and give them the exact filter to run.

## What can and cannot be confirmed in the site's logs

This is a log read; if the agent does not hold the site's logs, ask the user to export them. The exact user-agents that identify a user-initiated retrieval fetch (these CAN be log-confirmed): ChatGPT-User (OpenAI), Claude-User (Anthropic), Perplexity-User (Perplexity), Manus-User (Manus), meta-webindexer (Meta). Measured behavioral fingerprints: Claude requests /robots.txt first from a dedicated IP range; ChatGPT fetches from several Azure IPs in one burst; Manus renders the full page (CSS/JS/images) like a browser.

The correction most tools get wrong: Gemini, Copilot, and Grok present NO isolable retrieval user-agent. Gemini reads off the Googlebot index, so its retrieval is indistinguishable from ordinary Google crawling; Copilot arrives as plain Chrome; Grok as plain Safari or Chrome. You cannot log-confirm these three by user-agent. Infer Gemini from Googlebot access; for Copilot and Grok, rely on the referral signal (a human visit whose Referer is the assistant host: chatgpt.com, claude.ai, perplexity.ai, gemini.google.com, copilot.microsoft.com, grok.com), not a crawl UA. So "check your logs for each engine's bot" is only partly possible: log-confirm the bots that declare a UA, and infer the rest.

## Verifying real bots (anti-spoof)

The user-agent string is a label, not proof. To verify a real bot that DOES declare a UA, match the source IP against the vendor's published list or reverse DNS (for example OpenAI and Perplexity publish IP lists; Google and Apple verify via reverse DNS). Do not block or trust on user-agent alone.

## Crawl is not referral

AI platforms crawl many pages per visitor they send (some vendors extremely lopsided), so do not judge AI value by referral clicks alone. Crawl access is necessary for citation; it is not itself the outcome (see measurement.md).

## How to deliver a crawler finding

State, per search-index bot, whether it is allowed (DETERMINISTIC). Flag any blanket block that catches a search-index bot. Separate "you opted out of training" (fine, if intended) from "you accidentally opted out of being cited" (almost never intended). Recommend the exact robots.txt change.
