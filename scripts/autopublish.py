import os
import re
import shutil
import urllib.request
import json
from datetime import date

TODAY = date.today().isoformat()  # e.g. 2026-05-20

DRAFTS_DIR = 'src/content/drafts'
BLOG_DIR = 'src/content/blog'
DRAFTS_ASSETS_DIR = 'src/assets/drafts'
ASSETS_DIR = 'src/assets'
INDEXNOW_KEY = os.environ.get('INDEXNOW_KEY', '576c8a15fb864a5db799a6407203923a')
SITE_HOST = 'ecoliving-journey.com'

published_urls = []
published_titles = []

# Create directories if they don't exist
os.makedirs(DRAFTS_DIR, exist_ok=True)
os.makedirs(BLOG_DIR, exist_ok=True)
os.makedirs(DRAFTS_ASSETS_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

print(f"Running autopublish for date: {TODAY}")

# Check for articles due today
draft_files = [f for f in os.listdir(DRAFTS_DIR) if f.endswith('.md')]
print(f"Found {len(draft_files)} draft articles")

for filename in draft_files:
    filepath = os.path.join(DRAFTS_DIR, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract pubDate from frontmatter
    pub_match = re.search(r'^pubDate:\s*["\']?(\d{4}-\d{2}-\d{2})', content, re.MULTILINE)
    if not pub_match:
        print(f"  SKIP (no pubDate): {filename}")
        continue
    
    pub_date = pub_match.group(1)
    
    if pub_date != TODAY:
        print(f"  SKIP (future date {pub_date}): {filename}")
        continue
    
    print(f"  PUBLISHING: {filename} (pubDate: {pub_date})")
    
    # Extract heroImage filename for asset copying
    hero_match = re.search(r'^heroImage:\s*["\']?.*?([^/"\'\s]+\.webp)', content, re.MULTILINE)
    if hero_match:
        hero_filename = hero_match.group(1)
        draft_hero = os.path.join(DRAFTS_ASSETS_DIR, hero_filename)
        target_hero = os.path.join(ASSETS_DIR, hero_filename)
        
        if os.path.exists(draft_hero):
            shutil.copy2(draft_hero, target_hero)
            print(f"    Copied hero image: {hero_filename}")
        else:
            print(f"    WARNING: Hero image not found in drafts: {hero_filename}")
    
    # Move article to blog
    target_path = os.path.join(BLOG_DIR, filename)
    shutil.move(filepath, target_path)
    print(f"    Moved to blog: {filename}")
    
    # Build the URL slug from filename
    slug = filename.replace('.md', '')
    url = f"https://{SITE_HOST}/blog/{slug}/"
    published_urls.append(url)
    
    # Extract title for commit message
    title_match = re.search(r'^title:\s*["\'](.+?)["\']', content, re.MULTILINE)
    if title_match:
        published_titles.append(title_match.group(1))

# Submit to IndexNow if articles were published
if published_urls:
    print(f"\nPublished {len(published_urls)} articles:")
    for url in published_urls:
        print(f"  {url}")
    
    # Fire IndexNow
    try:
        payload = json.dumps({
            'host': SITE_HOST,
            'key': INDEXNOW_KEY,
            'keyLocation': f'https://{SITE_HOST}/{INDEXNOW_KEY}.txt',
            'urlList': published_urls
        }).encode()
        
        req = urllib.request.Request(
            'https://api.indexnow.org/indexnow',
            data=payload,
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        r = urllib.request.urlopen(req)
        print(f"\nIndexNow Status: {r.status}")
    except Exception as e:
        print(f"\nIndexNow Error: {e}")
    
    # Write publish summary
    with open('PUBLISH_LOG.md', 'a', encoding='utf-8') as f:
        f.write(f"\n## {TODAY}\n")
        for title, url in zip(published_titles, published_urls):
            f.write(f"- [{title}]({url})\n")
    
    print("\nAutopublish complete!")
else:
    print("\nNo articles scheduled for today.")
