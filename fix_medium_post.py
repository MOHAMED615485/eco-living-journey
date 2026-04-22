import os
import re

# Read the original article
with open('src/content/blog/best-solar-generator-home-backup-2026.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract title and description
title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
title = title_match.group(1) if title_match else 'Best Solar Generator for Home Backup Power 2026: Field-Tested Guide'

desc_match = re.search(r'description:\s*["\']([^"\']+)["\']', content)
description = desc_match.group(1) if desc_match else ''

# Remove frontmatter
content_no_frontmatter = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

# Fix star ratings - replace broken encoding with proper stars
content_no_frontmatter = content_no_frontmatter.replace('â˜…', '★')
content_no_frontmatter = content_no_frontmatter.replace('â˜†', '☆')

# Create canonical URL
canonical_url = 'https://ecoliving-journey.com/blog/best-solar-generator-home-backup-2026/'

# Build Medium post with proper formatting
medium_post = f'''# {title}

{description}

---

{content_no_frontmatter}

---

**Originally published at** [{canonical_url}]({canonical_url})

*This article was written by Ethan Clarke, who field-tests portable power stations for 73+ days to bring you real-world backup power insights. Read more at [Eco Living Journey](https://ecoliving-journey.com).*
'''

# Save fixed version
with open('medium-posts/medium-best-solar-generator-home-backup-2026-FIXED.md', 'w', encoding='utf-8') as f:
    f.write(medium_post)

print('✅ Fixed version created: medium-posts/medium-best-solar-generator-home-backup-2026-FIXED.md')
print('\nNow copy this to clipboard...')
