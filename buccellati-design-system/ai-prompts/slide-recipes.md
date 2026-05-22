# Slide Recipes — Per-layout briefing prompts

> Sometimes you don't need a whole deck — you need one slide. These are
> short prompts for generating a single Buccellati-compliant slide, one
> recipe per layout. Use them in Claude, ChatGPT, or Gemini.

---

## 01 — Cover

```text
Generate a Buccellati Cover slide for a deck titled
"[TITLE]" with subtitle "[SUBTITLE]", dated [MONTH YEAR].
Use Blu Buccellati #1B2A4E background. Center the BUCCELLATI wordmark
at y=1.4", title in 48pt Garamond Light Avorio at y=3.0", subtitle in
16pt Gill Sans Oro Chiaro at y=5.5", date in 11pt Gill Sans Cenere at
y=6.3". Add a 2"-wide Oro Antico hairline at y=6.95".
```

---

## 02 — Section Divider

```text
Generate a Buccellati Section Divider slide. Background Pergamena
#EAE2D2. Section number "[I/II/III/IV/V/VI]." top-left in 14pt Gill
Sans Bold Oro Antico tracked +200, followed by a 1.5" rigato rule of
40 vertical 0.5pt hairlines. Section title "[TITLE]" in 40pt Garamond
Light at y=3.2". Italic descriptor "[ONE LINE]" in 14pt Garamond Italic
Grafite below.
```

---

## 03 — Agenda

```text
Generate a Buccellati Agenda slide. Title "Agenda" in 28pt Garamond
sentence case top-left, followed by the standard eyebrow + Oro Antico
hairline. List six items in two columns (columns 1–5 and 7–12). Each
item: Roman numeral in Oro Antico 14pt + 18pt Garamond heading +
12pt Gill Sans italic Grafite descriptor. Items:
1. [HEADING] — [descriptor]
2. ...
```

---

## 04 — Statement

```text
Generate a Buccellati Statement slide. Eyebrow "[CATEGORY]". Title
"[ONE-SENTENCE THESIS, sentence case, declarative]". Body block in 16pt
Gill Sans, max 60 words, centered between columns 3–10:
"[BODY]"
```

---

## 05 — Two-column

```text
Generate a Buccellati Two-column slide. Eyebrow "[CATEGORY]". Title
"[DECLARATIVE]". Left column (columns 1–5): eyebrow "THE FACT" in Oro
Antico, body in 14pt Gill Sans. Right column (columns 8–12): eyebrow
"THE IMPLICATION", body in 14pt. Add a 0.5pt vertical Cenere hairline
at column 6.5.
Left content: [text]
Right content: [text]
```

---

## 06 — Three-column

```text
Generate a Buccellati Three-column slide. Eyebrow "[CATEGORY]". Title
"[DECLARATIVE]". Three equal columns at 1–4, 5–8, 9–12. Each column:
Oro Antico Roman numeral (I/II/III), 18pt Garamond heading, 12pt Gill
Sans body in Grafite. MAX 35 WORDS PER COLUMN.
Column I: [heading] — [body]
Column II: [heading] — [body]
Column III: [heading] — [body]
```

---

## 07 — Image-led

```text
Generate a Buccellati Image-led full-bleed slide. [IMAGE: describe the
photograph in Buccellati vocabulary — macro craft, archival heritage,
Italian context, etc.]. Caption block lower-left, 4" wide, on 60%
opacity Avorio scrim with: eyebrow "[CATEGORY]" + 18pt Garamond title
"[TITLE]" + 12pt Gill Sans Italic Grafite caption "[CAPTION]". Wordmark
in Avorio bottom-right.
```

---

## 08 — Image + Text 60/40

```text
Generate a Buccellati Image+Text 60/40 slide. [IMAGE: describe in
Buccellati vocabulary] filling left columns 1–7 from edge to gutter,
full vertical bleed. Right text block in columns 8–12 with eyebrow
"[CATEGORY]", H2 title "[TWO LINES, sentence case]", body in 14pt
Gill Sans:
"[BODY]"
```

---

## 09 — KPI dashboard

```text
Generate a Buccellati KPI slide. Eyebrow "[PERIOD]". Title "[ONE LINE
TAKEAWAY]". Three KPIs in columns 1–4, 5–8, 9–12. Each KPI:
- Label (Oro Antico, 9pt, +200 tracked, UPPERCASE)
- Numeral (64pt Garamond Light, Nero)
- Delta (14pt Gill Sans Bold) — ▲ Oro Antico for positive, ▼ Grafite
  for negative
- Context (11pt Gill Sans Italic, Grafite)

KPIs:
1. [LABEL] — [NUMERAL] — [DELTA] — [CONTEXT]
2. ...
Source line in 8pt Gill Sans Cenere above the footer.
```

---

## 10 — Chart

```text
Generate a Buccellati Chart slide. Eyebrow "[CATEGORY]". Title
"[DECLARATIVE ANSWER, sentence case]". One-line takeaway in 14pt Gill
Sans Italic directly under the title: "[THE 'SO WHAT']".

Chart specs:
- Type: [bar / line / column]
- Series in order: #1B2A4E, #A8894E, #4A4A48, #8A8A86, #C9A961, #7A8BA8
- NO gridlines except a single 0.5pt Cenere horizontal baseline
- NO 3D, NO shadows, NO gradients
- Data labels in 11pt Georgia tabular ON the bar, not in a legend
- For positive/negative: Oro Antico vs Grafite (never red/green)
- Axis labels in 10pt Gill Sans Grafite

Data: [paste table or CSV]
Source: [source line, 8pt Cenere]
```

---

## 11 — Table

```text
Generate a Buccellati Table slide. Eyebrow "[CATEGORY]". Title
"[DECLARATIVE]". Build a [N]-row × [M]-column table:
- Header row: 11pt Gill Sans Bold small caps, Avorio text on Blu
  Buccellati fill, 0.4" row height
- Body rows: 11pt Gill Sans for labels, 11pt Georgia tabular for
  numerals, 0.35" row height
- Row banding: alternate Avorio and Lino (#D9D2C3) at 30% opacity
- NO vertical rules. Horizontal hairlines only: 0.5pt Cenere between
  rows, 1pt Oro Antico above header and below last row
- Right-align numerals, left-align labels

Data: [paste table]
```

---

## 12 — Pull-quote

```text
Generate a Buccellati Pull-quote slide. Avorio background. Oversized
opening quote glyph "❝" in 120pt Garamond Italic Oro Antico, top-left.
Quote text in 32pt Garamond Italic Light Nero, left-aligned, max 9" wide:
"[QUOTE]"

Attribution in 12pt Gill Sans, +120 tracking, small caps, Grafite,
indented 1":
"—  [NAME], [TITLE]"
```

---

## 13 — Team / Org

```text
Generate a Buccellati Team slide. Eyebrow "[CATEGORY]". Title
"[DECLARATIVE]". 4-up portrait grid, each portrait on a 2.4" × 2.6"
Pergamena mat. Below each portrait:
- Name in 14pt Garamond Nero, centered
- Title in 10pt Gill Sans Italic +60 tracked Grafite, centered

People:
1. [Name] — [Title]
2. ...

All portraits black-and-white or warm-toned color, consistent lighting,
same angle and crop ratio. NO shadows, NO circular crops, NO colored
borders.
```

---

## 14 — Timeline

```text
Generate a Buccellati Timeline slide. Eyebrow "Heritage" or similar.
Title "[DECLARATIVE]". Horizontal axis: 1pt Oro Antico hairline at
y=4.6". Equal-spaced milestones (not chronologically scaled).

Each milestone:
- 0.16"-tall vertical tick mark at the axis, Oro Antico
- Year below in 12pt Garamond small caps +120 tracked, Nero
- Label above in 11pt Gill Sans Grafite, max 8 words, with a 0.5pt
  Cenere connector hairline from text to tick

Milestones:
- [YEAR] — [LABEL]
- ...
```

---

## 15 — Comparison

```text
Generate a Buccellati Comparison slide. Eyebrow "[CATEGORY]". Title
"[DECLARATIVE]". Two columns at 1–5 and 8–12 with 0.6"-tall heading
bands: left band Blu Buccellati with Avorio text "[LEFT HEADER]",
right band Pergamena with Nero text "[RIGHT HEADER]".

Below each band, an em-dash bulleted list (Oro Antico bullets, never
round dots), 14pt Gill Sans Nero, 0.6" vertical rhythm.

Optional 0.5pt vertical Oro Antico hairline at column 6.5.

Left items: [...]
Right items: [...]
```

---

## 16 — Closing

```text
Generate a Buccellati Closing slide. Full-bleed Blu Buccellati
background. Center the BUCCELLATI wordmark at y=2.5", 2.4" wide,
in Avorio. Below, "Grazie." in 40pt Garamond Italic Light Oro Chiaro,
centered at y=4.2". Add a 2"-wide Oro Antico hairline at y=5.7".
No contact information.
```
