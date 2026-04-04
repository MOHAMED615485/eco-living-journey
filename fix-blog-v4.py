c = open('src/pages/blog/index.astro', encoding='utf-8').read()

# Remove the broken IIFE image block and replace with simple approach
import re

# Remove the broken image IIFE block
old_img = """{(() => {
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

new_img = '<div class="card-image-placeholder">⚡</div>'

c = c.replace(old_img, new_img)

# Move image map to frontmatter section (before the return/template)
# Find the posts sort line and add imageMap after it
old_posts = """const posts = (await getCollection('blog')).sort(
  (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
);"""

new_posts = """const posts = (await getCollection('blog')).sort(
  (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
);

const imageMap = {
  'ecoflow-delta-3-plus-review': '/assets/ecoflow-delta-3-plus-review.webp',
  'jackery-explorer-1000-v2-review': '/assets/jackery-1000-v2-review.webp',
  'bluetti-ac200l-review': '/assets/bluetti-ac200l-review.webp',
  'best-solar-generator-home-backup-2026': '/assets/best-solar-generator-2026.webp',
  'best-solar-generator-chest-freezer-2026': '/assets/best-solar-generator-chest-freezer.webp',
  'how-many-watts-chest-freezer': '/assets/how-many-watts-chest-freezer.webp',
  'chest-freezer-blackout-math': '/assets/stocked-chest-freezer.webp',
  'what-is-lra-on-a-freezer': '/assets/lra-data-plate.webp',
  'ecoflow-vs-jackery-comparison': '/assets/solar-panels-home.webp',
  'how-long-food-lasts-without-power': '/assets/stocked-chest-freezer.webp',
};"""

c = c.replace(old_posts, new_posts)

# Now use imageMap in the template
c = c.replace(
    '<div class="card-image-placeholder">⚡</div>',
    """{imageMap[post.slug]
                ? <img class="card-image" src={imageMap[post.slug]} alt={post.data.title} loading="lazy" />
                : <div class="card-image-placeholder">⚡</div>
              }""",
    1  # only replace first occurrence
)

open('src/pages/blog/index.astro', 'w', encoding='utf-8').write(c)
print('done')
