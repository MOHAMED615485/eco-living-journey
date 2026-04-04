c = open('src/pages/blog/index.astro', encoding='utf-8').read()

# Fix import paths
c = c.replace(
    "import BaseHead from '../components/BaseHead.astro';",
    "import BaseHead from '../../components/BaseHead.astro';"
)
c = c.replace(
    "import Header from '../components/Header.astro';",
    "import Header from '../../components/Header.astro';"
)
c = c.replace(
    "import Footer from '../components/Footer.astro';",
    "import Footer from '../../components/Footer.astro';"
)

# Fix heroImage null check
c = c.replace(
    'post.data.heroImage',
    '(post.data.heroImage || "")'
)

# Fix slug null check
c = c.replace(
    'post.slug.includes(',
    '(post.slug || "").includes('
)

open('src/pages/blog/index.astro', 'w', encoding='utf-8').write(c)
print('done')
