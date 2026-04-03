import os

files = [
    "src/content/blog/best-solar-generator-chest-freezer-2026.md",
    "src/content/blog/bluetti-ac200l-review.md",
    "src/content/blog/best-solar-generator-home-backup-2026.md",
    "src/content/blog/jackery-explorer-1000-v2-review.md"
]

eco_btn = '<div class="cta-container"><a href="https://amzn.to/41D10iO" class="cta-button-amazon" target="_blank" rel="nofollow">Check EcoFlow DELTA 3 Plus on Amazon</a></div>'
jack_btn = '<div class="cta-container"><a href="https://amzn.to/47Esd8d" class="cta-button-amazon" target="_blank" rel="nofollow">Check Jackery Explorer 1000 V2 on Amazon</a></div>'
blue_btn = '<div class="cta-container"><a href="https://amzn.to/4sFpOCG" class="cta-button-amazon" target="_blank" rel="nofollow">Check Bluetti AC200L on Amazon</a></div>'

bestfors = [
    ("**Best for:** Any chest freezer regardless of LRA rating. The most reliable choice if you want zero surprises.", eco_btn),
    ("**Best for:** Budget-conscious buyers with modern chest freezers (LRA under 9.0) in moderate climates.", jack_btn),
    ("**Best for:** Budget-conscious homeowners with standard LRA freezers who want reliable backup at a lower price point.", jack_btn),
    ("**Best for:** Homeowners who want to run multiple appliances simultaneously for extended outages.", blue_btn),
    ("**Best for:** Homeowners who want extended whole-home backup and are willing to invest in a serious system.", blue_btn),
]

for filepath in files:
    if not os.path.exists(filepath):
        print("Skip: " + filepath)
        continue
    c = open(filepath, encoding="utf-8").read()
    for btn in [eco_btn, jack_btn, blue_btn]:
        c = c.replace
cd C:\projects\eco-living-journey

$script = @'
import os

files = [
    "src/content/blog/best-solar-generator-chest-freezer-2026.md",
    "src/content/blog/bluetti-ac200l-review.md",
    "src/content/blog/best-solar-generator-home-backup-2026.md",
    "src/content/blog/jackery-explorer-1000-v2-review.md"
]

eco_btn = '<div class="cta-container"><a href="https://amzn.to/41D10iO" class="cta-button-amazon" target="_blank" rel="nofollow">Check EcoFlow DELTA 3 Plus on Amazon</a></div>'
jack_btn = '<div class="cta-container"><a href="https://amzn.to/47Esd8d" class="cta-button-amazon" target="_blank" rel="nofollow">Check Jackery Explorer 1000 V2 on Amazon</a></div>'
blue_btn = '<div class="cta-container"><a href="https://amzn.to/4sFpOCG" class="cta-button-amazon" target="_blank" rel="nofollow">Check Bluetti AC200L on Amazon</a></div>'

bestfors = [
    ("**Best for:** Any chest freezer regardless of LRA rating. The most reliable choice if you want zero surprises.", eco_btn),
    ("**Best for:** Budget-conscious buyers with modern chest freezers (LRA under 9.0) in moderate climates.", jack_btn),
    ("**Best for:** Budget-conscious homeowners with standard LRA freezers who want reliable backup at a lower price point.", jack_btn),
    ("**Best for:** Homeowners who want to run multiple appliances simultaneously for extended outages.", blue_btn),
    ("**Best for:** Homeowners who want extended whole-home backup and are willing to invest in a serious system.", blue_btn),
]

for filepath in files:
    if not os.path.exists(filepath):
        print("Skip: " + filepath)
        continue
    c = open(filepath, encoding="utf-8").read()
    for btn in [eco_btn, jack_btn, blue_btn]:
        c = c.replace("\n\n" + btn + "\n\n", "\n\n")
        c = c.replace("\n\n" + btn + "\n", "\n\n")
    for bestfor, btn in bestfors:
        if bestfor in c:
            after = c[c.find(bestfor)+len(bestfor):c.find(bestfor)+len(bestfor)+300]
            if btn not in after:
                c = c.replace(bestfor, bestfor + "\n\n" + btn)
    open(filepath, "w", encoding="utf-8").write(c)
    print("Fixed: " + filepath)

print("All done")
