path = 'src/components/Header.astro'
content = open(path, encoding='utf-8').read()
old = '\t\t\t<HeaderLink href="/about">About</HeaderLink>'
new = '\t\t\t<HeaderLink href="/about">About</HeaderLink>\n\t\t\t<HeaderLink href="/contact">Contact</HeaderLink>'
result = content.replace(old, new)
if result == content:
    print('ERROR - line not found')
else:
    open(path, 'w', encoding='utf-8').write(result)
    print('SUCCESS - Contact link added to nav')
