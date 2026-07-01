#!/usr/bin/env python3
"""
check_crawlers.py - DETERMINISTIC AI-crawler access check from robots.txt.

Reads a site's robots.txt and reports, per AI bot, whether it is allowed or
blocked. Flags the single most expensive mistake: blocking a SEARCH-INDEX bot
(which gates AI citations) while only meaning to opt out of TRAINING.

Dependency-free (standard library only). This is a real, deterministic read of
robots.txt; it is NOT a measurement of whether you are actually cited.

Usage:
  python check_crawlers.py example.com
  python check_crawlers.py https://example.com
"""
import sys, urllib.request, urllib.error
from urllib.parse import urlparse

# (token, vendor, category). category drives the stakes of a block.
BOTS = [
    # search-index: blocking these COSTS citations
    ("OAI-SearchBot", "OpenAI", "search-index"),
    ("Claude-SearchBot", "Anthropic", "search-index"),
    ("PerplexityBot", "Perplexity", "search-index"),
    ("Googlebot", "Google", "search-index"),
    ("Bingbot", "Microsoft", "search-index"),
    ("Applebot", "Apple", "search-index"),
    # training: blocking these does NOT cost citations
    ("GPTBot", "OpenAI", "training"),
    ("ClaudeBot", "Anthropic", "training"),
    ("CCBot", "Common Crawl", "training"),
    ("Bytespider", "ByteDance", "training"),
    ("Google-Extended", "Google", "training-control"),
    ("Applebot-Extended", "Apple", "training-control"),
    # on-demand user fetchers: robots.txt is unreliable for these
    ("ChatGPT-User", "OpenAI", "on-demand"),
    ("Claude-User", "Anthropic", "on-demand"),
    ("Perplexity-User", "Perplexity", "on-demand"),
]

def fetch_robots(domain):
    host = urlparse(domain if "://" in domain else "https://" + domain).netloc or domain
    url = f"https://{host}/robots.txt"
    req = urllib.request.Request(url, headers={"User-Agent": "ai-visibility-optimizer/1.0 (+robots-check)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return host, r.read().decode("utf-8", "replace"), None
    except urllib.error.HTTPError as e:
        return host, "", f"HTTP {e.code}"
    except Exception as e:
        return host, "", str(e)

def parse_groups(text):
    # Map each user-agent (lowercased) to its list of Disallow path prefixes.
    groups, current = {}, []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        field, _, value = line.partition(":")
        field, value = field.strip().lower(), value.strip()
        if field == "user-agent":
            ua = value.lower()
            current = groups.setdefault(ua, [])
        elif field == "disallow" and current is not None:
            current.append(value)
    return groups

def is_blocked(groups, token):
    # A bot is blocked if its own group, or the wildcard group, disallows "/".
    for ua in (token.lower(), "*"):
        rules = groups.get(ua)
        if rules and any(p == "/" for p in rules):
            return True
    return False

def main():
    if len(sys.argv) < 2:
        print("usage: python check_crawlers.py <domain>"); sys.exit(2)
    host, text, err = fetch_robots(sys.argv[1])
    print(f"robots.txt for {host}")
    if err:
        print(f"  could not read robots.txt ({err}).")
        print("  No robots.txt usually means nothing is blocked, but verify the CDN/WAF is not challenging bots.")
        return
    groups = parse_groups(text)
    blocked_search = []
    print("\n  SEARCH-INDEX bots (blocking COSTS AI citations):")
    for token, vendor, cat in BOTS:
        if cat != "search-index":
            continue
        b = is_blocked(groups, token)
        print(f"    {'BLOCKED' if b else 'allowed'}  {token} ({vendor})")
        if b:
            blocked_search.append(f"{token} ({vendor})")
    print("\n  TRAINING bots (blocking does NOT cost citations; opting out of training is fine):")
    for token, vendor, cat in BOTS:
        if cat not in ("training", "training-control"):
            continue
        b = is_blocked(groups, token)
        note = " [control token, not a crawler]" if cat == "training-control" else ""
        print(f"    {'blocked' if b else 'allowed'}  {token} ({vendor}){note}")
    print("\n  ON-DEMAND user fetchers (robots.txt is unreliable for these; user-directed):")
    for token, vendor, cat in BOTS:
        if cat != "on-demand":
            continue
        b = is_blocked(groups, token)
        print(f"    {'disallowed (may be ignored)' if b else 'allowed'}  {token} ({vendor})")
    print("\n  VERDICT:")
    if blocked_search:
        print("    COSTLY MISCONFIGURATION: you are blocking search-index bots that gate AI citations:")
        for s in blocked_search:
            print(f"      - {s}")
        print("    If you only meant to opt out of training, unblock these and block only the training bots.")
    else:
        print("    No search-index bot is blocked via robots.txt. Access is the floor, not the finish line:")
        print("    also have the site owner confirm via their server logs that these crawlers actually receive 200s (CDN/WAF/JS can still block them).")
    print("\n  NOTE: this is a deterministic robots.txt read, not a measurement of whether you are cited.")

if __name__ == "__main__":
    main()
