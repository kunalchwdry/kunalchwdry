# GitHub profile update — Kunal Choudhary

This package contains the **ultimate arcade edition** animated profile README, 22 original GIFs, a contribution-snake SVG built from your public calendar, 12 playable mini-games with 20+ modes, and paste-ready account settings. It does not change your GitHub account automatically.

The main `README.md` includes cyberpunk code rain, orbiting particles, a coding robot, a Questbound finalist achievement reveal, animated project flows, a voice waveform, neon dividers, a contribution snake, and an ultimate Arcade Zone (12 games) with game previews and full mode packs. **Upload `README.md`, the complete `assets` folder, and the `games` folder together. Pasting only the Markdown will not include the custom animations or games.**

`animated-preview.html` embeds the graphics for an offline preview; its activity widgets are a snapshot. The project diagrams, robot and game previews are decorative illustrations, not live telemetry or call recordings. The snake's calendar levels were read from the public GitHub calendar for 2025-10-12 through 2026-10-11; its motion is decorative and its data is a dated snapshot. The data and sources are included in `assets/contribution-calendar.json`. All 12 games are client-side only, no trackers, no external APIs.

External typing and statistics widgets still use their original service URLs on GitHub. The earlier text-only version is retained as `README-clean.md`.

## 1. Profile settings

Open your GitHub profile → **Edit profile**.

**Name**

```text
Kunal Choudhary
```

**Bio — 140 characters, within GitHub's 160-character limit**

```text
BE AI & Data Science student building AI apps, backend systems and reproducible data pipelines. Python, TypeScript, PostgreSQL. Pune, India.
```

**Location**

```text
Pune, India
```

**Website**

```text
https://www.linkedin.com/in/kunal-choudhary-918270425/
```

If you use GitHub's separate LinkedIn/social field, put this URL there. You can leave Website empty until you have a portfolio site rather than repeating the same link twice.

## 2. Upload the ultimate arcade profile

1. Download and unzip `github-profile-animation-pack.zip`.
2. Open **https://github.com/kunalchwdry/kunalchwdry**.
3. Use **Add file → Upload files** to upload/replace `README.md`, the entire `assets` folder (22 GIFs + snake SVG + calendar JSON), and the entire `games` folder (12 HTML games). Preserve folder names: README uses paths such as `./assets/system-orbit.gif` and `./games/snake.html`.
4. Preview the README and commit the files. If you use Git locally, copy README, assets and games into the profile repository, then commit and push together.
5. **Enable Pages to make games playable:** Settings → Pages → Source: Deploy from a branch → Branch: main / root → Save. Games will then be at `https://kunalchwdry.github.io/kunalchwdry/games/` (hub) and each `.../games/*.html`.

The setup document is for your reference. You do not need to publish it, the HTML preview, or the animation generators for the images and games to work.

Suggested commit message:

```text
docs: simplify profile and highlight selected projects
```

The revised README keeps Mission 2030, your four main public projects, reported project metrics, learning focus, additional prototypes, contribution snake and ultimate Arcade Zone (12 games, 20+ modes), with custom animated illustrations and typing effects. Additional work and statistics remain collapsible. The inaccessible TRAXIS repository link is omitted; FlowCare's fork attribution and Anaya's starter attribution are explicit. Games are original client-side puzzles, not claims of hacking ability, and all modes are local difficulty variants, not online multiplayer.

## 3. Recommended pins

Use **Customize your pins** on your profile. Feature these repositories in this order:

1. **Questbound** — product depth and the Tech Zephyr finalist milestone.
2. **data-vortex-2026** — data/ML work, evaluation and reproducibility.
3. **anaya-health-assistant** — voice AI and applied health-information workflows.
4. **FlowCare** — healthcare data modeling and backend work; keep the fork attribution clear.

Don't use a showcase slot for `kunalchwdry`: its README already appears on your profile. Keep NoLimi available in your repositories and the collapsed "More work & prototypes" section, rather than using it as a flagship pin.

For FlowCare, describe the specific contributions you actually made in the repository README; don't claim the upstream project's complete implementation as your own. If you haven't made substantive changes to the fork, feature only the first three pins.

## 4. Paste-ready repository descriptions

Open each repository → **About** → gear icon → update Description.

### Questbound

```text
A productivity life RPG with server-authoritative quests, XP, gold and streaks, plus an AI companion. Built with Next.js, PostgreSQL and Supabase.
```

### data-vortex-2026

```text
A reproducible three-round data science pipeline for corrupted-data restoration, NLP evaluation and live signal analysis using Python, scikit-learn and SQLite.
```

### anaya-health-assistant

```text
A Hinglish-oriented health-information voice assistant using LiveKit, Gemini, Deepgram and Murf. A prototype, not a diagnostic or prescribing service.
```

### FlowCare

```text
A public fork of FlowCare, a provenance-aware hospital-discovery and appointment platform built with Next.js, TypeScript and Supabase.
```

### NoLimi

```text
A Python desktop-assistant prototype combining Gemini, voice interaction, browser automation and application launching.
```

### kunalchwdry

```text
My GitHub profile README: selected projects, tools and learning focus in backend systems, applied AI and reproducible data workflows.
```

## 5. Final check before publishing

- Keep the second-year student wording only while it is current.
- Confirm the Questbound finalist wording and project metrics against your own records; the edit preserves your supplied claims, not independent verification of them.
- Check that the FlowCare demo still opens. The README labels it as a demo, not verified live hospital operations.
- Keep InnerLoop explicitly separate from Questbound and its full AI reasoning layer marked as planned.
- Add a public TRAXIS link only when you have a working, shareable URL.
- Keep hardware concepts and health-information prototypes labeled accurately.
