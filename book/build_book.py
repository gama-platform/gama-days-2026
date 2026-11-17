"""Assemble the GAMA Days 2026 book of abstracts.

Inputs (this folder):
  cover.tex      cover page
  toc.tex        table of contents layout
  toc.json       one entry per abstract: printed page number, title, authors
  abstracts.pdf  the abstracts; its first page carries printed number 2
  originals/     optional: authors' PDFs named by Sciencesconf id (767597.pdf),
                 replacing that submission's pages where Sciencesconf's copy lost text
Outputs:
  ../public/book-gamadays2026-en.pdf   the book, served by the website
  ../public/images/book-cover.png      cover thumbnail for the website
  ../src/data/book.json                contents list for the website's book page

Printed page numbers of the abstracts are kept; cover and contents get roman
page labels. Contents entries and PDF bookmarks point to the abstracts.
Sciencesconf stamps each number at a fixed bottom-centre spot; where it lands on
the abstract's text or figures, the printed number is removed (the page label
still carries it). Its rule across the top of the page is kept only on the first
page of each abstract.
Run: python build_book.py   (needs lualatex and PyMuPDF)
"""
import json
import re
import subprocess
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "public" / "book-gamadays2026-en.pdf"
COVER_PNG = ROOT / "public" / "images" / "book-cover.png"
SITE_JSON = ROOT / "src" / "data" / "book.json"
FIRST_PRINTED = 2  # printed number of the first abstracts page

LATEX_ESCAPES = {"&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "$": r"\$"}


def tex_escape(s: str) -> str:
    return "".join(LATEX_ESCAPES.get(c, c) for c in s)


# Sciencesconf page number: text shown at baseline y = 54.018 (PDF coordinates),
# written as "... 54.018 Td [(34)]TJ" or "... 54.018007 Tm /cmr10 10.9 Tf [<0038003b>]TJ".
NUMBER_TJ = re.compile(rb"(54\.018\d*\s+T[dm]\s*(?:/\S+\s+[\d.]+\s+Tf\s*)?)\[[^\]]*\]\s*TJ")


def number_box(page: pymupdf.Page, printed: int) -> pymupdf.Rect:
    (box,) = [pymupdf.Rect(w[:4]) for w in page.get_text("words")
              if w[4] == str(printed) and w[1] > 770 and 280 < w[0] < 310]
    return box


def number_clashes(page: pymupdf.Page, printed: int) -> bool:
    """True if the number sits on a line of text, an image or a drawing.

    Words up to 6 pt to the side count: on some pages the letters under the
    number are missing, leaving the number inside a gap of the line.
    """
    num = number_box(page, printed)
    others = [pymupdf.Rect(w[:4]) for w in page.get_text("words")]
    others += [pymupdf.Rect(im["bbox"]) for im in page.get_image_info()]
    others += [dr["rect"] for dr in page.get_drawings()
               if dr["rect"].get_area() < 0.5 * page.rect.get_area()]  # not the page background
    return any(
        r != num
        and min(r.y1, num.y1) - max(r.y0, num.y0) > 0.3 * num.height
        and r.x0 < num.x1 + 6 and r.x1 > num.x0 - 6
        for r in others
    )


def drop_number(doc: pymupdf.Document, page: pymupdf.Page) -> None:
    hits = [(x, s) for x in page.get_contents()
            for s in [doc.xref_stream(x)] if NUMBER_TJ.search(s)]
    (xref, stream), = hits
    doc.update_stream(xref, NUMBER_TJ.sub(rb"\1[]TJ", stream, count=1))


# Sciencesconf rule across the top of every page, 58 pt from the top edge, written as
# "0 0 m 453.543 0 l S" (after a translation) or "72 783.864 m 525.543 783.864 l .398 w 0 0 0 RG S".
RULE_STROKE = re.compile(
    rb"(453\.543 0 l|525\.543 783\.864 l)(\s+(?:[\d.]+\s+w\s+)?(?:[\d.]+\s+[\d.]+\s+[\d.]+\s+RG\s+)?)S"
)


def drop_rule(doc: pymupdf.Document, page: pymupdf.Page) -> None:
    """Keep the rule's path but end it with "n" (no painting) instead of "S" (stroke)."""
    hits = [(x, s) for x in page.get_contents()
            for s in [doc.xref_stream(x)] if RULE_STROKE.search(s)]
    (xref, stream), = hits
    doc.update_stream(xref, RULE_STROKE.sub(rb"\1\2n", stream, count=1))


# Sciencesconf draws the submitted page as one form XObject: "q a 0 0 d e f cm /Fm1 Do Q".
PLACED_FORM = re.compile(rb"q\s+([\d.]+)\s+0\s+0\s+([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s+cm\s+/(\w+)\s+Do\s+Q")


def use_original(doc: pymupdf.Document, page: pymupdf.Page) -> str | None:
    """Swap the embedded submission for the author's PDF in originals/, if there is one.

    The original goes at the same place and in the same drawing order, under
    Sciencesconf's rule and number. Returns the original's file name when swapped.
    """
    for xref, name, _, bbox in page.get_xobjects():
        obj = doc.xref_object(xref)
        file = re.search(r"/PTEX\.FileName \(\./(\d+\.pdf)\)", obj)
        if file and (HERE / "originals" / file.group(1)).exists():
            break
    else:
        return None
    pno = int(re.search(r"/PTEX\.PageNumber (\d+)", obj).group(1)) - 1
    hits = [(x, s, m) for x in page.get_contents()
            for s in [doc.xref_stream(x)] for m in [PLACED_FORM.search(s)]
            if m and m.group(5).decode() == name]
    (cxref, stream, m), = hits
    a, d, e, f = (float(v) for v in m.group(1, 2, 3, 4))
    x0, y0, x1, y1 = bbox  # PDF coordinates, origin bottom-left
    H = page.rect.height
    target = pymupdf.Rect(e + a * x0, H - (f + d * y1), e + a * x1, H - (f + d * y0))
    doc.update_stream(cxref, stream[:m.start()] + stream[m.end():])
    page.show_pdf_page(target, pymupdf.open(HERE / "originals" / file.group(1)), pno,
                       keep_proportion=False, overlay=False)
    return file.group(1)


def lualatex(name: str) -> None:
    for _ in range(2):  # second pass places the cover's tikz overlay
        subprocess.run(
            ["lualatex", "-interaction=nonstopmode", "-halt-on-error", name],
            cwd=HERE, check=True, stdout=subprocess.DEVNULL,
        )


def main() -> None:
    toc = json.loads((HERE / "toc.json").read_text(encoding="utf-8"))
    (HERE / "toc-entries.tex").write_text(
        "\n".join(
            f"\\entry{{{e['page']}}}{{{tex_escape(e['title'])}}}{{{tex_escape(e['authors'])}}}"
            for e in toc
        ),
        encoding="utf-8",
    )
    lualatex("cover.tex")
    lualatex("toc.tex")

    book = pymupdf.open()
    book.insert_pdf(pymupdf.open(HERE / "cover.pdf"))
    book.insert_pdf(pymupdf.open(HERE / "toc.pdf"))
    front = book.page_count
    abstracts = pymupdf.open(HERE / "abstracts.pdf")
    first_pages = {e["page"] for e in toc}
    dropped, swapped = [], []
    for i, page in enumerate(abstracts):
        printed = FIRST_PRINTED + i
        if original := use_original(abstracts, page):
            swapped.append(f"{printed} ({original})")
        if printed not in first_pages:
            drop_rule(abstracts, page)
        if number_clashes(page, printed):
            drop_number(abstracts, page)
            dropped.append(printed)
    print("pages from authors' originals:", swapped)
    print("page number removed (overlaps content):", dropped)
    book.insert_pdf(abstracts)

    def physical(printed: int) -> int:  # 0-based index in the book
        return front + printed - FIRST_PRINTED

    # Contents entries: "gotopage:N" URIs -> internal links
    for i in range(1, front):
        page = book[i]
        for link in page.get_links():
            uri = link.get("uri", "")
            if uri.startswith("gotopage:"):
                page.delete_link(link)
                page.insert_link({
                    "kind": pymupdf.LINK_GOTO,
                    "from": link["from"],
                    "page": physical(int(uri.split(":", 1)[1])),
                    "to": pymupdf.Point(0, 0),
                })

    book.set_toc(
        [[1, "Contents", 2]]
        + [[1, f"{e['title']} — {e['authors']}", physical(e["page"]) + 1] for e in toc]
    )
    book.set_page_labels([
        {"startpage": 0, "prefix": "", "style": "r", "firstpagenum": 1},
        {"startpage": front, "prefix": "", "style": "D", "firstpagenum": FIRST_PRINTED},
    ])
    book.set_metadata({**book.metadata, "title": "GAMA Days 2026 — Book of Abstracts"})

    book[0].get_pixmap(dpi=110).save(COVER_PNG)
    SITE_JSON.write_text(
        json.dumps(
            [{**e, "pdfPage": physical(e["page"]) + 1} for e in toc],
            ensure_ascii=False, indent=1,
        ),
        encoding="utf-8",
    )

    tmp = OUT.with_suffix(".tmp.pdf")
    book.save(tmp, garbage=3, deflate=True)
    book.close()
    tmp.replace(OUT)
    print(f"{OUT.name}: {front} front pages + abstracts")


if __name__ == "__main__":
    main()
