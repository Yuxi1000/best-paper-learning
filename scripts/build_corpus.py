#!/usr/bin/env python3
"""Download 20 award papers and extract abstracts, argument excerpts, and figures."""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
CATALOG = json.loads((CORPUS / "catalog.json").read_text(encoding="utf-8"))
PDF_DIR = CORPUS / "pdfs"
UA = "best-paper-style-corpus/1.0 (personal research writing study; Python urllib)"

MIN_SIDE = 120
MIN_AREA = 20000
MAX_FIGS_PER_PAPER = 16
EXCERPT_CHARS = 1400

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"

SECTION_MAP = [
    ("problem-framing", re.compile(r"^(?:\d+\.?\s*)?(introduction|intro)\b", re.I)),
    ("claim-contribution", re.compile(r"^(?:\d+\.?\s*)?(contributions?|our contributions?)\b", re.I)),
    ("related-work", re.compile(r"^(?:\d+\.?\s*)?(related work|prior work|background)\b", re.I)),
    ("method-mechanism", re.compile(r"^(?:\d+\.?\s*)?(method|approach|model|proposed|architecture|framework)\b", re.I)),
    ("experiment-result", re.compile(r"^(?:\d+\.?\s*)?(experiment|result|evaluation|empirical)\b", re.I)),
    ("limitation-scope", re.compile(r"^(?:\d+\.?\s*)?(limitation|discussion|conclusion|broader impact)\b", re.I)),
]

FIG_RULES = [
    ("teaser", re.compile(r"\b(teaser|overview of our|we present|our method generates)\b", re.I)),
    ("architecture", re.compile(r"\b(architecture|overview|pipeline|framework|network|model diagram|block)\b", re.I)),
    ("ablation", re.compile(r"\b(ablation|component|variant)\b", re.I)),
    ("quantitative", re.compile(r"\b(fid|curve|plot|scaling|accuracy|comparison|versus|vs\.|trade-?off)\b", re.I)),
    ("analysis-diagram", re.compile(r"\b(illustration|schematic|analysis|mechanism|toy|intuition)\b", re.I)),
    ("qualitative", re.compile(r"\b(qualitative|sample|visuali[sz]ation|generated|result|example|comparison)\b", re.I)),
]


def fetch(url: str, dest: Path | None = None, retries: int = 4) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    last_err: Exception | None = None
    for i in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = resp.read()
            if dest:
                dest.write_bytes(data)
            return data
        except (urllib.error.URLError, TimeoutError) as err:
            last_err = err
            time.sleep(2 ** i)
    raise RuntimeError(f"failed to fetch {url}: {last_err}")


def arxiv_meta(arxiv_id: str) -> dict:
    xml = fetch(f"https://export.arxiv.org/api/query?id_list={arxiv_id}").decode("utf-8")
    root = ET.fromstring(xml)
    entry = root.find(f"{ATOM}entry")
    if entry is None:
        raise RuntimeError(f"no arXiv entry for {arxiv_id}")
    title = re.sub(r"\s+", " ", (entry.findtext(f"{ATOM}title") or "").strip())
    abstract = re.sub(r"\s+", " ", (entry.findtext(f"{ATOM}summary") or "").strip())
    authors = [a.findtext(f"{ATOM}name") or "" for a in entry.findall(f"{ATOM}author")]
    published = (entry.findtext(f"{ATOM}published") or "")[:10]
    license_url = ""
    rights = entry.find(f"{ARXIV}license")
    if rights is not None and rights.text:
        license_url = rights.text.strip()
    return {
        "title": title,
        "abstract": abstract,
        "authors": authors,
        "published": published,
        "license": license_url,
        "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}",
        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
    }


def clean_text(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = re.sub(r"-\n", "", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def split_sections(text: str) -> dict[str, str]:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    buckets: dict[str, list[str]] = defaultdict(list)
    current = "front-matter"
    for line in lines:
        mapped = None
        if len(line) < 80:
            for name, pat in SECTION_MAP:
                if pat.search(line):
                    mapped = name
                    break
        if mapped:
            current = mapped
            continue
        buckets[current].append(line)
    out = {}
    for name, parts in buckets.items():
        blob = clean_text(" ".join(parts))
        if len(blob) > 80:
            out[name] = blob[:EXCERPT_CHARS].rsplit(" ", 1)[0] + "…"
    return out


def classify_figure(caption: str, index: int) -> str:
    if index == 0 and not caption:
        return "teaser"
    for name, pat in FIG_RULES:
        if caption and pat.search(caption):
            return name
    if index == 0:
        return "teaser"
    return "qualitative"


def extract_captions(page: fitz.Page) -> list[str]:
    text = page.get_text("text")
    found = re.findall(r"(Figure\s+\d+[:.].{10,400})", text, flags=re.I | re.S)
    return [clean_text(c) for c in found]


def extract_pdf(paper: dict, pdf_path: Path) -> dict:
    doc = fitz.open(pdf_path)
    full = []
    captions_all = []
    saved_figs = []
    fig_count = 0
    for page_i, page in enumerate(doc):
        full.append(page.get_text("text"))
        captions_all.extend(extract_captions(page))
        if fig_count >= MAX_FIGS_PER_PAPER:
            continue
        for img_i, img in enumerate(page.get_images(full=True)):
            if fig_count >= MAX_FIGS_PER_PAPER:
                break
            xref = img[0]
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n >= 5:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
            except Exception:
                continue
            if pix.width < MIN_SIDE or pix.height < MIN_SIDE or pix.width * pix.height < MIN_AREA:
                continue
            # Skip very thin UI bars / logos.
            if pix.width / max(pix.height, 1) > 12 or pix.height / max(pix.width, 1) > 12:
                continue
            caption = captions_all[min(fig_count, len(captions_all) - 1)] if captions_all else ""
            ftype = classify_figure(caption, fig_count)
            out_name = f"{paper['id']}-p{page_i + 1:02d}-{fig_count + 1:02d}.png"
            out_path = CORPUS / "figures" / ftype / out_name
            pix.save(out_path)
            saved_figs.append(
                {
                    "file": f"figures/{ftype}/{out_name}",
                    "type": ftype,
                    "page": page_i + 1,
                    "width": pix.width,
                    "height": pix.height,
                    "caption": caption,
                }
            )
            fig_count += 1
    text = clean_text("\n".join(full))
    sections = split_sections(text)
    return {"sections": sections, "figures": saved_figs, "page_count": doc.page_count, "char_count": len(text)}


def write_abstract(paper: dict, meta: dict) -> None:
    authors = ", ".join(meta["authors"][:12])
    if len(meta["authors"]) > 12:
        authors += " et al."
    body = f"""# {meta['title']}

- id: `{paper['id']}`
- award: {paper['award']}
- venue: {paper['venue']} {paper['year']}
- arXiv: [{paper['arxiv']}](https://arxiv.org/abs/{paper['arxiv']})
- authors: {authors}
- posted: {meta['published']}
- license: {meta['license'] or 'see arXiv page'}
- paper_type: {paper['paper_type']}
- use_for: {', '.join(paper['use_for'])}

## Abstract

{meta['abstract']}
"""
    (CORPUS / "abstracts" / f"{paper['id']}.md").write_text(body, encoding="utf-8")


def write_arguments(paper: dict, sections: dict) -> None:
    mapping = {
        "problem-framing": "problem-framing",
        "claim-contribution": "claim-contribution",
        "related-work": "related-work",
        "method-mechanism": "method-mechanism",
        "experiment-result": "experiment-result",
        "limitation-scope": "limitation-scope",
        "front-matter": "problem-framing",
    }
    used = set()
    for src, dest in mapping.items():
        blob = sections.get(src)
        if not blob:
            continue
        used.add(dest)
        path = CORPUS / "arguments" / dest / f"{paper['id']}.md"
        path.write_text(
            f"# {paper['title']}\n\n"
            f"- id: `{paper['id']}`\n"
            f"- award: {paper['award']}\n"
            f"- section_bucket: {dest}\n"
            f"- source: arXiv:{paper['arxiv']}\n\n"
            f"## Excerpt (truncated; study the move, do not copy)\n\n{blob}\n",
            encoding="utf-8",
        )


def write_style_card(paper: dict, meta: dict, extracted: dict) -> None:
    fig_types = sorted({f["type"] for f in extracted["figures"]})
    body = f"""# Style card: {paper['id']}

- title: {meta['title']}
- award: {paper['award']}
- type: {paper['paper_type']}
- figures_extracted: {len(extracted['figures'])} ({', '.join(fig_types) or 'none'})
- pages: {extracted['page_count']}

## What to steal (patterns, not sentences)

- Abstract shape: problem -> limitation of status quo -> this paper's move -> evidence of success.
- Match this paper when the user's draft is: {', '.join(paper['use_for'])}.
- Open the abstract file and 1-2 argument excerpts before imitating.

## Figure inventory

"""
    for fig in extracted["figures"]:
        cap = fig["caption"][:180].replace("\n", " ")
        body += f"- `{fig['file']}` ({fig['type']}, p.{fig['page']}) {cap}\n"
    (CORPUS / "style-cards" / f"{paper['id']}.md").write_text(body, encoding="utf-8")


def write_index(rows: list[dict]) -> None:
    lines = [
        "# Best-paper style corpus",
        "",
        "Study these files before writing or drawing. Copy patterns, not sentences.",
        "",
        "| id | award | type | abstract | style card | use for |",
        "|---|---|---|---|---|---|",
    ]
    for p in rows:
        lines.append(
            f"| `{p['id']}` | {p['award']} | {p['paper_type']} | "
            f"[abstract](abstracts/{p['id']}.md) | [card](style-cards/{p['id']}.md) | "
            f"{', '.join(p['use_for'][:3])} |"
        )
    lines += [
        "",
        "## Folder map",
        "",
        "- `abstracts/` — one file per paper, official arXiv abstract",
        "- `arguments/` — truncated section excerpts by rhetorical move",
        "- `figures/` — extracted figures by visual genre",
        "- `style-cards/` — short imitation notes plus figure inventory",
        "- `pdfs/` — source PDFs from arXiv",
        "",
        "## Argument buckets",
        "",
        "- `arguments/problem-framing/`",
        "- `arguments/claim-contribution/`",
        "- `arguments/related-work/`",
        "- `arguments/method-mechanism/`",
        "- `arguments/experiment-result/`",
        "- `arguments/limitation-scope/`",
        "- `arguments/appendix/`",
        "",
        "## Figure buckets",
        "",
        "- `figures/teaser/`",
        "- `figures/architecture/`",
        "- `figures/qualitative/`",
        "- `figures/quantitative/`",
        "- `figures/ablation/`",
        "- `figures/analysis-diagram/`",
    ]
    (CORPUS / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    cap_lines = ["# Figure captions", ""]
    for p in rows:
        card = CORPUS / "style-cards" / f"{p['id']}.md"
        if card.exists():
            cap_lines.append(card.read_text(encoding="utf-8"))
            cap_lines.append("")
    (CORPUS / "figures" / "captions" / "ALL.md").write_text("\n".join(cap_lines), encoding="utf-8")


def main() -> None:
    rows = CATALOG["papers"]
    report = []
    for i, paper in enumerate(rows, 1):
        print(f"[{i}/{len(rows)}] {paper['id']} {paper['arxiv']}", flush=True)
        meta = arxiv_meta(paper["arxiv"])
        pdf_path = PDF_DIR / f"{paper['id']}-{paper['arxiv']}.pdf"
        if not pdf_path.exists() or pdf_path.stat().st_size < 20000:
            fetch(meta["pdf_url"], pdf_path)
            time.sleep(1.2)
        extracted = extract_pdf(paper, pdf_path)
        write_abstract(paper, meta)
        write_arguments(paper, extracted["sections"])
        write_style_card(paper, meta, extracted)
        report.append(
            {
                "id": paper["id"],
                "arxiv": paper["arxiv"],
                "title": meta["title"],
                "license": meta["license"],
                "figures": len(extracted["figures"]),
                "sections": sorted(extracted["sections"].keys()),
            }
        )
        time.sleep(0.4)
    (CORPUS / "build_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_index(rows)
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "extract_appendix", Path(__file__).with_name("extract_appendix.py")
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()
    print("done", json.dumps({"papers": len(report), "figures": sum(r["figures"] for r in report)}))


if __name__ == "__main__":
    main()
