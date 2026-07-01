# llms.txt: the honest take

Most GEO tools sell an llms.txt generator as a visibility lever. It is not one. This skill checks llms.txt as optional hygiene and tells the user the truth.

## What it is

An orientation file: a curated Markdown index at the domain root that maps a site's important pages. It is not a permission mechanism and not a ranking mechanism.

## Who actually reads it

Documented adoption is minimal:

- Google explicitly does not support it. Google has stated machine-readable files like llms.txt are not needed for generative AI features in Search, and has compared it to the outdated keywords meta tag.
- OpenAI, Anthropic, and Perplexity have not published documentation committing their crawlers to read it.
- Server-log analyses find AI crawlers rarely request the file.

## The verdict

There is no solid public evidence that adding llms.txt by itself makes AI systems recommend a brand more often. A weak site with a clean llms.txt file is still a weak site.

## The legitimate use

It is a documentation aid: an llms-full.txt that lets someone paste a product's docs into a coding assistant, and a supporting orientation layer for doc-heavy sites with scattered information. Useful there; not a visibility tactic.

## How to deliver an llms.txt finding

Report presence and validity (DETERMINISTIC). If the site is documentation-heavy, suggest it as optional hygiene. Never present it as a citation or ranking lever, and never let a clean llms.txt inflate a visibility assessment. If a prospect was sold llms.txt as a shortcut, say plainly that it is not one.
