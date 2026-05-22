# Changelog

All notable changes to the Buccellati Executive Presentation Design System
will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-05-21

Initial release.

### Added

- **Canonical design tokens** at `tokens/tokens.json` (W3C Design Tokens spec).
  Single source of truth for all downstream consumers.
- **CSS variables** at `css/variables.css` (flat custom-property mirror) and
  the production stylesheet at `css/buccellati.css`.
- **Sass variables** at `scss/_variables.scss` for any SCSS-based consumers.
- **Sixteen named slide masters** spec'd in `docs/04-layouts.md`:
  Cover · Section · Agenda · Statement · Two-column · Three-column ·
  Image-led · Image+Text 60/40 · KPI · Chart · Table · Pull-quote · Team ·
  Timeline · Comparison · Closing.
- **Python `.potx` generator** at `powerpoint/generate_potx.py` using
  python-pptx. Produces both `Buccellati_Executive.potx` and a 16-slide
  sample `Buccellati_Sample.pptx`. Shadow / round-corner / gradient
  defaults are explicitly suppressed via XML-level cleanup of the
  `<p:style><a:effectRef/>` block.
- **Proprietary outline ornaments** in `assets/svg/`:
  - `honeycomb-tulle.svg` — 7-cell hex flower in Oro Antico
  - `rigato-rule.svg` — 40 vertical hairlines forming a 1.5" band
  - `b-monogram.svg` — footer mark for content slides
  - `since-1919.svg` — cover / closing lockup
  - `wordmark-placeholder.svg` — tracked-caps stand-in (replace with
    licensed mark for production)
- **Eight long-form guideline documents** in `docs/`:
  01 Colour · 02 Typography · 03 Imagery · 04 Layouts · 05 Motifs &
  logo · 06 Voice & tone · 07 Accessibility · 08 Do's & Don'ts.
- **Three AI prompts** in `ai-prompts/`:
  - `system-prompt.md` — long-form briefing for Claude / ChatGPT / Gemini
  - `quick-prompt.md` — short single-message version
  - `slide-recipes.md` — one recipe per layout, sixteen in total
- **HTML preview** at `examples/preview.html` — a single-file demo of the
  full system that renders in the browser using `css/buccellati.css`.

### Design decisions

- **Avorio `#F5F1EA` over `#FFFFFF`, Nero Inchiostro `#1A1A1A` over `#000000`**
  — warmer, prints richer, reads luxury rather than digital.
- **Garamond / Gill Sans MT / Georgia** stack as the safe production
  default — every font ships with Microsoft 365 on both Windows and Mac.
- **Equal-spaced timeline milestones** rather than chronologically scaled
  — editorial convention; respects each event's weight and prevents
  label collision when dates cluster (e.g. 1919, 1925, 1929).
- **Oro Antico vs Grafite for positive / negative encoding** — light vs
  dark, accessible to all forms of colour-blindness, never red / green.
- **Em-dash bullets in Oro Antico** rather than round dots — quieter, more
  editorial, in keeping with the Maison's restraint.

### Caveats codified in `README.md`

- Hex values for Blu Buccellati and Oro Antico are derived approximations
  from publicly observable assets; replace with official values when
  available.
- Bespoke Typotheque Buccellati typeface is licensed; the Garamond / Gill
  Sans / Georgia stack is the production-safe fallback.
- The 1951 vs 1954 New York opening conflict is preserved — uses 1951
  until heritage team confirms.
- Richemont co-branding follows separate Richemont group standards.
- The wordmark SVG in the repo is a tracked-caps placeholder; replace
  with the official mark before any external-facing use.

[1.0.0]: https://github.com/buccellati/buccellati-design-system/releases/tag/v1.0.0
