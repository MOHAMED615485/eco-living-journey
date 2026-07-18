f="src/content/blog/best-solar-generator-cpap-machine.md"
c=open(f,encoding="utf-8").read()
c=c.replace('category: "Best Solar Generators"','category: "Best Solar Generators"\nfaqSchema: true')
c=c.replace('updatedDate: "Jul 12 2026"','updatedDate: "Jul 18 2026"')
disc='\n<p style="font-size:0.85rem;color:#666;padding:10px 16px;background:#f9f9f9;border-left:3px solid #2d6a4f;margin-bottom:1.5rem;border-radius:4px;"><em>This post contains affiliate links. I earn a small commission if you buy through my links, at no extra cost to you. I only recommend gear I have personally tested.</em></p>\n'
a="A solar generator is not a luxury for CPAP users — it is medical infrastructure."
c=c.replace(a, a+"\n"+disc, 1)
cta='''
Choosing the right generator for a CPAP comes down to watt-hours, DC output, and battery chemistry - get one wrong and it dies before morning. If you'd rather not guess, my **Solar Generator Buyer's Toolkit** walks you through the exact numbers for your setup before you spend a cent.

<div style="background:#f5f0dc;border:2px solid #2d6a4f;border-radius:8px;padding:1rem 1.25rem;margin:1.5rem 0;">
  <p style="margin:0 0 8px;font-weight:600;color:#2d6a4f;">&#9889; Solar Generator Buyer's Toolkit - $19</p>
  <p style="margin:0 0 12px;font-size:0.95rem;">The exact watt-hour math, DC-vs-AC runtime guide, and a sizing calculator so you buy the right generator for your CPAP the first time.</p>
  <a href="https://ethanecoliving.gumroad.com/l/solar-generator-toolkit-2026" style="display:inline-block;background:#3d8b6f;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;">Get the Toolkit - $19 &rarr;</a>
</div>

'''
c=c.replace("## Emergency Kit for CPAP Users", cta+"## Emergency Kit for CPAP Users", 1)
open(f,"w",encoding="utf-8").write(c)
print("Gumroad CTA:", c.count("gumroad.com/l/"))
print("correct link:", "solar-generator-toolkit-2026" in c)
print("disclosure:", "affiliate links" in c)
print("faqSchema:", "faqSchema: true" in c)
