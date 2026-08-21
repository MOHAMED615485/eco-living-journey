# -*- coding: utf-8 -*-
import os, re
pats = ["73-day", "73 Day", "73 days", "73-Day", "field test", "field-tested", "field tested", "I tested", "we tested", "in my testing", "my testing", "Kill A Watt", "I measured", "I ran it", "own money", "I spent"]
roots = ["src", "public"]
hits = 0
for root in roots:
    for dp, dn, fn in os.walk(root):
        if "node_modules" in dp or ".astro" in dp:
            continue
        for f in fn:
            if not f.endswith((".md", ".astro", ".ts", ".js", ".json", ".txt", ".html")):
                continue
            path = os.path.join(dp, f)
            try:
                c = open(path, encoding="utf-8").read()
            except Exception:
                continue
            lines = c.split("\n")
            for i, line in enumerate(lines, 1):
                for p in pats:
                    if p in line:
                        hits += 1
                        s = line.strip()
                        print(f"{path}:{i}: {s[:160]}")
                        break
print()
print("TOTAL MATCHES:", hits)
