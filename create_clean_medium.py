import os
import re

# Read the article
with open('src/content/blog/best-solar-generator-home-backup-2026.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract title and description
title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
title = title_match.group(1) if title_match else 'Best Solar Generator for Home Backup Power 2026: Field-Tested Guide'

desc_match = re.search(r'description:\s*["\']([^"\']+)["\']', content)
description = desc_match.group(1) if desc_match else ''

# Remove frontmatter
content_no_frontmatter = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

# Remove the markdown table entirely and replace with a cleaner format
table_pattern = r'\|[^\n]+\|[\s\S]*?\n\n'
content_no_frontmatter = re.sub(table_pattern, '''
**Quick Comparison:**

- **EcoFlow DELTA 3 Plus:** 1,024Wh | 1,800W output | 12.3kg | ★★★★★ Surge | ★★★☆☆ Value | 8-9hr freezer runtime
- **Jackery 1000 V2:** 1,070Wh | 2,000W output | 11.8kg | ★★★★☆ Surge | ★★★★★ Value | 8.5hr freezer runtime  
- **Bluetti AC200L:** 2,048Wh | 2,400W output | 28kg | ★★★★★ Surge | ★★★☆☆ Value | 12+hr freezer runtime

''', content_no_frontmatter)

# Create canonical URL
canonical_url = 'https://ecoliving-journey.com/blog/best-solar-generator-home-backup-2026/'

# Build Medium post
medium_post = f'''# {title}

{description}

---

{content_no_frontmatter}

---

**Originally published at** [{canonical_url}]({canonical_url})

*This article was written by Ethan Clarke, who field-tests portable power stations for 73+ days to bring you real-world backup power insights. Read more at [Eco Living Journey](https://ecoliving-journey.com).*
'''

# Save
with open('medium-posts/medium-best-solar-CLEAN.md', 'w', encoding='utf-8') as f:
    f.write(medium_post)

print('✅ Clean version created without table!')
