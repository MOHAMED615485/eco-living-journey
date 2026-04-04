content = '''---
import BaseHead from '../components/BaseHead.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import { getCollection } from 'astro:content';

const posts = (await getCollection('blog')).sort(
  (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
);
---

<html lang="en">
<head>
  <BaseHead title="Blog - Eco Living Journey" description="Solar generator reviews, backup power guides, and blackout prep tips from 73 days of real testing." />
  <style>
    :root {
      --green: #2d6a4f;
      --green-light: #a8d5b5;
      --green-pale: #d8f0e3;
      --cream: #f5f0dc;
      --cream-dark: #ede8d0;
      --text: #1a3d2b;
      --text-muted: #5a7a68;
      --orange: #e8790a;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: var(--cream);
      font-family: "DM Sans", sans-serif;
      color: var(--text);
    }

    .blog-hero {
      background: var(--green);
      padding: 48px 24px;
      text-align: center;
    }

    .blog-hero h1 {
      font-family: "DM Serif Display", serif;
      font-size: clamp(28px, 4vw, 42px);
      color: white;
      margin-bottom: 12px;
    }

    .blog-hero p {
      color: rgba(255,255,255,0.75);
      font-size: 16px;
      max-width: 500px;
      margin: 0 auto;
    }

    .blog-container {
      max-width: 1100px;
      margin: 0 auto;
      padding: 40px 20px 80px;
    }

    /* FILTER TABS */
    .filter-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 32px;
      justify-content: center;
    }

    .filter-tab {
      padding: 8px 20px;
      border-radius: 50px;
      border: 2px solid var(--green-light);
      background: white;
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .filter-tab:hover, .filter-tab.active {
      background: var(--green);
      border-color: var(--green);
      color: white;
    }

    /* SEARCH BAR */
    .search-wrap {
      max-width: 480px;
      margin: 0 auto 32px;
      position: relative;
    }

    .search-input {
      width: 100%;
      padding: 14px 20px 14px 48px;
      border-radius: 50px;
      border: 2px solid var(--green-light);
      background: white;
      font-size: 15px;
      font-family: "DM Sans", sans-serif;
      color: var(--text);
      outline: none;
      transition: border-color 0.2s;
    }

    .search-input:focus { border-color: var(--green); }

    .search-icon {
      position: absolute;
      left: 18px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 18px;
      color: var(--text-muted);
    }

    /* STATS BAR */
    .stats-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      font-size: 13px;
      color: var(--text-muted);
    }

    .stats-bar strong { color: var(--text); }

    /* GRID */
    .posts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 24px;
    }

    /* CARD */
    .post-card {
      background: white;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(45,106,79,0.10);
      border: 1px solid rgba(168,213,181,0.3);
      transition: all 0.25s;
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
    }

    .post-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 40px rgba(45,106,79,0.18);
    }

    .post-card.hidden { display: none; }

    .card-image {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }

    .card-image-placeholder {
      width: 100%;
      height: 200px;
      background: linear-gradient(135deg, var(--green) 0%, var(--green-light) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 48px;
    }

    .card-body {
      padding: 20px;
      flex: 1;
      display: flex;
      flex-direction: column;
    }

    .card-category {
      display: inline-block;
      background: var(--green-pale);
      color: var(--green);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 20px;
      margin-bottom: 10px;
    }

    .card-title {
      font-family: "DM Serif Display", serif;
      font-size: 17px;
      color: var(--text);
      line-height: 1.35;
      margin-bottom: 10px;
      flex: 1;
    }

    .card-excerpt {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 14px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .card-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      color: var(--text-muted);
      border-top: 1px solid var(--cream-dark);
      padding-top: 12px;
    }

    .card-date { font-weight: 500; }

    .card-read-more {
      color: var(--green);
      font-weight: 700;
      font-size: 12px;
    }

    .no-results {
      text-align: center;
      padding: 60px 20px;
      color: var(--text-muted);
      display: none;
    }

    .no-results.visible { display: block; }

    @media (max-width: 600px) {
      .posts-grid { grid-template-columns: 1fr; }
      .filter-tabs { gap: 8px; }
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

    <!-- SEARCH -->
    <div class="search-wrap">
      <span class="search-icon">🔍</span>
      <input
        type="text"
        class="search-input"
        id="searchInput"
        placeholder="Search articles..."
        oninput="filterPosts()"
      />
    </div>

    <!-- FILTER TABS -->
    <div class="filter-tabs">
      <button class="filter-tab active" onclick="setFilter('all', this)">All Articles</button>
      <button class="filter-tab" onclick="setFilter('review', this)">Reviews</button>
      <button class="filter-tab" onclick="setFilter('guide', this)">Guides</button>
      <button class="filter-tab" onclick="setFilter('comparison', this)">Comparisons</button>
      <button class="filter-tab" onclick="setFilter('calculator', this)">Calculators</button>
    </div>

    <!-- STATS -->
    <div class="stats-bar">
      <span><strong id="visibleCount">{posts.length}</strong> articles</span>
      <span>Updated April 2026</span>
    </div>

    <!-- GRID -->
    <div class="posts-grid" id="postsGrid">
      {posts.map((post) => {
        const category =
          post.slug.includes('review') ? 'review' :
          post.slug.includes('comparison') || post.slug.includes('vs') ? 'comparison' :
          post.slug.includes('best') || post.slug.includes('calculator') ? 'calculator' : 'guide';

        const categoryLabel =
          category === 'review' ? 'Review' :
          category === 'comparison' ? 'Comparison' :
          category === 'calculator' ? 'Best Picks' : 'Guide';

        const dateStr = new Date(post.data.pubDate).toLocaleDateString('en-US', {
          month: 'short', day: 'numeric', year: 'numeric'
        });

        return (
          <a
            href={`/blog/${post.slug}/`}
            class="post-card"
            data-category={category}
            data-title={post.data.title.toLowerCase()}
          >
            {post.data.heroImage ? (
              <img
                class="card-image"
                src={post.data.heroImage}
                alt={post.data.title}
                loading="lazy"
              />
            ) : (
              <div class="card-image-placeholder">⚡</div>
            )}
            <div class="card-body">
              <span class="card-category">{categoryLabel}</span>
              <div class="card-title">{post.data.title}</div>
              <div class="card-excerpt">{post.data.description}</div>
              <div class="card-footer">
                <span class="card-date">{dateStr}</span>
                <span class="card-read-more">Read more →</span>
              </div>
            </div>
          </a>
        );
      })}
    </div>

    <div class="no-results" id="noResults">
      <div style="font-size:48px;margin-bottom:16px;">🔍</div>
      <div style="font-size:18px;font-weight:600;margin-bottom:8px;">No articles found</div>
      <div>Try a different search term or category</div>
    </div>

  </div>

  <Footer />

  <script is:inline>
    var currentFilter = 'all';

    function setFilter(filter, btn) {
      currentFilter = filter;
      document.querySelectorAll('.filter-tab').forEach(function(t) {
        t.classList.remove('active');
      });
      btn.classList.add('active');
      filterPosts();
    }

    function filterPosts() {
      var search = document.getElementById('searchInput').value.toLowerCase();
      var cards = document.querySelectorAll('.post-card');
      var visible = 0;

      cards.forEach(function(card) {
        var matchFilter = currentFilter === 'all' || card.dataset.category === currentFilter;
        var matchSearch = search === '' || card.dataset.title.includes(search);
        if (matchFilter && matchSearch) {
          card.classList.remove('hidden');
          visible++;
        } else {
          card.classList.add('hidden');
        }
      });

      document.getElementById('visibleCount').textContent = visible;
      var noResults = document.getElementById('noResults');
      if (visible === 0) {
        noResults.classList.add('visible');
      } else {
        noResults.classList.remove('visible');
      }
    }
  </script>
</body>
</html>
'''

with open('src/pages/blog.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
