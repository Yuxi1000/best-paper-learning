# Best Paper Learning

A Cursor skill plus a local corpus of **20 official CVPR / ICCV / NeurIPS / ICML / ICLR Best or Outstanding papers**. The agent studies their writing and figure craft *before* helping you draft, revise, or draw.

This repository is meant to be cloned as a Cursor skill:

```text
~/.cursor/skills/best-paper-style/
```

Remote: [github.com/Yuxi1000/best-paper-learning](https://github.com/Yuxi1000/best-paper-learning)

## Install

PDFs are stored with Git LFS. Install [Git LFS](https://git-lfs.com), then:

```bash
git lfs install
git clone git@github.com:Yuxi1000/best-paper-learning.git ~/.cursor/skills/best-paper-style
mkdir -p ~/.cursor/agents
cp ~/.cursor/skills/best-paper-style/agents/paper-style-coach.md ~/.cursor/agents/
```

Windows (PowerShell):

```powershell
git lfs install
git clone git@github.com:Yuxi1000/best-paper-learning.git "$env:USERPROFILE\.cursor\skills\best-paper-style"
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\agents" | Out-Null
Copy-Item "$env:USERPROFILE\.cursor\skills\best-paper-style\agents\paper-style-coach.md" "$env:USERPROFILE\.cursor\agents\paper-style-coach.md"
```

Restart Cursor (or start a new agent chat) so it picks up the skill.

If this folder is already your skill directory, you only need `git pull`.

## How to use

In Cursor, attach or invoke the skill, then say for example:

```text
Use the best-paper-style skill. Rewrite this abstract.
Use paper-style-coach. Design Fig.1 as an old-vs-new architecture.
帮我按顶会 appendix 的写法列补充材料。
```

The agent must open matching abstracts, argument excerpts, and figures **before** drafting. It should imitate moves, not copy sentences or pixels.

## Layout

```text
SKILL.md                 Cursor skill (workflow)
examples.md              Invocation examples
agents/paper-style-coach.md
references/
  exemplar-map.md        Which papers to study for which task
  writing-playbook.md
  figure-playbook.md
  paper-notes.md
corpus/
  INDEX.md
  abstracts/             20 official arXiv abstracts
  arguments/             intro / method / experiments / limitations / appendix
  figures/               classified crops + page-renders + appendix pages
  pdfs/                  arXiv PDFs (Git LFS)
  style-cards/
scripts/
  build_corpus.py        Re-download and extract
  extract_appendix.py    Rebuild the appendix bucket only
```

## Corpus policy

See `corpus/NOTICE.md`.

- Sources are author-posted arXiv PDFs of award papers.
- Stored extracts are for personal study of writing and figure craft.
- Do not republish the corpus as a paper, and do not paste exemplar sentences into a manuscript.
- Four papers have no appendix in the arXiv PDF: `vggt`, `var`, `swin`, `generative-image-dynamics`.

## Rebuild

```bash
python scripts/build_corpus.py          # full refresh (network)
python scripts/extract_appendix.py      # appendix bucket only, local PDFs
```

Requires Python 3.10+ and `pymupdf`.
