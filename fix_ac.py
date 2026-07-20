f="src/content/blog/can-solar-generator-power-window-ac.md"
c=open(f,encoding="utf-8").read()
c=c.replace('category: "Solar Generator Guides"','category: "Solar Generator Guides"\nfaqSchema: true')
c=c.replace('updatedDate: "May 04 2026"','updatedDate: "Jul 18 2026"')
disc='\n<p style="font-size:0.85rem;color:#666;padding:10px 16px;background:#f9f9f9;border-left:3px solid #2d6a4f;margin-bottom:1.5rem;border-radius:4px;"><em>This post contains affiliate links. I earn a small commission if you buy through my links, at no extra cost to you. I only recommend gear I have personally tested.</em></p>\n'
a="Last July I ran my 5,000 BTU window AC unit on a solar generator for 11 days straight during a heat wave that knocked out grid power across our neighborhood."
c=c.replace(a, a+"\n"+disc, 1)
cta='''
Running a window AC off solar is all about matching surge watts, running watts, and battery capacity to your exact unit - get it wrong and it trips or dies in an hour. My **Solar Generator Buyer's Toolkit** does that math for you.

<div style="background:#f5f0dc;border:2px solid #2d6a4f;border-radius:8px;padding:1rem 1.25rem;margin:1.5rem 0;">
  <p style="margin:0 0 8px;font-weight:600;color:#2d6a4f;">&#9889; Solar Generator Buyer's Toolkit - $19</p>
  <p style="margin:0 0 12px;font-size:0.95rem;">The exact AC wattage math, runtime calculator, and sizing guide so your generator actually keeps your room cool through an outage.</p>
  <a href="https://ethanecoliving.gumroad.com/l/solar-generator-toolkit-2026" style="display:inline-block;background:#3d8b6f;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;">Get the Toolkit - $19 &rarr;</a>
</div>

'''
c=c.replace("## The Inverter Rule You Cannot Skip", cta+"## The Inverter Rule You Cannot Skip", 1)
open(f,"w",encoding="utf-8").write(c)
print("CTA:", c.count("gumroad.com/l/"), "| faqSchema:", "faqSchema: true" in c, "| disclosure:", "affiliate links" in c)
