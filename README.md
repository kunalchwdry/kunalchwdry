
<div align="center">

# Kunal Choudhary

<a href="https://github.com/kunalchwdry">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&pause=1200&color=58A6FF&center=true&vCenter=true&width=720&lines=AI+Engineer+in+Progress;Backend+%26+Intelligent+Systems;AI+products+built+on+secure+foundations;Data+%C2%B7+Automation+%C2%B7+Real-World+Workflows;Mission+2030" alt="Typing SVG" />
</a>

**AI Engineer in Progress · AI Builder · Backend & Intelligent Systems**

I build intelligent systems that connect **AI, software engineering, data, automation, and real-world workflows**.<br/>
2nd-year BE AI & Data Science student from India, working across LLM applications, voice AI, secure backends, and adaptive systems.

[![GitHub](https://img.shields.io/badge/GitHub-kunalchwdry-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kunalchwdry)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Add_Link-0d1117?style=for-the-badge&logo=linkedin&logoColor=0A66C2)](#connect)
![Profile Views](https://komarev.com/ghpvc/?username=kunalchwdry&color=0d1117&style=for-the-badge&label=PROFILE+VIEWS)

[Currently Building](#currently-building) · [Philosophy](#engineering-philosophy) · [Projects](#featured-projects) · [Tech Stack](#tech-stack) · [GitHub Activity](#github-activity) · [Mission 2030](#mission-2030)

</div>

---

## About

```yaml
name: Kunal Choudhary
role: AI Engineer in Progress
education: BE Artificial Intelligence & Data Science (2nd year)
location: India

direction: AI Engineering → Intelligent Systems → AI Products → AI Infrastructure

builds:
  - Secure backend platforms (JWT, RBAC, PostgreSQL RLS)
  - Server-authoritative transactional systems
  - LLM-powered and voice-first applications
  - Adaptive productivity systems
  - Desktop and workflow automation
  - Embedded speech-processing systems

approach: building → learning → experimenting → shipping
mission: 2030
```

---

## Currently Building

| Area | What that looks like in my projects |
|---|---|
| `AI / LLM Applications` | Gemini-powered assistants, multi-provider LLM architecture with failover |
| `Voice AI` | Conversational voice pipelines with STT → LLM → TTS |
| `Backend Engineering` | FastAPI services, JWT auth, RBAC, audit logging, integration testing |
| `Data Systems` | PostgreSQL / Supabase schema design, Row Level Security, transactional logic |
| `Adaptive Systems` | Productivity loops that plan, measure, and adapt |
| `Automation` | Voice-driven desktop control, browser automation, app launching |
| `Embedded AI` | ESP32-S3 + ESP-SR speech processing and noise cancellation |

---

## Engineering Philosophy

I don't treat AI as a feature bolted onto an app. Intelligence is only as reliable as the data, backend, and authorization layers underneath it.

```mermaid
flowchart LR
    P["Problem"] --> S["System Design"]
    S --> D["Data Model"]
    D --> B["Backend & Security"]
    B --> AI["AI / Intelligence"]
    AI --> UX["User Experience"]
    UX --> M["Measure"]
    M --> I["Iterate"]
    I -.-> P

    classDef core fill:#0d1117,stroke:#58a6ff,color:#c9d1d9;
    class P,S,D,B,AI,UX,M,I core;
```

- **Foundations first** — schema design, server-side validation, and access control before AI.
- **Structured context over loose prompts** — AI works better when it reasons over well-modeled data.
- **Server-authoritative logic** — critical state (permissions, rewards, records) is never trusted to the client.

---

## Featured Projects

### Project Map

```mermaid
flowchart TB
    ME(("Kunal"))

    ME --> SEC["Secure Backend Systems"]
    ME --> ADP["Adaptive Systems"]
    ME --> VOICE["Voice & Speech AI"]
    ME --> AUTO["AI Automation"]
    ME --> DATA["Data & AI"]

    SEC --> TRAXIS["TRAXIS"]
    SEC --> QB["Questbound"]
    ADP --> QB
    ADP --> IL["InnerLoop"]
    VOICE --> ANAYA["Anaya Health Assistant"]
    VOICE --> SC["SHIELD-COM"]
    VOICE --> NL["NoLimi"]
    AUTO --> NL
    DATA --> DV["DataVortex"]

    classDef me fill:#1f6feb,stroke:#58a6ff,color:#ffffff;
    classDef theme fill:#161b22,stroke:#30363d,color:#c9d1d9;
    classDef proj fill:#0d1117,stroke:#58a6ff,color:#58a6ff;
    class ME me;
    class SEC,ADP,VOICE,AUTO,DATA theme;
    class TRAXIS,QB,IL,ANAYA,SC,NL,DV proj;
```

### Overview

| Project | Domain | Core Stack | Repository |
|---|---|---|---|
| **TRAXIS** | Polar expedition logistics & asset management | React · Vite · TypeScript · FastAPI · PostgreSQL · Supabase | [Traxis](https://github.com/kunalchwdry/Traxis) |
| **Questbound** | Life RPG / gamified adaptive productivity | Next.js · React · PostgreSQL · Supabase · Drizzle ORM | [Questbound](https://github.com/kunalchwdry/Questbound) |
| **InnerLoop** | Student productivity & continuous improvement | React · Vite · Supabase · PostgreSQL · Tailwind CSS | — |
| **Anaya Health Assistant** | Voice AI for healthcare access | LiveKit Agents · Gemini · Deepgram · Murf Falcon · SQLite | [anaya-health-assistant](https://github.com/kunalchwdry/anaya-health-assistant) |
| **SHIELD-COM** | Embedded speech processing for soldier communication | ESP32-S3 · ESP-SR | — |
| **NoLimi** | Personal AI desktop assistant | Python · Gemini API · Speech Recognition · TTS | — |
| **DataVortex** | Data / AI project | *Documentation in progress* | — |

> Click any section below to expand the architecture and engineering details.

---

### TRAXIS

**Integrated Polar Expedition Logistics & Asset Management System**

`Smart India Hackathon 2026` · `Problem Statement 26062` · `MoES / NCPOR`

A multi-tenant operational platform for managing polar expeditions — personnel, cargo, assets, inventory, incidents, and organization access — with authorization enforced on the server and at the database layer.

`React` `Vite` `TypeScript` `FastAPI` `PostgreSQL` `Supabase` `JWT` `RBAC` `RLS`

<details>
<summary><b>Authorization Pipeline</b></summary>

<br/>

Every request passes through a server-authoritative chain. The client never decides what a user is allowed to see or change.

```mermaid
sequenceDiagram
    autonumber
    participant C as React Client
    participant API as FastAPI
    participant J as JWT Verification
    participant O as Organization Resolution
    participant R as RBAC / Scoped Permissions
    participant DB as PostgreSQL + RLS

    C->>API: Request with access token
    API->>J: Verify token
    J-->>API: Authenticated user
    API->>O: Resolve organization context
    O-->>API: Tenant scope
    API->>R: Check role and scoped permissions
    R-->>API: Allowed / denied
    API->>DB: Query within tenant scope
    DB-->>API: Rows filtered by RLS policies
    API-->>C: Authorized response
```

- **Defense in depth** — authorization is checked in the API layer *and* enforced by PostgreSQL Row Level Security.
- **Multi-tenancy** — organization resolution scopes every operation to the correct tenant.
- **Auditability** — audit logging records operational actions.

</details>

<details>
<summary><b>Operational Domain Model</b></summary>

<br/>

```mermaid
flowchart LR
    ORG["Organization"] --> ACC["Access Workflows"]
    ORG --> EXP["Expedition Lifecycle"]
    EXP --> PER["Personnel"]
    EXP --> CAR["Cargo"]
    EXP --> AST["Assets"]
    EXP --> INV["Inventory"]
    EXP --> INC["Incidents"]

    PER --> AUD["Audit Log"]
    CAR --> AUD
    AST --> AUD
    INV --> AUD
    INC --> AUD
    ACC --> AUD

    classDef node fill:#0d1117,stroke:#58a6ff,color:#c9d1d9;
    classDef audit fill:#161b22,stroke:#f78166,color:#f78166;
    class ORG,ACC,EXP,PER,CAR,AST,INV,INC node;
    class AUD audit;
```

</details>

<details>
<summary><b>What I Built</b></summary>

<br/>

- Designed a multi-tenant architecture for polar expedition logistics.
- Implemented JWT authentication with role-based access control and scoped permissions.
- Secured data access with PostgreSQL Row Level Security.
- Modeled expedition lifecycle, personnel, cargo, assets, inventory, and incident workflows.
- Built organization access workflows for tenant onboarding and membership.
- Added audit logging for operational traceability.
- Wrote backend integration tests to validate authorization and workflow behavior.

</details>

---

### Questbound

**A Life RPG — Gamified Adaptive Productivity Platform**

Questbound turns productivity into an adaptive game system. Quests, XP, gold, attributes, and streaks are calculated by a server-side transactional engine, while an AI companion — the Oracle — adapts to the user's emotional context.

`Next.js` `React` `PostgreSQL` `Supabase` `Drizzle ORM` `Multi-Provider LLM` `Naive Bayes`

<details>
<summary><b>Server-Authoritative Game Engine</b></summary>

<br/>

Rewards are never calculated on the client. Every progression change is validated and committed as a transaction.

```mermaid
flowchart LR
    A["Player completes quest"] --> B["Server API"]
    B --> C{"Authorized<br/>& valid?"}
    C -- No --> X["Reject request"]
    C -- Yes --> D["Begin Transaction"]
    D --> E["Calculate XP & Gold"]
    E --> F["Update Attributes"]
    F --> G["Update Streaks"]
    G --> H["Commit"]
    H --> I["Return new player state"]

    classDef ok fill:#0d1117,stroke:#3fb950,color:#c9d1d9;
    classDef bad fill:#0d1117,stroke:#f85149,color:#f85149;
    class A,B,D,E,F,G,H,I ok;
    class X bad;
```

- **Anti-cheat by design** — the client submits actions, the server decides outcomes.
- **Transactional integrity** — XP, gold, attributes, and streaks update atomically.

</details>

<details>
<summary><b>Oracle AI Companion</b></summary>

<br/>

```mermaid
flowchart LR
    U["User message"] --> NB["Local Naive Bayes<br/>Emotion Classification"]
    NB --> CTX["Context Builder<br/>emotion + player state"]
    CTX --> RT["LLM Provider Router"]
    RT --> P1["Primary Provider"]
    RT -. failover .-> P2["Fallback Provider"]
    P1 --> RES["Oracle Response"]
    P2 --> RES

    classDef n fill:#0d1117,stroke:#a371f7,color:#c9d1d9;
    class U,NB,CTX,RT,P1,P2,RES n;
```

- **Local emotion classification** with Naive Bayes — lightweight, runs without an external API call.
- **Multi-provider LLM architecture** with failover for resilience.

</details>

<details>
<summary><b>What I Built</b></summary>

<br/>

- Engineered a server-side transactional game engine for quests, XP, gold, attributes, and streaks.
- Designed server-authoritative reward calculation with authorization checks.
- Integrated adaptive planning into the RPG progression model.
- Built the Oracle AI companion with multi-provider LLM routing and failover.
- Implemented local Naive Bayes emotion classification.
- Added community and social features around shared progress.

</details>

---

### InnerLoop

**AI-Powered Student Productivity & Continuous-Improvement Platform**

A connected system that moves students from knowing their day to measurable improvement — built on structured student context and an AI-ready architecture.

`React` `Vite` `Supabase` `PostgreSQL` `Tailwind CSS`

<details>
<summary><b>The Improvement Loop</b></summary>

<br/>

```mermaid
flowchart LR
    K["Know Your Day"] --> PL["Plan"]
    PL --> F["Focus"]
    F --> H["Build Habits"]
    H --> L["Learn"]
    L --> M["Measure"]
    M --> AD["Adapt"]
    AD -.-> K

    CTX[("Structured Student Context<br/>timetable · tasks · goals<br/>habits · focus · learning")]
    CTX --- PL
    CTX --- M

    AI["AI Context & Reasoning Layer<br/>(planned)"]
    CTX -. planned .-> AI

    classDef built fill:#0d1117,stroke:#3fb950,color:#c9d1d9;
    classDef planned fill:#0d1117,stroke:#8b949e,color:#8b949e,stroke-dasharray: 5 5;
    class K,PL,F,H,L,M,AD,CTX built;
    class AI planned;
```

</details>

<details>
<summary><b>Build Status</b></summary>

<br/>

| Component | Status |
|---|---|
| Timetable context | Implemented |
| Tasks & goals | Implemented |
| Habits & focus | Implemented |
| Learning tracking | Implemented |
| Analytics | Implemented |
| Adaptive planning foundations | Implemented |
| Structured, AI-ready data architecture | Implemented |
| Full AI context & reasoning layer | **Planned** |

</details>

**Connection to Questbound:** both explore adaptive productivity — InnerLoop through structured planning and analytics, Questbound through game mechanics. They are separate projects.

---

### Anaya Health Assistant

**Voice AI for Accessible Healthcare Information**

A voice-first conversational assistant focused on healthcare access, Hinglish and Indian-language accessibility, and a strictly non-diagnostic, non-prescriptive design.

`LiveKit Agents` `SIP` `Gemini` `Deepgram` `Murf Falcon` `SQLite`

<details>
<summary><b>Voice Pipeline</b></summary>

<br/>

```mermaid
flowchart LR
    U["User<br/>voice / call"] --> LK["LiveKit Agents / SIP"]
    LK --> STT["Deepgram<br/>Speech-to-Text"]
    STT --> LLM["Gemini<br/>+ safety boundaries"]
    LLM --> TTS["Murf Falcon<br/>Text-to-Speech"]
    TTS --> LK
    LK --> U
    LLM <--> DB[("SQLite")]

    classDef n fill:#0d1117,stroke:#58a6ff,color:#c9d1d9;
    class U,LK,STT,LLM,TTS,DB n;
```

</details>

<details>
<summary><b>Design Principles</b></summary>

<br/>

- **Voice-first** — lowers the barrier for users who find text interfaces difficult.
- **Hinglish / Indian-language accessibility** — designed around how users actually speak.
- **Non-diagnostic & non-prescriptive** — provides information and guidance, not diagnoses or prescriptions.

</details>

---

### SHIELD-COM

**Embedded AI Speech Processing for Soldier Communication**

A hardware-software system exploring active noise cancellation and neural speech processing for communication in noisy operational environments.

`ESP32-S3` `ESP-SR` `Embedded Systems` `Speech Processing`

<details>
<summary><b>System Flow</b></summary>

<br/>

```mermaid
flowchart LR
    MIC["Voice input<br/>noisy environment"] --> MCU["ESP32-S3"]
    MCU --> SR["ESP-SR<br/>neural speech processing"]
    SR --> ANC["Active noise cancellation"]
    ANC --> OUT["Clearer communication output"]

    classDef n fill:#0d1117,stroke:#d29922,color:#c9d1d9;
    class MIC,MCU,SR,ANC,OUT n;
```

- Hardware-software integration on the ESP32-S3.
- On-device speech processing using the ESP-SR framework.

</details>

---

### NoLimi

**Personal AI Desktop Assistant**

A Python assistant that combines natural-language interaction with desktop automation.

`Python` `Gemini API` `Speech Recognition` `Text-to-Speech` `Browser Automation`

<details>
<summary><b>Command Flow</b></summary>

<br/>

```mermaid
flowchart LR
    V["Voice command"] --> SR["Speech Recognition"]
    SR --> G["Gemini API<br/>natural-language understanding"]
    G --> R{"Action Router"}
    R --> B["Browser Automation"]
    R --> A["Application Launching"]
    R --> S["System Controls"]
    R --> C["Conversational Reply"]
    B --> T["Text-to-Speech"]
    A --> T
    S --> T
    C --> T

    classDef n fill:#0d1117,stroke:#3fb950,color:#c9d1d9;
    class V,SR,G,R,B,A,S,C,T n;
```

- **Broader direction:** `AI + Desktop Automation + Cybersecurity` — an ongoing direction, not a completed feature set.

</details>

---

### DataVortex

**Data / AI Project**

<details>
<summary><b>Details</b></summary>

<br/>

Project documentation is being finalized. Architecture, stack, and context will be added here.

</details>

---

## Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,fastapi,postgres,supabase,sqlite,react,nextjs,ts,vite,tailwind,git,github&theme=dark" alt="Tech Stack" />

</div>

<br/>

| Layer | Technologies |
|---|---|
| **AI / LLM** | `Gemini API` · `Multi-Provider LLM Routing` · `Naive Bayes` · `NLP` |
| **Voice & Speech** | `LiveKit Agents` · `SIP` · `Deepgram` · `Murf Falcon` · `Speech Recognition` · `Text-to-Speech` · `ESP-SR` |
| **Backend** | `Python` · `FastAPI` · `REST APIs` · `JWT` · `RBAC` · `Audit Logging` · `Integration Testing` |
| **Data** | `PostgreSQL` · `Supabase` · `Row Level Security` · `Drizzle ORM` · `SQLite` · `Transactional Systems` |
| **Frontend** | `React` · `Next.js` · `TypeScript` · `Vite` · `Tailwind CSS` |
| **Embedded** | `ESP32-S3` |
| **Tools** | `Git` · `GitHub` · `Browser Automation` |

---

## GitHub Activity

<div align="center">

<img src="https://streak-stats.demolab.com?user=kunalchwdry&theme=tokyonight&hide_border=true&background=0D1117&ring=58A6FF&fire=58A6FF&currStreakLabel=58A6FF" alt="GitHub Streak" />

<br/><br/>

<img height="170" src="https://github-readme-stats.vercel.app/api?username=kunalchwdry&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&include_all_commits=true&count_private=true" alt="GitHub Stats" />
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=kunalchwdry&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&langs_count=8" alt="Top Languages" />

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=kunalchwdry&theme=tokyo-night&hide_border=true&bg_color=0D1117&color=58A6FF&line=58A6FF&point=FFFFFF" alt="Contribution Graph" width="100%" />

</div>

---

## What I Like Building

| | |
|---|---|
| **AI-powered applications** | LLM assistants, voice agents, AI companions |
| **Secure backend platforms** | Multi-tenant APIs with RBAC, RLS, and audit trails |
| **Adaptive systems** | Products that measure behavior and adapt over time |
| **Automation tools** | Voice-driven desktop and browser automation |
| **Embedded AI** | On-device speech processing on microcontrollers |
| **Real-world operational software** | Logistics, healthcare access, student workflows |

---

## Engineering Interests

`Artificial Intelligence` · `Machine Learning` · `Generative AI` · `LLMs & Agents` · `Voice AI` · `Backend Systems` · `Data Systems` · `Computer Vision` · `Cybersecurity` · `Embedded AI` · `Developer Tools` · `Intelligent Automation`

---

## Current Learning

<details open>
<summary><b>What I'm going deeper on</b></summary>

<br/>

| Track | Focus |
|---|---|
| **ML Foundations** | Core machine learning concepts and model training |
| **Deep Learning** | PyTorch and neural-network workflows |
| **LLM Systems** | RAG, agentic architectures, evaluation |
| **Backend Engineering** | API design, testing, reliability |
| **System Design** | Data modeling, authorization, scalable architecture |

```text
building → learning → experimenting → shipping → repeat
```

</details>

---

## Mission 2030

```mermaid
flowchart LR
    A["AI Engineering"] --> B["Intelligent Systems"]
    B --> C["AI Products"]
    C --> D["AI Infrastructure"]

    classDef n fill:#0d1117,stroke:#58a6ff,color:#58a6ff;
    class A,B,C,D n;
```

> Build deep technical foundations, ship increasingly complex AI systems, and grow into an engineer capable of designing intelligent systems end-to-end.

---

## Connect

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-kunalchwdry-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kunalchwdry)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Add_Link-0d1117?style=for-the-badge&logo=linkedin&logoColor=0A66C2)](#connect)

<sub>Open to collaborating on AI systems, backend platforms, and real-world intelligent software.</sub>

</div>

<!--
TODO:
1. Replace "#connect" in both LinkedIn badges with your real LinkedIn URL.
2. Add repository links for InnerLoop, SHIELD-COM, NoLimi, and DataVortex once public.
3. Fill in the DataVortex section with verified project details.
-->
