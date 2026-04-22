import glob

files = glob.glob('src/content/blog/*.md')
fixed = 0

for f in files:
    content = open(f, 'r', encoding='utf-8').read()
    if 'amzn.to' in content or 'awin1.com' in content:
        new = content.replace(
            'text-decoration:none;display:inline-block',
            'text-decoration:none!important;color:#ffffff!important;display:inline-block'
        ).replace(
            'text-decoration:none;display:block',
            'text-decoration:none!important;color:#ffffff!important;display:block'
        )
        if new != content:
            open(f, 'w', encoding='utf-8').write(new)
            fixed += 1
            print('Fixed:', f)

print('Total files fixed:', fixed)
