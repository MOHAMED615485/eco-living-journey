import re

# Read the file
with open('src/components/BaseHead.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old Clarity ID with the new one
content = content.replace('wf28mimveg', 'wf2f6vli35')

# Also remove the ?ref=bwt parameter since the new code doesn't have it
content = content.replace('https://www.clarity.ms/tag/"+i+"?ref=bwt"', 'https://www.clarity.ms/tag/"+i')

# Write back
with open('src/components/BaseHead.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Clarity tracking code updated to wf2f6vli35')
