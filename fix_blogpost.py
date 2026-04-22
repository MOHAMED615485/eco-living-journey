import pathlib

bp = pathlib.Path('src/layouts/BlogPost.astro')
content = bp.read_text(encoding='utf-8')

# Add import
old = "import Footer from '../components/Footer.astro';"
new = old + "\nimport PremiumLeadWidget from '../components/PremiumLeadWidget.astro';"
content = content.replace(old, new)

# Add component before </body>
content = content.replace('</body>', '<PremiumLeadWidget />\n</body>')

bp.write_text(content, encoding='utf-8')
print('DONE - BlogPost.astro updated!')
