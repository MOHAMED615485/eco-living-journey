import os
import re

files = [
    'src/content/blog/best-solar-generator-home-backup-2026.md',
    'src/content/blog/best-solar-generator-chest-freezer-2026.md',
    'src/content/blog/ecoflow-vs-jackery-comparison.md',
    'src/content/blog/ecoflow-delta-3-plus-review.md',
]

for f in files:
    if not os.path.exists(f):
        continue
    c = open(f, encoding='utf-8').read()
    c = re.sub(r'<span class="star-filled">(.*?)</span>', r'\1', c)
    c = re.sub(r'<span class="star-empty">(.*?)</span>', r'\1', c)
    open(f, 'w', encoding='utf-8').write(c)
    print('Cleaned: ' + f)

print('done')
