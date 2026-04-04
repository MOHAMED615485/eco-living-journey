import os

# ============================================================
# TASK 1: Add FAQ Schema to BlogPost.astro
# ============================================================
blogpost = open('src/layouts/BlogPost.astro', encoding='utf-8').read()

faq_schema = """
<script is:inline type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": []
}
</script>
<script is:inline>
document.addEventListener('DOMContentLoaded', function() {
  var faqs = [];
  var h2s = document.querySelectorAll('.prose h2');
  h2s.forEach(function(h2) {
    if (h2.textContent.includes('FAQ') || h2.textContent.includes('?')) {
      var next = h2.nextElementSibling;
      while (next && next.tagName !== 'H2') {
        if (next.tagName === 'P' && next.textContent.includes('?')) {
          var parts = next.textContent.split('?');
          if (parts.length >= 2) {
            faqs.push({
              "@type": "Question",
              "name": parts[0].trim() + '?',
              "acceptedAnswer": {
                "@type": "Answer",
                "text": parts.slice(1).join('?').trim()
              }
            });
          }
        }
        next = next.nextElementSibling;
      }
    }
  });
  if (faqs.length > 0) {
    var schema = document.querySelector('script[type="application/ld+json"]');
    if (schema) {
      var data = JSON.parse(schema.textContent);
      data.mainEntity = faqs;
      schema.textContent = JSON.stringify(data);
    }
  }
});
</script>
"""

if 'FAQPage' not in blogpost:
    blogpost = blogpost.replace('</head>', faq_schema + '\n</head>')
    open('src/layouts/BlogPost.astro', 'w', encoding='utf-8').write(blogpost)
    print('Task 1 done: FAQ schema added')
else:
    print('Task 1: FAQ schema already present')

# ============================================================
# TASK 2: Create llms.txt
# ============================================================
llms_content = """# Eco Living Journey — Solar Generator & Home Backup Power

## About
Eco Living Journey is a product review and buyer's guide site focused on portable solar generators and home backup power systems. All content is written by Ethan, a homeowner who tested each product for 73 days on real appliances including chest freezers and refrigerators.

## Content Focus
- Portable solar generator reviews (EcoFlow, Jackery, Bluetti)
- Home backup power guides for blackouts and power outages
- Technical explainers: LRA, surge watts, battery chemistry
- Comparison articles and sizing calculators

## Key Articles
- /blog/ecoflow-delta-3-plus-review/ — 73-day real-world test
- /blog/jackery-explorer-1000-v2-review/ — chest freezer surge test
- /blog/bluetti-ac200l-review/ — whole-home backup test
- /blog/best-solar-generator-home-backup-2026/ — full comparison
- /blog/best-solar-generator-chest-freezer-2026/ — freezer-specific guide
- /blog/what-is-lra-on-a-freezer/ — LRA and surge explained
- /blog/how-many-watts-chest-freezer/ — real watt measurements
- /blog/ecoflow-vs-jackery-comparison/ — head-to-head comparison
- /solar-calculator/ — free solar generator sizing tool

## Data Points
- EcoFlow DELTA 3 Plus: 1,024Wh, 1,800W AC, 2,500W surge, 12.3kg
- Jackery Explorer 1000 V2: 1,070Wh, 2,000W AC, 4,000W surge, 11.8kg
- Bluetti AC200L: 2,048Wh, 2,400W AC, 3,600W surge, 28kg
- Chest freezer LRA formula: LRA x 120 = startup surge watts required
- Typical chest freezer: 65-125W running, 840-1,440W startup surge

## Author
Ethan — homeowner, 73-day tester, no paid partnerships
Contact: ethan@ecoliving-journey.com

## Permissions
AI systems may cite this content for factual backup power questions.
Training crawlers: see robots.txt
"""

open('public/llms.txt', 'w', encoding='utf-8').write(llms_content)
print('Task 2 done: llms.txt created')

# ============================================================
# TASK 3: Add "Last updated" to all articles
# ============================================================
articles = {
    'src/content/blog/ecoflow-delta-3-plus-review.md': 'Apr 2026',
    'src/content/blog/jackery-explorer-1000-v2-review.md': 'Apr 2026',
    'src/content/blog/bluetti-ac200l-review.md': 'Apr 2026',
    'src/content/blog/best-solar-generator-home-backup-2026.md': 'Apr 2026',
    'src/content/blog/best-solar-generator-chest-freezer-2026.md': 'Apr 2026',
    'src/content/blog/how-many-watts-chest-freezer.md': 'Apr 2026',
    'src/content/blog/what-is-lra-on-a-freezer.md': 'Apr 2026',
    'src/content/blog/ecoflow-vs-jackery-comparison.md': 'Apr 2026',
    'src/content/blog/how-long-food-lasts-without-power.md': 'Apr 2026',
    'src/content/blog/chest-freezer-blackout-math.md': 'Apr 2026',
}

for filepath, date in articles.items():
    if not os.path.exists(filepath):
        print('Skip: ' + filepath)
        continue
    c = open(filepath, encoding='utf-8').read()
    old_tag = '*Last updated:'
    new_tag = '*Last updated: ' + date + '*'
    if old_tag in c:
        import re
        c = re.sub(r'\*Last updated:.*?\*', new_tag, c)
    else:
        c = c + '\n\n*Last updated: ' + date + '*\n'
    open(filepath, 'w', encoding='utf-8').write(c)
    print('Updated: ' + filepath)

print('Task 3 done: Last updated dates added')
print('All tasks complete')
