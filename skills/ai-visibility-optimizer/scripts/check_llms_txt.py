#!/usr/bin/env python3
"""
check_llms_txt.py - DETERMINISTIC llms.txt presence/validity check, told honestly.

Checks whether a site has /llms.txt (and /llms-full.txt), and reports basic
validity. It deliberately does NOT score llms.txt as a visibility lever, because
it is not one: no major engine commits to reading it and Google explicitly does
not support it. This check exists to set expectations correctly, not to sell a file.

Dependency-free (standard library only).

Usage:
  python check_llms_txt.py example.com
"""
import sys, urllib.request, urllib.error
from urllib.parse import urlparse

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ai-visibility-optimizer/1.0 (+llmstxt-check)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            ct = r.headers.get("Content-Type", "")
            return r.status, ct, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, "", ""
    except Exception as e:
        return None, str(e), ""

def assess(body):
    # Minimal validity: it should be Markdown-ish, start with an H1, and list links.
    lines = [l for l in body.splitlines()]
    has_h1 = any(l.strip().startswith("# ") for l in lines[:5])
    link_count = sum(1 for l in lines if "](" in l)
    return has_h1, link_count

def main():
    if len(sys.argv) < 2:
        print("usage: python check_llms_txt.py <domain>"); sys.exit(2)
    host = urlparse(sys.argv[1] if "://" in sys.argv[1] else "https://" + sys.argv[1]).netloc or sys.argv[1]
    for name in ("llms.txt", "llms-full.txt"):
        status, ct, body = fetch(f"https://{host}/{name}")
        if status == 200 and body.strip():
            has_h1, links = assess(body)
            print(f"{name}: PRESENT ({len(body)} bytes, {links} links, {'H1 ok' if has_h1 else 'no leading H1'})")
        elif status == 200:
            print(f"{name}: present but empty")
        elif status is None:
            print(f"{name}: could not fetch ({ct})")
        else:
            print(f"{name}: not found (HTTP {status})")
    print(
        "\nHONEST NOTE: llms.txt is an orientation file, not a ranking or permission lever.\n"
        "Google has stated it does not support llms.txt; OpenAI, Anthropic, and Perplexity have not\n"
        "committed their crawlers to read it, and server logs show it is rarely fetched. A clean\n"
        "llms.txt does not make AI cite you more. It is reasonable hygiene for documentation-heavy\n"
        "sites (especially llms-full.txt for pasting docs into coding assistants); it is not a\n"
        "visibility tactic. Do not let its presence or absence move a visibility assessment."
    )

if __name__ == "__main__":
    main()
