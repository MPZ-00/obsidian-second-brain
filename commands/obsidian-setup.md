---
description: Interactive per-user setup - configure vault path, enable/disable commands, wire hooks
category: meta
triggers_en: ["setup brain", "configure commands", "disable commands", "enable commands", "obsidian setup", "setup obsidian"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-setup`:

1. Read `_CLAUDE.md` at the vault root if it exists — extract the current `disabled_commands:` list (default: empty = all commands enabled).

2. Print the full command catalog grouped by category, showing enabled/disabled status for each:

   **Core vault** — save, log, task, project, person, capture, find, adr, init, projects
   **Vault health** — health, reconcile
   **Thinking tools** — challenge, emerge, connect, graduate
   **Research** — research, research-deep, x-read, youtube, x-pulse, notebooklm
   **Planning** — daily, recap, review, board
   **Advanced** — world, synthesize, ingest, decide, visualize, export, learn
   **Utilities** — create-command, obsidian-setup

3. Ask which commands or groups to disable. Accept group names ("disable thinking tools", "disable planning") or individual command names ("disable x-pulse, notebooklm"). Leave core vault and vault health enabled by default.

4. Show the updated enabled/disabled list and ask the user to confirm before writing.

5. Write the `disabled_commands:` block to `_CLAUDE.md`. If the block already exists, replace it in place. Format:

   ```yaml
   disabled_commands:
     - obsidian-challenge
     - obsidian-emerge
   ```

6. Ask if the user wants to wire the SessionStart hook (auto-injects `_CLAUDE.md` into every session):
   - If yes: ask for the vault path if not already known, then run `bash scripts/setup.sh "<vault-path>"` or print the exact `~/.claude/settings.json` snippet to add manually.
   - If no: skip silently.

7. Summarize what changed.
