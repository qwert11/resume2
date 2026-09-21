# Yurii Zaika

**AI / Python Engineer**

xetr11@gmail.com · t.me/xetr_11 · github.com/qwert11 · Dnipro, Ukraine · remote or hybrid

Ten years of production engineering plus a personal track in Python and ML. Built a real-time speech pipeline: faster-whisper on CUDA, pyannote diarization, VAD and streaming — 55 modules, 15,500 lines of Python, with regression measurements of latency and RTF. Alongside it: data pipelines on SQLAlchemy and Playwright, and daily work with AI agents.

## At a glance

- 10 years — in production retail systems, 2016 to now
- 15 500 lines — of Python in the speech pipeline: 55 modules, STT and diarization
- 27 — repositories in 2026: freelance and personal projects
- 6 sources — in the listings pipeline: OLX, LUN, Rieltor, Metrazh, Telegram, FB

## What I delivered

- Leading the trading system client migration from Delphi 6 to Delphi 12/13, with a purpose-built tool that diffs forms and database mappings between versions so the switch does not break store operations.
- Architected and built the network's SMS notification platform: SMPP and GSM API, .NET Web API and MS SQL, designed for peak-volume campaigns.
- Built a real-time speech pipeline in Python: faster-whisper on GPU, pyannote diarization, VAD and streaming capture — 55 modules and 15,500 lines of code.
- Wrote its quality regression suite — RTF, latency, noise robustness, accuracy ceilings — and drive decisions from the numbers rather than impressions.
- Built Python data pipelines: SQLAlchemy 2 and Alembic over PostgreSQL, Playwright for protected pages, six listing sources merged into one catalog.

## Stack

- **Data:** MS SQL Server, T-SQL, PostgreSQL
- **Quality and delivery:** xUnit / NUnit, NSubstitute / Moq, AutoFixture, FluentAssertions, SonarQube, Jenkins, Docker, Serilog / NLog, Elastic APM, Git / приватний NuGet
- **Engineering practice:** Legacy modernization, Modular monolith, Three-tier architecture, Integration design, Production ownership
- **Python:** Python 3.11, FastAPI, SQLAlchemy 2, Alembic, Pydantic, Typer CLI, Playwright, selectolax, NumPy, pytest, ruff / black, Jinja2
- **Speech and ML:** faster-whisper (CUDA), pyannote.audio, VAD, Speaker diarization, Quality evaluation: RTF, latency, Streaming audio pipelines, WASAPI / sounddevice, PyTorch / GPU
- **Working with AI agents:** Claude Code, MCP-сервери, Custom subagents and hooks, Agent tooling (CDP), Prompt engineering
- **JS / TS ecosystem:** Next.js 16, React 19, NestJS, Prisma, Node.js

## Key projects

### Real-time speech pipeline (ORK) · 2026
*Author*

Real-time speech recognition from calls: parallel microphone and system-audio capture, VAD-based segmentation, faster-whisper on GPU, pyannote diarization with incremental clustering, translation. A separate regression suite — RTF, latency under load, noise robustness — shows exactly where quality is lost.

`Python 3.11` `faster-whisper` `pyannote.audio` `CUDA` `FastAPI` `NumPy` `WASAPI`


### Real-estate data pipeline · 2026
*Author*

A listings parser with pagination, normalization and price history: SQLAlchemy 2 models with Alembic migrations over PostgreSQL, two transports — plain HTTP and Playwright for protected pages — a Typer CLI, pydantic-settings config and pytest coverage.

`Python` `SQLAlchemy 2` `Alembic` `PostgreSQL` `Playwright` `selectolax` `Typer` `pytest`


### Legacy system map · 2026
*Author*

A tool for mapping the trading system before migration: Python parses .dfm and .pas files, extracts stored-procedure calls and form relations, and a Next.js app renders it as an annotated map.

`Python` `Next.js` `TypeScript` `PostgreSQL`


### AM Mobility — web and mobile app · 2026
*Full stack developer*

Client project: a NestJS back end with Swagger and PostgreSQL, a Next.js web app, and an Expo / React Native mobile app with MapLibre maps, geolocation and offline state.

`NestJS` `Next.js` `Expo` `React Native` `PostgreSQL` `MapLibre` `TanStack Query`


### Trading client migration: Delphi 6 to Delphi 12 · 2024 — 2026
*Migration lead*

Moving the trading system client (955 units, 828 forms) to a modern compiler with a core redesign. Built a separate tool that diffs forms and table mappings between the old and new versions, so the migration runs without stopping stores.

`Delphi 12/13` `Object Pascal` `VCL` `MS SQL` `DevExpress` `FastReport`

https://github.com/qwert11/d6_d13_dbmapping_checker


### SMS Messenger · 2020 — 2023
*Architect and developer*

The network's SMS notification platform: an in-house gateway to carriers over SMPP and to modems over GSM API, campaign queues, an API for internal systems.

`ASP.NET Core` `Web API` `SMPP` `GSM API` `MS SQL` `Hangfire`


## Experience

### Freelance and personal projects — AI / Python and Full Stack Developer
2026-03 — present · Dnipro · remote · Python, ML and full stack work

- A real-time speech pipeline: faster-whisper on CUDA, pyannote diarization, VAD, WASAPI capture — 55 modules, 15,500 lines of Python.
- And a regression suite for it: RTF, latency under load, noise robustness, quality ceilings — decisions come from measurements, not impressions.
- A real-estate parser in Python: SQLAlchemy 2 and Alembic over PostgreSQL, Playwright and selectolax, a Typer CLI, pytest and ruff.
- A listings pipeline over six sources with geocoding, deduplication and catalog publishing through GitHub Actions.
- A legacy-code analyzer: Python parses .dfm and .pas files and diffs stored-procedure calls, Next.js renders the system map with annotations.
- Client work: NestJS with Prisma and PostgreSQL, Next.js 16 with React 19, a mobile app on Expo with MapLibre maps.
- Daily work with AI agents: MCP servers, custom subagents and hooks, and my own CDP browser inspector as agent tooling.

### ATB-Market — Lead Application Programmer
2016-06 — present · Dnipro · Ukraine's largest grocery retail network

- Own the client side of the network's trading system: 955 units, 828 forms, MS SQL, covering supply documents, pricing and fiscal invoices.
- Since 2018 also build internal services on ASP.NET Core and Angular: access, audit, reporting, integrations — 33 of the network's systems carry my code.
- UAM: access management for 2,000+ users on OpenID Connect, ADFS and Kerberos.
- Network integrations: EDI and e-document flow, M.E.Doc, Oracle EBS, 1C, Kafka, BizTalk, SSIS and SSRS.
- Fiscal-law changes delivered end to end: excise stamps and AED, UKTZED, customs simplifications, VAT rates, in a live retail network.
- Leading the client migration from Delphi 6 to Delphi 12/13 with an in-house form and DB-mapping diff tool.
- Engineering practice: xUnit and NSubstitute tests, SonarQube and Jenkins, Serilog, Docker, a private NuGet feed.


## Education and certificates

- **Computer Engineering · computer systems and networks** — Zaporizhzhia Institute of Economics and Information Technologies (2008 — 2011)
- **Mining Engineer, underground development** — Kryvyi Rih Technical University (1998 — 2003)
- **Angular 9** — Luxoft (2021)
- **Programming in Delphi** — Institute of Modern Professions (2006)

## Languages

- **Ukrainian** — native
- **English** — technical documentation and written communication; spoken at basic level