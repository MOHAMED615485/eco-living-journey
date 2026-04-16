import re

path = 'src/layouts/BlogPost.astro'
content = open(path, encoding='utf-8').read()

old = '''<script is:inline type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": []
}
</script>'''

new = ''

result = content.replace(old, new)

if result == content:
    print('ERROR - block not found, check spacing')
else:
    open(path, 'w', encoding='utf-8').write(result)
    print('SUCCESS - empty FAQPage block removed')
