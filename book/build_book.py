"""Assemble the GAMA Days 2026 book of abstracts.

Inputs (this folder):
  cover.tex      cover page
  toc.tex        table of contents layout
  toc.json       one entry per abstract: printed page number, title, authors
  abstracts.pdf  the abstracts; its first page carries printed number 2
Outputs:
  ../public/book-gamadays2026-en.pdf   the book, served by the website
  ../public/images/book-cover.png      cover thumbnail for the website
  ../src/data/book.json                contents list for the website's book page

Printed page numbers of the abstracts are kept; cover and contents get roman
page labels. Contents entries and PDF bookmarks point to the abstracts.
Run: python build_book.py   (needs lualatex and PyMuPDF)
"""
import json
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
    book.insert_pdf(pymupdf.open(HERE / "abstracts.pdf"))

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
