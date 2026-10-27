# Upload the ultimate arcade profile — 12 games + modes

## What to upload

1. Download and unzip `github-profile-animation-pack.zip` (16 MiB, 44 files).
2. Open https://github.com/kunalchwdry/kunalchwdry.
3. Upload/replace **`README.md`, the complete `assets` folder (22 GIFs + snake SVG + calendar JSON), and the complete `games` folder (12 HTML games)** together. Keep folder names unchanged.
4. Preview README and commit.
5. **Enable GitHub Pages:** Settings → Pages → Source: Deploy from a branch → Branch: main, Folder: / (root) → Save. Wait ~1 minute.

After Pages:
- Hub: `https://kunalchwdry.github.io/kunalchwdry/games/`
- Each game: `.../games/snake.html`, `memory.html`, `quest.html`, `hacker.html`, `2048.html`, `tetris.html`, `minesweeper.html`, `flappy.html`, `bug.html`, `typing.html`, `dungeon.html`, `runner.html`

**Pasting only README is not enough.** Custom animations use `./assets/` and games use `./games/`.

## Included — 22 GIFs + 12 games

### GIFs
- 4 core game previews: snake, memory, quest, hacker
- 8 new game previews: 2048, tetris, mines, flappy, bug, typing, dungeon, runner
- 10 motion assets: cyberpunk-console, coding-mascot, achievement-unlock, system-orbit, quest-flow, datavortex-flow, anaya-wave, flowcare-provenance, system-pipeline, neon-divider
- 1 SVG: contribution-snake.svg (16 animated segments, 365 actual public-calendar days, export date inside graphic)
- 1 JSON: contribution-calendar.json (sources + levels)

### Games — 12 total, all original, client-side only, no trackers

**Core 4 — Now with full mode packs:**
- **Neon Snake:** Classic (walls kill), No Walls wrap, Obstacles 5 blocks, Portal teleport. Difficulties: Easy 150ms, Normal 110ms, Hard 80ms, Insane 55ms. Power-up P slows 3s.
- **Memory Matrix:** Easy 4×4/8 pairs, Normal 4×5/10 pairs, Hard 6×6/18 pairs, Blitz 60s timed, Extreme 90s + 40 moves limit.
- **Questbound Clicker:** Normal, Hardcore 2× slower 2× gold, Speedrun race to lvl 25, Boss Rush boss every 5, Idle 3× passive. Prestige ×1.5 multiplier, boss HP bar.
- **Neon Breach:** Easy 3 chars/8 tries/A-F,0-1, Normal 4/10/A-F,0-3, Hard 5/10/A-F,0-5, Extreme 6/8/A-F,0-7, Timed 60s unlimited, Mastermind no repeats. Hint (costs attempt) + streak.

**Arcade Classics (4 new):**
- **Tech 2048:** Merge PY→TS→PG→RE→...→2048. Arrows/WASD, swipe, undo, best saved.
- **Stack Builder Tetris:** Classic Tetris, 10 lines = level up, next preview.
- **Code Mines:** Minesweeper 9×9/10 to 20×20/80 mines. Left reveal, right flag/long-press.
- **Flappy Code:** Flap through { } [ ] gaps. Easy wider, Hard narrow, Insane tiny, Reverse flips gravity every 5.

**Coding + RPG (4 new):**
- **Bug Squasher:** Click green 🐛 bugs, avoid red ✨ features in Hard/Insane. Normal/Hard/Insane/Zen. Accuracy tracking.
- **Typing Blitz:** Type code snippets JS/Python/SQL/Mixed/Hard no-backspace. WPM + accuracy, 60s.
- **Dungeon Crawler:** Questbound RPG — random walk map, HP, gold, XP, exit 🚪 to next floor. Normal/Hard/Rogue permadeath/Explorer 12×12.
- **XP Runner:** Endless runner — Space/Tap to jump, avoid bugs, collect XP orbs. Easy/Hard/Insane/Double Jump (2 jumps).

All scores/best saved in localStorage per mode.

## Optional: regenerate animations

```bash
python -m pip install pillow numpy
python animation-source.py
python extra-animation-source.py
python game-preview-source.py
python game-preview-source-v2.py
```

DejaVu fonts used when available, fallback otherwise.

### Refresh only the contribution snake

```bash
python -m pip install pillow numpy requests beautifulsoup4
python extra-animation-source.py --refresh-snake
```

Reads public calendar, updates `assets/contribution-calendar.json` and `assets/contribution-snake.svg`. Upload changed files after. Use `--as-of YYYY-MM-DD` for specific date. Fails rather than inventing data if calendar cannot be read.

Nothing has been published to your GitHub account automatically.
