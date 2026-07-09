import glob, os, re
FIXES = {
 "/blog/power-outage-food-safety/": "/blog/how-long-food-last-fridge-power-outage/",
 "/blog/jackery-1000-v2-review/": "/blog/jackery-explorer-1000-v2-review/",
 "/blog/how-many-watts-does-a-chest-freezer-use/": "/blog/how-many-watts-chest-freezer/",
 "/blog/best-solar-generator-chest-freezer/": "/blog/best-solar-generator-chest-freezer-2026/",
 "/blog/will-solar-generator-run-chest-freezer/": "/blog/best-solar-generator-chest-freezer-2026/",
 "/blog/portable-solar-vs-gas-generator/": "/blog/best-solar-generator-2026/",
 "/blog/lifepo4-vs-lithium-ion-batteries/": "/blog/best-solar-generator-2026/",
 "/blog/72-hour-power-outage-survival-guide/": "/blog/what-to-do-during-power-outage/",
}
n=0
for f in glob.glob("src/content/blog/*.md"):
    c=open(f,encoding="utf-8").read(); o=c
    for a,b in FIXES.items(): c=c.replace(a,b)
    if c!=o: open(f,"w",encoding="utf-8").write(c); n+=1
print("STEP 1a: links fixed in",n,"files")
for d in ["hello","best-solar-camping-2026","best-solar-generator-camping-2026"]:
    p=f"src/content/blog/{d}.md"
    if os.path.exists(p): os.remove(p); print("STEP 1b: deleted",d)
rules=["/blog/best-solar-camping-2026/ /blog/solar-generator-for-camping/ 301",
"/blog/best-solar-generator-camping-2026/ /blog/solar-generator-for-camping/ 301",
"/blog/hello/ / 301",
"https://www.ecoliving-journey.com/* https://ecoliving-journey.com/:splat 301"]
rf="public/_redirects"; ex=open(rf,encoding="utf-8").read()
new=[r for r in rules if r not in ex]
if new: open(rf,"w",encoding="utf-8").write("\n".join(new)+"\n"+ex); print("STEP 1c: added",len(new),"redirects")
p="src/components/BaseHead.astro"; c=open(p,encoding="utf-8").read()
c=c.replace("  image?: string;\n  type?: string;\n}","  image?: string;\n  type?: string;\n  robots?: string;\n}")
c=c.replace("const { title, description, image = '/social-preview.webp', type = 'website' } = Astro.props;","const { title, description, image = '/social-preview.webp', type = 'website', robots } = Astro.props;")
c=c.replace('<meta charset="utf-8" />','<meta charset="utf-8" />\n{robots && <meta name="robots" content={robots} />}',1)
open(p,"w",encoding="utf-8").write(c); print("STEP 1d: BaseHead robots meta added")
p="src/layouts/BlogPost.astro"; c=open(p,encoding="utf-8").read()
c=c.replace("const { title, description, pubDate, updatedDate, heroImage } = Astro.props;","const { title, description, pubDate, updatedDate, heroImage, robots } = Astro.props;")
if "robots={robots}" not in c:
    m=re.search(r'<BaseHead[^>]*/>',c)
    if m: c=c.replace(m.group(0),m.group(0).replace("/>"," robots={robots} />"),1)
open(p,"w",encoding="utf-8").write(c); print("STEP 1e: BlogPost passes robots")
print("\n=== STEP 1 DONE ===")
