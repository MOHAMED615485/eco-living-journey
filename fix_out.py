f="src/content/blog/how-long-do-power-outages-last.md"
c=open(f,encoding="utf-8").read()
c=c.replace('category: "Power Outage Prep"','category: "Power Outage Prep"\nfaqSchema: true')
c=c.replace('updatedDate: "Apr 30 2026"','updatedDate: "Jul 18 2026"')
disc='\n<p style="font-size:0.85rem;color:#666;padding:10px 16px;background:#f9f9f9;border-left:3px solid #2d6a4f;margin-bottom:1.5rem;border-radius:4px;"><em>This post contains affiliate links. I earn a small commission if you buy through my links, at no extra cost to you. I only recommend gear I have personally tested.</em></p>\n'
a="An ice storm is somewhere in between, and almost always longer than the utility company initially tells you."
c=c.replace(a, a+"\n"+disc, 1)
cta='''
Knowing an outage could last days is one thing - being ready for it is another. My **72-Hour Power Outage Survival Kit** is the printable, room-by-room plan I built after my own multi-day outage, so your family isn't caught scrambling.

<div style="background:#f5f0dc;border:2px solid #2d6a4f;border-radius:8px;padding:1rem 1.25rem;margin:1.5rem 0;">
  <p style="margin:0 0 8px;font-weight:600;color:#2d6a4f;">&#128267; 72-Hour Power Outage Survival Kit - $27</p>
  <p style="margin:0 0 12px;font-size:0.95rem;">Printable room-by-room checklist + solar generator sizing guide + 7-day no-fridge meal plan. Built for the outages that last longer than a day.</p>
  <a href="https://ethanecoliving.gumroad.com/l/72-hour-power-outage-survival-kit" style="display:inline-block;background:#3d8b6f;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;">Get the Kit - $27 &rarr;</a>
</div>

'''
c=c.replace("## Emergency Kit for Extended Outages", cta+"## Emergency Kit for Extended Outages", 1)
open(f,"w",encoding="utf-8").write(c)
print("CTA:", c.count("gumroad.com/l/"), "| faqSchema:", "faqSchema: true" in c, "| disclosure:", "affiliate links" in c)
