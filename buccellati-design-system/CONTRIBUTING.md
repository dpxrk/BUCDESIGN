# Contributing

Thank you for your interest in improving the Buccellati Executive
Presentation Design System. This is a small, careful repository — most
contributions are token tweaks, layout refinements, and prompt iterations.

## How to propose a change

1. Open an issue first. Describe what you'd like to change and why.
   For visual changes, attach a before/after mock.
2. Branch from `main` using a short kebab-case name:
   `fix/kpi-numeral-overflow`, `docs/clarify-trajan-licensing`, etc.
3. Make your change. **If you touch a token value, you touch it in
   `tokens/tokens.json` only** — do not edit derived CSS / SCSS / Python
   directly. The CI workflow regenerates derived files on push.
4. Run the local checks (below).
5. Open a pull request describing the change, the rationale, and any
   visual evidence.

## Local checks

```bash
# Regenerate the .potx and sample .pptx
cd powerpoint
pip install -r requirements.txt
python generate_potx.py

# Verify the .pptx renders without theme defaults intruding
soffice --headless --convert-to pdf out/Buccellati_Sample.pptx
# (optional) eyeball page 1 to confirm shadow / gradient / round-corner
# defaults are still suppressed
```

## What we accept

- Bug fixes (a slide master that misaligns, a shadow that escapes the
  suppression pass, a font-fallback that breaks on Mac)
- New layouts, *only* if they fit the existing 16-master architecture and
  do not duplicate an existing layout
- Documentation clarifications, especially historical / heritage details
  the Maison's archive team can confirm
- Improvements to the AI prompts that yield more reliably compliant decks
- Localisation (Italian, French — translation of titles and eyebrow copy
  in the sample deck)

## What we don't accept

- New colors outside the documented palette
- New fonts beyond the Garamond / Gill Sans MT / Georgia stack
- Decorative motifs beyond the existing ornament vocabulary
- "Bold" or "modernized" reinterpretations of the system. Restraint is
  the design — the Maison is quieter than its content.
- Co-branding lockups with Richemont or any other Maison. Those are
  governed by Richemont group brand standards, not this document.

## Style of writing in documentation

The docs themselves follow the system's voice:

- Sentence-case headings
- Declarative statements, no exclamation marks
- Italian-articulate where natural; English everywhere else
- British "Jewellery" spelling
- Specific examples over abstractions

When in doubt, write less.

## Versioning

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html):

- **Patch** (`1.0.x`) — typo fixes, doc clarifications, internal generator
  refactors that don't change output
- **Minor** (`1.x.0`) — new layouts, new ornaments, additive token entries
- **Major** (`x.0.0`) — token renames, palette changes, breaking changes
  to the `.potx` structure or the AI prompts

Update `CHANGELOG.md` in every pull request.

## Code of conduct

Be respectful, be specific, and be quiet. The Maison's tone is the
project's tone.
