content = '''---
import BaseHead from '../../components/BaseHead.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import { getCollection } from 'astro:content';

const posts = (await getCollection('blog')).sort(
  (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
);

function getCategory(slug) {
  const s = (slug || '').toLowerCase();
  if (s.includes('review')) return 'review';
  if (s.includes('vs') || s.includes('comparison')) return 'comparison';
  if (s.includes('best')) return 'calculator';
  return 'guide';
}

function getCategoryLabel(slug) {
  const cat = getCategory(slug);
  if (cat === 'review') return 'Review';
  if (cat === 'comparison') return 'Comparison';
  if (cat === 'calculator') return 'Best Picks';
  return 'Guide';
}

const images = {
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
};
---

<html lang="en">
<head>
  <BaseHead
    title="Blog - Eco Living Journey"
    description="Solar generator reviews, backup power guides, and blackout prep tips from 73 days of real testing."
  />
  <style>
    :root {
      --green: #2d6a4f; --green-mid: #3d8b6f; --green-light: #a8d5b5;
      --green-pale: #d8f0e3; --cream: #f5f0dc; --cream-dark: #ede8d0;
      --text: #1a3d2b; --text-muted: #5a7a68;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--cream); font-family: "DM Sans", sans-serif; color: var(--text); }

    .blog-hero {
      background: var(--green);
      padding: 48px 24px;
      text-align: center;
    }
    .blog-hero h1 {
      font-family: "DM Serif Display", serif;
      font-size: clamp(28px,4vw,42px);
      color: white;
      margin-bottom: 12px;
    }
    .blog-hero p { color: rgba(255,255,255,0.75); font-size: 16px; max-width: 500px; margin: 0 auto; }

    .blog-container { max-width: 1100px; margin: 0 auto; padding: 40px 20px 80px; }

    .search-wrap { max-width: 480px; margin: 0 auto 28px; position: relative; }
    .search-input {
      width: 100%; padding: 14px 20px 14px 48px;
      border-radius: 50px; border: 2px solid var(--green-light);
      background: white; font-size: 15px; color: var(--text);
      outline: none; font-family: "DM Sans", sans-serif;
    }
    .search-input:focus { border-color: var(--green); }
    .search-icon { position: absolute; left: 18px; top: 50%; transform: translateY(-50%); font-size: 18px; }

    .filter-tabs { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 28px; justify-content: center; }
    .filter-tab {
      padding: 8px 20px; border-radius: 50px;
      border: 2px solid var(--green-light); background: white;
      color: var(--text-muted); font-size: 13px; font-weight: 600;
      cursor: pointer; transition: all 0.2s; text-decoration: none;
    }
    .filter-tab:hover, .filter-tab.active {
      background: var(--green); border-color: var(--green); color: white;
    }

    .stats-bar {
      display: flex; justify-content: space-between;
      margin-bottom: 24px; font-size: 13px; color: var(--text-muted);
    }
    .stats-bar strong { color: var(--text); }

    .posts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 24px;
    }

    .post-card {
      background: white; border-radius: 16px; overflow: hidden;
      box-shadow: 0 4px 20px rgba(45,106,79,0.10);
      border: 1px solid rgba(168,213,181,0.3);
      transition: all 0.25s; display: flex; flex-direction: column;
      text-decoration: none; color: inherit;
    }
    .post-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(45,106,79,0.18); }
    .post-card.hidden { display: none; }

    .card-image { width: 100%; height: 200px; object-fit: cover; }
    .card-image-placeholder {
      width: 100%; height: 200px;
      background: linear-gradient(135deg, var(--green) 0%, var(--green-light) 100%);
      display: flex; align-items: center; justify-content: center; font-size: 48px;
    }

    .card-body { padding: 20px; flex: 1; display: flex; flex-direction: column; }
    .card-category {
      display: inline-block; background: var(--green-pale); color: var(--green);
      font-size: 11px; font-weight: 700; letter-spacing: 1px;
      text-transform: uppercase; padding: 4px 10px; border-radius: 20px; margin-bottom: 10px;
    }
    .card-title {
      font-family: "DM Serif Display", serif; font-size: 17px;
      color: var(--text); line-height: 1.35; margin-bottom: 10px; flex: 1;
    }
    .card-excerpt {
      font-size: 13px; color: var(--text-muted); line-height: 1.55; margin-bottom: 14px;
      display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
    }
    .card-footer {
      display: flex; align-items: center; justify-content: space-between;
      font-size: 12px; color: var(--text-muted);
      border-top: 1px solid var(--cream-dark); padding-top: 12px;
    }
    .card-read-more { color: var(--green); font-weight: 700; }

    .no-results { text-align: center; padding: 60px 20px; color: var(--text-muted); display: none; }
    .no-results.visible { display: block; }

    @media (max-width: 600px) {
      .posts-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <Header />

  <div class="blog-hero">
    <h1>Solar Generator Guides</h1>
    <p>Real tests. Real numbers. 73 days of hands-on backup power research.</p>
  </div>

  <div class="blog-container">
    <div class="search-wrap">
      <span class="search-icon">🔍</span>
      <input type="text" class="search-input" id="searchInput" placeholder="Search articles..." oninput="filterPosts()" />
    </div>

    <div class="filter-tabs">
      <button class="filter-tab active" onclick="setFilter(\'all\', this)">All Articles</button>
      <button class="filter-tab" onclick="setFilter(\'review\', this)">Reviews</button>
      <button class="filter-tab" onclick="setFilter(\'guide\', this)">Guides</button>
      <button class="filter-tab" onclick="setFilter(\'comparison\', this)">Comparisons</button>
      <button class="filter-tab" onclick="setFilter(\'calculator\', this)">Best Picks</button>
      <a href="/contact/" class="filter-tab" style="background:var(--green);color:white;border-color:var(--green);">✉️ Contact Ethan</a>
    </div>

    <div class="stats-bar">
      <span><strong id="visibleCount">{posts.length}</strong> articles</span>
      <span>Updated April 2026</span>
    </div>

    <div class="posts-grid" id="postsGrid">
      {posts.map((post) => {
        const cat = getCategory(post.slug);
        const label = getCategoryLabel(post.slug);
        const imgSrc = images[post.slug] || null;
        const dateStr = new Date(post.data.pubDate).toLocaleDateString('en-US', {
          month: 'short', day: 'numeric', year: 'numeric'
        });
        return (
          <a href={`/blog/${post.slug}/`} class="post-card" data-category={cat} data-title={(post.data.title || '').toLowerCase()}>
            {imgSrc
              ? <img class="card-image" src={imgSrc} alt={post.data.title} loading="lazy" />
              : <div class="card-image-placeholder">&#9889;</div>
            }
            <div class="card-body">
              <span class="card-category">{label}</span>
              <div class="card-title">{post.data.title}</div>
              <div class="card-excerpt">{post.data.description}</div>
              <div class="card-footer">
                <span>{dateStr}</span>
                <span class="card-read-more">Read more &rarr;</span>
              </div>
            </div>
          </a>
        );
      })}
    </div>

    <div class="no-results" id="noResults">
      <div style="font-size:48px;margin-bottom:16px;">🔍</div>
      <p>No articles found. Try a different search or category.</p>
    </div>
  </div>

  <Footer />

  <script is:inline>
    var currentFilter = 'all';
    function setFilter(filter, btn) {
      currentFilter = filter;
      document.querySelectorAll('.filter-tab').forEach(function(t) { t.classList.remove('active'); });
      btn.classList.add('active');
      filterPosts();
    }
    function filterPosts() {
      var search = document.getElementById('searchInput').value.toLowerCase();
      var cards = document.querySelectorAll('.post-card');
      var visible = 0;
      cards.forEach(function(card) {
        var matchFilter = currentFilter === 'all' || card.dataset.category === currentFilter;
        var matchSearch = search === '' || (card.dataset.title || '').includes(search);
        if (matchFilter && matchSearch) { card.classList.remove('hidden'); visible++; }
        else { card.classList.add('hidden'); }
      });
      document.getElementById('visibleCount').textContent = visible;
      document.getElementById('noResults').classList.toggle('visible', visible === 0);
    }
  </script>
</body>
</html>
'''

with open('src/pages/blog/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
