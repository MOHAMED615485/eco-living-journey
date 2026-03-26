# Eco Living Journey

```sh
npm create astro@latest -- --template blog
🧑‍🚀 Project Mission: Bridging the gap between sustainable tech and everyday life. Follow the journey at ecoliving-journey.com.Features:✅ Custom styling for Eco Living Journey✅ 100/100 Lighthouse performance✅ SEO-optimized with Absolute URLs for OpenGraph/Social previews✅ Cloudflare Pages deployment ready✅ Sitemap & RSS Feed support✅ Markdown & MDX support for blog content🚀 Project StructureInside of your Astro project, you'll see the following folders and files:Plaintext├── public/
├── src/
│   ├── components/       # Includes BaseHead.astro with SEO fixes
│   ├── content/          # Blog collections (Solar, Appliances, etc.)
│   ├── layouts/
│   └── pages/
├── astro.config.mjs      # Updated with site: '[https://ecoliving-journey.com](https://ecoliving-journey.com)'
├── README.md
├── package.json
└── tsconfig.json
Astro looks for .astro or .md files in the src/pages/ directory. Each page is exposed as a route based on its file name.There's nothing special about src/components/, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.The src/content/ directory contains "collections" of related Markdown and MDX documents. Use getCollection() to retrieve posts from src/content/blog/, and type-check your frontmatter using an optional schema. See Astro's Content Collections docs to learn more.Any static assets, like images, can be placed in the public/ directory.🧞 CommandsAll commands are run from the root of the project, from a terminal:CommandActionnpm installInstalls dependenciesnpm run devStarts local dev server at localhost:4321npm run buildBuild your production site to ./dist/npm run previewPreview your build locally, before deployingnpm run astro ...Run CLI commands like astro add, astro checknpm run astro -- --helpGet help using the Astro CLI👀 Want to learn more?Check out the official documentation or follow the project updates on Medium and Pinterest.CreditThis theme is based off of the lovely Bear Blog and adapted for the Eco Living Journey project.
---

### **Step-by-Step to finish:**

1.  **Open** your `README.md` file.
2.  **Delete everything** inside it.
3.  **Paste** the block above.
4.  **Save** the file.
5.  **Push to GitHub:**
    ```powershell
    git add README.md
    git commit -m "docs: update readme for eco living journey"
    git push
    ```

**Would you like me to check if your `astro.config.mjs` is also ready, since the README mentions the site URL fix?**