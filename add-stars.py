import os

# File 1: best-solar-generator-home-backup-2026.md
f1 = 'src/content/blog/best-solar-generator-home-backup-2026.md'
if os.path.exists(f1):
    c = open(f1, encoding='utf-8').read()
    old = '| Feature | EcoFlow DELTA 3 Plus | Jackery 1000 V2 | Bluetti AC200L |\n|---|---|---|---|\n| Battery | 1,024Wh | 1,070Wh | 2,048Wh |\n| AC Output | 1,800W (2,500W boost) | 2,000W | 2,400W |\n| Weight | 12.3kg | 11.8kg | 28kg |'
    new = '| Feature | EcoFlow DELTA 3 Plus | Jackery 1000 V2 | Bluetti AC200L |\n|---|---|---|---|\n| Battery | 1,024Wh | 1,070Wh | 2,048Wh |\n| AC Output | 1,800W (2,500W boost) | 2,000W | 2,400W |\n| Weight | 12.3kg | 11.8kg | 28kg |\n| Surge Reliability | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2605 |\n| Value for Money | \u2605\u2605\u2605\u2606\u2606 | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2606\u2606 |\n| Battery Life | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2605 |\n| Overall | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 | \u2605\u2605\u2605\u2605\u2606 |'
    if old in c:
        c = c.replace(old, new)
        open(f1, 'w', encoding='utf-8').write(c)
        print('Updated: ' + f1)
    else:
        print('Table not matched: ' + f1)

# File 2: ecoflow-vs-jackery-comparison.md
f2 = 'src/content/blog/ecoflow-vs-jackery-comparison.md'
if os.path.exists(f2):
    c = open(f2, encoding='utf-8').read()
    old = '| Feature | EcoFlow DELTA 3 Plus | Jackery Explorer 1000 V2 |\n| :--- | :--- | :--- |'
    new = '| Feature | EcoFlow DELTA 3 Plus | Jackery Explorer 1000 V2 |\n| :--- | :--- | :--- |\n| Overall Rating | \u2605\u2605\u2605\u2605\u2605 | \u2605\u2605\u2605\u2605\u2606 |'
    if old in c:
        c = c.replace(old, new)
        open(f2, 'w', encoding='utf-8').write(c)
        print('Updated: ' + f2)
    else:
        print('Table not matched: ' + f2)

# File 3: ecoflow-delta-3-plus-review.md
f3 = 'src/content/blog/ecoflow-delta-3-plus-review.md'
if os.path.exists(f3):
    c = open(f3, encoding='utf-8').read()
    old = '| **EcoFlow DELTA 3 Plus** | 1,024Wh | \U0001f7e2 7,200W | 80 min | Fastest charging + highest surge |\n| Jackery Explorer 1000 V2 | 1,070Wh | \U0001f7e1 2,000W | ~5 hours | \U0001f7e2 Most portable, 30-day cookie |\n| Bluetti Elite 200v2 | 2,073Wh | \U0001f7e1 3,900W | ~3 hours | \U0001f7e2 Highest capacity for long outages |'
    new = '| **EcoFlow DELTA 3 Plus** | 1,024Wh | \U0001f7e2 7,200W | 80 min | Fastest charging + highest surge | \u2605\u2605\u2605\u2605\u2605 |\n| Jackery Explorer 1000 V2 | 1,070Wh | \U0001f7e1 2,000W | ~5 hours | \U0001f7e2 Most portable, 30-day cookie | \u2605\u2605\u2605\u2605\u2606 |\n| Bluetti Elite 200v2 | 2,073Wh | \U0001f7e1 3,900W | ~3 hours | \U0001f7e2 Highest capacity for long outages | \u2605\u2605\u2605\u2605\u2606 |'
    if old in c:
        c = c.replace(old, new)
        # Also update header
        c = c.replace('| \U0001f7e2 Best Feature |', '| \U0001f7e2 Best Feature | Rating |')
        c = c.replace('| :--- | :--- | :--- | :--- | :--- |', '| :--- | :--- | :--- | :--- | :--- | :--- |')
        open(f3, 'w', encoding='utf-8').write(c)
        print('Updated: ' + f3)
    else:
        print('Table not matched: ' + f3)

print('All done')
