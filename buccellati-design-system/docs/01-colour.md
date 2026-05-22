# 01 · Colour

> A monochrome ivory-and-black backbone with one regal blue and a warm matte
> gold. Restraint is the rule; saturated digital colour is the violation.

## The palette

### Primary — the always-on backbone

| Name              | Hex       | RGB             | Where it lives                                                                                          |
| ----------------- | --------- | --------------- | ------------------------------------------------------------------------------------------------------- |
| Avorio            | `#F5F1EA` | 245, 241, 234   | Default slide background. Warm off-white — **never** stark `#FFFFFF`.                                  |
| Nero Inchiostro   | `#1A1A1A` | 26, 26, 26      | Primary headline and body text. Softer than pure black — prints richer.                                |
| Pergamena         | `#EAE2D2` | 234, 226, 210   | Section-divider background. A muted alternate to Avorio for breathing-room slides.                     |

### Accent — used sparingly (one accent per slide, never two)

| Name              | Hex       | RGB             | Where it lives                                                                                          |
| ----------------- | --------- | --------------- | ------------------------------------------------------------------------------------------------------- |
| Blu Buccellati    | `#1B2A4E` | 27, 42, 78      | Cover / section / closing backgrounds. KPI highlight. Primary chart color. From the silk-box lining.   |
| Oro Antico        | `#A8894E` | 168, 137, 78    | Logo-printed-in-gold accent. Horizontal hairlines, section numbers, eyebrows. **Matte**, never shiny.  |
| Oro Chiaro        | `#C9A961` | 201, 169, 97    | Secondary gold for highlight states and chart secondary series.                                        |

### Neutrals — chart greys, dividers, table rules

| Name              | Hex       | RGB             | Where it lives                                                  |
| ----------------- | --------- | --------------- | --------------------------------------------------------------- |
| Grafite           | `#4A4A48` | 74, 74, 72      | Secondary body text, captions                                   |
| Cenere            | `#8A8A86` | 138, 138, 134   | Tertiary text, axis labels, footer copy                         |
| Lino              | `#D9D2C3` | 217, 210, 195   | Table row banding, soft fills                                   |
| Polvere           | `#BFB8A8` | 191, 184, 168   | Chart background series 2                                       |
| Blu Polvere       | `#7A8BA8` | 122, 139, 168   | A tint of Blu Buccellati for chart series 6                     |

## The chart series — use in this order, never out of sequence

1. **Blu Buccellati** `#1B2A4E` — primary series
2. **Oro Antico**    `#A8894E` — secondary
3. **Grafite**       `#4A4A48` — tertiary
4. **Cenere**        `#8A8A86` — quaternary
5. **Oro Chiaro**    `#C9A961` — highlight
6. **Blu Polvere**   `#7A8BA8` — sixth/final

> **Rule.** Positive / negative encoding uses **Oro Antico (positive) vs
> Grafite (negative)** — light vs dark. Never red / green. This keeps charts
> accessible to colour-blind viewers and consistent with the system's
> restraint.

## The PowerPoint Theme Colors panel — exact mapping

Configure under **Slide Master → Colors → Customize Colors** and save as
the named theme **"Buccellati Executive"**:

| Theme slot              | Color           | Hex       |
| ----------------------- | --------------- | --------- |
| Background 1 (Light 1)  | Avorio          | `#F5F1EA` |
| Text 1 (Dark 1)         | Nero Inchiostro | `#1A1A1A` |
| Background 2 (Light 2)  | Pergamena       | `#EAE2D2` |
| Text 2 (Dark 2)         | Blu Buccellati  | `#1B2A4E` |
| Accent 1                | Blu Buccellati  | `#1B2A4E` |
| Accent 2                | Oro Antico      | `#A8894E` |
| Accent 3                | Grafite         | `#4A4A48` |
| Accent 4                | Cenere          | `#8A8A86` |
| Accent 5                | Oro Chiaro      | `#C9A961` |
| Accent 6                | Blu Polvere     | `#7A8BA8` |
| Hyperlink               | Oro Antico      | `#A8894E` |
| Followed Hyperlink      | Grafite         | `#4A4A48` |

## Contrast & accessibility

| Pairing                         | Ratio    | WCAG    |
| ------------------------------- | -------- | ------- |
| Avorio on Nero Inchiostro       | 16.4 : 1 | AAA     |
| Avorio on Blu Buccellati        | 11.7 : 1 | AAA     |
| Nero Inchiostro on Avorio       | 16.4 : 1 | AAA     |
| Grafite on Avorio (body muted)  | 9.5 : 1  | AAA     |
| Cenere on Avorio (footer/axis)  | 3.6 : 1  | AA Large only — use 9pt+ for body |

## Forbidden colours

- Pure white `#FFFFFF` — use Avorio instead
- Pure black `#000000` — use Nero Inchiostro instead
- Saturated digital reds, greens, oranges, purples, teals — anywhere
- Microsoft 365 "Design Ideas" auto-palettes — disable

## Canonical source

The hex values live in [`tokens/tokens.json`](../tokens/tokens.json). CSS,
SCSS, and the Python generator all derive from there. **Change the token,
not the consumer.**
