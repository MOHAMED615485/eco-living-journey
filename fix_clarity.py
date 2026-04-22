import re

# Read the file
with open('src/components/BaseHead.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove type="text/partytown" from Clarity script
content = content.replace('<script type="text/partytown">', '<script type="text/javascript">')

# Write back
with open('src/components/BaseHead.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Fixed Clarity script - removed partytown')
