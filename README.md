::: {align="center"}
`<img src="https://capsule-render.vercel.app/api?type=waving&height=230&color=0:050816,35:0d1b3d,70:123a66,100:7c3aed&text=KUNAL%20CHOUDHARY&fontSize=46&fontColor=ffffff&fontAlignY=35&desc=BUILDING%20INTELLIGENT%20SYSTEMS%20%E2%80%A2%20MISSION%202030&descAlignY=57&descSize=16&animation=fadeIn" width="100%" alt="Kunal Choudhary — Mission 2030"/>`{=html}
`<a href="https://readme-typing-svg.demolab.com">`{=html}
`<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=19&pause=1100&color=58A6FF&center=true&vCenter=true&width=850&lines=AI+ENGINEERING+%2F+BACKEND+SYSTEMS;DATA+INTEGRITY+%E2%86%92+INTELLIGENCE+%E2%86%92+IMPACT;TECH+ZEPHYR+4.0+%7C+GRAND+FINALE+FINALIST;10%2C384+LIVE-COLLECTED+RECORDS+%7C+p%3D0.0043;BUILD.+MEASURE.+BREAK.+REBUILD.;MISSION+2030+IS+IN+PROGRESS." alt="Animated engineering tagline"/>`{=html}
`</a>`{=html}
`<br/>`{=html}
![GitHub](https://img.shields.io/badge/GitHub-kunalchwdry-0d1117?style=for-the-badge&logo=github&logoColor=white)
![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0d1117?style=for-the-badge&logo=linkedin&logoColor=0A66C2)
![Tech](https://img.shields.io/badge/TECH%20ZEPHYR%204.0-Grand%20Finale%20Finalist-7c3aed?style=for-the-badge&logo=trophy&logoColor=white)
![Profile](https://komarev.com/ghpvc/?username=kunalchwdry&style=for-the-badge&color=0d1117&label=VISITORS)
AI engineer in progress. Systems thinker by habit. Builder by default.
I build systems where AI meets real software engineering --- from
secure APIs and data pipelines to voice-first applications and adaptive
products.
BE Artificial Intelligence & Data Science · India · Mission 2030
:::
---
``` text
┌──(kunal㉿forge-x)-[~/mission-2030]
└─$ ./status --verbose

  IDENTITY      AI ENGINEER IN PROGRESS
  SPECIALTY     Intelligent systems · Backend · Applied AI
  PRINCIPLE     Foundations first. Validate before you claim.
  LOOP          BUILD → MEASURE → LEARN → SHIP → REPEAT
  FINAL BOSS    AI INFRASTRUCTURE [NOT DEFEATED]
```
`01` / THE PLAYER
```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="60%" valign="top">
```
I'm a second-year BE AI & Data Science student focused on building the
engineering foundations behind useful AI products.
My work spans LLM applications, voice AI, backend architecture, data
science, automation, and embedded speech systems. I care about what
happens underneath the demo: authorization, data quality, failure
states, reproducibility, and whether a claim can actually be verified.
Right now, I'm building and hardening projects that turn messy
real-world workflows into systems with clear rules, traceable data, and
measurable outcomes.
Current north star: AI Engineering → Intelligent Systems → AI
Products → AI Infrastructure.
```{=html}
</td>
```
```{=html}
<td width="40%" valign="top">
```
``` yaml
player: Kunal Choudhary
class: AI Engineer
level: 02 → 99
guild: Forge-X
quest: Mission 2030

loadout:
  backend: FastAPI / Next.js
  data: PostgreSQL / Supabase
  intelligence: LLMs / NLP
  voice: STT → LLM → TTS
  mindset: ship_and_verify

boss:
  name: AI Infrastructure
  status: ACTIVE
```
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
`02` / CURRENT OPERATIONS
---
Mission                             What I'm working on
---
FlowCare                        Provenance-first hospital discovery
and outpatient coordination, with
patient and hospital workflows
TRAXIS                          Multi-tenant polar expedition
logistics, assets, inventory, and
operational access control
Questbound                      Adaptive productivity RPG with
server-authoritative progression
and an AI companion
DataVortex                      Reproducible, three-round data
science pipeline: restoration → NLP
→ live signal tracking
Learning track                  ML foundations, PyTorch,
evaluation, RAG, agentic systems,
and reliable backend design
> **Operating principle:** a feature is not finished because it works
> once. It is finished when its behavior, boundaries, and failure modes
> are understood.
---
`03` / ENGINEERING PHILOSOPHY
``` mermaid
flowchart LR
    P["Real problem"] --> S["System design"]
    S --> D["Data model"]
    D --> A["Auth & backend"]
    A --> I["AI / intelligence"]
    I --> U["User experience"]
    U --> M["Measure"]
    M --> R["Review & iterate"]
    R -.-> P

    classDef core fill:#0b1220,stroke:#58a6ff,color:#e6edf3,stroke-width:1.5px;
    class P,S,D,A,I,U,M,R core;
```
Foundations before features. Data models, server-side
validation, and access control come before AI glitter.
The server owns critical state. Permissions, rewards, and
important transitions are never trusted to the browser.
Structured context beats prompt chaos. Useful intelligence
depends on well-modeled inputs and explicit constraints.
Failures are part of the product. Loading, empty, unauthorized,
stale, and error states deserve deliberate behavior.
Evidence over impressive numbers. Metrics need a reproducible
method, a clear denominator, and honest limitations.
AI is a component, not the architecture. The surrounding system
determines whether intelligence is safe and useful.
---
`04` / PROJECT ARCHIVE
◈ FlowCare
Provenance-first healthcare discovery & outpatient coordination
![Repository](https://img.shields.io/badge/Repository-FlowCare-0d1117?style=flat-square&logo=github)
![Live](https://img.shields.io/badge/Live%20Demo-Open-1f6feb?style=flat-square&logo=vercel)
![Next.js](https://img.shields.io/badge/Next.js-15-black?style=flat-square&logo=nextdotjs)
![Supabase](https://img.shields.io/badge/Supabase-Postgres%20%2B%20RLS-3ecf8e?style=flat-square&logo=supabase)
FlowCare treats hospital discovery as a data provenance and trust
problem, not merely a directory problem. Claims should have a source,
verifier, and freshness context; when certainty is missing, the system
should expose the uncertainty rather than manufacture confidence.
Stack: Next.js 15 · TypeScript · Tailwind CSS · Supabase ·
PostgreSQL · RLS · Zod · Vitest · Vercel
``` mermaid
flowchart LR
    B["Browser"] --> R["Next.js route"]
    R --> V["Validation · auth · rate limits"]
    V --> P["Repository boundary"]
    P --> DEMO["Demo repository"]
    P --> LIVE["Supabase repository"]
    LIVE --> DB[("PostgreSQL + RLS")]
    DB --> EVT["Appointment events"]
    DB --> PROV["Provenance & freshness"]

    classDef app fill:#0b1220,stroke:#58a6ff,color:#e6edf3;
    classDef data fill:#0b1220,stroke:#3fb950,color:#e6edf3;
    class B,R,V,P,DEMO,LIVE app;
    class DB,EVT,PROV data;
```
What it explores - Hospital discovery by locality, specialty,
service, and plain-language intent. - Appointment request and
confirmation workflows with server-authoritative data. - Hospital-side
operational views scoped to staff membership and appointment
relationships. - Appointment-derived waiting and consultation signals,
with explicit stale/unavailable states. - Patient visit history and
reliability outcomes based on official appointment events. - AI-assisted
search intent extraction without allowing the model to write SQL or
confirm bookings.
Engineering focus - PostgreSQL Row Level Security and
relationship-scoped access. - Validated, version-aware appointment
transitions and idempotent event handling. - Clear separation between
demo data and live database paths. - Explicit error states rather than
silently converting database failures into empty results. - Provenance
and freshness treated as data-model concerns, not just UI labels.
Honest status note: the repository includes additive migrations for
care-access truth, appointment-derived traffic, and patient reliability.
Production behavior depends on the deployed database migration and
live-path verification; demo-backed flows should not be mistaken for
verified live hospital operations.
---
◈ TRAXIS
Polar expedition logistics & asset management
![Repository](https://img.shields.io/badge/Repository-TRAXIS-0d1117?style=flat-square&logo=github)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data-4169E1?style=flat-square&logo=postgresql)
Smart India Hackathon 2026 · Problem Statement 26062 · MoES / NCPOR
TRAXIS is a multi-tenant operations platform concept for polar
expedition logistics: personnel, cargo, assets, inventory, incidents,
and organization access workflows.
Stack: React · Vite · TypeScript · FastAPI · PostgreSQL · Supabase ·
JWT · RBAC · RLS
``` mermaid
sequenceDiagram
    participant C as Client
    participant API as FastAPI
    participant AUTH as Token verification
    participant TEN as Tenant resolver
    participant ACL as Role / permission checks
    participant DB as PostgreSQL + RLS

    C->>API: Request + access token
    API->>AUTH: Verify identity
    AUTH-->>API: Authenticated subject
    API->>TEN: Resolve organization
    TEN-->>API: Tenant context
    API->>ACL: Check role and scope
    ACL-->>API: Allow / deny
    API->>DB: Tenant-scoped operation
    DB-->>API: RLS-filtered result
    API-->>C: Authorized response
```
Engineering focus - Server-side JWT verification and role-based
authorization. - Organization-scoped operations and multi-tenant
boundaries. - PostgreSQL RLS as a second authorization layer. -
Operational models for expedition lifecycle, personnel, cargo, assets,
inventory, and incidents. - Audit logging and integration tests for
access and workflow behavior.
Core rule: the client can request an action; it does not get to
decide whether that action is allowed.
---
◈ Questbound
A life RPG powered by adaptive productivity systems
![Repository](https://img.shields.io/badge/Repository-Questbound-0d1117?style=flat-square&logo=github)
![Grand](https://img.shields.io/badge/Tech%20Zephyr%204.0-IIT%20Bhubaneswar%20Finalist-7c3aed?style=flat-square&logo=trophy)
🏆 Tech Zephyr 4.0 --- Grand Finale Finalist, IIT Bhubaneswar
Questbound turns productivity into a game system built around quests,
XP, gold, attributes, streaks, and an AI companion called the Oracle.
Selected for the offline Grand Finale, involving a pitch, live demo, and
technical Q&A.
Stack: Next.js · React · PostgreSQL · Supabase · Drizzle ORM ·
Multi-provider LLM routing · Naive Bayes
``` mermaid
flowchart LR
    Q["Quest completed"] --> API["Server API"]
    API --> V{"Authorized & valid?"}
    V -- No --> X["Reject"]
    V -- Yes --> TX["Transaction"]
    TX --> XP["Calculate XP / gold"]
    XP --> ATTR["Update attributes"]
    ATTR --> ST["Update streaks"]
    ST --> COMMIT["Commit state"]
    COMMIT --> OUT["Return player state"]

    classDef ok fill:#0b1220,stroke:#58a6ff,color:#e6edf3;
    classDef bad fill:#220d12,stroke:#f85149,color:#f85149;
    class Q,API,TX,XP,ATTR,ST,COMMIT,OUT ok;
    class X bad;
```
The interesting engineering - Server-authoritative reward
calculation; the browser never chooses its own rewards. - Transactional
updates for progression state. - Oracle companion with multi-provider
routing and fallback behavior. - Lightweight local Naive Bayes emotion
classification feeding structured context. - 24+ architecture decision
records documenting key system decisions. - Test hardening across pure
logic, SQL behavior, and end-to-end flows. - Additive migration workflow
with fingerprint checks and advisory locking.
Design split: deterministic code handles critical state; the LLM
sits at the product's flexible edge.
---
◈ DataVortex
A three-round national data science competition
![Repository](https://img.shields.io/badge/Repository-DataVortex-0d1117?style=flat-square&logo=github)
AARUUSH '26 · SRM Institute of Science and Technology · "Rebuilding
the Social Engine"
A three-round pipeline that rebuilt a simulated social platform's data,
semantic layer, and live signal tracking. The work emphasizes
reproducibility, explicit data repairs, and honest evaluation.
Stack: Python · pandas · scikit-learn · TF-IDF · SQLite · Jupyter ·
Mann--Whitney U · public data sources
``` mermaid
flowchart LR
    R1["ROUND 1<br/>Data restoration<br/>12,360 → 10,221 rows<br/>27 logged repairs"]
    R2["ROUND 2<br/>NLP classification<br/>9,000 labelled texts<br/>Macro-F1: 0.613 / 0.805"]
    R3["ROUND 3<br/>Live signal tracking<br/>10,384 collected records<br/>21 sweeps · 9 spikes"]

    R1 --> R2 --> R3

    classDef a fill:#0b1220,stroke:#3fb950,color:#e6edf3;
    classDef b fill:#0b1220,stroke:#a371f7,color:#e6edf3;
    classDef c fill:#0b1220,stroke:#f78166,color:#e6edf3;
    class R1 a;
    class R2 b;
    class R3 c;
```
Round 1 --- Data restoration - Recovered 12,360 corrupted rows into
10,221 analysis-ready records. - Logged 27 individually justified,
reversible repairs instead of silently altering data. - Built a SQLite
analysis core and answered the analytical question set with SQL. -
Reproducible pipeline with automated tests.
Round 2 --- Semantic recovery - Evaluated sentiment and topic
classification over 9,000 labelled texts. - Compared TF-IDF and linear
models, with LDA/NMF cross-checks. - Reported sentiment macro-F1 of
0.6134 and topic macro-F1 of 0.8051. - Used a fixed split and
seed, with explicit error analysis.
Round 3 --- Live signal tracking - Collected 10,384 records
across 21 sweeps and 5 languages. - Logged HTTP outcomes and
used public sources under their applicable access constraints. - Applied
the Round 2 model to the collected data without retraining it on the
target results. - Reported 9 engagement spikes and a gold-day
positivity shift from 0.391 to 0.306 with Mann--Whitney U, p =
0.0043.
Why it matters: data integrity → applied ML → live analysis,
connected into one reproducible pipeline.
> "The data survived. It understood. Now it watches back." --- ARCHIVE
> NODE 07
---
◈ InnerLoop
Student productivity & continuous improvement
InnerLoop explores the loop between planning, focus, habits, learning,
and measurable improvement. It is a separate project from Questbound:
InnerLoop emphasizes structured planning and analytics, while Questbound
explores game mechanics.
Stack: React · Vite · Supabase · PostgreSQL · Tailwind CSS
``` mermaid
flowchart LR
    K["Know your day"] --> P["Plan"]
    P --> F["Focus"]
    F --> H["Build habits"]
    H --> L["Learn"]
    L --> M["Measure"]
    M --> A["Adapt"]
    A -.-> K
    CTX[("Structured student context<br/>timetable · tasks · goals<br/>habits · focus · learning")]
    CTX --- P
    CTX --- M
    CTX -. planned .-> AI["AI reasoning layer"]

    classDef built fill:#0b1220,stroke:#3fb950,color:#e6edf3;
    classDef planned fill:#10151d,stroke:#8b949e,color:#8b949e,stroke-dasharray: 5 5;
    class K,P,F,H,L,M,A,CTX built;
    class AI planned;
```
Implemented foundations: timetable context, tasks and goals, habits
and focus, learning tracking, analytics, adaptive-planning foundations,
and structured AI-ready data.
Planned: the full AI context and reasoning layer.
---
◈ Anaya Health Assistant
Voice-first healthcare information access
![Repository](https://img.shields.io/badge/Repository-Anaya-0d1117?style=flat-square&logo=github)
Anaya explores voice-first healthcare information with a focus on
Hinglish and Indian-language accessibility. It is designed to be
non-diagnostic and non-prescriptive.
Stack: LiveKit Agents · SIP · Gemini · Deepgram · Murf Falcon ·
SQLite
``` mermaid
flowchart LR
    U["Voice / phone call"] --> LK["LiveKit / SIP"]
    LK --> STT["Deepgram<br/>Speech to text"]
    STT --> LLM["Gemini<br/>Safety-bounded response"]
    LLM --> TTS["Murf Falcon<br/>Text to speech"]
    TTS --> LK
    LK --> U
    LLM <--> DB[("SQLite")]

    classDef n fill:#0b1220,stroke:#58a6ff,color:#e6edf3;
    class U,LK,STT,LLM,TTS,DB n;
```
Voice-first interaction to reduce dependence on text-heavy
interfaces.
Hinglish-oriented conversational experience.
Information and guidance rather than diagnosis or prescription.
Speech-to-text → language model → text-to-speech pipeline.
---
◈ SHIELD-COM
Embedded speech processing for noisy environments
Smart India Hackathon 2026 · Team entry / college internal round
A hardware-software concept exploring embedded speech processing and
active-noise-cancellation approaches for communication in noisy
operational environments.
Stack: ESP32-S3 · ESP-SR · Embedded systems · Speech processing
``` mermaid
flowchart LR
    MIC["Audio input"] --> MCU["ESP32-S3"]
    MCU --> SR["ESP-SR processing"]
    SR --> OUT["Processed communication output"]

    classDef n fill:#0b1220,stroke:#d29922,color:#e6edf3;
    class MIC,MCU,SR,OUT n;
```
The project explores the hardware/software boundary and on-device
speech-processing capabilities. The diagram represents the intended
system direction, not a claim that every component is
production-validated.
---
◈ NoLimi
Personal AI desktop assistant
A Python assistant combining natural-language interaction with voice
input, speech output, browser automation, and application launching.
Stack: Python · Gemini API · Speech recognition · TTS · Browser
automation
``` mermaid
flowchart LR
    V["Voice command"] --> SR["Speech recognition"]
    SR --> G["Gemini API"]
    G --> R{"Action router"}
    R --> B["Browser automation"]
    R --> A["Launch application"]
    R --> C["Conversational reply"]
    B --> T["Text-to-speech"]
    A --> T
    C --> T

    classDef n fill:#0b1220,stroke:#3fb950,color:#e6edf3;
    class V,SR,G,R,B,A,C,T n;
```
Exploration direction: AI + desktop automation + cybersecurity. This
is an ongoing direction, not a claim that every possible automation
feature is complete.
---
`05` / PROJECT CONSTELLATION
``` mermaid
flowchart TB
    ME(("Kunal Choudhary"))
    ME --> SEC["Secure backend systems"]
    ME --> ADP["Adaptive systems"]
    ME --> VOICE["Voice & speech AI"]
    ME --> DATA["Data & applied ML"]
    ME --> HEALTH["Healthcare access"]
    ME --> AUTO["Automation"]

    SEC --> T["TRAXIS"]
    SEC --> Q["Questbound"]
    ADP --> Q
    ADP --> IL["InnerLoop"]
    VOICE --> AN["Anaya"]
    VOICE --> SH["SHIELD-COM"]
    HEALTH --> FC["FlowCare"]
    DATA --> DV["DataVortex"]
    AUTO --> NL["NoLimi"]

    classDef root fill:#1f6feb,stroke:#58a6ff,color:#fff;
    classDef domain fill:#161b22,stroke:#8b949e,color:#e6edf3;
    classDef project fill:#0b1220,stroke:#58a6ff,color:#58a6ff;
    class ME root;
    class SEC,ADP,VOICE,DATA,HEALTH,AUTO domain;
    class T,Q,IL,AN,SH,FC,DV,NL project;
```
---
Project                                                          Domain                  Core technologies
---
FlowCare              Healthcare discovery &  Next.js, TypeScript,
coordination            Supabase, PostgreSQL,
RLS
TRAXIS                  Polar logistics & asset React, Vite, FastAPI,
management              PostgreSQL, JWT, RBAC
Questbound          Adaptive productivity   Next.js, PostgreSQL,
RPG                     Supabase, Drizzle, LLM
routing
InnerLoop                                                        Student productivity    React, Vite, Supabase,
PostgreSQL
Anaya   Voice healthcare        LiveKit, Gemini,
information             Deepgram, Murf
SHIELD-COM                                                       Embedded speech         ESP32-S3, ESP-SR
processing
NoLimi                                                           Desktop assistant &     Python, Gemini API,
automation              speech tools
DataVortex    Data science & live     pandas, scikit-learn,
analysis                TF-IDF, SQLite
---
`06` / TECH ARSENAL
::: {align="center"}
`<img src="https://skillicons.dev/icons?i=python,fastapi,postgres,supabase,sqlite,react,nextjs,ts,vite,tailwind,git,github,linux&theme=dark" alt="Technology icons"/>`{=html}
:::
---
Layer                               Tools & concepts
---
AI / LLM                        Gemini API, multi-provider routing,
NLP, Naive Bayes, LLM applications
Machine learning                pandas, scikit-learn, TF-IDF,
evaluation, statistical testing,
Jupyter
Voice & speech                  LiveKit Agents, SIP, Deepgram, Murf
Falcon, speech recognition, TTS,
ESP-SR
Backend                         Python, FastAPI, Next.js route
handlers, REST APIs, validation,
integration testing
Data                            PostgreSQL, Supabase, SQLite, RLS,
Drizzle ORM, transactional
workflows
Security                        JWT verification, RBAC, tenant
scoping, audit logging, server-side
authorization
Frontend                        React, Next.js, TypeScript, Vite,
Tailwind CSS
Embedded                        ESP32-S3, on-device
speech-processing exploration
Workflow                        Git, GitHub, automation,
reproducible pipelines
---
`07` / FIELD REPORTS
---
Event / track                       Work
---
Tech Zephyr 4.0 --- IIT           🏆 Questbound selected as a Grand
Bhubaneswar                       Finale Finalist; offline pitch,
demo, and technical Q&A
AARUUSH '26 --- DataVortex      Three-round pipeline: restoration →
NLP → live signal tracking
Smart India Hackathon 2026      Team work across TRAXIS and
SHIELD-COM problem tracks
`08` / CURRENT LEARNING TREE
```{=html}
<details open>
```
```{=html}
<summary>
```
`<b>`{=html}Active learning tracks`</b>`{=html}
```{=html}
</summary>
```
`<br/>`{=html}
---
Track                               Current focus
---
ML foundations                  Core concepts, data preparation,
training and evaluation
Deep learning                   PyTorch, neural networks, practical
model workflows
LLM systems                     RAG, agentic architectures,
evaluation, failure analysis
Backend engineering             API design, authorization, testing,
reliability
System design                   Data modeling, tenant boundaries,
scalable architecture
```{=html}
</details>
```
---
`09` / GITHUB TELEMETRY
::: {align="center"}
`<img src="https://streak-stats.demolab.com?user=kunalchwdry&theme=tokyonight&hide_border=true&background=0D1117&ring=58A6FF&fire=7C3AED&currStreakLabel=58A6FF" alt="GitHub streak"/>`{=html}
`<br/>`{=html}`<br/>`{=html}
`<img height="165" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=kunalchwdry&theme=tokyonight" alt="Languages across repositories"/>`{=html}
`<img height="165" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=kunalchwdry&theme=tokyonight" alt="GitHub statistics"/>`{=html}
`<img height="165" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=kunalchwdry&theme=tokyonight&utcOffset=5.5" alt="Productive time"/>`{=html}
:::
``` text
┌──(kunal㉿github)-[~/telemetry]
└─$ ./mission-report

  grand finale finalist ......... Tech Zephyr 4.0 · IIT Bhubaneswar
  competition rounds shipped .... 3 · DataVortex
  records collected ............. 10,384
  collection sweeps ............. 21
  languages in collected data ... 5
  reported statistical result ... p = 0.0043
  architecture decision records . 24+
```
`<sub>`{=html}Stats cards are generated by third-party services and may
occasionally be unavailable or delayed. Project metrics above describe
the stated project runs, not live GitHub counters.`</sub>`{=html}
---
`10` / THE SIDE QUEST
You wake up inside THE SOCIAL ENGINE. Corrupted rows shimmer across the
floor. A terminal flickers in the dark:
``` text
> signal detected
> records recovered: 10,384
> anomaly probability: p = 0.0043
> new quest unlocked: MISSION 2030
```
Choose your route:
---
Portal                              Mission
---
🗃️ Enter the Data                  Follow the evidence. Repair the
Caves                 records. Track the signal.
🎙️ Climb the Voice                 Explore voice-first AI and speech
Tower     pipelines.
🔐 Enter the Security              Cross the tenant boundary without
Vault                     breaking authorization.
🧪 Visit the                       Build systems where deterministic
Alchemist             rules meet adaptive AI.
🏥 Open FlowCare       Trace a claim back to its source.
```{=html}
<details>
```
```{=html}
<summary>
```
💎 `<b>`{=html}Secret room: The Golden Record`</b>`{=html}
```{=html}
</summary>
```
`<br/>`{=html}
``` text
☠ FINAL BOSS — MISSION 2030
TARGET: AI INFRASTRUCTURE
STATUS: ACTIVE

WEAPONS:
  [x] foundations first
  [x] server decides
  [x] validate before you claim
  [x] measure, then improve

CRITICAL HIT:
  Data integrity → applied intelligence → useful systems
```
Achievement unlocked: keep building things that survive contact with
reality.
```{=html}
</details>
```
---
`11` / MISSION 2030
``` mermaid
flowchart LR
    A["AI Engineering"] --> B["Intelligent Systems"]
    B --> C["AI Products"]
    C --> D["AI Infrastructure"]

    classDef n fill:#0b1220,stroke:#58a6ff,color:#e6edf3,stroke-width:1.5px;
    class A,B,C,D n;
```
The goal is to build deep technical foundations, ship increasingly
complex AI systems, and become an engineer who can design intelligent
products end-to-end --- from data and infrastructure to the user
experience.
Not a claim that the mission is complete. A direction worth earning.
---
`12` / CONNECT
::: {align="center"}
![GitHub](https://img.shields.io/badge/GitHub-Explore%20my%20work-0d1117?style=for-the-badge&logo=github)
![LinkedIn](https://img.shields.io/badge/LinkedIn-Let's%20connect-0d1117?style=for-the-badge&logo=linkedin&logoColor=0A66C2)
Open to collaborating on AI systems, backend platforms, data
pipelines, and real-world intelligent software.
`<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&pause=1800&color=8B949E&center=true&vCenter=true&width=700&lines=Foundations+first.+Then+intelligence.;Build.+Measure.+Break.+Rebuild.;The+data+survived.+It+understood.+Now+it+watches+back." alt="Closing tagline"/>`{=html}
`<br/>`{=html}
`<img src="https://capsule-render.vercel.app/api?type=waving&height=130&color=0:7c3aed,35:123a66,70:0d1b3d,100:050816&section=footer&animation=fadeIn" width="100%" alt="Footer wave"/>`{=html}
:::
