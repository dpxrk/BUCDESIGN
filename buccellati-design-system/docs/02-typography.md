# 02 · Typography

> The Maison's typographic DNA is a **low-contrast, oblique-stress serif
> rooted in inscriptional Roman capitals** — not a high-contrast Didone, not
> a humanist book-face. The PowerPoint system below translates that into
> fonts that ship with Microsoft 365 on every laptop in the Maison.

## Background

Buccellati commissioned a bespoke typeface from Typotheque (The Hague),
art-directed by Out There. Per Typotheque's Custom Fonts page: *"Commissioned
and art-directed by Out There, Typotheque created a bespoke typeface for
Buccellati. It is based on History 2, creating lower case set, and more
sophisticated set of capitals."* In designer Peter Biľak's 2010 Typotheque
article "The history of History," History layer 2 is described as *"a low
contrast model of letters with oblique stress."*

The wordmark on `buccellati.com` is delivered as an SVG (vector outline),
not live web type, so the bespoke face is reserved for identity assets.

## The PowerPoint type system

Two fonts ship as the theme. A third (Georgia) is used inside data tables
and charts. Every font listed in the fallback column ships with Microsoft
365 on Windows and Mac, so the deck renders correctly anywhere in the
Buccellati estate.

| Role                  | Primary (if licensed)      | Universal fallback                                         |
| --------------------- | -------------------------- | ---------------------------------------------------------- |
| Display / Cover       | Trajan Pro 3               | **Cormorant Garamond Light** → Garamond — small caps       |
| H1 / Section title    | Cormorant Garamond Light   | **Garamond** (Adobe, EB, or Microsoft Garamond)            |
| H2 / Slide title      | Cormorant Garamond Medium  | **Garamond Bold / Regular**                                |
| Eyebrow / Small caps  | Optima Bold tracked        | **Gill Sans MT Bold** — letter-spaced +200                 |
| Body                  | Optima Regular             | **Gill Sans MT** (Calibri Light as last resort)            |
| Caption / Footnote    | Optima Regular 9pt         | **Gill Sans MT 9pt** in Grafite                            |
| Data / numerals       | Cormorant Infant Tabular   | **Georgia** (tabular figures on, oldstyle off)             |

### Theme Fonts pair

Under **Slide Master → Fonts → Customize Fonts**, save the pair as
**"Buccellati Executive"**:

- **Headings font:** Garamond
- **Body font:** Gill Sans MT

## Type scale (16:9, 13.333" × 7.5")

| Level             | Size  | Weight        | Tracking | Leading | Notes                              |
| ----------------- | ----- | ------------- | -------- | ------- | ---------------------------------- |
| Display (Cover)   | 54 pt | Light         | +120     | 1.10    | All caps or small caps             |
| H1 Section        | 40 pt | Regular       | +60      | 1.15    | Title case                         |
| H2 Slide title    | 28 pt | Regular       | +40      | 1.20    | Sentence case                      |
| Eyebrow           | 9 pt  | Bold (sans)   | +200     | 1.00    | UPPERCASE, Oro Antico              |
| Body L            | 16 pt | Regular       | 0        | 1.40    | Statement slides                   |
| Body M (default)  | 14 pt | Regular       | 0        | 1.40    | Most content                       |
| Body S            | 12 pt | Regular       | 0        | 1.40    | Three-column body, table cells     |
| Caption           | 9 pt  | Regular       | +20      | 1.30    | Photo credits, source lines        |
| KPI numeral       | 64 pt | Light (serif) | 0        | 1.00    | 72pt where a single-column KPI fits |

### Setting rules

- **Default alignment:** left, ragged right. **Never justify** body text —
  justified copy creates rivers and reads corporate-default.
- **Numerical alignment:** right, with tabular figures.
- **Max line length:** body text never wider than 8 inches (~70 characters
  at 14pt Gill Sans).
- **Bold inside body text:** disallowed. Use small caps for emphasis.
- **Italic inside body text:** allowed but rare — reserve for one-line
  takeaways under chart titles and for descriptors under section titles.
- **Underline:** never. Use Oro Antico hyperlink colour for live links and
  let context do the work.

## Embedding & licensing

In PowerPoint: **File → Options → Save → Embed fonts in the file**

- **"Embed only the characters used in the presentation"** — smaller file,
  cannot edit downstream without the font installed.
- **"Embed all characters"** — larger file, fully editable downstream.
  Use this if the deck will be edited by a Richemont colleague who may
  not have your fonts.

Garamond, Georgia, Calibri, and Gill Sans MT are standard Microsoft 365
installs on both Windows and Mac and require **no embedding** — use them
as the default in the `.potx` to guarantee fidelity on any laptop.

> **The bespoke Buccellati typeface is licensed** and must not be embedded
> in files distributed outside the Maison without Typotheque licensing
> confirmation.

## What never happens to type

- Microsoft default fonts (Calibri, Aptos, Arial) as a display face
- All-caps headlines other than the Display style (use small caps instead)
- Drop shadows, glows, outline effects, gradient fills
- Faux bold or faux italic — use a real weight or stop
- Letter-spacing under -10 — never tighten serif body text
- Stretched / condensed type — set the right cut or stop
