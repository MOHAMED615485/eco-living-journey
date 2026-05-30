import pathlib, re

f = pathlib.Path('src/content/blog/best-emergency-kit-power-outage-2026.md')
c = f.read_text(encoding='utf-8')

# Replace object-style heroImage with string style
c = re.sub(
    r'heroImage:\n\s+src: ".*?"\n\s+alt: ".*?"',
    'heroImage: "../../assets/best-emergency-kit-power-outage.webp"',
    c
)

f.write_text(c, encoding='utf-8')

# Verify
if 'heroImage: "' in f.read_text(encoding='utf-8'):
    print('FIXED - heroImage is now a string')
else:
    print('ERROR - check manually')
