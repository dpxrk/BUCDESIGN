# 04 · Layout & the 16 slide masters

> Every layout is a named master in the `.potx`. Sixteen of them. Build
> every slide from a master — **never format slide-by-slide**.

## Canvas

- **Aspect ratio:** 16:9 widescreen
- **Dimensions:** 13.333" × 7.5" (33.867 × 19.05 cm) — the PowerPoint
  2013+ default
- **Export — projector:** 1920 × 1080 px at 144 DPI
- **Export — print PDF:** 300 DPI

## Margins (safe area)

- **Outer margin:** 0.6" on all four sides
- **Live area:** 12.133" × 6.3"
- Set as four guides in Slide Master at: x = 0.6", x = 12.733",
  y = 0.6", y = 6.9"

## Grid

- **12 columns** across the 12.133" live area
- **Column width:** 0.94" · **Gutter:** 0.18"
- For **two-column** layouts: columns 1–5 + 8–12 (with 6–7 as gutter)
- For **three-column** layouts: 1–4, 5–8, 9–12

## Whitespace doctrine

- A slide is no more than **40% inked** (text + image + chart). Empty
  space is a Buccellati signal.
- A single-statement slide is preferable to a crowded slide. If a slide
  has more than three text blocks, **split it**.
- Body text never wider than 8 inches (≈ 70 characters at 14pt body).

## Page architecture — every content slide

```
┌─────────────────────────────────────────────────┐
│ [0.6" top margin]                               │
│ EYEBROW · 9pt Gill Sans Bold +200 · Oro Antico  │
│                                                 │
│ Slide title — 28pt Garamond — Nero              │
│ ──── (1pt Oro Antico rule, 1.5" wide)           │
│                                                 │
│ [Content area — grid-based]                     │
│                                                 │
│                                                 │
│ [0.6" bottom margin]                            │
│ B  · slide 04 / 32      Confidential · 05.2026  │
└─────────────────────────────────────────────────┘
```

- **Footer left:** small "B" monogram (0.3" tall) + slide counter
- **Footer right:** "Confidential" classification + date (MM.YYYY)
- **Footer type:** 8 pt Gill Sans MT in Cenere — barely there

## The sixteen layouts

### 01 Cover / Title

- Background: full-bleed Blu Buccellati `#1B2A4E`
- Wordmark: 2.2" wide, horizontally centered, y ≈ 1.4"
- Title: 48–54pt Cormorant Garamond Light, Avorio, centered, y ≈ 3.0"
- Subtitle: 16pt Gill Sans Light, Oro Chiaro, +120 tracking, y ≈ 5.5"
- Date / presenter: 11pt Gill Sans, Cenere, y ≈ 6.3"
- Oro Antico hairline at y ≈ 6.95", 2" wide

### 02 Section Divider

- Background: Pergamena `#EAE2D2` (alternative: Blu Buccellati)
- Section number: "I." through "VI." — 14pt Gill Sans Bold small caps,
  Oro Antico, +200 tracking, top-left
- Rigato rule beneath section number — 1.5" cluster of 40 vertical
  hairlines, 0.5pt, Nero
- Section title: 40pt Garamond Light, Nero, left-aligned, y ≈ 3.2"
- Optional descriptor: 14pt Garamond Italic, Grafite, y ≈ 4.6"
- Honeycomb motif: 1.5" Oro Antico outline, bottom-right (optional)

### 03 Agenda

- Title "Agenda" — 28pt Garamond, top-left
- Two-column list across columns 1–5 and 7–12 (gutter 6)
- Each item: Roman numeral (I., II., III.) in Oro Antico at 14pt,
  followed by an 18pt Garamond Light heading and a 12pt Gill Sans
  italic descriptor in Grafite
- Vertical rhythm: 0.78" between items
- Right column reserved for a single editorial image when desired

### 04 Content — single column statement

- Eyebrow + title block at top
- One body block centered between columns 3–10, 16pt Gill Sans,
  max 60 words
- Optional 72pt Garamond Light pull-numeral in Oro Antico above the body

### 05 Content — two-column

- Left: columns 1–5, body text or list
- Right: columns 8–12, body text or image
- Optional 0.5pt Cenere vertical hairline at x = column 6.5
- Use for: comparison, problem/solution, narrative + visual

### 06 Content — three-column

- Three equal columns at 1–4, 5–8, 9–12
- Each column: Oro Antico Roman numeral, eyebrow, H3 title (18pt Garamond),
  body (12pt Gill Sans)
- **Max 35 words per column.** Three-column layouts are about parallelism,
  not density.

### 07 Image-led — full-bleed

- Full-bleed photograph
- Optional caption block lower-left, 4" wide, on a 60% opacity Avorio
  rectangle, 0.4" inset
- Caption contains: eyebrow + 18pt Garamond title + 12pt Gill Sans italic
- Wordmark in Avorio at bottom-right, 0.9" wide

### 08 Image + Text 60/40

- Left: image filling columns 1–7 from edge to gutter, full vertical bleed
- Right: text block in columns 8–12 with eyebrow + H2 title + body
- Variant: mirror left/right where the image's gravity demands it

### 09 Data — KPI dashboard (1, 3, or 4 metrics)

- Three-up: three vertical blocks at columns 1–4, 5–8, 9–12
- Each block: eyebrow label, 64–72pt Garamond Light numeral, 14pt delta
  indicator (▲ Oro Antico for positive, ▼ Grafite for negative), 11pt
  Gill Sans italic context
- Source line at 8pt Gill Sans Cenere above the footer

### 10 Data — Chart slide

- Title at top-left (28pt Garamond, sentence case)
- **One-line takeaway** immediately below the title — the "so what",
  14pt Gill Sans Italic. McKinsey rule: lead with the answer.
- Chart area in columns 1–9 (left two-thirds), 4.5" tall
- Right column 10–12 for annotation / legend
- Chart styling — non-negotiable:
  - No chart border
  - No gridlines except a single 0.5pt Cenere horizontal baseline
  - No 3D, no shadows, no gradients
  - Axis labels 10pt Gill Sans in Grafite
  - Data labels 11pt Georgia tabular figures **on** the bar/line, not in a legend
  - Series colour order: Blu → Oro Antico → Grafite → Cenere → Oro Chiaro → Blu Polvere
  - Positive / negative: Oro Antico vs Grafite (never red / green)
- **Edward Tufte's rule applies: maximise data-ink ratio.**

### 11 Data — Table

- Header row: 11pt Gill Sans Bold small caps, Avorio text on Blu
  Buccellati fill, 0.4" row height
- Body rows: 11pt Gill Sans for labels, 11pt Georgia tabular for numerals,
  0.35" row height
- Row banding: alternate Avorio and Lino at 30% opacity
- **No vertical rules.** Only horizontal hairlines: 0.5pt Cenere between
  rows, 1pt Oro Antico above the header and below the last row
- Right-align numerals; left-align labels

### 12 Pull-quote

- Background: Avorio
- Opening glyph: oversized "❝" — 120pt Garamond Italic in Oro Antico,
  top-left of the quote block
- Quote text: 32pt Garamond Italic Light, Nero, left-aligned, max 9" wide
- Attribution: 12pt Gill Sans, +120 tracking, small caps, Grafite, indented
- Use for founder quotes, leadership voice, client testimonials.
  **Never for marketing slogans.**

### 13 Team / Org

- Title + eyebrow at top
- Portrait grid: 4-up or 6-up, each portrait on a 2.4" × 2.6" Pergamena mat
- Below each portrait: 14pt Garamond name, 10pt Gill Sans italic title in
  Grafite
- Portrait treatment: black-and-white or warm-toned colour, **consistent
  lighting, same angle and crop across all members**
- No drop shadows, no circular crops, no coloured borders

### 14 Timeline

- Horizontal axis: 1pt Oro Antico hairline at y ≈ 4.6", running from
  x = 1.2" to x = 12.133"
- Era markers: 0.16"-tall vertical tick marks at each milestone
- Date labels below axis: 12pt Garamond small caps, Nero, +120 tracking
- Milestone text above axis: 11pt Gill Sans, Grafite, max 8 words per
  milestone, with a 0.5pt Cenere connector hairline from text to tick
- **Equal spacing between milestones** — editorial timelines respect each
  event's weight rather than its chronological distance

Anchor dates verified from Maison sources:

- **1919** — founding, Milan, Via degli Orefici
- **1925** — Rome boutique at Via Condotti 30–31
- **1929** — Florence
- **1951** — first US boutique, New York
- **1979** — Place Vendôme, Paris (first Italian jeweller to open there)
- **2019** — centenary; Richemont acquisition closed 26 September

### 15 Comparison

- Two-column comparison at columns 1–5 + 8–12
- Each column has a 0.6"-tall heading band (one in Blu / Avorio text,
  one in Pergamena / Nero text)
- Body bullets use an **em-dash bullet in Oro Antico** — never a round dot
- Optional 0.5pt vertical Oro Antico hairline at x = column 6.5

### 16 Closing / Thank You

- Background: Blu Buccellati
- Wordmark: 2.4" wide, centered horizontally, y ≈ 2.5"
- "Grazie." in 40pt Garamond Italic Light, Oro Chiaro, centered at y ≈ 4.2"
- Oro Antico hairline 2" wide, centered at y ≈ 5.7"
- **No contact information by default** — decks are internal. When
  required, contact block at 10pt Gill Sans, Avorio at 70% opacity

## Alignment doctrine

- **All elements snap to the 12-column grid.** No element placed by eye.
- Default text alignment: left, ragged right. **Never justify.**
- Numerical alignment: right, with tabular figures.
- Image alignment: snap to grid; never tilt; never group with text borders.
