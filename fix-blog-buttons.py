c = open('src/pages/blog/index.astro', encoding='utf-8').read()

# Fix filter tabs - the issue is "Calculators" should be "Best Picks" 
# and add Contact Us button
old_tabs = '''    <!-- FILTER TABS -->
    <div class="filter-tabs">
      <button class="filter-tab active" onclick="setFilter('all', this)">All Articles</button>
      <button class="filter-tab" onclick="setFilter('review', this)">Reviews</button>
      <button class="filter-tab" onclick="setFilter('guide', this)">Guides</button>
      <button class="filter-tab" onclick="setFilter('comparison', this)">Comparisons</button>
      <button class="filter-tab" onclick="setFilter('calculator', this)">Calculators</button>
    </div>'''

new_tabs = '''    <!-- FILTER TABS -->
    <div class="filter-tabs">
      <button class="filter-tab active" onclick="setFilter('all', this)">All Articles</button>
      <button class="filter-tab" onclick="setFilter('review', this)">Reviews</button>
      <button class="filter-tab" onclick="setFilter('guide', this)">Guides</button>
      <button class="filter-tab" onclick="setFilter('comparison', this)">Comparisons</button>
      <button class="filter-tab" onclick="setFilter('calculator', this)">Best Picks</button>
      <a href="/contact/" class="filter-tab" style="background:var(--green);color:white;border-color:var(--green);text-decoration:none;">✉️ Contact Ethan</a>
    </div>'''

if old_tabs in c:
    c = c.replace(old_tabs, new_tabs)
    print('Tabs fixed')
else:
    # Try to find and replace just the calculators button
    c = c.replace(
        "setFilter('calculator', this)>Calculators</button>",
        "setFilter('calculator', this)>Best Picks</button>\n      <a href=\"/contact/\" class=\"filter-tab\" style=\"background:var(--green);color:white;border-color:var(--green);text-decoration:none;\">✉️ Contact Ethan</a>"
    )
    print('Partial fix applied')

open('src/pages/blog/index.astro', 'w', encoding='utf-8').write(c)
print('done')
