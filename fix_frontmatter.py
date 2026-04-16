from pathlib import Path

path = Path('src/content/blog/will-1000w-solar-generator-run-refrigerator.md')
content = path.read_text(encoding='utf-8')

old = '''---
title: "Will a 1000W Solar Generator Run a Refrigerator? (Ethan's Real Test)"
description: "Can a 1000W solar generator actually power your fridge? Ethan tested three models for 73 days. Here's the honest answer — including what most guides get wrong."
pubDate: 2026-04-14
author: "Ethan"
heroImage: "/images/1000w-solar-generator-refrigerator.jpg"
heroImageAlt: "1000W solar generator connected to a standard kitchen refrigerator"
tags: ["solar generators", "refrigerator", "home backup power", "buying guide"]
featured: false
---'''

new = '''---
title: "Will a 1000W Solar Generator Run a Refrigerator? (Ethan's Real Test)"
description: "Can a 1000W solar generator actually power your fridge? Ethan tested three models for 73 days. Here's the honest answer — including what most guides get wrong."
pubDate: "Apr 14 2026"
heroImage: "../../assets/will-1000w-solar-generator-run-refrigerator.webp"
---'''

result = content.replace(old, new)
if result == content:
    print('ERROR - frontmatter not matched')
else:
    path.write_text(result, encoding='utf-8')
    print('SUCCESS - frontmatter fixed')
