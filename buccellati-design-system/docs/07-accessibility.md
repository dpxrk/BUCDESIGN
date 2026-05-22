# 07 · Accessibility & production quality

> Accessibility is not a finishing pass. It is baked into the colour
> system (contrast), the chart system (positive / negative encoding by
> lightness, not hue), and the master slides (titles, reading order,
> alt text).

## Contrast

| Pair                                | Ratio    | WCAG    |
| ----------------------------------- | -------- | ------- |
| Avorio on Nero Inchiostro           | 16.4 : 1 | AAA     |
| Avorio on Blu Buccellati            | 11.7 : 1 | AAA     |
| Nero Inchiostro on Avorio           | 16.4 : 1 | AAA     |
| Grafite on Avorio (muted body)      | 9.5 : 1  | AAA     |
| Cenere on Avorio (footer / axis)    | 3.6 : 1  | AA for 9pt+ only |
| Oro Antico on Avorio (eyebrow)      | 4.0 : 1  | AA Large, AAA Large |

All approved combinations exceed WCAG AA. Cenere `#8A8A86` on Avorio is
acceptable for footer copy and chart axis labels (9pt+ only) but is **not**
acceptable for body copy.

## Color independence

Charts use **Oro Antico (positive) vs Grafite (negative)** — light vs dark.
This is accessible to all forms of colour-blindness and to monochrome
print. Never encode positive / negative by red / green.

## Type sizing

- **Minimum body type:** 12pt. Most projectors at 8m viewing distance lose
  legibility below this.
- Footer / source citations at 8pt are acceptable because they are
  reference, not reading.

## Alt text

Every image, chart, and logo carries meaningful alt text. The AI prompt
generates one automatically for each `[IMAGE: …]` placeholder. A good
alt text describes the subject and what it conveys, not the file name.

**Good:** *"Bar chart showing revenue share by region: Americas 34%, EMEA
31%, Asia-Pacific 22%, Japan 8%, Middle East 5%. Americas leads."*

**Bad:** *"chart"* or *"slide-10.jpg"*

## Slide titles

Every slide has a title in the master's title placeholder. This is read
by screen readers and PowerPoint's outline view. **Do not use a textbox
instead of the title placeholder** — the screen reader will not find it.

## Reading order

Check via **Home → Arrange → Selection Pane**. Reading order proceeds top
→ bottom in the Selection Pane. Confirm that the title is read first, the
body copy second, and the footer last.

## Tables

- Mark the header row as a header row (Table Tools → Design → Header Row).
- Avoid merged cells — screen readers do not handle them gracefully.
- Right-align numerals; left-align labels. (Visual rule that also helps
  a non-sighted user understand cell semantics.)

## Hyperlinks

- Hyperlink colour is Oro Antico `#A8894E`, contrast ratio 4.0 : 1 on
  Avorio — meets AA for large text. Underline hyperlinks in body copy to
  satisfy AA for non-large text contrast independence.

## Animation & transitions

- **None by default.** No fade-throughs, no Morph between non-cover slides,
  no entrance / exit animations on bullet points.
- Cover and Section slides may use a single 0.5s fade transition in
  presentation mode, but never in print or PDF export.
- Animations are not accessibility violations per se, but the WCAG 2.1
  "Animation from Interactions" guideline is best satisfied by not
  introducing any.

## Production quality gate

Before any deck leaves a Buccellati office for the CEO or Richemont Group,
run:

- [ ] Spell-check across the whole deck
- [ ] **PowerPoint Accessibility Checker** (Review → Check Accessibility)
- [ ] Font-embedding pass (File → Options → Save → Embed fonts)
- [ ] Source-citation pass — every data slide has its source in 8pt Gill
      Sans Cenere at the lower-left above the footer
- [ ] The gut-check: *"Would this slide feel at home next to a Macri
      bracelet in a boutique window?"*
- [ ] Open the deck on a Windows machine *and* a Mac. Verify font fidelity
      on both. (Garamond's exact cut varies; this is why the system uses
      Garamond rather than Cormorant as the default fallback.)

## Languages

The PowerPoint defaults to British English ("Jewellery"). For decks
delivered in Italian, switch the proofing language at the slide-master
level (Review → Language → Set Proofing Language) before authoring so
spell-check works correctly throughout. The visual system is
language-agnostic; only the proofing dictionary changes.
