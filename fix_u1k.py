f="src/content/blog/best-solar-generator-under-1000.md"
c=open(f,encoding="utf-8").read()
c=c.replace("See the Jackery 1000 V2 on Amazon","See the Jackery 1000 V2 at Jackery")
c=c.replace("Check Jackery 1000 V2 Price on Amazon","Check Jackery 1000 V2 Price at Jackery")
c=c.replace("&#9889; Jackery 1000 V2 on Amazon &rarr;","&#9889; Jackery 1000 V2 at Jackery &rarr;")
c=c.replace('category: "Best Solar Generators"','category: "Best Solar Generators"\nfaqSchema: true')
c=c.replace('updatedDate: "Apr 24 2026"','updatedDate: "Jul 18 2026"')
disc='\n<p style="font-size:0.85rem;color:#666;padding:10px 16px;background:#f9f9f9;border-left:3px solid #2d6a4f;margin-bottom:1.5rem;border-radius:4px;"><em>This post contains affiliate links. I earn a small commission if you buy through my links, at no extra cost to you. I only recommend gear I have personally tested.</em></p>\n'
a="The $1000 price point is where solar generators get serious."
c=c.replace(a, a+"\n"+disc, 1)
cta='''
Picking the right one under $1,000 comes down to matching the specs to what you actually need to run - and that's exactly where most buyers overspend or under-buy. My **Solar Generator Buyer's Toolkit** gives you the sizing math and a calculator so you get it right the first time.

<div style="background:#f5f0dc;border:2px solid #2d6a4f;border-radius:8px;padding:1rem 1.25rem;margin:1.5rem 0;">
  <p style="margin:0 0 8px;font-weight:600;color:#2d6a4f;">&#9889; Solar Generator Buyer's Toolkit - $19</p>
  <p style="margin:0 0 12px;font-size:0.95rem;">The exact wattage math, a sizing calculator, and a runtime guide so you buy the right generator under $1,000 - not too much, not too little.</p>
  <a href="https://ethanecoliving.gumroad.com/l/solar-generator-toolkit-2026" style="display:inline-block;background:#3d8b6f;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;">Get the Toolkit - $19 &rarr;</a>
</div>

'''
c=c.replace("## 3 Things That Matter More Than Price", cta+"## 3 Things That Matter More Than Price", 1)
open(f,"w",encoding="utf-8").write(c)
print("on Amazon remaining (should be 2):", c.count("on Amazon"))
print("at Jackery (should be 3):", c.count("at Jackery"))
print("Gumroad CTA:", c.count("gumroad.com/l/"), "| faqSchema:", "faqSchema: true" in c)
