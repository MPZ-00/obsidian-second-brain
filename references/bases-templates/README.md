---
type: reference
description: "Templates for the 8 standard folder Bases used by AI-Brain vaults"
ai-first: true
---

# Bases Templates

These `.base` files are the canonical folder views for an AI-Brain vault. `/obsidian-init` copies the relevant ones into the appropriate vault folders during bootstrap. Each one is a live filtered view over note frontmatter — open in Obsidian to see the data.

## Files

| Template | Goes to | Filters | Views |
|---|---|---|---|
| `_Projects.base` | `Projects/` | `note.type == "project"` | Active / Planning / On hold / All |
| `_People.base` | `People/` | `note.type == "person"` | By recency / Strong ties / Gallery |
| `_Ideas.base` | `Ideas/` | `note.type == "idea"` | Exploring / All |
| `_Knowledge.base` | `Knowledge/` | folder match | ADRs / Patterns / Learnings / All |
| `_Research.base` | `Research/` | `note.type == "research"` | YouTube / Web / Deep / All |
| `_Dev Logs.base` | `Dev Logs/` | `note.type == "dev-log"` | Recent / By project / All |
| `_Tasks.base` | `Tasks/` | `note.type == "task"` | Open / Overdue / Done |
| `_Logs.base` | `Logs/` | `note.type == "log"` | Recent / All |

## Frontmatter assumptions

The bases assume the AI-first vault frontmatter conventions:

- `type` — required, drives the per-folder filter (`project`, `person`, `idea`, `task`, `dev-log`, `log`, `research`, `decision-record`, etc.)
- `status` — optional, drives groupBy and status-icon formulas (`active | planning | on-hold | completed | archived` for projects; `exploring | active | archived | graduated` for ideas; `in-progress | done | waiting` for tasks)
- `strength` — optional, on people notes (`high | medium | low`)
- `last-interaction` — optional, on people notes (ISO date) — accessed as `note["last-interaction"]` because of the hyphen
- `subtype` — required on research notes (`web | deep | youtube`)
- `date-watched` — optional, on YouTube research notes
- `priority` — optional, on tasks (`high | medium | low`)
- `due` — optional ISO date, on tasks
- `project` — optional, on dev logs (project name string)

If your vault uses different field names, edit the templates before copying or adapt the filters in-place. Bases use YAML — Obsidian normalizes them on first open.

## Hand-installing on an existing vault

```bash
for src in scripts/bases-templates/*.base; do
  fname=$(basename "$src")
  case "$fname" in
    _Projects.base)  cp "$src" "<vault>/Projects/$fname" ;;
    _People.base)    cp "$src" "<vault>/People/$fname" ;;
    _Ideas.base)     cp "$src" "<vault>/Ideas/$fname" ;;
    _Knowledge.base) cp "$src" "<vault>/Knowledge/$fname" ;;
    _Research.base)  cp "$src" "<vault>/Research/$fname" ;;
    "_Dev Logs.base")cp "$src" "<vault>/Dev Logs/$fname" ;;
    _Tasks.base)     cp "$src" "<vault>/Tasks/$fname" ;;
    _Logs.base)      cp "$src" "<vault>/Logs/$fname" ;;
  esac
done
```

Then refresh stats: `python scripts/vault_stats.py --vault <vault>`
