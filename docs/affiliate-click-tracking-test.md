# Affiliate click tracking — test branch

This change adds a GA4 event named `affiliate_click` for outbound Amazon Associates and Awin links.

## Event parameters

- `merchant`: amazon, jackery, bluetti, survivex, or awin
- `affiliate_network`: amazon_associates or awin
- `advertiser_id`: Awin advertiser ID when present
- `product`: link data-product, aria-label, title, or visible link text (max 100 characters)
- `article_path`: current page path
- `placement`: cta, table, header, footer, or content
- `link_domain`: destination hostname only; query strings and full affiliate URLs are not sent

The listener uses event delegation, so it also works for links added after page load. It does not rewrite affiliate URLs or intercept navigation. GA4's dataLayer queue is initialized before interaction; the GA library download remains deferred until the window load event.

## Test before production

1. Deploy this branch only to a non-production preview environment, if available.
2. Open a page with an Amazon affiliate link and click it once. Repeat with a Jackery Awin link and a Bluetti Awin link.
3. In GA4 DebugView or Realtime, confirm one `affiliate_click` event per click.
4. Check the event parameters above. Confirm `merchant`, `affiliate_network`, `article_path`, and `placement` are correct.
5. Confirm normal outbound navigation still works and no duplicate events appear.
6. Check an Awin link with an advertiser ID not in the small mapping: it should still be counted as `merchant=awin`, not silently dropped.

## GA4 reporting setup

In GA4 Admin → Custom definitions, create event-scoped custom dimensions for:
`merchant`, `affiliate_network`, `advertiser_id`, `product`, `article_path`, `placement`, and `link_domain`.

Do not mark this event as a key event until event quality has been checked and the reporting definition is agreed. GA4 reports will not backfill custom dimensions for historical events.

## Scope and caveats

- This change is on `test/affiliate-click-tracking` only. It is not merged or deployed to the live website.
- It counts link clicks, not confirmed orders or commissions. A click does not prove a sale.
- Amazon detection currently covers common Amazon country domains and requires a `tag` query parameter.
- Awin advertiser mapping is deliberately limited to IDs observed in the inspected article links: Jackery 59183, Bluetti 59271, SurviveX 124484. Other Awin advertisers are still tracked under the generic `awin` merchant label.
- This is a code-level change only; a real GA4 DebugView test requires a preview deployment and browser interaction.
