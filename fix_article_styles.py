import pathlib

f = pathlib.Path('src/content/blog/best-emergency-kit-power-outage-2026.md')
c = f.read_text(encoding='utf-8')

# Fix affiliate links - old broken link -> new working link
OLD_LINK = 'https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvivex.com%2Fproducts%2Flarge-survival-kit&clickref=emergency-kit-article'
NEW_LINK = 'https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvive-x.com%2Fcollections%2Ffirst-aid-kits'
c = c.replace(OLD_LINK, NEW_LINK)

# Fix TOP PICK box - white text on green, white button
OLD_TOP = '''<div style="background: #2d6a4f; color: white; border-radius: 12px; padding: 20px 24px; margin: 28px 0;">
  <p style="margin: 0 0 8px; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; opacity: 0.85;">⚡ TOP PICK</p>
  <p style="margin: 0 0 4px; font-size: 18px; font-weight: 700;">SurviveX 72-Hour Emergency Kit</p>
  <p style="margin: 0 0 16px; font-size: 13px; opacity: 0.9;">Best all-in-one kit for families — built for 72+ hour outages, not just camping weekends</p>
  <a href="https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvive-x.com%2Fcollections%2Ffirst-aid-kits" target="_blank" rel="noopener sponsored" style="display: inline-block; background: white; color: #2d6a4f; font-weight: 700; font-size: 14px; padding: 12px 24px; border-radius: 8px; text-decoration: none;">Check Price on SurviveX →</a>
</div>'''

NEW_TOP = '''<div style="background: #2d6a4f; color: white; border-radius: 12px; padding: 24px 28px; margin: 28px 0; border: none;">
  <p style="margin: 0 0 10px; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px; color: #74c69d;">⚡ TOP PICK</p>
  <p style="margin: 0 0 6px; font-size: 20px; font-weight: 800; color: white; line-height: 1.3;">SurviveX 72-Hour Emergency Kit</p>
  <p style="margin: 0 0 20px; font-size: 14px; color: rgba(255,255,255,0.9); line-height: 1.6;">Best all-in-one kit for families — built for 72+ hour outages, not just camping weekends</p>
  <a href="https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvive-x.com%2Fcollections%2Ffirst-aid-kits" target="_blank" rel="noopener sponsored" style="display: inline-block; background: #ffffff; color: #1a1a1a; font-weight: 800; font-size: 15px; padding: 14px 28px; border-radius: 8px; text-decoration: none; letter-spacing: 0.3px;">Check Price on SurviveX →</a>
</div>'''

c = c.replace(OLD_TOP, NEW_TOP)

# Fix product cards - cream bg with clear green button text
OLD_CARD_1 = '''<div style="background: #f5f0dc; border-left: 4px solid #2d6a4f; border-radius: 0 10px 10px 0; padding: 16px 20px; margin: 20px 0;">
  <p style="margin: 0 0 4px; font-size: 13px; font-weight: 700; color: #2d6a4f;">SurviveX 72-Hour Family Kit</p>
  <p style="margin: 0 0 12px; font-size: 12px; color: #555;">Covers 2 adults + 2 kids for 72 hours • Waterproof pack • 20% off with affiliate discount</p>
  <a href="https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvive-x.com%2Fcollections%2Ffirst-aid-kits" target="_blank" rel="noopener sponsored" style="display: inline-block; background: #2d6a4f; color: white; font-weight: 700; font-size: 13px; padding: 10px 20px; border-radius: 8px; text-decoration: none;">See Current Price →</a>
</div>'''

NEW_CARD_1 = '''<div style="background: white; border: 2px solid #2d6a4f; border-radius: 10px; padding: 20px 24px; margin: 20px 0; box-shadow: 0 2px 8px rgba(45,106,79,0.1);">
  <p style="margin: 0 0 6px; font-size: 15px; font-weight: 800; color: #1a1a1a;">SurviveX 72-Hour Family Kit</p>
  <p style="margin: 0 0 16px; font-size: 13px; color: #444; line-height: 1.5;">Covers 2 adults + 2 kids for 72 hours • Waterproof pack • 20% off with affiliate discount</p>
  <a href="https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvive-x.com%2Fcollections%2Ffirst-aid-kits" target="_blank" rel="noopener sponsored" style="display: inline-block; background: #2d6a4f; color: white; font-weight: 700; font-size: 14px; padding: 12px 24px; border-radius: 8px; text-decoration: none;">See Current Price →</a>
</div>'''

OLD_CARD_2 = '''<div style="background: #f5f0dc; border-left: 4px solid #2d6a4f; border-radius: 0 10px 10px 0; padding: 16px 20px; margin: 20px 0;">
  <p style="margin: 0 0 4px; font-size: 13px; font-weight: 700; color: #2d6a4f;">SurviveX Solo Kit</p>
  <p style="margin: 0 0 12px; font-size: 12px; color: #555;">72-hour single person coverage • 8.4 lbs • Apartment-sized</p>
  <a href="https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvive-x.com%2Fcollections%2Ffirst-aid-kits" target="_blank" rel="noopener sponsored" style="display: inline-block; background: #2d6a4f; color: white; font-weight: 700; font-size: 13px; padding: 10px 20px; border-radius: 8px; text-decoration: none;">See Current Price →</a>
</div>'''

NEW_CARD_2 = '''<div style="background: white; border: 2px solid #2d6a4f; border-radius: 10px; padding: 20px 24px; margin: 20px 0; box-shadow: 0 2px 8px rgba(45,106,79,0.1);">
  <p style="margin: 0 0 6px; font-size: 15px; font-weight: 800; color: #1a1a1a;">SurviveX Solo Kit</p>
  <p style="margin: 0 0 16px; font-size: 13px; color: #444; line-height: 1.5;">72-hour single person coverage • 8.4 lbs • Apartment-sized</p>
  <a href="https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvive-x.com%2Fcollections%2Ffirst-aid-kits" target="_blank" rel="noopener sponsored" style="display: inline-block; background: #2d6a4f; color: white; font-weight: 700; font-size: 14px; padding: 12px 24px; border-radius: 8px; text-decoration: none;">See Current Price →</a>
</div>'''

# Fix closing CTA box
OLD_CLOSE = '''<div style="background: #2d6a4f; color: white; border-radius: 12px; padding: 20px 24px; margin: 28px 0;">
  <p style="margin: 0 0 8px; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; opacity: 0.85;">Ready to get prepared?</p>
  <p style="margin: 0 0 16px; font-size: 15px;">The SurviveX 72-Hour Kit is what I recommend to every homeowner who asks where to start.</p>
  <a href="https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvive-x.com%2Fcollections%2Ffirst-aid-kits" target="_blank" rel="noopener sponsored" style="display: inline-block; background: white; color: #2d6a4f; font-weight: 700; font-size: 14px; padding: 12px 24px; border-radius: 8px; text-decoration: none;">Check Price on SurviveX →</a>
</div>'''

NEW_CLOSE = '''<div style="background: #2d6a4f; color: white; border-radius: 12px; padding: 24px 28px; margin: 28px 0;">
  <p style="margin: 0 0 10px; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px; color: #74c69d;">Ready to get prepared?</p>
  <p style="margin: 0 0 20px; font-size: 16px; color: white; line-height: 1.6; font-weight: 500;">The SurviveX 72-Hour Kit is what I recommend to every homeowner who asks where to start.</p>
  <a href="https://www.awin1.com/cread.php?awinmid=124484&awinaffid=2815020&ued=https%3A%2F%2Fsurvive-x.com%2Fcollections%2Ffirst-aid-kits" target="_blank" rel="noopener sponsored" style="display: inline-block; background: white; color: #1a1a1a; font-weight: 800; font-size: 15px; padding: 14px 28px; border-radius: 8px; text-decoration: none;">Check Price on SurviveX →</a>
</div>'''

c = c.replace(OLD_CARD_1, NEW_CARD_1)
c = c.replace(OLD_CARD_2, NEW_CARD_2)
c = c.replace(OLD_CLOSE, NEW_CLOSE)

f.write_text(c, encoding='utf-8')

# Report
new = f.read_text(encoding='utf-8')
print('New link count:', new.count('survive-x.com'))
print('Old broken links remaining:', new.count('survivex.com'))
print('White cards:', new.count('background: white; border: 2px solid #2d6a4f'))
print('DONE!')
