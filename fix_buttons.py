import glob, os
cf=0; total=0
for f in glob.glob("src/content/blog/*.md"):
    c=open(f,encoding="utf-8").read(); orig=c
    lines=c.split("\n")
    for i,ln in enumerate(lines):
        if "awin1.com" not in ln or "on Amazon" not in ln: continue
        if "Jackery" in ln or "awinmid=59183" in ln:
            lines[i]=ln.replace("on Amazon","at Jackery"); total+=1
        elif "Bluetti" in ln or "awinmid=59271" in ln:
            lines[i]=ln.replace("on Amazon","at Bluetti"); total+=1
    c="\n".join(lines)
    if c!=orig: open(f,"w",encoding="utf-8").write(c); cf+=1; print("fixed:",os.path.basename(f))
print(f"\n{total} buttons fixed across {cf} files")
left=sum(1 for f in glob.glob("src/content/blog/*.md") for ln in open(f,encoding="utf-8").read().split("\n") if "awin1.com" in ln and "on Amazon" in ln)
print("remaining (must be 0):",left)
