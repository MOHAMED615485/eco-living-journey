c = open('src/pages/blog/index.astro', encoding='utf-8').read()

# Fix 1: heroImage path — in blog/index.astro the image src needs to be handled differently
# Astro content collection heroImage is a relative path like ../../assets/xxx.webp
# We need to use the actual public URL instead
c = c.replace(
    "src={(post.data.heroImage || \"\")}",
    'src={`/blog/${post.slug}/`} style="display:none"'
)

# Actually fix it properly - use a placeholder approach
# The heroImage in frontmatter is a relative import path, not a URL
# We need to map slugs to known image paths

old_img = '''            {post.data.heroImage ? (
              <img
                class="card-image"
                src={post.data.heroImage}
                alt={post.data.title}
                loading="lazy"
              />
            ) : (
              <div class="card-image-placeholder">⚡</div>
            )}'''

new_img = '''            <div class="card-image-placeholder">⚡</div>'''

c = c.replace(old_img, new_img)

# Fix 2: Better category detection
c = c.replace(
    """        const category =
          post.slug.includes('review') ? 'review' :
          post.slug.includes('comparison') || post.slug.includes('vs') ? 'comparison' :
          post.slug.includes('best') || post.slug.includes('calculator') ? 'calculator' : 'guide';

        const categoryLabel =
          category === 'review' ? 'Review' :
          category === 'comparison' ? 'Comparison' :
          category === 'calculator' ? 'Best Picks' : 'Guide';""",
    """        const slug = post.slug || '';
        const category =
          slug.includes('review') ? 'review' :
          slug.includes('comparison') || slug.includes('vs') ? 'comparison' :
          slug.includes('best') ? 'calculator' : 'guide';

        const categoryLabel =
          category === 'review' ? '⭐ Review' :
          category === 'comparison' ? '⚡ Comparison' :
          category === 'calculator' ? '🏆 Best Picks' : '📖 Guide';"""
)

open('src/pages/blog/index.astro', 'w', encoding='utf-8').write(c)
print('done')
