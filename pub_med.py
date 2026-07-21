import os
src="src/content/drafts/best-solar-generator-medical-equipment.md"
c=open(src,encoding="utf-8").read()
c=c.replace("pubDate: 2026-05-28","pubDate: 2026-07-21")
c=c.replace("updatedDate: 2026-05-28","updatedDate: 2026-07-21")
c=c.replace('category: "Best Solar Generators"','category: "Best Solar Generators"\nfaqSchema: true')
disc='''
<p style="font-size:0.85rem;color:#666;padding:10px 16px;background:#f9f9f9;border-left:3px solid #2d6a4f;margin-bottom:1rem;border-radius:4px;"><em>This post contains affiliate links. I earn a small commission if you buy through my links, at no extra cost to you. I only recommend gear I have personally tested.</em></p>

<p style="font-size:0.85rem;color:#666;padding:10px 16px;background:#fff8f0;border-left:3px solid #b35c00;margin-bottom:1.5rem;border-radius:4px;"><em>This guide covers powering medical devices during outages - it is not medical advice. Always follow your device manufacturer's instructions and consult your healthcare provider about backup power for life-sustaining equipment.</em></p>
'''
a="His oxygen saturation was dropping."
c=c.replace(a, a+"\n"+disc, 1)
cta='''
Sizing a generator to life-critical medical equipment leaves zero room for guessing - you need enough runtime, pure sine wave output, and the right battery. My **Solar Generator Buyer's Toolkit** gives you the exact watt-hour math for your specific devices.

<div style="background:#f5f0dc;border:2px solid #2d6a4f;border-radius:8px;padding:1rem 1.25rem;margin:1.5rem 0;">
  <p style="margin:0 0 8px;font-weight:600;color:#2d6a4f;">&#9889; Solar Generator Buyer's Toolkit - $19</p>
  <p style="margin:0 0 12px;font-size:0.95rem;">The exact watt-hour math, runtime calculator, and pure-sine-wave checklist so your backup keeps critical medical devices running through an outage.</p>
  <a href="https://ethanecoliving.gumroad.com/l/solar-generator-toolkit-2026" style="display:inline-block;background:#3d8b6f;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;">Get the Toolkit - $19 &rarr;</a>
</div>

'''
c=c.replace("## The 3 Best Solar Generators for Medical Use", cta+"## The 3 Best Solar Generators for Medical Use", 1)
open("src/content/blog/best-solar-generator-medical-equipment.md","w",encoding="utf-8").write(c)
os.remove(src)
print("CTA:", c.count("gumroad.com/l/"), "| disclosure:", "affiliate links" in c, "| medical note:", "not medical advice" in c, "| faqSchema:", "faqSchema: true" in c)
