import pathlib, re

f = pathlib.Path('src/content/blog/best-emergency-kit-power-outage-2026.md')
c = f.read_text(encoding='utf-8')

old = '''heroImage:
  src: "../../assets/best-emergency-kit-power-outage.webp"
  alt: "Best emergency kit for power outages laid out on a table"'''

new = 'heroImage: "../../assets/best-emergency-kit-power-outage.webp"'

c = c.replace(old, new)
f.write_text(c, encoding='utf-8')

check = f.read_text(encoding='utf-8')
if 'heroImage: "' in check and 'src:' not in check[:500]:
    print('FIXED!')
else:
    print('NOT FIXED - heroImage still:', check[check.find('heroImage'):check.find('heroImage')+100])
