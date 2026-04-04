c = open('src/styles/global.css', encoding='utf-8').read()

premium_blog = '''
/* ============================================
   PREMIUM BLOG TYPOGRAPHY & LAYOUT
   ============================================ */

/* Article body */
.prose {
  font-family: "DM Sans", Georgia, serif !important;
  font-size: 1.05rem !important;
  line-height: 1.85 !important;
  color: #1a1a1a !important;
  max-width: 740px !important;
  margin: 0 auto !important;
}

/* H1 */
.prose h1 {
  font-family: "DM Serif Display", Georgia, serif !important;
  font-size: 2.4rem !important;
  line-height: 1.15 !important;
  color: #0d0d0d !important;
  margin-bottom: 1rem !important;
  letter-spacing: -0.5px !important;
}

/* H2 */
.prose h2 {
  font-family: "DM Serif Display", Georgia, serif !important;
  font-size: 1.65rem !important;
  color: #1a1a1a !important;
  margin-top: 2.5rem !important;
  margin-bottom: 0.75rem !important;
  padding-bottom: 0.4rem !important;
  border-bottom: 2px solid #2d6a4f !important;
  letter-spacing: -0.3px !important;
}

/* H3 */
.prose h3 {
  font-family: "DM Serif Display", Georgia, serif !important;
  font-size: 1.25rem !important;
  color: #1a1a1a !important;
  margin-top: 2rem !important;
  margin-bottom: 0.5rem !important;
}

/* Paragraphs */
.prose p {
  margin-bottom: 1.4rem !important;
  color: #2d2d2d !important;
}

/* Bold */
.prose strong {
  color: #0d0d0d !important;
  font-weight: 700 !important;
}

/* Links */
.prose a {
  color: #2d6a4f !important;
  text-decoration: underline !important;
  text-decoration-color: rgba(45,106,79,0.35) !important;
  text-underline-offset: 3px !important;
  transition: all 0.2s !important;
}

.prose a:hover {
  color: #1a3d2b !important;
  text-decoration-color: #2d6a4f !important;
}

/* Blockquote */
.prose blockquote {
  border-left: 4px solid #2d6a4f !important;
  background: #f0f7f4 !important;
  padding: 16px 20px !important;
  border-radius: 0 8px 8px 0 !important;
  margin: 1.5rem 0 !important;
  font-style: italic !important;
  color: #2d2d2d !important;
}

/* Horizontal rule */
.prose hr {
  border: none !important;
  border-top: 2px solid #e8e8e8 !important;
  margin: 2.5rem 0 !important;
}

/* Lists */
.prose ul li {
  margin-bottom: 0.4rem !important;
  color: #2d2d2d !important;
}

.prose ol li {
  margin-bottom: 0.4rem !important;
  color: #2d2d2d !important;
}

/* Code inline */
.prose code {
  background: #f4f4f4 !important;
  padding: 2px 6px !important;
  border-radius: 4px !important;
  font-size: 0.88rem !important;
  color: #c0392b !important;
}

/* Article container padding */
article {
  padding: 0 16px !important;
}
'''

open('src/styles/global.css', 'w', encoding='utf-8').write(c + premium_blog)
print('done')
