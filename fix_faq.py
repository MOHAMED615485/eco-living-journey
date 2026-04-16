from pathlib import Path

file = Path("src/content/blog/how-long-food-lasts-without-power.md")
content = file.read_text(encoding="utf-8")

faq_block = """

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does food last without power?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Refrigerated food stays safe for up to 4 hours without power. A full freezer holds for 48 hours, a half-full freezer for 24 hours."
      }
    },
    {
      "@type": "Question",
      "name": "What foods spoil first during a power outage?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meat, fish, poultry, dairy, and cooked leftovers spoil fastest. Hard cheeses, butter, and whole fruits and vegetables last longer."
      }
    },
    {
      "@type": "Question",
      "name": "Should I open my refrigerator during a power outage?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keep the refrigerator closed as much as possible. An unopened refrigerator stays cold for about 4 hours. Every time you open it, cold air escapes and food spoils faster."
      }
    }
  ]
}
</script>
"""

if 'application/ld+json' not in content:
    content = content + faq_block
    file.write_text(content, encoding="utf-8")
    print("SUCCESS - FAQ schema added")
else:
    print("Schema already exists - check file manually")
