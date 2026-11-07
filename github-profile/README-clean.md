<div align="center">

<h1>Kunal Choudhary</h1>
<p><strong>AI & Data Science student · Backend systems · Applied AI</strong></p>
<p>Pune, India · Foundations first. Then intelligence.</p>

[LinkedIn](https://www.linkedin.com/in/kunal-choudhary-918270425/) · [Selected projects](#selected-projects) · [Current focus](#current-focus)

</div>

I'm a second-year **BE Artificial Intelligence & Data Science** student building AI applications, backend systems and reproducible data pipelines.

I care about the engineering behind the demo: **authorization, data quality, evaluation and failure handling**. My long-term direction is AI infrastructure; my current work is about getting the foundations right.

## Selected projects

### ⚔️ [Questbound](https://github.com/kunalchwdry/Questbound) — Productivity as a life RPG

Turn real-world tasks into quests, XP, gold, attributes and streaks, supported by an AI companion called the Oracle.

- **Engineering focus:** server-authoritative rewards, transactional progression and multi-provider LLM routing.
- **Design choice:** deterministic code governs critical state; the LLM supports the conversational layer.
- **Recognition:** Tech Zephyr 4.0 Grand Finale Finalist, IIT Bhubaneswar.

**Stack:** Next.js · TypeScript · PostgreSQL · Supabase · Drizzle ORM

### 🌀 [DataVortex](https://github.com/kunalchwdry/data-vortex-2026) — Data restoration to live analysis

A three-round data science pipeline for AARUUSH '26: restore corrupted data, evaluate NLP models and track signals in a live-collected corpus.

- **Restoration:** 12,360 raw rows → 10,221 analysis-ready records, with 27 logged repairs.
- **Evaluation:** reported macro-F1 of **0.6134** for sentiment and **0.8051** for topic classification.
- **Collection:** 10,384 records across 21 sweeps and 5 languages.

**Engineering focus:** traceable repairs, fixed splits and seeds, automated checks, and explicit error analysis. These figures describe the documented project runs; reproduction steps and limitations are in the repository.

**Stack:** Python · pandas · scikit-learn · TF-IDF · SQLite · Jupyter

### 🎙️ [Anaya](https://github.com/kunalchwdry/anaya-health-assistant) — Voice-first health information

A Hinglish-oriented voice assistant exploring basic health information and healthcare facility discovery through natural conversation.

- **Pipeline:** speech-to-text → language model → text-to-speech, connected through LiveKit.
- **Engineering focus:** caller memory, facility lookup and specialist handoffs.
- **Scope:** a health-information prototype, not a diagnostic, prescribing or emergency-response service.

**Stack:** LiveKit Agents · Gemini · Deepgram · Murf Falcon · SIP · SQLite

*Built on the [Murf/LiveKit starter](https://github.com/murf-ai/murf-livekit-starter), with Anaya-specific voice and health-access workflows.*

### 🏥 [FlowCare](https://github.com/kunalchwdry/FlowCare) — Provenance-aware healthcare discovery

Hospital discovery and appointment workflows built around a question: **where did this information come from, and how fresh is it?**

- **Engineering focus:** per-fact provenance, relationship-scoped access and explicit stale or unavailable states.
- **Workflow focus:** appointment requests, staff-scoped operations and server-side state transitions.
- **Status:** demo-backed flows are distinct from verified live hospital integrations.

**Stack:** Next.js · TypeScript · Supabase · PostgreSQL · RLS · Zod · Vitest

[Demo](https://flowcare-five.vercel.app) · [Upstream project](https://github.com/slicqq/FlowCare)

*Public fork of [slicqq/FlowCare](https://github.com/slicqq/FlowCare); the upstream project and this fork's changes are linked separately.*

<details>
<summary><strong>More work & prototypes</strong></summary>

<br/>

- **TRAXIS** — A team project/concept for multi-tenant polar-expedition logistics, assets and inventory. Focus: JWT verification, RBAC and tenant-scoped operations. **React · FastAPI · PostgreSQL.** Smart India Hackathon 2026 work; no public repository linked here.
- **InnerLoop** — A separate student-productivity project for planning, focus, habits and analytics. **React · Vite · Supabase.** Foundational workflows are implemented; the full AI reasoning layer is planned. This is separate from Questbound.
- **SHIELD-COM** — An embedded speech-processing concept for noisy environments. **ESP32-S3 · ESP-SR.** Smart India Hackathon 2026 team/internal-round work; intended architecture, not a production-validated system.
- **[NoLimi](https://github.com/kunalchwdry/NoLimi)** — A Python desktop-assistant prototype combining voice interaction, Gemini, browser automation and application launching.

</details>

## Tools I use

| Area | Technologies |
| --- | --- |
| **Backend** | Python, FastAPI, Next.js route handlers, validation |
| **Data** | PostgreSQL, Supabase, SQLite, Drizzle ORM |
| **AI & ML** | Gemini, NLP, scikit-learn, TF-IDF, Naive Bayes, evaluation |
| **Voice** | LiveKit, Deepgram, Murf Falcon, SIP |
| **Frontend** | TypeScript, React, Next.js, Vite, Tailwind CSS |
| **Workflow** | Git, Linux, automated testing, reproducible pipelines |

## Current focus

- Strengthening **ML foundations and PyTorch** through practical model workflows.
- Learning **RAG, agentic systems and LLM evaluation**, including failure analysis.
- Improving **backend reliability** through authorization, testing and better data modeling.

## How I approach building

- **The server owns critical state.** Permissions and rewards should not be decided by the browser.
- **Claims need evidence.** Data and metrics should be traceable, reproducible and accompanied by limitations.
- **Failure modes are part of the product.** Validate inputs, test boundaries and surface errors clearly.

## Let's connect

Open to collaborating on **AI applications, backend systems, voice interfaces and data pipelines**.

[Connect on LinkedIn](https://www.linkedin.com/in/kunal-choudhary-918270425/)

---

**Mission 2030:** build toward AI infrastructure through strong foundations, useful products and measurable progress.
