---
title: "Freezer LRA Explained: The Surge Number That Matters Most"
description: "LRA is the hidden surge number on your freezer's data plate. It determines whether your backup battery survives or trips at 2 AM. Here is exactly how to find it, calculate your surge watts, and choose the right battery."
pubDate: "Mar 22 2026"
heroImage: "../../assets/lra-data-plate.webp"
---

## What Is LRA on a Freezer Data Plate?

⚡ **The Quick Answer:** LRA stands for Locked Rotor Amps — the surge of electricity your freezer's compressor needs to start from a dead stop. Multiply your LRA by 120 to get your surge watts. Any backup battery must have a surge capacity above that number or it will trip and shut off the moment your compressor kicks on — usually at 2 AM when you are asleep.

---

There is a sticker on the back of your chest freezer that most people have never read.

It has been there since the day you bought it. It has a small grid of electrical numbers printed on it. And somewhere in that grid is a number labeled **LRA** — a number that will determine whether your emergency food supply survives the next power outage, or ends up in a garbage bag.

I did not know what LRA meant until the morning I lost $847 worth of grass-fed beef. That was a Tuesday in January 2023. An ice storm knocked out our grid for 31 hours. The cheap 500W battery I had trusted tripped its internal breaker at 2 AM and shut off completely. By 6 AM, the meat had been sitting at 48°F for six hours.

We threw it all out.

That morning I pulled every appliance away from the wall and read every data plate in my house. That is when I found the LRA number — and understood exactly why my battery had failed.

---

## 💡 The Beginner's Breakdown: What LRA Actually Means

Let me keep this simple because the concept is straightforward once you see it.

Your chest freezer has a mechanical compressor inside — a motor that pumps refrigerant through insulated walls to keep everything frozen. That motor does not run constantly. It cycles on and off every 30 to 45 minutes throughout the day to hold the target temperature.

Here is the part nobody explains: **starting a motor from a dead stop requires a massive jolt of electricity.**

Think about push-starting a car. Once it is rolling, keeping it moving takes almost no effort. Getting it moving from completely still — that takes everything you have.

Your freezer compressor works the same way. Once the motor is spinning, it only needs 150 watts or so to keep going. But in the fraction of a second it takes to break inertia and get spinning from a complete stop, it demands five to seven times that amount.

Electricians call this the **Locked Rotor Amps** — the current the motor draws when the rotor is literally locked still, fighting against pressurized gas and friction. This surge happens every single time the compressor cycles on. Silently. Whether you are awake or asleep. Day and night throughout a power outage.

Your backup battery sees that spike and has to decide: absorb it, or trip the breaker to protect itself.

A battery rated for 500W continuous output with a 600W surge limit will trip every single time. A battery rated for 7,200W surge will not even notice.

That is the entire LRA story in three paragraphs.

---

## 🛠️ How to Find Your LRA in Three Minutes

This is the most useful thing you will do today. Pull your freezer from the wall right now.

**Step 1 — Find the data plate**
Look for a silver or white rectangular sticker on the back panel. Some models have it on the inside of the lid rim or on the bottom of the unit. It will have a grid of electrical specifications — voltage, amperage, model number, serial number, and several other ratings.

**Step 2 — Locate these two specific numbers**

Your data plate will show something like this:

```
Model:   MFC07M2AWW
Volts:   115V
Amps:    1.5A
LRA:     8.3A
Hz:      60
```

The **Amps** figure is your running current — what the freezer draws once the compressor is already running at steady state.

The **LRA** figure is your surge current — what the compressor demands at the instant of startup.

**Step 3 — Calculate your actual numbers**

Running watts = Volts × Amps
Running watts = 115 × 1.5 = **172 watts**

Surge watts = Volts × LRA
Surge watts = 115 × 8.3 = **954 watts**

This freezer runs at 172 watts continuously but demands 954 watts at every startup. Any backup battery needs a surge capacity above 954 watts to function reliably — ideally with at least 20% headroom, meaning 1,145 watts minimum.

**Step 4 — Use the free calculator instead**
If numbers are not your thing, the [free blackout calculator](/local-quote/) does all of this automatically. Enter your appliances and get your exact surge requirement in two minutes.

---

## 📊 LRA Reference: Typical Numbers by Freezer Size

Your exact numbers depend on your specific brand and model — always read your own data plate. But this table gives you a realistic baseline for what to expect:

| Freezer Size | Running Watts | Typical LRA | Surge Watts | Battery Surge Needed |
| :--- | :--- | :--- | :--- | :--- |
| 5 cu. ft. chest | ~100W | ~5.0A | ~600W | 🟢 720W+ |
| 7 cu. ft. chest | ~150W | ~7.5A | ~900W | 🟡 1,080W+ |
| 10 cu. ft. chest | ~200W | ~10.0A | ~1,200W | 🟡 1,440W+ |
| 15 cu. ft. chest | ~250W | ~12.5A | ~1,500W | 🔴 1,800W+ |
| 15 cu. ft. upright | ~400W | ~16.0A | ~1,920W | 🔴 2,304W+ |

Notice the upright freezer numbers. Upright freezers run significantly harder than chest freezers of the same size because cold air falls out every time the door opens — so the compressor cycles more frequently and works harder against a warmer internal temperature.

If you own an upright freezer, add 30% to whatever number you find on the data plate when calculating your minimum battery surge requirement.

---

## Why Surge Capacity Beats Storage Capacity Every Time

Here is the mistake I see repeated constantly in prepper forums and homesteading groups.

People compare portable power stations by **watt-hours** — the total energy storage. They look for the biggest number at the best price. A 1,000Wh battery versus a 2,000Wh battery. More storage, more runtime. That logic makes sense for phones and laptops.

It completely misses the point for chest freezers.

A 2,000Wh battery with a 1,000W surge limit will fail on your 7 cu. ft. chest freezer just as badly as a 300Wh unit with the same surge limit. The battery trips the moment the compressor tries to start. It does not matter how much energy is stored — if the surge capacity is too low, the battery shuts off every single time.

**The spec that matters is surge capacity, not storage capacity.**

For your chest freezer, find that LRA number. Calculate your surge watts. Add 20% safety margin. Find a battery whose surge rating exceeds that number. Everything else is secondary.

---

## What If My Data Plate Does Not List LRA?

Some older units — particularly models manufactured before 2005 — have simplified data plates that show only voltage and running amperage without an explicit LRA figure.

In that case, use this conservative estimate: **multiply your running amps by 6.**

If your data plate shows 1.5A running amps with no LRA listed, estimate your LRA at 9.0A and your surge at 1,080 watts. This gives you enough headroom for most residential compressor motors and accounts for the higher startup demands of older equipment.

For newer freezers purchased in the last 15 years, LRA is almost always listed. If you genuinely cannot find it on the physical plate, search your exact model number followed by "specification sheet" — the manufacturer's technical document will include the full electrical specifications.

---

## The Three-Minute Action Plan

Everything above reduces to this:

**Right now:** Pull your freezer from the wall. Find the data plate. Write down the LRA number and the voltage.

**Calculation:** Surge watts = LRA × Voltage.

**Battery requirement:** Your battery's surge capacity must exceed that number by at least 20%.

**Shortcut:** Use the [free calculator](/local-quote/) if you want to skip the math and get a recommendation for your specific setup.

That is the entire framework. It takes three minutes to gather the data and two minutes with the calculator. Five minutes of work protects your entire emergency food supply.

The alternative is trusting a battery you picked based on marketing copy and hoping it handles the startup spike at 2 AM.

I tried that approach. It cost me $847.

<div class="cta-container">
  <a href="/local-quote/" class="cta-button">
    🧮 Calculate My Surge Requirements Free →
  </a>
</div>

---

*— Ethan*

---

## 👍 Common LRA Questions Answered

**My battery says "peak power 2000W" — is that the surge rating?**
Yes. Peak power, surge capacity, and peak output are all different names for the same specification. That is the number to compare against your LRA-calculated surge watts. Make sure it exceeds your requirement with at least 20% headroom.

**Do I need to check LRA for my refrigerator too?**
Yes — if you plan to run your kitchen refrigerator during a blackout, it has its own LRA number. Modern refrigerators typically surge between 800W and 1,500W depending on size and compressor type. Check both appliances and use the higher surge requirement when choosing your battery.

**My freezer is 20 years old — does that change things?**
Older compressors tend to have higher LRA numbers than modern equivalents. They also degrade over time, which can push startup demands higher. For a freezer older than 15 years, add an extra 15–20% to your calculated surge requirement as a safety buffer.

**Does ambient temperature affect LRA?**
Not the LRA rating itself — that is a fixed electrical property. But hot ambient temperatures mean the compressor cycles more frequently and works harder, which can cause it to draw closer to its LRA ceiling more consistently. In a 95°F garage in August, assume your compressor is running at near-maximum startup demand every single cycle.

**Can I test my surge without a data plate?**
Yes. A clamp meter or smart plug with energy monitoring will show you the actual startup spike in real time. Plug in the smart plug, connect the freezer, watch the wattage reading when the compressor cycles on. The peak reading is your real-world surge. This is actually more accurate than the data plate calculation for older units.

