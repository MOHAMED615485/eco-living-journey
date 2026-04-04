c = open('src/pages/blog/index.astro', encoding='utf-8').read()

# Fix 1: Category detection - check title instead of slug
old_cat = """        const slug = post.slug || '';
        const category =
          slug.includes('review') ? 'review' :
          slug.includes('comparison') || slug.includes('vs') ? 'comparison' :
          slug.includes('best') ? 'calculator' : 'guide';

        const categoryLabel =
          category === 'review' ? '⭐ Review' :
          category === 'comparison' ? '⚡ Comparison' :
          category === 'calculator' ? '🏆 Best Picks' : '📖 Guide';"""

new_cat = """        const slug = (post.slug || '').toLowerCase();
        const title = (post.data.title || '').toLowerCase();
        const category =
          slug.includes('review') || title.includes('review') ? 'review' :
          slug.includes('vs') || slug.includes('comparison') || title.includes('vs') || title.includes('comparison') ? 'comparison' :
          slug.includes('best') || title.includes('best') ? 'calculator' : 'guide';

        const categoryLabel =
          category === 'review' ? 'Review' :
          category === 'comparison' ? 'Comparison' :
          category === 'calculator' ? 'Best Picks' : 'Guide';"""

c = c.replace(old_cat, new_cat)

# Fix 2: Images - map known slugs to their webp filenames
old_placeholder = '            <div class="card-image-placeholder">⚡</div>'

new_image = """            {(() => {
              const imageMap = {
                'ecoflow-delta-3-plus-review': '/src/assets/ecoflow-delta-3-plus-review.webp',
                'jackery-explorer-1000-v2-review': '/src/assets/jackery-1000-v2-review.webp',
                'bluetti-ac200l-review': '/src/assets/bluetti-ac200l-review.webp',
                'best-solar-generator-home-backup-2026': '/src/assets/best-solar-generator-2026.webp',
                'best-solar-generator-chest-freezer-2026': '/src/assets/best-solar-generator-chest-freezer.webp',
                'how-many-watts-chest-freezer': '/src/assets/how-many-watts-chest-freezer.webp',
                'chest-freezer-blackout-math': '/src/assets/stocked-chest-freezer.webp',
                'what-is-lra-on-a-freezer': '/src/assets/lra-data-plate.webp',
                'ecoflow-vs-jackery-comparison': '/src/assets/solar-panels-home.webp',
                'how-long-food-lasts-without-power': '/src/assets/stocked-chest-freezer.webp',
              };
              const imgSrc = imageMap[post.slug];
              return imgSrc
                ? <img class="card-image" src={imgSrc} alt={post.data.title} loading="lazy" />
                : <div class="card-image-placeholder">⚡</div>;
            })()}"""

c = c.replace(old_placeholder, new_image)

open('src/pages/blog/index.astro', 'w', encoding='utf-8').write(c)
print('done')
