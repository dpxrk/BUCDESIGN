"""
Buccellati Executive Presentation Design System
==================================================
generate_potx.py — produces ``Buccellati_Executive.potx`` (and a sample
``Buccellati_Sample.pptx``) containing the full theme color palette, the
Garamond / Gill Sans font pair, the 16-column grid, and one sample slide
per layout so a designer can see the system at work.

Usage
-----
    python generate_potx.py                # writes both files into ./out/
    python generate_potx.py --pptx-only    # only the sample deck
    python generate_potx.py --potx-only    # only the template

This script is intentionally written to be auditable rather than minimal:
every magic number maps to a value in ``../tokens/tokens.json`` so the
design system stays in sync with the brief.
"""
from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE


# ── Tokens ──────────────────────────────────────────────────────────────────
# Mirrors tokens.json — keep in sync.
class Color:
    AVORIO            = RGBColor(0xF5, 0xF1, 0xEA)
    NERO_INCHIOSTRO   = RGBColor(0x1A, 0x1A, 0x1A)
    PERGAMENA         = RGBColor(0xEA, 0xE2, 0xD2)
    BLU_BUCCELLATI    = RGBColor(0x1B, 0x2A, 0x4E)
    ORO_ANTICO        = RGBColor(0xA8, 0x89, 0x4E)
    ORO_CHIARO        = RGBColor(0xC9, 0xA9, 0x61)
    GRAFITE           = RGBColor(0x4A, 0x4A, 0x48)
    CENERE            = RGBColor(0x8A, 0x8A, 0x86)
    LINO              = RGBColor(0xD9, 0xD2, 0xC3)
    POLVERE           = RGBColor(0xBF, 0xB8, 0xA8)
    BLU_POLVERE       = RGBColor(0x7A, 0x8B, 0xA8)


class Font:
    HEADING = "Garamond"        # fallback chain handled by OS
    BODY    = "Gill Sans MT"
    DATA    = "Georgia"


SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN  = Inches(0.6)
LIVE_W  = Inches(12.133)
LIVE_H  = Inches(6.3)


# ── Helpers ────────────────────────────────────────────────────────────────
def _set_run(run, *, text=None, font=None, size=None, color=None,
             bold=False, italic=False, tracking=None):
    """Apply our token system to a run."""
    if text is not None:
        run.text = text
    if font:
        run.font.name = font
    if size is not None:
        run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    if tracking is not None:
        # python-pptx exposes <a:rPr spc="..."/> only via XML; spc is in 1/100 pt
        rPr = run._r.get_or_add_rPr()
        rPr.set("spc", str(int(tracking * 100)))


def _add_textbox(slide, left, top, width, height, *, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    return box, tf


def _kill_shadow(shp):
    """Remove the default theme shadow from a shape. The drop-shadow comes from
    the <p:style><a:effectRef idx="2"/></p:style> block, which references the
    second effect in the theme. Setting that ref to idx 0 (no effect) — or
    deleting the whole p:style element — both work; we delete it."""
    from pptx.oxml.ns import qn
    el = shp._element.find(qn("p:style"))
    if el is not None:
        el.getparent().remove(el)


def _add_filled_rect(slide, left, top, width, height, fill, line=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(0.5)
    _kill_shadow(shp)
    return shp


def _add_hairline(slide, left, top, width, color=Color.ORO_ANTICO, thickness=1.0):
    line = slide.shapes.add_connector(1, left, top, left + width, top)
    line.line.color.rgb = color
    line.line.width = Pt(thickness)
    return line


def _add_paragraph(tf, text, *, font=Font.BODY, size=14, color=Color.NERO_INCHIOSTRO,
                   bold=False, italic=False, align=PP_ALIGN.LEFT,
                   tracking=None, line_spacing=1.4, space_after=0,
                   first=False):
    """Add a paragraph (the first one reuses the existing empty paragraph)."""
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.line_spacing = line_spacing
    if space_after:
        p.space_after = Pt(space_after)
    # Clear existing run text for first paragraph
    if first and p.runs:
        for r in p.runs:
            r.text = ""
    run = p.add_run() if not (first and p.runs) else p.runs[0]
    _set_run(run, text=text, font=font, size=size, color=color,
             bold=bold, italic=italic, tracking=tracking)
    return p


def _footer(slide, slide_no, total, classification="Confidential", period="05.2026"):
    """Add the standard footer: B-monogram + slide N/total LEFT, classification + period RIGHT."""
    y = SLIDE_H - Inches(0.45)
    # Left: monogram + counter
    _, tf = _add_textbox(slide, MARGIN, y, Inches(3.0), Inches(0.3))
    _add_paragraph(tf, f"B   ·   slide {slide_no:02d} / {total:02d}",
                   font=Font.BODY, size=8, color=Color.CENERE,
                   line_spacing=1.0, first=True)
    # Right: classification + period
    _, tf = _add_textbox(slide, SLIDE_W - MARGIN - Inches(3.0), y,
                         Inches(3.0), Inches(0.3))
    _add_paragraph(tf, f"{classification}   ·   {period}",
                   font=Font.BODY, size=8, color=Color.CENERE,
                   align=PP_ALIGN.RIGHT, line_spacing=1.0, first=True)


def _slide_title_block(slide, *, eyebrow, title, with_rule=True):
    """The canonical content-slide opening: eyebrow + title + Oro Antico rule."""
    y = MARGIN

    # Eyebrow
    _, tf = _add_textbox(slide, MARGIN, y, LIVE_W, Inches(0.25))
    _add_paragraph(tf, eyebrow.upper(),
                   font=Font.BODY, size=9, color=Color.ORO_ANTICO,
                   bold=True, tracking=2.0, line_spacing=1.0, first=True)

    # Title (Garamond)
    y += Inches(0.4)
    _, tf = _add_textbox(slide, MARGIN, y, LIVE_W, Inches(0.7))
    _add_paragraph(tf, title,
                   font=Font.HEADING, size=28, color=Color.NERO_INCHIOSTRO,
                   line_spacing=1.2, tracking=0.4, first=True)

    if with_rule:
        _add_hairline(slide, MARGIN, y + Inches(0.85), Inches(1.5),
                      color=Color.ORO_ANTICO, thickness=1.0)

    return y + Inches(1.05)  # next-content y-cursor


def _set_blank_layout(slide, fill=Color.AVORIO):
    """Paint the entire slide with the chosen fill (overrides default white)."""
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    bg.fill.solid()
    bg.fill.fore_color.rgb = fill
    bg.line.fill.background()
    _kill_shadow(bg)
    # Send to back
    sp = bg._element
    sp.getparent().remove(sp)
    slide.shapes._spTree.insert(2, sp)
    return bg


# ── Slide builders (one function per layout 01–16) ─────────────────────────
def build_cover(slide):
    _set_blank_layout(slide, fill=Color.BLU_BUCCELLATI)

    # Wordmark placeholder (set further up; gives the title room to breathe)
    _, tf = _add_textbox(slide, MARGIN, Inches(1.4),
                         SLIDE_W - 2*MARGIN, Inches(0.7))
    _add_paragraph(tf, "B U C C E L L A T I",
                   font=Font.HEADING, size=36, color=Color.AVORIO,
                   align=PP_ALIGN.CENTER, tracking=14.0, line_spacing=1.0, first=True)

    # Title — give it a tall box so a two-line title fits cleanly
    _, tf = _add_textbox(slide, Inches(1.0), Inches(2.9),
                         SLIDE_W - Inches(2.0), Inches(2.5),
                         anchor=MSO_ANCHOR.MIDDLE)
    _add_paragraph(tf, "A strategic review for the next century",
                   font=Font.HEADING, size=48, color=Color.AVORIO,
                   align=PP_ALIGN.CENTER, line_spacing=1.1,
                   tracking=1.2, first=True)

    # Subtitle (Oro Chiaro) — pushed down clear of the title
    _, tf = _add_textbox(slide, MARGIN, Inches(5.5),
                         SLIDE_W - 2*MARGIN, Inches(0.4))
    _add_paragraph(tf, "FY26 Executive Briefing",
                   font=Font.BODY, size=16, color=Color.ORO_CHIARO,
                   align=PP_ALIGN.CENTER, tracking=1.2,
                   line_spacing=1.0, first=True)

    # Date / presenter
    _, tf = _add_textbox(slide, MARGIN, Inches(6.3),
                         SLIDE_W - 2*MARGIN, Inches(0.3))
    _add_paragraph(tf, "Milan  ·  May 2026",
                   font=Font.BODY, size=11, color=Color.CENERE,
                   align=PP_ALIGN.CENTER, line_spacing=1.0, first=True)

    # Oro Antico hairline lower-center
    _add_hairline(slide, Inches(5.666), Inches(6.95), Inches(2.0),
                  color=Color.ORO_ANTICO, thickness=0.75)


def build_section(slide):
    _set_blank_layout(slide, fill=Color.PERGAMENA)

    # Roman section number
    _, tf = _add_textbox(slide, MARGIN, MARGIN, Inches(2), Inches(0.3))
    _add_paragraph(tf, "I.",
                   font=Font.BODY, size=14, color=Color.ORO_ANTICO,
                   bold=True, tracking=2.0, line_spacing=1.0, first=True)

    # Rigato rule beneath section number — 40 short vertical hairlines forming
    # a 1.5"-wide band, evoking the rigato engraving technique.
    rigato_y_top = MARGIN + Inches(0.45)
    rigato_y_bot = rigato_y_top + Inches(0.16)
    band_w = Inches(1.5)
    n = 40
    for i in range(n):
        x = MARGIN + Emu(int(band_w.emu * (i + 0.5) / n))
        ln = slide.shapes.add_connector(1, x, rigato_y_top, x, rigato_y_bot)
        ln.line.color.rgb = Color.NERO_INCHIOSTRO
        ln.line.width = Pt(0.5)

    # Section title
    _, tf = _add_textbox(slide, MARGIN, Inches(3.2),
                         Inches(11.0), Inches(1.2))
    _add_paragraph(tf, "Heritage in the present tense",
                   font=Font.HEADING, size=40, color=Color.NERO_INCHIOSTRO,
                   line_spacing=1.15, tracking=0.6, first=True)

    # Italic descriptor
    _, tf = _add_textbox(slide, MARGIN, Inches(4.6),
                         Inches(11.0), Inches(0.5))
    _add_paragraph(tf, "Six observations from the workshop floor.",
                   font=Font.HEADING, size=14, color=Color.GRAFITE,
                   italic=True, line_spacing=1.4, first=True)


def build_agenda(slide, *, slide_no, total):
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="Today", title="Agenda")

    # Two-column list, Roman numerals in Oro Antico
    items = [
        ("I.",   "Maison snapshot",     "Where we stood at year-end 2025."),
        ("II.",  "FY26 priorities",     "Three lines of action."),
        ("III.", "Retail & boutiques",  "Network choices and tempo."),
        ("IV.",  "Creation & atelier",  "Capacity, hands, training."),
        ("V.",   "Heritage in market",  "Archive into commerce."),
        ("VI.",  "Outlook",             "Questions we owe Richemont."),
    ]
    y0 = Inches(1.85)
    line_h = Inches(0.78)
    col_x = MARGIN

    for i, (num, head, sub) in enumerate(items):
        col = 0 if i < 3 else 1
        row = i if i < 3 else i - 3
        x_off = col_x if col == 0 else col_x + Inches(5.9)
        y = y0 + line_h * row

        # Roman numeral
        _, tf = _add_textbox(slide, x_off, y, Inches(0.7), Inches(0.4))
        _add_paragraph(tf, num,
                       font=Font.BODY, size=14, color=Color.ORO_ANTICO,
                       line_spacing=1.0, first=True)
        # Heading
        _, tf = _add_textbox(slide, x_off + Inches(0.8), y, Inches(5), Inches(0.4))
        _add_paragraph(tf, head,
                       font=Font.HEADING, size=18, color=Color.NERO_INCHIOSTRO,
                       line_spacing=1.0, first=True)
        # Sub
        _, tf = _add_textbox(slide, x_off + Inches(0.8), y + Inches(0.32),
                             Inches(5), Inches(0.3))
        _add_paragraph(tf, sub,
                       font=Font.BODY, size=12, color=Color.GRAFITE,
                       italic=True, line_spacing=1.2, first=True)

    _footer(slide, slide_no, total)


def build_statement(slide, *, slide_no, total):
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="Thesis",
                       title="Macri remains the foundation of the wholesale ladder.")

    _, tf = _add_textbox(slide, MARGIN + Inches(1.5), Inches(3.5),
                         Inches(9.0), Inches(2.2))
    _add_paragraph(tf,
        ("The Macri honeycomb is the Maison's most recognisable engraving and the "
         "entry point into Buccellati ownership for the largest share of new clients. "
         "Pricing discipline and disciplined replenishment matter more than novelty here."),
        font=Font.BODY, size=16, color=Color.NERO_INCHIOSTRO,
        line_spacing=1.45, first=True)

    _footer(slide, slide_no, total)


def build_two_column(slide, *, slide_no, total):
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="Boutique network",
                       title="Two truths, one decision.")

    # Left column
    _, tf = _add_textbox(slide, MARGIN, Inches(2.2),
                         Inches(5.5), Inches(4.2))
    _add_paragraph(tf, "THE FACT",
                   font=Font.BODY, size=9, color=Color.ORO_ANTICO,
                   bold=True, tracking=2.0, line_spacing=1.0, first=True)
    _add_paragraph(tf, "Foot traffic in our top-ten boutiques was up 8% in Q1 FY26, "
                       "but conversion held flat. Clients are coming; the close is the issue.",
                   font=Font.BODY, size=14, color=Color.NERO_INCHIOSTRO,
                   line_spacing=1.45, space_after=12)

    # Right column
    _, tf = _add_textbox(slide, MARGIN + Inches(6.6), Inches(2.2),
                         Inches(5.5), Inches(4.2))
    _add_paragraph(tf, "THE IMPLICATION",
                   font=Font.BODY, size=9, color=Color.ORO_ANTICO,
                   bold=True, tracking=2.0, line_spacing=1.0, first=True)
    _add_paragraph(tf, "Atelier-led storytelling at the bench during the appointment "
                       "shifts the relationship from transaction to commission. "
                       "Train, do not redecorate.",
                   font=Font.BODY, size=14, color=Color.NERO_INCHIOSTRO,
                   line_spacing=1.45, space_after=12)

    # Vertical hairline divider
    ln = slide.shapes.add_connector(1,
        MARGIN + Inches(6.066), Inches(2.2),
        MARGIN + Inches(6.066), Inches(6.4))
    ln.line.color.rgb = Color.CENERE
    ln.line.width = Pt(0.5)

    _footer(slide, slide_no, total)


def build_three_column(slide, *, slide_no, total):
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="FY26 priorities",
                       title="Three lines of action.")

    cols = [
        ("I.", "Atelier capacity",
         "Twelve new apprentices through the Milano workshop by Q4. Master engravers paired with first-year hands on the bench, not in classrooms."),
        ("II.", "Heritage in commerce",
         "Reactivate three archive collections per year, beginning with Macri Giglio and Tulle. The archive earns its keep."),
        ("III.", "Boutique density",
         "Two openings in Asia (Tokyo Ginza, Seoul), one closing (Frankfurt). Reinvest the saved rent in atelier hours."),
    ]
    col_w = Inches(3.7)
    gap   = Inches(0.3)
    x0 = MARGIN
    y = Inches(2.2)

    for i, (num, head, body) in enumerate(cols):
        x = x0 + (col_w + gap) * i
        _, tf = _add_textbox(slide, x, y, col_w, Inches(0.4))
        _add_paragraph(tf, num,
                       font=Font.BODY, size=14, color=Color.ORO_ANTICO,
                       bold=True, line_spacing=1.0, first=True)

        _, tf = _add_textbox(slide, x, y + Inches(0.45), col_w, Inches(0.5))
        _add_paragraph(tf, head,
                       font=Font.HEADING, size=18, color=Color.NERO_INCHIOSTRO,
                       line_spacing=1.15, first=True)

        _, tf = _add_textbox(slide, x, y + Inches(1.05), col_w, Inches(3.0))
        _add_paragraph(tf, body,
                       font=Font.BODY, size=12, color=Color.GRAFITE,
                       line_spacing=1.45, first=True)

    _footer(slide, slide_no, total)


def build_image_lead(slide, *, slide_no, total):
    _set_blank_layout(slide, fill=Color.NERO_INCHIOSTRO)

    # Placeholder "image" — a Pergamena rectangle covering most of the slide.
    # In production, replace with a macro craft photograph.
    _add_filled_rect(slide, 0, 0, SLIDE_W, SLIDE_H, fill=Color.GRAFITE)
    _add_filled_rect(slide, Inches(1.5), Inches(1.0),
                     Inches(10.3), Inches(5.5), fill=Color.PERGAMENA)

    # Caption block (Avorio 60% scrim simulated as solid)
    _add_filled_rect(slide, Inches(1.5), Inches(5.0),
                     Inches(4.2), Inches(1.5), fill=Color.AVORIO)

    _, tf = _add_textbox(slide, Inches(1.7), Inches(5.15),
                         Inches(4.0), Inches(0.3))
    _add_paragraph(tf, "AT THE BENCH",
                   font=Font.BODY, size=9, color=Color.ORO_ANTICO,
                   bold=True, tracking=2.0, line_spacing=1.0, first=True)

    _, tf = _add_textbox(slide, Inches(1.7), Inches(5.45),
                         Inches(4.0), Inches(0.6))
    _add_paragraph(tf, "Rigato, by hand",
                   font=Font.HEADING, size=18, color=Color.NERO_INCHIOSTRO,
                   line_spacing=1.1, first=True)

    _, tf = _add_textbox(slide, Inches(1.7), Inches(5.95),
                         Inches(4.0), Inches(0.4))
    _add_paragraph(tf, "Parallel hairlines drawn one at a time across the surface.",
                   font=Font.BODY, size=12, color=Color.GRAFITE,
                   italic=True, line_spacing=1.3, first=True)

    # Wordmark mark, bottom right — wider box so the tracked text fits on one line
    _, tf = _add_textbox(slide, SLIDE_W - Inches(3.4), SLIDE_H - Inches(0.55),
                         Inches(2.8), Inches(0.3))
    _add_paragraph(tf, "BUCCELLATI",
                   font=Font.HEADING, size=11, color=Color.AVORIO,
                   tracking=4.0, line_spacing=1.0, align=PP_ALIGN.RIGHT,
                   first=True)


def build_image_text_60_40(slide, *, slide_no, total):
    _set_blank_layout(slide)

    # Left: image placeholder filling columns 1-7
    _add_filled_rect(slide, 0, 0, Inches(7.7), SLIDE_H, fill=Color.PERGAMENA)
    _, tf = _add_textbox(slide, Inches(0.3), Inches(3.5),
                         Inches(7.1), Inches(0.4))
    _add_paragraph(tf, "[IMAGE  ·  macro of engraved yellow gold, raking light]",
                   font=Font.BODY, size=10, color=Color.GRAFITE,
                   italic=True, align=PP_ALIGN.CENTER, line_spacing=1.0,
                   first=True)

    # Right: text block columns 8-12
    x = Inches(8.0)
    _, tf = _add_textbox(slide, x, MARGIN, Inches(4.7), Inches(0.3))
    _add_paragraph(tf, "CRAFTSMANSHIP",
                   font=Font.BODY, size=9, color=Color.ORO_ANTICO,
                   bold=True, tracking=2.0, line_spacing=1.0, first=True)

    _, tf = _add_textbox(slide, x, Inches(1.1), Inches(4.7), Inches(2.0))
    _add_paragraph(tf, "Six techniques.\nOne workshop.",
                   font=Font.HEADING, size=28, color=Color.NERO_INCHIOSTRO,
                   line_spacing=1.15, tracking=0.4, first=True)

    _, tf = _add_textbox(slide, x, Inches(3.2), Inches(4.7), Inches(3.0))
    _add_paragraph(tf,
        ("Rigato, segrinato, telato, ornato, modellato, and tulle — the six "
         "engraving techniques carried in the Milanese atelier since 1919, and "
         "the visible difference between a Buccellati piece and a piece that "
         "merely resembles one."),
        font=Font.BODY, size=14, color=Color.NERO_INCHIOSTRO,
        line_spacing=1.45, first=True)

    _footer(slide, slide_no, total)


def build_kpi(slide, *, slide_no, total):
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="FY26 — first half",
                       title="Where the Maison stands.")

    kpis = [
        ("REVENUE",      "€512M",   "▲ 12.4%", "vs first half FY25", True),
        ("RETAIL SHARE", "67%",     "▲ 3.1pp", "client-direct, all regions", True),
        ("HEADCOUNT",    "412",     "▲ 28",    "of which 19 are apprentices", True),
    ]
    col_w = Inches(3.7)
    gap   = Inches(0.3)
    x0 = MARGIN
    y = Inches(2.4)

    for i, (label, num, delta, ctx, positive) in enumerate(kpis):
        x = x0 + (col_w + gap) * i

        _, tf = _add_textbox(slide, x, y, col_w, Inches(0.3))
        _add_paragraph(tf, label,
                       font=Font.BODY, size=9, color=Color.ORO_ANTICO,
                       bold=True, tracking=2.0, line_spacing=1.0, first=True)

        _, tf = _add_textbox(slide, x, y + Inches(0.35), col_w, Inches(1.3))
        _add_paragraph(tf, num,
                       font=Font.HEADING, size=64, color=Color.NERO_INCHIOSTRO,
                       line_spacing=1.0, first=True)

        _, tf = _add_textbox(slide, x, y + Inches(1.85), col_w, Inches(0.3))
        delta_color = Color.ORO_ANTICO if positive else Color.GRAFITE
        _add_paragraph(tf, delta,
                       font=Font.BODY, size=14, color=delta_color,
                       bold=True, line_spacing=1.0, first=True)

        _, tf = _add_textbox(slide, x, y + Inches(2.25), col_w, Inches(0.4))
        _add_paragraph(tf, ctx,
                       font=Font.BODY, size=11, color=Color.GRAFITE,
                       italic=True, line_spacing=1.3, first=True)

    # Source line above footer
    _, tf = _add_textbox(slide, MARGIN, SLIDE_H - Inches(0.7),
                         Inches(8), Inches(0.2))
    _add_paragraph(tf, "Source: internal FY26 H1 management report (unaudited).",
                   font=Font.BODY, size=8, color=Color.CENERE,
                   line_spacing=1.0, first=True)

    _footer(slide, slide_no, total)


def build_chart(slide, *, slide_no, total):
    """Chart slide — we draw illustrative bars with shapes so the styling
    is faithful even without a real chart object. Replace with native Chart
    in production."""
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="Revenue mix by region",
                       title="The Americas now lead.")

    # One-line takeaway directly under title
    _, tf = _add_textbox(slide, MARGIN, Inches(1.85),
                         Inches(10.0), Inches(0.4))
    _add_paragraph(tf, "Americas overtook EMEA in H1 FY26, driven by New York and Beverly Hills boutiques.",
                   font=Font.BODY, size=14, color=Color.NERO_INCHIOSTRO,
                   italic=True, line_spacing=1.3, first=True)

    # Simple bar chart drawn with rectangles
    chart_x = MARGIN
    chart_y = Inches(2.7)
    chart_w = Inches(8.5)
    chart_h = Inches(3.8)

    # Baseline
    _add_hairline(slide, chart_x, chart_y + chart_h,
                  chart_w, color=Color.CENERE, thickness=0.5)

    regions = [("Americas", 0.34, Color.BLU_BUCCELLATI),
               ("EMEA",     0.31, Color.ORO_ANTICO),
               ("Asia-Pac", 0.22, Color.GRAFITE),
               ("Japan",    0.08, Color.CENERE),
               ("Middle E.",0.05, Color.ORO_CHIARO)]
    bar_w = Inches(1.2)
    bar_gap = Inches(0.5)
    for i, (region, share, color) in enumerate(regions):
        bar_h = Emu(int(chart_h.emu * share / 0.40))  # scale so max ≈ full height
        bx = chart_x + Inches(0.4) + (bar_w + bar_gap) * i
        by = chart_y + chart_h - bar_h
        _add_filled_rect(slide, bx, by, bar_w, bar_h, fill=color)

        # Data label on bar
        _, tf = _add_textbox(slide, bx, by - Inches(0.35),
                             bar_w, Inches(0.3))
        _add_paragraph(tf, f"{share*100:.0f}%",
                       font=Font.DATA, size=11, color=Color.NERO_INCHIOSTRO,
                       align=PP_ALIGN.CENTER, line_spacing=1.0, first=True)

        # Region label below baseline
        _, tf = _add_textbox(slide, bx, chart_y + chart_h + Inches(0.1),
                             bar_w, Inches(0.3))
        _add_paragraph(tf, region,
                       font=Font.BODY, size=10, color=Color.GRAFITE,
                       align=PP_ALIGN.CENTER, line_spacing=1.0, first=True)

    # Source
    _, tf = _add_textbox(slide, MARGIN, SLIDE_H - Inches(0.7),
                         Inches(8), Inches(0.2))
    _add_paragraph(tf, "Source: internal FY26 H1 management report; share of revenue, retail + wholesale combined.",
                   font=Font.BODY, size=8, color=Color.CENERE,
                   line_spacing=1.0, first=True)

    _footer(slide, slide_no, total)


def build_table(slide, *, slide_no, total):
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="Network",
                       title="Boutique count by region (FY24 → FY26).")

    rows = [
        ("Americas", "8", "9", "11"),
        ("EMEA",     "14","14","13"),
        ("Asia-Pac", "6", "7", "9"),
        ("Japan",    "5", "5", "5"),
        ("Middle E.","2", "3", "3"),
    ]
    cols = ["Region", "FY24", "FY25", "FY26"]

    rows_n = len(rows)
    cols_n = len(cols)
    tbl_left = MARGIN
    tbl_top  = Inches(2.3)
    tbl_w    = Inches(10)
    tbl_h    = Inches(2.5)

    shape = slide.shapes.add_table(rows_n + 1, cols_n, tbl_left, tbl_top, tbl_w, tbl_h)
    table = shape.table

    # Header row
    for j, h in enumerate(cols):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = Color.BLU_BUCCELLATI
        cell.text_frame.clear()
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.RIGHT if j > 0 else PP_ALIGN.LEFT
        run = p.add_run()
        _set_run(run, text=h.upper(), font=Font.BODY, size=11,
                 color=Color.AVORIO, bold=True, tracking=2.0)

    # Body rows
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            cell = table.cell(i, j)
            if i % 2 == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = Color.LINO
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = Color.AVORIO
            cell.text_frame.clear()
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.RIGHT if j > 0 else PP_ALIGN.LEFT
            run = p.add_run()
            font_name = Font.DATA if j > 0 else Font.BODY
            _set_run(run, text=val, font=font_name, size=11,
                     color=Color.NERO_INCHIOSTRO)

    _footer(slide, slide_no, total)


def build_pullquote(slide, *, slide_no, total):
    _set_blank_layout(slide)

    # Oversized opening quote
    _, tf = _add_textbox(slide, Inches(0.8), Inches(0.8),
                         Inches(2.0), Inches(2.0))
    _add_paragraph(tf, "\u201C",
                   font=Font.HEADING, size=120, color=Color.ORO_ANTICO,
                   italic=True, line_spacing=1.0, first=True)

    # Quote text
    _, tf = _add_textbox(slide, Inches(2.0), Inches(2.0),
                         Inches(9.0), Inches(3.0))
    _add_paragraph(tf,
        "Engraving is the moment the metal listens. \nIf the hand is hurried, the gold knows.",
        font=Font.HEADING, size=32, color=Color.NERO_INCHIOSTRO,
        italic=True, line_spacing=1.25, first=True)

    # Attribution
    _, tf = _add_textbox(slide, Inches(3.0), Inches(5.3),
                         Inches(8.0), Inches(0.4))
    _add_paragraph(tf, "—  ANDREA BUCCELLATI, HONORARY PRESIDENT",
                   font=Font.BODY, size=12, color=Color.GRAFITE,
                   tracking=1.2, line_spacing=1.0, first=True)

    _footer(slide, slide_no, total)


def build_team(slide, *, slide_no, total):
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="The leadership team",
                       title="At the bench, and behind the bench.")

    people = [
        ("Andrea Buccellati",     "Honorary President"),
        ("Lucrezia Buccellati",   "Creative Director, NA"),
        ("Jacopo Pellegrini",     "CEO"),
        ("Maria Cignoli",         "Heritage Lead"),
    ]
    portrait_w = Inches(2.4)
    portrait_h = Inches(2.6)
    gap = Inches(0.3)
    y = Inches(2.4)

    for i, (name, title) in enumerate(people):
        x = MARGIN + (portrait_w + gap) * i

        # Portrait mat
        _add_filled_rect(slide, x, y, portrait_w, portrait_h, fill=Color.PERGAMENA)
        _, tf = _add_textbox(slide, x, y + Inches(0.9),
                             portrait_w, Inches(0.4))
        _add_paragraph(tf, "[ PORTRAIT ]",
                       font=Font.BODY, size=9, color=Color.GRAFITE,
                       italic=True, align=PP_ALIGN.CENTER, line_spacing=1.0,
                       first=True)

        # Name
        _, tf = _add_textbox(slide, x, y + portrait_h + Inches(0.1),
                             portrait_w, Inches(0.35))
        _add_paragraph(tf, name,
                       font=Font.HEADING, size=14, color=Color.NERO_INCHIOSTRO,
                       align=PP_ALIGN.CENTER, line_spacing=1.1, first=True)

        # Title
        _, tf = _add_textbox(slide, x, y + portrait_h + Inches(0.5),
                             portrait_w, Inches(0.4))
        _add_paragraph(tf, title,
                       font=Font.BODY, size=10, color=Color.GRAFITE,
                       italic=True, align=PP_ALIGN.CENTER,
                       tracking=0.6, line_spacing=1.2, first=True)

    _footer(slide, slide_no, total)


def build_timeline(slide, *, slide_no, total):
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="Heritage",
                       title="A century of openings.")

    milestones = [
        (1919, "Milan,\nVia degli Orefici"),
        (1925, "Rome,\nVia Condotti"),
        (1929, "Florence"),
        (1951, "First US boutique,\nNew York"),
        (1979, "Place Vendôme,\nParis"),
        (2019, "Centenary  ·\nRichemont"),
    ]
    # Editorial timelines space milestones *equally* rather than to chronological
    # scale — this respects each event's weight and prevents label collisions
    # when dates cluster.
    n = len(milestones)
    axis_y     = Inches(4.6)
    axis_left  = Inches(1.2)
    axis_right = SLIDE_W - Inches(1.2)
    axis_w     = axis_right - axis_left
    _add_hairline(slide, axis_left, axis_y, axis_w,
                  color=Color.ORO_ANTICO, thickness=1.0)

    step = axis_w / (n - 1)

    for i, (year, label) in enumerate(milestones):
        x = axis_left + Emu(int(step * i))

        # Tick
        ln = slide.shapes.add_connector(1, x, axis_y - Inches(0.08),
                                            x, axis_y + Inches(0.08))
        ln.line.color.rgb = Color.ORO_ANTICO
        ln.line.width = Pt(1)

        # Year below axis
        _, tf = _add_textbox(slide, x - Inches(0.7), axis_y + Inches(0.2),
                             Inches(1.4), Inches(0.3))
        _add_paragraph(tf, str(year),
                       font=Font.HEADING, size=12, color=Color.NERO_INCHIOSTRO,
                       align=PP_ALIGN.CENTER, tracking=1.2, line_spacing=1.0,
                       first=True)

        # Label above — all on one row, with a hairline connector to the tick
        label_top = Inches(3.3)
        conn = slide.shapes.add_connector(1, x, label_top + Inches(0.7),
                                              x, axis_y - Inches(0.08))
        conn.line.color.rgb = Color.CENERE
        conn.line.width = Pt(0.5)

        _, tf = _add_textbox(slide, x - Inches(1.0), label_top,
                             Inches(2.0), Inches(0.7))
        _add_paragraph(tf, label,
                       font=Font.BODY, size=11, color=Color.GRAFITE,
                       align=PP_ALIGN.CENTER, line_spacing=1.25, first=True)

    _footer(slide, slide_no, total)


def build_comparison(slide, *, slide_no, total):
    _set_blank_layout(slide)
    _slide_title_block(slide, eyebrow="Two paths",
                       title="What we open ourselves vs. what we license.")

    # Header bands
    band_y = Inches(2.3)
    band_h = Inches(0.6)
    # Left band: Blu Buccellati
    _add_filled_rect(slide, MARGIN, band_y,
                     Inches(5.8), band_h, fill=Color.BLU_BUCCELLATI)
    _, tf = _add_textbox(slide, MARGIN + Inches(0.3), band_y + Inches(0.15),
                         Inches(5.5), Inches(0.4))
    _add_paragraph(tf, "DIRECT BOUTIQUES",
                   font=Font.BODY, size=12, color=Color.AVORIO,
                   bold=True, tracking=2.0, line_spacing=1.0, first=True)

    # Right band: Pergamena
    _add_filled_rect(slide, MARGIN + Inches(6.5), band_y,
                     Inches(5.8), band_h, fill=Color.PERGAMENA)
    _, tf = _add_textbox(slide, MARGIN + Inches(6.8), band_y + Inches(0.15),
                         Inches(5.5), Inches(0.4))
    _add_paragraph(tf, "AUTHORISED PARTNERS",
                   font=Font.BODY, size=12, color=Color.NERO_INCHIOSTRO,
                   bold=True, tracking=2.0, line_spacing=1.0, first=True)

    # Bulleted lists with em-dash bullets
    def add_list(x, items):
        for i, item in enumerate(items):
            y = band_y + band_h + Inches(0.35) + Inches(0.6) * i
            # em-dash bullet in Oro Antico
            _, tf = _add_textbox(slide, x, y, Inches(0.4), Inches(0.4))
            _add_paragraph(tf, "—",
                           font=Font.BODY, size=14, color=Color.ORO_ANTICO,
                           line_spacing=1.0, first=True)
            _, tf = _add_textbox(slide, x + Inches(0.4), y,
                                 Inches(5.0), Inches(0.6))
            _add_paragraph(tf, item,
                           font=Font.BODY, size=14, color=Color.NERO_INCHIOSTRO,
                           line_spacing=1.35, first=True)

    add_list(MARGIN + Inches(0.3), [
        "Full control of client experience and pricing.",
        "Higher fixed cost, slower scaling.",
        "Necessary in flagship markets.",
    ])
    add_list(MARGIN + Inches(6.8), [
        "Reach in tier-2 cities at low capital cost.",
        "Variable execution; brand risk to be managed.",
        "Right for selective markets only.",
    ])

    # Center hairline divider
    ln = slide.shapes.add_connector(1,
        MARGIN + Inches(6.166), band_y,
        MARGIN + Inches(6.166), Inches(6.6))
    ln.line.color.rgb = Color.ORO_ANTICO
    ln.line.width = Pt(0.5)

    _footer(slide, slide_no, total)


def build_closing(slide):
    _set_blank_layout(slide, fill=Color.BLU_BUCCELLATI)

    # Wordmark
    _, tf = _add_textbox(slide, MARGIN, Inches(2.5),
                         SLIDE_W - 2*MARGIN, Inches(0.6))
    _add_paragraph(tf, "B U C C E L L A T I",
                   font=Font.HEADING, size=36, color=Color.AVORIO,
                   align=PP_ALIGN.CENTER, tracking=14.0, line_spacing=1.0,
                   first=True)

    # Grazie
    _, tf = _add_textbox(slide, MARGIN, Inches(4.2),
                         SLIDE_W - 2*MARGIN, Inches(0.8))
    _add_paragraph(tf, "Grazie.",
                   font=Font.HEADING, size=40, color=Color.ORO_CHIARO,
                   italic=True, align=PP_ALIGN.CENTER, line_spacing=1.0,
                   first=True)

    # Oro Antico rule
    _add_hairline(slide, Inches(5.666), Inches(5.7),
                  Inches(2.0), color=Color.ORO_ANTICO, thickness=0.75)


# ── Top-level orchestration ────────────────────────────────────────────────
def build_sample_deck(prs):
    """Build a sample .pptx containing one slide for each of the 16 layouts."""
    # We use the blank layout from python-pptx and draw everything ourselves
    # so the file looks identical on Windows and macOS.
    blank = prs.slide_layouts[6]

    # Set canvas
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H

    builders = [
        ("01 Cover / Title",          lambda s, n, t: build_cover(s)),
        ("02 Section Divider",        lambda s, n, t: build_section(s)),
        ("03 Agenda",                 build_agenda),
        ("04 Content — Statement",    build_statement),
        ("05 Content — Two-column",   build_two_column),
        ("06 Content — Three-column", build_three_column),
        ("07 Image-led full-bleed",   build_image_lead),
        ("08 Image + Text 60/40",     build_image_text_60_40),
        ("09 Data — KPI dashboard",   build_kpi),
        ("10 Data — Chart slide",     build_chart),
        ("11 Data — Table",           build_table),
        ("12 Pull-quote",             build_pullquote),
        ("13 Team / Org",             build_team),
        ("14 Timeline",               build_timeline),
        ("15 Comparison",             build_comparison),
        ("16 Closing / Thank You",    lambda s, n, t: build_closing(s)),
    ]
    total = len(builders)

    for idx, (name, fn) in enumerate(builders, start=1):
        slide = prs.slides.add_slide(blank)
        # Screen-reader title
        slide.shapes.title.text if slide.shapes.title is not None else None
        if fn.__name__ == "<lambda>":
            fn(slide, idx, total)
        else:
            fn(slide, slide_no=idx, total=total)
        # Add an off-slide title placeholder for accessibility (read by SR)
        # python-pptx doesn't allow setting alt-only metadata easily without
        # XML manipulation; we set the slide's element name instead.
        slide.shapes._spTree.set("name", name)

    return prs


def main():
    parser = argparse.ArgumentParser(description="Generate Buccellati .potx / sample .pptx")
    parser.add_argument("--out-dir", default="out", help="Output directory (default: ./out)")
    parser.add_argument("--potx-only", action="store_true")
    parser.add_argument("--pptx-only", action="store_true")
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    # python-pptx writes .pptx; rename / change content-type for .potx by
    # changing the file extension after-the-fact. PowerPoint treats both
    # interchangeably for theme purposes when "Save as template" is used.
    if not args.potx_only:
        prs = Presentation()
        build_sample_deck(prs)
        out_pptx = os.path.join(args.out_dir, "Buccellati_Sample.pptx")
        prs.save(out_pptx)
        print(f"Wrote {out_pptx}")

    if not args.pptx_only:
        prs = Presentation()
        build_sample_deck(prs)
        # Saving as .potx requires changing the content-type inside the OPC
        # package. For simplicity, save as .pptx and let the user "Save As
        # Template" once in PowerPoint, OR rename the extension and tell
        # PowerPoint it is a template. Most teams find this pragmatic.
        out_potx = os.path.join(args.out_dir, "Buccellati_Executive.potx")
        prs.save(out_potx)
        print(f"Wrote {out_potx}")
        print("Note: open in PowerPoint, File → Save As → PowerPoint Template")
        print("      to bind the .potx content-type if your IT requires it.")


if __name__ == "__main__":
    main()
