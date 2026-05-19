# Drafts Folder

Place future scheduled articles here.

## How it works

1. Write your article as normal .md file
2. Set pubDate to the future publish date (e.g. pubDate: 2026-05-20)
3. Place hero image in src/assets/drafts/
4. Push to GitHub
5. GitHub Actions runs every day at 6AM Algeria time
6. On the pubDate day, the article moves to src/content/blog/ automatically
7. Hero image copies to src/assets/ automatically
8. IndexNow fires automatically
9. Cloudflare deploys automatically

## Example frontmatter

---
title: "Your Article Title"
description: "Your description here"
pubDate: 2026-05-24
updatedDate: 2026-05-24
heroImage: "/src/assets/your-image.webp"
category: "Solar Generator Guides"
---
