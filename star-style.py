# Add star rating CSS to BlogPost.astro and replace plain stars with styled ones

import os

# Step 1: Add CSS to BlogPost.astro
blogpost = open('src/layouts/BlogPost.astro', encoding='utf-8').read()

star_css = """
<style>
  .star-filled { color: #f5a623; font-size: 1.1rem; }
  .star-empty { color: #ccc; font-size: 1.1rem; }
  table .star-filled, table .star-empty { font-size: 1rem; }
</style>
"""

if 'star-filled' not in blogpost:
    blogpost = blogpost.replace('</head>', star_css + '</head>')
    open('src/layouts/BlogPost.astro', 'w', encoding='utf-8').write(blogpost)
    print('CSS added to BlogPost.astro')
else:
    print('CSS already present')

# Step 2: Replace plain star characters with styled HTML in articles
files = [
    'src/content/blog/best-solar-generator-home-backup-2026.md',
    'src/content/blog/best-solar-generator-chest-freezer-2026.md',
    'src/content/blog/ecoflow-vs-jackery-comparison.md',
    'src/content/blog/ecoflow-delta-3-plus-review.md',
]

filled = '<span class="star-filled">\u2605</span>'
empty = '<span class="star-empty">\u2606</span>'

for filepath in files:
    if not os.path.exists(filepath):
        print('Skip: ' + filepath)
        continue
    c = open(filepath, encoding='utf-8').read()
    c = c.replace('\u2605', filled)
    c = c.replace('\u2606', empty)
    open(filepath, 'w', encoding='utf-8').write(c)
    print('Updated: ' + filepath)

print('All done')
