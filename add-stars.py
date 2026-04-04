import os

# ============================================================
# ARTICLE 1: Best Solar Generator Home Backup 2026
# ============================================================
f1 = 'src/content/blog/best-solar-generator-home-backup-2026.md'
if os.path.exists(f1):
    c = open(f1, encoding='utf-8').read()
    
    old1 = '''| Feature | EcoFlow DELTA 3 Plus | Jackery Explorer 1000 V2 | Bluetti AC200L |
|---|---|---|---|
| Battery | 1,024Wh | 1,070Wh | 2,048Wh |
| AC Output | 1,800W | 2,000W | 2,400W |
| Surge | 2,500W | 4,000W | 3,600W |
| Weight | 12.3kg | 11.8kg | 28kg |
| Wall charge to 80% | 1 hour | 1.7 hours | 2 hours |
| Best for | Reliability | Value | Multi-appliance |'''

    new1 = '''| Feature | EcoFlow DELTA 3 Plus | Jackery Explorer 1000 V2 | Bluetti AC200L |
|---|---|---|---|
| Overall Rating | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2605 |
| Surge Reliability | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2605 |
| Battery Life | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2605 |
| Value for Money | \u2605\u2605\u2605\u2606\u2606 | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2606\u2606 |
| Ease of Use | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2606 |
| Battery | 1,024Wh | 1,070Wh | 2,048Wh |
| AC Output | 1,800W | 2,000W | 2,400W |
| Surge | 2,500W | 4,000W | 3,600W |
| Weight | 12.3kg | 11.8kg | 28kg |
| Wall charge to 80% | 1 hour | 1.7 hours | 2 hours |
| Best for | Reliability | Value | Multi-appliance |'''

    if old1 in c:
        c = c.replace(old1, new1)
        open(f1, 'w', encoding='utf-8').write(c)
        print('Updated: ' + f1)
    else:
        print('Table not found in: ' + f1)

# ============================================================
# ARTICLE 2: Best Solar Generator Chest Freezer 2026
# ============================================================
f2 = 'src/content/blog/best-solar-generator-chest-freezer-2026.md'
if os.path.exists(f2):
    c = open(f2, encoding='utf-8').read()

    old2 = '''| | EcoFlow DELTA 3 Plus | Jackery 1000 V2 | Bluetti AC200L |
|---|---|---|---|
| Surge capacity | 2,500W | 4,000W | 3,600W |
| Freezer-only runtime | 8.9 hours | 8.5 hours | 18.4 hours |
| Surge failures (73 days) | 0 | 2 | 0 |
| High LRA handling | All LRA values | LRA under 9.0 | All LRA values |
| Weight | 12.3kg | 11.8kg | 28kg |
| Wall charge to 80% | 1 hour | 1.7 hours | 2 hours |
| Best for | Reliability | Value | Multi-appliance |'''

    new2 = '''| | EcoFlow DELTA 3 Plus | Jackery 1000 V2 | Bluetti AC200L |
|---|---|---|---|
| Overall Rating | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2605 |
| Surge Reliability | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2605 |
| Runtime Score | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2605 |
| Value for Money | \u2605\u2605\u2605\u2606\u2606 | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2606\u2606 |
| Surge capacity | 2,500W | 4,000W | 3,600W |
| Freezer-only runtime | 8.9 hours | 8.5 hours | 18.4 hours |
| Surge failures (73 days) | 0 | 2 | 0 |
| High LRA handling | All LRA values | LRA under 9.0 | All LRA values |
| Weight | 12.3kg | 11.8kg | 28kg |
| Wall charge to 80% | 1 hour | 1.7 hours | 2 hours |
| Best for | Reliability | Value | Multi-appliance |'''

    if old2 in c:
        c = c.replace(old2, new2)
        open(f2, 'w', encoding='utf-8').write(c)
        print('Updated: ' + f2)
    else:
        print('Table not found in: ' + f2)

# ============================================================
# ARTICLE 3: EcoFlow vs Jackery Comparison
# ============================================================
f3 = 'src/content/blog/ecoflow-vs-jackery-comparison.md'
if os.path.exists(f3):
    c = open(f3, encoding='utf-8').read()

    old3 = '''| Feature | EcoFlow DELTA 3 Plus | Jackery Explorer 1000 V2 |
|---|---|---|
| Battery | 1,024Wh | 1,070Wh |
| AC Output | 1,800W | 2,000W |
| Surge | 2,500W | 4,000W |
| Weight | 12.3kg | 11.8kg |
| Wall charge to 80% | 1 hour | 1.7 hours |'''

    new3 = '''| Feature | EcoFlow DELTA 3 Plus | Jackery Explorer 1000 V2 |
|---|---|---|
| Overall Rating | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 |
| Surge Reliability | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 |
| Battery Life | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2605 |
| Value for Money | \u2605\u2605\u2605\u2606\u2606 | \u2605\u2605\u2605\u2605\u2605 |
| App Experience | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 |
| Battery | 1,024Wh | 1,070Wh |
| AC Output | 1,800W | 2,000W |
| Surge | 2,500W | 4,000W |
| Weight | 12.3kg | 11.8kg |
| Wall charge to 80% | 1 hour | 1.7 hours |'''

    if old3 in c:
        c = c.replace(old3, new3)
        open(f3, 'w', encoding='utf-8').write(c)
        print('Updated: ' + f3)
    else:
        print('Table not found in: ' + f3)

# ============================================================
# ARTICLE 4: EcoFlow DELTA 3 Plus Review
# ============================================================
f4 = 'src/content/blog/ecoflow-delta-3-plus-review.md'
if os.path.exists(f4):
    c = open(f4, encoding='utf-8').read()

    old4 = '''| Feature | EcoFlow DELTA 3 Plus | Jackery Explorer 1000 V2 | Bluetti AC200L |
|---|---|---|---|
| Battery | 1,024Wh | 1,070Wh | 2,048Wh |
| AC Output | 1,800W | 2,000W | 2,400W |
| Surge | 2,500W | 4,000W | 3,600W |
| Weight | 12.3kg | 11.8kg | 28kg |'''

    new4 = '''| Feature | EcoFlow DELTA 3 Plus | Jackery Explorer 1000 V2 | Bluetti AC200L |
|---|---|---|---|
| Overall Rating | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2605 |
| Surge Reliability | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2605 |
| Battery Life | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2605 |
| Value for Money | \u2605\u2605\u2605\u2606\u2606 | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2606\u2606 |
| Battery | 1,024Wh | 1,070Wh | 2,048Wh |
| AC Output | 1,800W | 2,000W | 2,400W |
| Surge | 2,500W | 4,000W | 3,600W |
| Weight | 12.3kg | 11.8kg | 28kg |'''

    if old4 in c:
        c = c.replace(old4, new4)
        open(f4, 'w', encoding='utf-8').write(c)
        print('Updated: ' + f4)
    else:
        print('Table not found in: ' + f4)

print('All done')
