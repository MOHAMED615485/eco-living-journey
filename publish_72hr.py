import os
src="src/content/drafts/72-hour-power-outage-survival-guide.md"
c=open(src,encoding="utf-8").read()
c=c.replace("pubDate: 2026-05-26","pubDate: 2026-07-17")
c=c.replace("updatedDate: 2026-05-26","updatedDate: 2026-07-17")
c=c.replace('category: "Power Outage Prep"','category: "Power Outage Prep"\nfaqSchema: true')
disc='\n<p style="font-size:0.85rem;color:#666;padding:10px 16px;background:#f9f9f9;border-left:3px solid #2d6a4f;margin-bottom:1.5rem;border-radius:4px;"><em>This post contains affiliate links. I earn a small commission if you buy through my links, at no extra cost to you. I only recommend gear I have personally tested.</em></p>\n'
a="Day three was the day I realized how badly I had failed to prepare my family."
c=c.replace(a, a+"\n"+disc, 1)
cta1='''
If you want this whole checklist done for you - printable, room-by-room, with a solar generator sizing guide and a 7-day no-fridge meal plan - the **72-Hour Power Outage Survival Kit** packages all of it in one place.

<div style="background:#f5f0dc;border:2px solid #2d6a4f;border-radius:8px;padding:1rem 1.25rem;margin:1.5rem 0;">
  <p style="margin:0 0 8px;font-weight:600;color:#2d6a4f;">&#128267; 72-Hour Power Outage Survival Kit - $27</p>
  <p style="margin:0 0 12px;font-size:0.95rem;">Printable room-by-room checklist + solar generator sizing guide + 7-day no-fridge meal plan. Built for the outages that last longer than a day.</p>
  <a href="https://mohamedcanepie.gumroad.com/l/lngbnm" style="display:inline-block;background:#3d8b6f;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;">Get the Kit - $27 &rarr;</a>
</div>

'''
c=c.replace("## The Florida 72-Hour Hurricane Reality", cta1+"## The Florida 72-Hour Hurricane Reality", 1)
cta2='''
Everything in this guide - the six systems, the room-by-room checklist, the kit list - is condensed into one printable pack in the **72-Hour Power Outage Survival Kit**, so your family isn't scrambling when the lights go out.

<div style="background:#f5f0dc;border:2px solid #2d6a4f;border-radius:8px;padding:1rem 1.25rem;margin:1.5rem 0;">
  <p style="margin:0 0 8px;font-weight:600;color:#2d6a4f;">&#128267; Get the Complete 72-Hour Kit - $27</p>
  <p style="margin:0 0 12px;font-size:0.95rem;">Printable checklist + watt calculator + no-fridge meal plan. One download, ready before the next storm.</p>
  <a href="https://mohamedcanepie.gumroad.com/l/lngbnm" style="display:inline-block;background:#3d8b6f;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;">Get the Kit - $27 &rarr;</a>
</div>

'''
c=c.replace("## Frequently Asked Questions", cta2+"## Frequently Asked Questions", 1)
open("src/content/blog/72-hour-power-outage-survival-guide.md","w",encoding="utf-8").write(c)
os.remove(src)
print("Gumroad CTAs:", c.count("gumroad.com/l/lngbnm"))
print("disclosure:", "affiliate links" in c)
print("faqSchema:", "faqSchema: true" in c)
print("date:", "2026-07-17" in c)
print("moved to blog, removed from drafts")
