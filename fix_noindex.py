from pathlib import Path

files = [
    'src/content/blog/5-simple-swaps.md',
    'src/content/blog/solar-vs-gas.md'
]

for f in files:
    p = Path(f)
    if not p.exists():
        print(f'NOT FOUND: {f}')
        continue
    content = p.read_text(encoding='utf-8')
    if 'robots:' in content:
        print(f'ALREADY HAS ROBOTS: {f}')
    else:
        content = content.replace('---\n', '---\nrobots: noindex\n', 1)
        p.write_text(content, encoding='utf-8')
        print(f'DONE: {f}')
