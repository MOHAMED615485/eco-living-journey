# Update global.css with premium table design + fix star coloring via JS in BlogPost.astro

# Step 1: Premium CSS for tables
css_content = open('src/styles/global.css', encoding='utf-8').read()

old = """/* Gold star ratings in tables */
table td:last-child {
  color: #f5a623;
  font-size: 1.2rem;
  letter-spacing: 2px;
}"""

new = """/* Premium table styling */
.prose table {
  border-collapse: separate !important;
  border-spacing: 0 !important;
  border-radius: 12px !important;
  overflow: hidden !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.15), 0 2px 8px rgba(0,0,0,0.10), inset 0 0 0 2px #1a1a1a !important;
  border: 2px solid #1a1a1a !important;
  width: 100% !important;
}

.prose table thead tr {
  background: linear-gradient(135deg, #111111 0%, #333333 100%) !important;
}

.prose table thead th {
  color: #ffffff !important;
  font-weight: 700 !important;
  font-size: 0.82rem !important;
  letter-spacing: 0.8px !important;
  padding: 14px 16px !important;
  border: none !important;
  text-transform: uppercase !important;
}

.prose table tbody tr:nth-child(odd) {
  background: #fafafa !important;
}

.prose table tbody tr:nth-child(even) {
  background: #ffffff !important;
}

.prose table tbody tr:hover {
  background: #fff8ee !important;
  transition: background 0.2s !important;
}

.prose table td {
  padding: 12px 16px !important;
  border-bottom: 1px solid #e8e8e8 !important;
  border-right: 1px solid #e8e8e8 !important;
  color: #1a1a1a !important;
  font-size: 0.92rem !important;
}

.prose table td:last-child {
  border-right: none !important;
}

.prose table tbody tr:last-child td {
  border-bottom: none !important;
}

/* Gold stars */
td.star-cell {
  color: #f5a623 !important;
  font-size: 1.2rem !important;
  letter-spacing: 3px !important;
  font-weight: 700 !important;
}"""

css_content = css_content.replace(old, new)
open('src/styles/global.css', 'w', encoding='utf-8').write(css_content)
print('CSS updated')

# Step 2: Add JS to BlogPost.astro to mark star cells
blogpost = open('src/layouts/BlogPost.astro', encoding='utf-8').read()

star_js = """
<script is:inline>
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('td').forEach(function(td) {
      if (td.textContent.includes('\u2605') || td.textContent.includes('\u2606')) {
        td.classList.add('star-cell');
      }
    });
  });
</script>
"""

if 'star-cell' not in blogpost:
    blogpost = blogpost.replace('</body>', star_js + '</body>')
    open('src/layouts/BlogPost.astro', 'w', encoding='utf-8').write(blogpost)
    print('JS added to BlogPost.astro')
else:
    print('JS already present')

print('All done')
