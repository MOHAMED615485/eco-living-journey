import os

# CTA buttons for each review article
ctas = {
    "src/content/blog/ecoflow-delta-3-plus-review.md": """
<div style="margin:24px 0;">
  <a href="https://amzn.to/41D10iO" target="_blank" rel="noopener noreferrer" style="background-color:#c2410c;color:#ffffff;padding:14px 32px;border-radius:8px;font-weight:700;font-size:16px;text-decoration:none;display:inline-block;box-shadow:0 4px 6px rgba(0,0,0,0.1);">
    🛒 Check EcoFlow DELTA 3 Plus Price on Amazon →
  </a>
</div>
""",
    "src/content/blog/jackery-explorer-1000-v2-review.md": """
<div style="margin:24px 0;">
  <a href="https://amzn.to/47Esd8d" target="_blank" rel="noopener noreferrer" style="background-color:#c2410c;color:#ffffff;padding:14px 32px;border-radius:8px;font-weight:700;font-size:16px;text-decoration:none;display:inline-block;box-shadow:0 4px 6px rgba(0,0,0,0.1);">
    🛒 Check Jackery Explorer 1000 V2 Price on Amazon →
  </a>
</div>
""",
    "src/content/blog/bluetti-ac200l-review.md": """
<div style="margin:24px 0;">
  <a href="https://amzn.to/4sFpOCG" target="_blank" rel="noopener noreferrer" style="background-color:#c2410c;color:#ffffff;padding:14px 32px;border-radius:8px;font-weight:700;font-size:16px;text-decoration:none;display:inline-block;box-shadow:0 4px 6px rgba(0,0,0,0.1);">
    🛒 Check Bluetti AC200L Price on Amazon →
  </a>
</div>
"""
}

def add_cta_after_first_paragraph(filepath, cta):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip the frontmatter (between --- and ---)
    parts = content.split("---")
    if len(parts) < 3:
        print(f"SKIP — could not parse frontmatter in {filepath}")
        return

    frontmatter = "---" + parts[1] + "---"
    body = "---".join(parts[2:])

    # Find the end of the first paragraph in the body
    # First paragraph ends at the first double newline after some content
    lines = body.strip().split("\n")
    first_para_end = 0
    in_para = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped and not in_para:
            in_para = True
        elif in_para and not stripped:
            first_para_end = i
            break

    if first_para_end == 0:
        # fallback — insert after line 3
        first_para_end = 3

    # Check if CTA already exists
    if "amzn.to" in body[:500]:
        print(f"SKIP — CTA already exists near top of {filepath}")
        return

    # Insert CTA after first paragraph
    lines.insert(first_para_end, cta)
    new_body = "\n".join(lines)
    new_content = frontmatter + "\n" + new_body

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"SUCCESS — CTA added to {filepath}")

# Run for all 3 review articles
for filepath, cta in ctas.items():
    if os.path.exists(filepath):
        add_cta_after_first_paragraph(filepath, cta)
    else:
        print(f"NOT FOUND — {filepath}")

print("\nDone. Now run: git add -A && git commit -m 'fix: add early CTA buttons to review articles' && git push origin main")
