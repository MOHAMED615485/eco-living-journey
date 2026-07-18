import glob
FIXES = {
 "https://mohamedcanepie.gumroad.com/l/lngbnm": "https://ethanecoliving.gumroad.com/l/72-hour-power-outage-survival-kit",
 "https://mohamedcanepie.gumroad.com/l/lkfqit": "https://ethanecoliving.gumroad.com/l/solar-generator-toolkit-2026",
 "https://ethanecoliving.gumroad.com/l/lngbnm": "https://ethanecoliving.gumroad.com/l/72-hour-power-outage-survival-kit",
}
files=0
for f in glob.glob("src/content/blog/*.md"):
    c=open(f,encoding="utf-8").read(); o=c
    for a,b in FIXES.items(): c=c.replace(a,b)
    if c!=o: open(f,"w",encoding="utf-8").write(c); files+=1
print("Fixed links in",files,"files")
lm=sum(open(f,encoding="utf-8").read().count("mohamedcanepie") for f in glob.glob("src/content/blog/*.md"))
ll=sum(open(f,encoding="utf-8").read().count("/l/lngbnm") for f in glob.glob("src/content/blog/*.md"))
print("Remaining wrong-store:",lm,"| wrong-slug:",ll,"(both must be 0)")
