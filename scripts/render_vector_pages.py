#!/usr/bin/env python3
"""Render PDF pages that contain figures when raster extraction was too sparse."""

from pathlib import Path
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
PDF_DIR = CORPUS / "pdfs"
OUT = CORPUS / "figures" / "page-renders"
OUT.mkdir(parents=True, exist_ok=True)

CATALOG = json.loads((CORPUS / "catalog.json").read_text(encoding="utf-8"))


def main() -> None:
    cards = CORPUS / "style-cards"
    for paper in CATALOG["papers"]:
        card = (cards / f"{paper['id']}.md").read_text(encoding="utf-8")
        n_figs = 0
        for line in card.splitlines():
            if line.startswith("- figures_extracted:"):
                n_figs = int(line.split(":")[1].split("(")[0].strip())
        if n_figs >= 6:
            continue
        pdfs = list(PDF_DIR.glob(f"{paper['id']}-*.pdf"))
        if not pdfs:
            continue
        doc = fitz.open(pdfs[0])
        saved = 0
        dest = OUT / paper["id"]
        dest.mkdir(exist_ok=True)
        for i, page in enumerate(doc):
            text = page.get_text("text")
            if i > 0 and "Figure" not in text and "Fig." not in text:
                continue
            if i > 10 or saved >= 8:
                break
            pix = page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
            path = dest / f"page-{i + 1:02d}.png"
            pix.save(path)
            saved += 1
        print(paper["id"], "rendered", saved)


if __name__ == "__main__":
    main()
