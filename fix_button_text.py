import pathlib

f = pathlib.Path('src/content/blog/best-emergency-kit-power-outage-2026.md')
c = f.read_text(encoding='utf-8')

# Fix all green buttons - make text white and explicitly visible
old_btn = 'style="display: inline-block; background: #2d6a4f; color: white; font-weight: 700; font-size: 14px; padding: 12px 24px; border-radius: 8px; text-decoration: none;">See Current Price →</a>'
new_btn = 'style="display: inline-block; background: #2d6a4f; color: #ffffff !important; font-weight: 800; font-size: 14px; padding: 12px 24px; border-radius: 8px; text-decoration: none !important; opacity: 1;">See Current Price →</a>'

c = c.replace(old_btn, new_btn)

# Fix TOP PICK button
old_top_btn = 'style="display: inline-block; background: #ffffff; color: #1a1a1a; font-weight: 800; font-size: 15px; padding: 14px 28px; border-radius: 8px; text-decoration: none; letter-spacing: 0.3px;">Check Price on SurviveX →</a>'
new_top_btn = 'style="display: inline-block; background: #ffffff; color: #1a1a1a !important; font-weight: 800; font-size: 15px; padding: 14px 28px; border-radius: 8px; text-decoration: none !important;">Check Price on SurviveX →</a>'

c = c.replace(old_top_btn, new_top_btn)

# Fix closing CTA button
old_close_btn = 'style="display: inline-block; background: white; color: #1a1a1a; font-weight: 800; font-size: 15px; padding: 14px 28px; border-radius: 8px; text-decoration: none;">Check Price on SurviveX →</a>'
new_close_btn = 'style="display: inline-block; background: #ffffff; color: #1a1a1a !important; font-weight: 800; font-size: 15px; padding: 14px 28px; border-radius: 8px; text-decoration: none !important;">Check Price on SurviveX →</a>'

c = c.replace(old_close_btn, new_close_btn)

f.write_text(c, encoding='utf-8')
print('DONE - buttons fixed')
