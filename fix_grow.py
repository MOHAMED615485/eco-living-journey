content = open('src/layouts/BlogPost.astro', encoding='utf-8').read()
old = '<script defer src="https://f.convertkit.com/ckjs/ck.5.js"></script>'
new = old + '\n    <script async src="https://cdn.mediavine.com/grow/grow.js"></script>'
open('src/layouts/BlogPost.astro', 'w', encoding='utf-8').write(content.replace(old, new))
print('Done')