---
title: "What Size Solar Generator Do I Need? (The Honest Calculator Guide)"
description: "Most solar generator sizing guides tell you to add up your watts and buy bigger. That's wrong. Here's how Ethan actually calculates the right size — and why most people overbuy or underbuy."
pubDate: "Jun 14 2026"
updatedDate: "Jun 14 2026"
heroImage: "../../assets/best-solar-generator-2026.webp"
category: "Solar Generator Guides"
faqSchema: true
---

The most common question I get after every review is some version of: "But what size do I actually need?"

It seems like a simple question. Add up your watts, buy something bigger. Done.

Except that is not how it works — and every person who sizes a generator that way either buys too little and watches it trip on day one, or spends $800 more than they needed to.

The right size depends on three numbers that most buying guides never mention. Here is how to find yours in about 10 minutes.

<div style="margin:24px 0;">
  <a href="https://amzn.to/3JackeryV2" target="_blank" rel="noopener noreferrer"
    style="background-color:#c2410c;color:#ffffff;padding:14px 32px;border-radius:8px;
    font-weight:700;font-size:16px;text-decoration:none;color:#ffffff!important;
    display:inline-block;box-shadow:0 4px 6px rgba(0,0,0,0.1);">
    🔋 Jump to Recommendations →
  </a>
</div>

---

## The Three Numbers That Actually Matter

### Number 1: Your Surge Watt Requirement
This is the number most people miss entirely.

Every appliance with a motor — refrigerator, freezer, CPAP, well pump, AC unit — draws a surge of power at startup that is 3-7x higher than its running watts. This surge lasts 1-3 seconds, but if your generator cannot deliver it, the appliance will not start.

Your generator's surge capacity must exceed your highest surge demand — not your total running watts.

**How to find it:** Look for the LRA (Locked Rotor Amps) on your appliance's data plate. Multiply by 120 (for 120V appliances) to get surge watts.

Example: refrigerator with LRA 9.1 → 9.1 × 120 = 1,092W surge required

### Number 2: Your Total Running Watts
This determines how long your battery lasts — not whether it starts.

Add up the running watts of everything you plan to run simultaneously. This is your continuous load.

**Common running watts:**
| Appliance | Running Watts |
|---|---|
| Full-size refrigerator | 100-200W |
| Chest freezer | 30-100W |
| CPAP (no humidifier) | 30-50W |
| CPAP (with humidifier) | 100-150W |
| Tower fan | 40-55W |
| LED lights (room) | 20-40W |
| Phone charging (2 phones) | 20-30W |
| Laptop | 45-65W |
| Wi-Fi router | 8-12W |
| 55" TV | 80-120W |

### Number 3: Your Runtime Requirement
How many hours do you need to run before recharging?

Runtime formula: **Battery capacity (Wh) ÷ Total running watts = Hours**

Example: 1,000Wh battery ÷ 200W load = 5 hours

This tells you whether a 500Wh, 1,000Wh, or 2,000Wh battery is right for your situation.

---

## The Sizing Calculator

**Step 1:** List everything you want to run simultaneously and add up running watts.

**Step 2:** Find the highest LRA appliance and calculate its surge requirement.

**Step 3:** Choose a generator where: surge capacity > your surge requirement AND capacity (Wh) > (total running watts × hours needed)

---

## Real-World Sizing Examples

### Scenario 1: Overnight CPAP + Basic Lights + Phone
- CPAP without humidifier: 40W
- LED light: 20W
- Phone charging: 15W
- **Total running: 75W**
- **Runtime needed:** 8 hours
- **Capacity needed:** 75W × 8 hours = 600Wh minimum
- **Surge concern:** CPAP — minimal surge, ~200W
- **Recommendation:** 500Wh generator ✅ (Jackery Explorer 500)

### Scenario 2: Refrigerator + CPAP + Fan + Lights + Phone
- Refrigerator: 150W
- CPAP with humidifier: 120W
- Tower fan: 45W
- Lights: 30W
- Phone: 20W
- **Total running: 365W**
- **Runtime needed:** 12 hours
- **Capacity needed:** 365W × 12 hours = 4,380Wh (impractical — run in shifts)
- **Practical approach:** Run refrigerator 4 hours on, 4 hours off — CPAP all night
- **Actual draw:** ~250W average
- **Capacity needed:** 250W × 12 hours = 3,000Wh
- **Surge concern:** Refrigerator LRA 9.1 → 1,092W surge
- **Recommendation:** 2,000Wh generator (Bluetti AC200L) or 1,000Wh + smart cycling

### Scenario 3: Full Home Backup — Refrigerator + Freezer + Well Pump + CPAP
- Refrigerator: 150W
- Chest freezer: 60W
- Well pump (½ HP): 900W
- CPAP: 40W
- **Total running: 1,150W** (not all at once)
- **Surge concern:** Well pump LRA 15A → 3,450W surge
- **Recommendation:** Bluetti AC200L (4,800W surge) minimum, or soft starter + 2,000W generator

---

## The Most Common Sizing Mistakes

**Mistake 1 — Sizing for running watts only**
Bought a 1,500W generator for a 900W refrigerator. Generator trips every time the compressor starts because the surge requirement (1,200W) exceeds the surge capacity.

**Mistake 2 — Assuming you need to run everything simultaneously**
A 1,000Wh generator can run a refrigerator AND a CPAP all night if you cycle them intelligently — refrigerator 6 hours on, CPAP all 8 hours. Total draw: ~400Wh refrigerator + ~320Wh CPAP = 720Wh. Fits in 1,000Wh.

**Mistake 3 — Ignoring inverter efficiency**
Solar generator inverters are 85-90% efficient. A 1,000Wh battery delivers approximately 850-900Wh of usable power. Always calculate with 85% of rated capacity for real-world planning.

**Mistake 4 — Buying for peak load instead of average load**
Your refrigerator draws 1,200W for 2 seconds at startup, then 150W for the next 10 minutes. Size for the surge but plan runtime around the average.

---

## Quick Recommendation by Use Case

| Use Case | Recommended Size | Best Model |
|---|---|---|
| CPAP only overnight | 500Wh | Jackery Explorer 500 |
| CPAP + fridge + lights | 1,000Wh | Jackery Explorer 1000 V2 |
| Full home — no well pump | 2,000Wh | Bluetti AC200L |
| RV with roof AC | 2,000Wh + soft starter | EcoFlow DELTA Pro |
| Well pump backup | 2,000Wh + high surge | Bluetti AC200L |
| Medical equipment critical | 2,000Wh pure sine wave | Bluetti AC200L |

---

## The One Question That Simplifies Everything

If you do not want to do the math, answer this one question:

**"What is the single most power-hungry appliance I absolutely must run?"**

- CPAP only → 500-1,000Wh
- Refrigerator → 1,000Wh
- Chest freezer + refrigerator → 1,000-2,000Wh
- Well pump → 2,000Wh + high surge capacity
- RV roof AC → 2,000Wh + soft starter

Everything else — lights, phones, fans, routers — adds runtime requirements but rarely changes the model you need.

<div style="margin:24px 0;">
  <a href="https://amzn.to/3JackeryV2" target="_blank" rel="noopener noreferrer"
    style="background-color:#c2410c;color:#ffffff;padding:14px 32px;border-radius:8px;
    font-weight:700;font-size:16px;text-decoration:none;color:#ffffff!important;
    display:inline-block;box-shadow:0 4px 6px rgba(0,0,0,0.1);">
    🔋 See Top Rated Solar Generators →
  </a>
</div>

---

## Frequently Asked Questions

### What size solar generator do I need for a refrigerator?
A refrigerator drawing 150W running with a surge requirement of 1,000-1,200W needs a solar generator with at least 1,500W surge capacity and 1,000Wh battery capacity for 6-8 hours of runtime. The Jackery Explorer 1000 V2 and EcoFlow DELTA 3 Plus both handle standard refrigerators.

### What size solar generator do I need for a CPAP machine?
A CPAP without humidifier draws 30-50W and needs only 500Wh of battery capacity for a full 10-hour night. A CPAP with humidifier draws 100-150W and needs 1,000-1,500Wh for overnight use. Any generator with pure sine wave output works — the Jackery Explorer 500 is sufficient for CPAP-only use.

### Is 1000W enough for a solar generator?
A 1,000Wh solar generator handles most home backup needs: refrigerator cycling, CPAP overnight, fan, lights, and phone charging. It cannot continuously run high-draw appliances like AC units, electric stoves, or large well pumps. For most families, 1,000Wh covers 80% of outage needs.

### How many watts do I need for a solar generator?
Calculate: add up running watts of all appliances you want to run simultaneously, multiply by hours of runtime needed, and ensure the generator's surge capacity exceeds your highest single-appliance surge requirement. Most households need 1,000-2,000Wh for meaningful outage coverage.

### What can a 2000W solar generator run?
A 2,000Wh solar generator can run: a full-size refrigerator for 10-14 hours, a chest freezer for 18-24 hours, a CPAP all night plus a refrigerator simultaneously, all household lights and electronics for 20+ hours, or an RV roof AC with a soft starter for 2-3 hours. The Bluetti AC200L is the standard 2,000Wh recommendation.

### Is it better to get a bigger solar generator?
Not necessarily. A larger generator costs more, weighs more, and charges more slowly. Buy the size you actually need based on your surge and runtime calculations. Most people overbuy because they size for peak load rather than average load — intelligent cycling of appliances often lets a 1,000Wh unit do what people think requires 2,000Wh.
