#!/usr/bin/env python3
"""Extract appendix sections from already-downloaded award-paper PDFs."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
PDF_DIR = CORPUS / "pdfs"
OUT_DIR = CORPUS / "arguments" / "appendix"
FIG_DIR = CORPUS / "figures" / "appendix"
CATALOG = json.loads((CORPUS / "catalog.json").read_text(encoding="utf-8"))

EXCERPT_CHARS = 1600
MAX_SECTION_EXCERPT = 1200
MAX_RENDER_PAGES = 8

EXPLICIT_HEAD = re.compile(
    r"(?i)^\s*(?:(?:\d+\s+)?appendix(?:es)?|supplementary materials?|supplemental materials?|supplementary)\s*$"
)
APPENDIX_LINE = re.compile(
    r"(?i)^\s*(?:appendix(?:\s+[a-z0-9]+)?|a\.\s+appendix|supplementary(?:\s+material)?)\b"
)
LETTERED_HEAD = re.compile(
    r"^\s*(?:Appendix\s+)?([A-H])(?:\.(\d+(?:\.\d+)*))?\.?\s+([A-Z][A-Za-z][\w\s,:\-]{2,70})$"
)
ICLR_HEAD = re.compile(
    r"^([A-H])(?:\.\d+)*\.?\s+([A-Z][A-Z0-9 ,:\-]{6,80})$"
)
REFS_HEAD = re.compile(r"(?i)^\s*references\s*$|^\s*bibliography\s*$")

GENRE_RULES = [
    ("proofs", re.compile(r"proof|lemma|theorem|proposition|corollary|derivation|notation|bound", re.I)),
    ("extra-experiments", re.compile(r"additional experiment|extra experiment|more result|ablation|additional result|further experiment|more experiment", re.I)),
    ("hyperparams-implementation", re.compile(r"implementation|hyperparameter|training detail|architecture detail|compute|prompt|captioning detail", re.I)),
    ("failure-cases", re.compile(r"failure|limitation|negative result|error analysis|ethical", re.I)),
    ("datasets-protocol", re.compile(r"dataset|annotation|protocol|human stud|data collection|filtering question", re.I)),
    ("qualitative-extra", re.compile(r"qualitative|more sample|extra visual|more example|visual rationale", re.I)),
]

# Manual start pages when heading detection is noisy (1-indexed).
OVERRIDES = {
    "brickgpt": 13,
    "emergent-mirage": 12,
    "richhf": 12,
    "sd3-rectified-flow": 17,
    "sedd": 12,
    "uniad": 13,
    "videopoet": 13,
    "visprog": 12,
    "stde": 12,  # references on p11, remainder is appendix
    "never-train-from-scratch": 11,
    "privacy-auditing": 16,
    "shallow-safety": 14,
    "train-for-the-worst": 12,
    "llm-finetuning-dynamics": 16,
    "llm-debate": 31,
    "vit-registers": 12,
}


def clean_text(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = re.sub(r"-\n", "", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def classify_genre(title: str, blob: str) -> str:
    hay = f"{title}\n{blob[:500]}"
    for name, pat in GENRE_RULES:
        if pat.search(hay):
            return name
    if re.search(r"proof|lemma|theorem", blob[:400], re.I):
        return "proofs"
    return "other"


def find_refs_page(doc: fitz.Document) -> int | None:
    for i, page in enumerate(doc):
        lines = [ln.strip() for ln in page.get_text("text").splitlines() if ln.strip()][:12]
        if any(REFS_HEAD.match(ln) for ln in lines):
            return i + 1
    return None


def detect_start(doc: fitz.Document, paper_id: str) -> tuple[int | None, str]:
    if paper_id in OVERRIDES:
        start = OVERRIDES[paper_id]
        if start <= doc.page_count:
            return start, "override"
    refs = find_refs_page(doc)
    scores: list[tuple[int, int]] = []
    for i, page in enumerate(doc):
        if i < 6:
            continue
        lines = [ln.strip() for ln in page.get_text("text").splitlines() if ln.strip()][:18]
        score = 0
        if any(EXPLICIT_HEAD.match(ln) for ln in lines[:8]):
            score += 12
        if any(APPENDIX_LINE.match(ln) and len(ln) < 60 for ln in lines[:8]):
            score += 8
        if any(LETTERED_HEAD.match(ln) for ln in lines[:10]):
            score += 4
            if refs and i + 1 > refs:
                score += 4
        if "in this appendix" in " ".join(lines).lower():
            score += 3
        if score:
            scores.append((score, i + 1))
    if scores:
        scores.sort(key=lambda x: (-x[0], x[1]))
        best_score, page = scores[0]
        if best_score >= 8:
            return page, f"detected:{best_score}"
        if refs and page > refs and best_score >= 4:
            return page, f"after-refs:{best_score}"
    if refs and refs < doc.page_count:
        # Content after a mid-paper references block is often the appendix
        # only if many pages remain.
        remaining = doc.page_count - refs
        if remaining >= 4:
            return refs + 1, "after-references"
    return None, "none"


def split_appendix_sections(pages: list[tuple[int, str]]) -> list[dict]:
    """pages: list of (page_no, text)."""
    raw_lines: list[tuple[int, str]] = []
    for page_no, text in pages:
        for ln in text.splitlines():
            s = ln.strip()
            if s:
                raw_lines.append((page_no, s))

    sections: list[dict] = []
    current = {"id": "A", "title": "Appendix (opening)", "start_page": pages[0][0] if pages else 1, "lines": []}
    for page_no, ln in raw_lines:
        if len(ln) < 90 and " . . " not in ln and "...." not in ln:
            letter_m = LETTERED_HEAD.match(ln)
            iclr_m = None if letter_m else ICLR_HEAD.match(ln)
            if iclr_m:
                letter_m = iclr_m
            if letter_m:
                if current["lines"]:
                    sections.append(current)
                letter = letter_m.group(1)
                if letter_m.lastindex >= 3 and letter_m.group(3):
                    sub = letter_m.group(2)
                    title = letter_m.group(3).strip()
                    sid = f"{letter}.{sub}" if sub else letter
                else:
                    sub = None
                    title = letter_m.group(2).strip()
                    sid = letter_m.group(0).split()[0].rstrip(".")
                current = {"id": sid, "title": title, "start_page": page_no, "lines": []}
                continue
            if EXPLICIT_HEAD.match(ln) or re.match(r"(?i)^appendix\b", ln):
                # keep as opener, do not flush unless we already have prose
                if not current["lines"]:
                    current["title"] = ln
                    current["start_page"] = page_no
                continue
        current["lines"].append(ln)
    if current["lines"] or not sections:
        sections.append(current)

    out = []
    for sec in sections:
        blob = clean_text(" ".join(sec["lines"]))
        if len(blob) < 60:
            continue
        if blob.count(" . .") >= 2:  # table-of-contents leaders, not body text
            continue
        excerpt = blob[:MAX_SECTION_EXCERPT]
        if len(blob) > MAX_SECTION_EXCERPT:
            excerpt = excerpt.rsplit(" ", 1)[0] + "…"
        genre = classify_genre(sec["title"], blob)
        out.append(
            {
                "id": sec["id"],
                "title": sec["title"],
                "start_page": sec["start_page"],
                "genre": genre,
                "chars": len(blob),
                "excerpt": excerpt,
            }
        )
    if not out and pages:
        blob = clean_text(" ".join(t for _, t in pages))
        excerpt = blob[:MAX_SECTION_EXCERPT]
        if len(blob) > MAX_SECTION_EXCERPT:
            excerpt = excerpt.rsplit(" ", 1)[0] + "…"
        if len(excerpt) >= 60:
            out.append(
                {
                    "id": "A",
                    "title": "Appendix body",
                    "start_page": pages[0][0],
                    "genre": classify_genre("appendix", blob),
                    "chars": len(blob),
                    "excerpt": excerpt,
                }
            )
    return out


def render_pages(doc: fitz.Document, paper_id: str, start: int) -> list[str]:
    dest = FIG_DIR / paper_id
    dest.mkdir(parents=True, exist_ok=True)
    saved = []
    last = min(doc.page_count, start - 1 + MAX_RENDER_PAGES)
    for i in range(start - 1, last):
        pix = doc[i].get_pixmap(matrix=fitz.Matrix(1.45, 1.45), alpha=False)
        path = dest / f"page-{i + 1:02d}.png"
        pix.save(path)
        saved.append(f"figures/appendix/{paper_id}/page-{i + 1:02d}.png")
    return saved


def write_paper_file(paper: dict, info: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Appendix: {paper['title']}",
        "",
        f"- id: `{paper['id']}`",
        f"- award: {paper['award']}",
        f"- arXiv: {paper['arxiv']}",
        f"- appendix_present: {str(info['present']).lower()}",
        f"- start_page: {info.get('start_page')}",
        f"- appendix_pages: {info.get('appendix_pages')}",
        f"- detection: {info.get('detection')}",
        f"- genres: {', '.join(info.get('genres') or []) or 'none'}",
        "",
    ]
    if not info["present"]:
        lines += [
            "No appendix / supplementary section was found in the arXiv PDF. "
            "Some papers ship a separate supplemental zip; do not invent appendix content.",
            "",
        ]
        (OUT_DIR / f"{paper['id']}.md").write_text("\n".join(lines), encoding="utf-8")
        return

    lines += ["## Table of contents", ""]
    for sec in info["sections"]:
        lines.append(
            f"- `{sec['id']}` {sec['title']} — *{sec['genre']}* (p.{sec['start_page']})"
        )
    lines += ["", "## Excerpts (study the move, do not copy)", ""]
    for sec in info["sections"]:
        lines += [
            f"### {sec['id']}. {sec['title']}",
            "",
            f"- genre: `{sec['genre']}`",
            f"- start_page: {sec['start_page']}",
            "",
            sec["excerpt"],
            "",
        ]
    if info.get("renders"):
        lines += ["## Page renders", ""]
        for p in info["renders"]:
            lines.append(f"- `{p}`")
        lines.append("")
    (OUT_DIR / f"{paper['id']}.md").write_text("\n".join(lines), encoding="utf-8")

    # Genre slices for the skill's bucketed reading.
    by_genre: dict[str, list[dict]] = defaultdict(list)
    for sec in info["sections"]:
        by_genre[sec["genre"]].append(sec)
    for genre, secs in by_genre.items():
        gdir = OUT_DIR / genre
        gdir.mkdir(parents=True, exist_ok=True)
        body = [
            f"# Appendix/{genre}: {paper['title']}",
            "",
            f"- id: `{paper['id']}`",
            f"- source: arXiv:{paper['arxiv']}",
            "",
        ]
        for sec in secs:
            body += [f"## {sec['id']}. {sec['title']}", "", sec["excerpt"], ""]
        (gdir / f"{paper['id']}.md").write_text("\n".join(body), encoding="utf-8")


def write_index(rows: list[dict]) -> None:
    lines = [
        "# Appendix corpus",
        "",
        "Study these files when writing supplementary material, extra ablations, proofs, hyperparameter lists, or rebuttal appendices.",
        "",
        "| id | present | start | pages | genres | file |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        genres = ", ".join(r.get("genres") or [])
        lines.append(
            f"| `{r['id']}` | {r['present']} | {r.get('start_page') or '—'} | "
            f"{r.get('appendix_pages') or '—'} | {genres or '—'} | "
            f"[md]({r['id']}.md) |"
        )
    lines += [
        "",
        "## Genre buckets",
        "",
        "- `proofs/`",
        "- `extra-experiments/`",
        "- `hyperparams-implementation/`",
        "- `failure-cases/`",
        "- `datasets-protocol/`",
        "- `qualitative-extra/`",
        "- `other/`",
        "",
        "Page renders: `../../figures/appendix/<id>/`",
    ]
    (OUT_DIR / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def process_paper(paper: dict) -> dict:
    pdfs = list(PDF_DIR.glob(f"{paper['id']}-*.pdf"))
    if not pdfs:
        return {"id": paper["id"], "present": False, "detection": "no-pdf", "genres": []}
    doc = fitz.open(pdfs[0])
    start, how = detect_start(doc, paper["id"])
    if start is None or start > doc.page_count:
        return {
            "id": paper["id"],
            "present": False,
            "detection": how,
            "start_page": None,
            "appendix_pages": 0,
            "sections": [],
            "genres": [],
        }
    page_texts = [(i + 1, doc[i].get_text("text")) for i in range(start - 1, doc.page_count)]
    sections = split_appendix_sections(page_texts)
    genres = sorted({s["genre"] for s in sections})
    renders = render_pages(doc, paper["id"], start)
    info = {
        "id": paper["id"],
        "present": True,
        "detection": how,
        "start_page": start,
        "appendix_pages": doc.page_count - start + 1,
        "sections": sections,
        "genres": genres,
        "renders": renders,
    }
    return info


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for paper in CATALOG["papers"]:
        info = process_paper(paper)
        write_paper_file(paper, info)
        rows.append(
            {
                "id": info["id"],
                "present": info["present"],
                "start_page": info.get("start_page"),
                "appendix_pages": info.get("appendix_pages"),
                "genres": info.get("genres") or [],
                "n_sections": len(info.get("sections") or []),
            }
        )
        print(
            f"{paper['id']:28s} present={info['present']} start={info.get('start_page')} "
            f"pages={info.get('appendix_pages')} sections={len(info.get('sections') or [])} "
            f"genres={info.get('genres')}",
            flush=True,
        )
    write_index(rows)
    (CORPUS / "appendix_report.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print("done", sum(1 for r in rows if r["present"]), "/", len(rows))


if __name__ == "__main__":
    main()
