import os
from datetime import datetime, timedelta

# Article data with all details
articles = [
    {
        'num': 1,
        'status': '✅ PUBLISHED',
        'title': 'Best Solar Generator for Home Backup Power 2026',
        'slug': 'best-solar-generator-home-backup-2026',
        'image': 'best-solar-generator-2026.jpg',
        'tags': ['Solar Power', 'Emergency Preparedness', 'Product Review', 'Off Grid Living', 'Home Backup Power'],
        'date': 'Apr 21 (TODAY - DONE!)',
        'priority': 'HIGH - Main money article'
    },
    {
        'num': 2,
        'title': 'Will a 1000W Solar Generator Run a Refrigerator?',
        'slug': 'will-1000w-solar-generator-run-refrigerator',
        'image': 'will-1000w-solar-generator-run-refrigerator.jpg',
        'tags': ['Solar Power', 'Refrigerator', 'Emergency Preparedness', 'Power Outage', 'Home Backup Power'],
        'date': 'Apr 22',
        'priority': 'HIGH - Published Apr 14, high traffic potential'
    },
    {
        'num': 3,
        'title': 'EcoFlow DELTA 3 Plus Review',
        'slug': 'ecoflow-delta-3-plus-review',
        'image': 'ecoflow-delta-3-plus-review.jpg',
        'tags': ['Solar Power', 'Product Review', 'EcoFlow', 'Portable Power Station', 'Emergency Preparedness'],
        'date': 'Apr 23',
        'priority': 'HIGH - Money article with affiliate links'
    },
    {
        'num': 4,
        'title': 'Jackery Explorer 1000 V2 Review',
        'slug': 'jackery-explorer-1000-v2-review',
        'image': 'jackery-1000-v2-review.jpg',
        'tags': ['Solar Power', 'Product Review', 'Jackery', 'Portable Power Station', 'Emergency Preparedness'],
        'date': 'Apr 24',
        'priority': 'HIGH - Money article with affiliate links'
    },
    {
        'num': 5,
        'title': 'Bluetti AC200L Review',
        'slug': 'bluetti-ac200l-review',
        'image': 'bluetti-ac200l-review.jpg',
        'tags': ['Solar Power', 'Product Review', 'Bluetti', 'Portable Power Station', 'Emergency Preparedness'],
        'date': 'Apr 25',
        'priority': 'HIGH - Money article with affiliate links'
    },
    {
        'num': 6,
        'title': 'What Appliances Can a Solar Generator Run?',
        'slug': 'what-appliances-can-solar-generator-run',
        'image': 'what-appliances-solar-generator.jpg',
        'tags': ['Solar Power', 'Emergency Preparedness', 'Home Appliances', 'Off Grid Living', 'Power Outage'],
        'date': 'Apr 26',
        'priority': 'MEDIUM - Info article, good SEO'
    },
    {
        'num': 7,
        'title': 'EcoFlow vs Jackery: Which Solar Generator Brand is Better?',
        'slug': 'ecoflow-vs-jackery-comparison',
        'image': 'ecoflow-vs-jackery-comparison.jpg',
        'tags': ['Solar Power', 'Product Comparison', 'EcoFlow', 'Jackery', 'Buying Guide'],
        'date': 'Apr 27',
        'priority': 'HIGH - Comparison article drives sales'
    },
    {
        'num': 8,
        'title': 'Best Solar Generator for Camping 2026',
        'slug': 'best-solar-generator-camping-2026',
        'image': 'best-solar-generator-camping-2026.jpg',
        'tags': ['Solar Power', 'Camping', 'Outdoor Recreation', 'Product Review', 'Off Grid Living'],
        'date': 'Apr 28',
        'priority': 'MEDIUM - Different audience'
    },
    {
        'num': 9,
        'title': 'Portable Power Station vs Gas Generator',
        'slug': 'portable-power-station-vs-gas-generator',
        'image': 'gas-vs-battery.jpg',
        'tags': ['Solar Power', 'Gas Generator', 'Product Comparison', 'Emergency Preparedness', 'Buying Guide'],
        'date': 'Apr 29',
        'priority': 'MEDIUM - Comparison drives decisions'
    },
    {
        'num': 10,
        'title': 'Best Solar Generator for Chest Freezer',
        'slug': 'best-solar-generator-chest-freezer',
        'image': 'best-solar-generator-chest-freezer.jpg',
        'tags': ['Solar Power', 'Chest Freezer', 'Food Storage', 'Emergency Preparedness', 'Power Outage'],
        'date': 'Apr 30',
        'priority': 'MEDIUM - Niche but targeted'
    },
    {
        'num': 11,
        'title': 'How Many Watts Does a Chest Freezer Use?',
        'slug': 'how-many-watts-chest-freezer',
        'image': 'how-many-watts-chest-freezer.jpg',
        'tags': ['Chest Freezer', 'Power Consumption', 'Energy Efficiency', 'Solar Power', 'Home Appliances'],
        'date': 'May 1',
        'priority': 'LOW - Supporting content'
    },
    {
        'num': 12,
        'title': 'LiFePO4 vs Lithium-Ion: Which Battery Technology is Better?',
        'slug': 'lifepo4-vs-lithium-ion',
        'image': 'lifepo4-vs-lithium-comparison.jpg',
        'tags': ['Battery Technology', 'LiFePO4', 'Lithium Ion', 'Solar Power', 'Technical Guide'],
        'date': 'May 2',
        'priority': 'LOW - Technical, builds authority'
    },
    {
        'num': 13,
        'title': 'Best Solar Generator for Well Pump',
        'slug': 'best-solar-generator-well-pump',
        'image': 'well-pump-solar-generator.jpg',
        'tags': ['Solar Power', 'Well Pump', 'Off Grid Living', 'Emergency Water', 'Product Review'],
        'date': 'May 3',
        'priority': 'MEDIUM - Niche audience'
    },
    {
        'num': 14,
        'title': 'Chest Freezer Blackout Math: How Long Will Your Food Last?',
        'slug': 'chest-freezer-blackout-math',
        'image': 'chest-freezer-stocked.jpg',
        'tags': ['Power Outage', 'Food Storage', 'Chest Freezer', 'Emergency Preparedness', 'Food Safety'],
        'date': 'May 5',
        'priority': 'LOW - Supporting content'
    },
    {
        'num': 15,
        'title': 'How Long Does Food Last Without Power?',
        'slug': 'how-long-food-lasts-without-power',
        'image': 'power-outage.jpg',
        'tags': ['Power Outage', 'Food Safety', 'Emergency Preparedness', 'Food Storage', 'Home Safety'],
        'date': 'May 6',
        'priority': 'LOW - Info content'
    },
    {
        'num': 16,
        'title': 'What is LRA on a Freezer? (Locked Rotor Amps Explained)',
        'slug': 'what-is-lra-on-a-freezer',
        'image': 'lra-data-plate.jpg',
        'tags': ['Freezer', 'Technical Guide', 'Electrical', 'Home Appliances', 'Power Requirements'],
        'date': 'May 8',
        'priority': 'LOW - Technical FAQ'
    },
    {
        'num': 17,
        'title': 'What is a Solar Generator? Complete Beginner Guide',
        'slug': 'solar-generator',
        'image': 'solar-panels-home.jpg',
        'tags': ['Solar Power', 'Beginner Guide', 'Renewable Energy', 'Off Grid Living', 'Emergency Preparedness'],
        'date': 'May 9',
        'priority': 'MEDIUM - Top-of-funnel content'
    },
    {
        'num': 18,
        'title': 'Best Solar Camping Gear 2026',
        'slug': 'best-solar-camping-2026',
        'image': 'best-solar-camping-hero.jpg',
        'tags': ['Solar Power', 'Camping', 'Outdoor Gear', 'Product Review', 'Off Grid Living'],
        'date': 'May 10',
        'priority': 'LOW - Different audience'
    }
]

# Generate PDF content
pdf_content = """MEDIUM PUBLISHING GUIDE
Eco Living Journey - Complete Publishing Schedule
Generated: April 21, 2026

═══════════════════════════════════════════════════════════════════

📋 PUBLISHING RULES - READ FIRST!

✅ Publish 1 article per day (never more than 2)
✅ Publish between 8-10 AM EST for best reach
✅ Always verify canonical URL is set correctly
✅ Add hero image BEFORE publishing
✅ Use all 5 tags exactly as written
✅ Check preview before publishing

❌ DON'T publish multiple articles same day
❌ DON'T skip the canonical URL step
❌ DON'T change the tags (Medium SEO is optimized)

═══════════════════════════════════════════════════════════════════

"""

for article in articles:
    status = article.get('status', '⏳ TO DO')
    
    pdf_content += f"""
{'='*70}
ARTICLE #{article['num']}: {status}
{'='*70}

📅 PUBLISH DATE: {article['date']}
🎯 PRIORITY: {article['priority']}

TITLE: {article['title']}

───────────────────────────────────────────────────────────────────

STEP 1: IMPORT TO MEDIUM
───────────────────────────────────────────────────────────────────

1. Go to: https://medium.com/p/import

2. Paste this URL:
   https://ecoliving-journey.com/blog/{article['slug']}/

3. Click "Import"

4. Wait for import to complete

───────────────────────────────────────────────────────────────────

STEP 2: ADD HERO IMAGE
───────────────────────────────────────────────────────────────────

1. Click at the VERY TOP of the article (before the title)
2. Press ENTER to create space
3. Click the "+" button on the left
4. Select "Image"
5. Upload this file:
   C:\\Users\\DELL\\Desktop\\eco-living-journey\\medium-images\\{article['image']}

───────────────────────────────────────────────────────────────────

STEP 3: ADD TAGS (Copy-paste exactly)
───────────────────────────────────────────────────────────────────

Tag 1: {article['tags'][0]}
Tag 2: {article['tags'][1]}
Tag 3: {article['tags'][2]}
Tag 4: {article['tags'][3]}
Tag 5: {article['tags'][4]}

───────────────────────────────────────────────────────────────────

STEP 4: VERIFY CANONICAL URL
───────────────────────────────────────────────────────────────────

1. Click "⋯" (three dots menu) → "More settings"
2. Scroll to "Advanced settings"
3. Verify "Canonical link" shows:
   https://ecoliving-journey.com/blog/{article['slug']}/

───────────────────────────────────────────────────────────────────

STEP 5: PUBLISH
───────────────────────────────────────────────────────────────────

1. Click green "Publish" button
2. Review preview
3. Click "Publish now"
4. ✅ Mark this article as DONE in your checklist!

═══════════════════════════════════════════════════════════════════

"""

# Add calendar view at the end
pdf_content += """

═══════════════════════════════════════════════════════════════════
📅 QUICK CALENDAR VIEW
═══════════════════════════════════════════════════════════════════

WEEK 1 (Apr 21-27) - PRIORITY ARTICLES:
□ Apr 21: Best Solar Generator Home Backup ✅ DONE
□ Apr 22: Will 1000W Run Refrigerator
□ Apr 23: EcoFlow DELTA 3 Plus Review
□ Apr 24: Jackery Explorer 1000 V2 Review
□ Apr 25: Bluetti AC200L Review
□ Apr 26: What Appliances Can Solar Generator Run
□ Apr 27: EcoFlow vs Jackery Comparison

WEEK 2 (Apr 28 - May 3):
□ Apr 28: Best Solar Generator Camping
□ Apr 29: Portable Power Station vs Gas Generator
□ Apr 30: Best Solar Generator Chest Freezer
□ May 1: How Many Watts Chest Freezer
□ May 2: LiFePO4 vs Lithium-Ion
□ May 3: Best Solar Generator Well Pump

WEEK 3 (May 5-10):
□ May 5: Chest Freezer Blackout Math
□ May 6: How Long Food Lasts Without Power
□ May 8: What is LRA on Freezer
□ May 9: Solar Generator Beginner Guide
□ May 10: Best Solar Camping Gear

═══════════════════════════════════════════════════════════════════

🎯 AFTER PUBLISHING ALL ARTICLES:

1. Monitor Medium stats dashboard
2. Respond to comments within 24 hours
3. Share top performers on Pinterest/Facebook
4. Track which articles drive most traffic back to your site
5. Update your site with "As featured on Medium" badge

═══════════════════════════════════════════════════════════════════

💡 TIPS FOR SUCCESS:

- Respond to every comment - boosts Medium algorithm
- Clap for related articles in your niche - builds network
- Join Medium publications about solar/prepping
- Cross-link articles when relevant
- Update with new info every 6 months

═══════════════════════════════════════════════════════════════════

END OF GUIDE
"""

# Save as text file first
with open('MEDIUM_PUBLISHING_GUIDE.txt', 'w', encoding='utf-8') as f:
    f.write(pdf_content)

print('✅ Publishing guide created: MEDIUM_PUBLISHING_GUIDE.txt')
print('\nNow converting to PDF...')
