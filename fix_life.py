f="src/content/blog/how-long-does-solar-generator-last.md"
c=open(f,encoding="utf-8").read()
c=c.replace('category: "Solar Generator Guides"','category: "Solar Generator Guides"\nfaqSchema: true')
c=c.replace('updatedDate: "May 10 2026"','updatedDate: "Jul 18 2026"')
disc='\n<p style="font-size:0.85rem;color:#666;padding:10px 16px;background:#f9f9f9;border-left:3px solid #2d6a4f;margin-bottom:1.5rem;border-radius:4px;"><em>This post contains affiliate links. I earn a small commission if you buy through my links, at no extra cost to you. I only recommend gear I have personally tested.</em></p>\n'
a="The most honest answer I can give you is this: the solar generator itself will outlast the battery by a decade."
c=c.replace(a, a+"\n"+disc, 1)
cta='''
A solar generator that lasts 10-15 years is only worth it if you buy the right one for your needs. My **Solar Generator Buyer's Toolkit** helps you match capacity and chemistry to your actual use, so you're not replacing it - or regretting it - in two years.

<div style="background:#f5f0dc;border:2px solid #2d6a4f;border-radius:8px;padding:1rem 1.25rem;margin:1.5rem 0;">
  <p style="margin:0 0 8px;font-weight:600;color:#2d6a4f;">&#9889; Solar Generator Buyer's Toolkit - $19</p>
  <p style="margin:0 0 12px;font-size:0.95rem;">The sizing math, battery-chemistry guide, and a calculator so you buy a generator that lasts - and fits what you actually need.</p>
  <a href="https://ethanecoliving.gumroad.com/l/solar-generator-toolkit-2026" style="display:inline-block;background:#3d8b6f;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;">Get the Toolkit - $19 &rarr;</a>
</div>

'''
c=c.replace("## Is a Solar Generator Worth the Investment?", cta+"## Is a Solar Generator Worth the Investment?", 1)
open(f,"w",encoding="utf-8").write(c)
print("CTA:", c.count("gumroad.com/l/"), "| faqSchema:", "faqSchema: true" in c, "| disclosure:", "affiliate links" in c)
