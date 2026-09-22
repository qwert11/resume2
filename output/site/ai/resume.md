# Yurii Zaika

**AI / Python Engineer**

xetr11@gmail.com · t.me/xetr_11 · github.com/qwert11 · Dnipro, Ukraine · remote or hybrid

Ten years of production engineering, now applied to Python and ML. Built a real-time speech pipeline: faster-whisper on CUDA, pyannote diarization, VAD and streaming, with regression measurements of latency and real-time factor (RTF). Alongside it: tooling for LLM agents (MCP servers, custom subagents, a CDP browser inspector) and data pipelines on SQLAlchemy and Playwright.

## At a glance

- 10 years — in production retail systems, 2016 to now
- 33 — internal systems of the network I built or extended
- 27 — repositories in 2026: freelance and personal projects
- 6 sources — in the listings pipeline: OLX, LUN, Rieltor, Metrazh, Telegram, FB

## What I delivered

- Built a real-time speech pipeline in Python: faster-whisper on GPU, pyannote diarization, VAD and streaming capture.
- Wrote its quality regression suite — RTF, latency, noise robustness, accuracy ceilings — and drive decisions from the numbers rather than impressions.
- Built Python data pipelines: SQLAlchemy 2 and Alembic over PostgreSQL, Playwright for protected pages, six listing sources merged into one catalog.
- Built tooling for LLM agents: MCP servers, custom subagents and hooks, and a CDP browser inspector written as agent tooling.

## Stack

- **Python:** Python 3.11, FastAPI, SQLAlchemy 2, Alembic, Pydantic, Typer CLI, Playwright, selectolax, NumPy, pytest, ruff
- **Speech and ML:** faster-whisper (CUDA), pyannote.audio, VAD, Speaker diarization, Quality evaluation: RTF, latency, Streaming audio pipelines, WASAPI / sounddevice, PyTorch / GPU
- **Working with AI agents:** Claude Code, MCP servers, Custom subagents and hooks, Agent tooling (CDP), Prompt engineering
- **Data:** MS SQL Server, T-SQL, PostgreSQL
- **Engineering practice:** Production ownership, GitHub Actions
- **Node.js back end:** NestJS, Prisma, Node.js

## Key projects

### Real-time speech pipeline · 2026 — present
*Author*

Real-time speech recognition from calls: parallel microphone and system-audio capture, VAD-based segmentation, faster-whisper on GPU, pyannote diarization with incremental clustering, translation. A separate regression suite — RTF, latency under load, noise robustness — shows exactly where quality is lost.

`Python 3.11` `faster-whisper` `pyannote.audio` `CUDA` `FastAPI` `NumPy` `WASAPI`


### Real-estate data pipeline · 2026
*Author*

A listings parser with pagination, normalization and price history: SQLAlchemy 2 models with Alembic migrations over PostgreSQL, two transports — plain HTTP and Playwright for protected pages — a Typer CLI, pydantic-settings config and pytest coverage.

`Python` `SQLAlchemy 2` `Alembic` `PostgreSQL` `Playwright` `selectolax` `Typer` `pytest`


### Legacy system map · 2026
*Author*

A tool for mapping the trading system before migration: Python parses .dfm and .pas files, extracts stored-procedure calls and screen relations, and a Next.js app renders it as an annotated map.

`Python` `Next.js` `TypeScript` `PostgreSQL`


### Tooling for AI agents · 2026 — present
*Author*

An in-house CDP browser inspector — console, network, DOM, screenshots — used as agent tooling in place of Playwright MCP; MCP servers over PostgreSQL; custom subagents and hooks for a check-fix-recheck loop.

`Node.js` `Chrome DevTools Protocol` `MCP` `Claude Code` `PowerShell`


## Experience

### Personal projects and freelance — Independent developer
2026-03 — present · Dnipro · remote · alongside the full-time role at ATB-Market

- Authored three of the projects above end to end — the speech pipeline with its regression suite, the real-estate parser and the legacy system map.
- A listings pipeline over six sources with geocoding, deduplication and catalog publishing through GitHub Actions.
- Client work: NestJS with Prisma and PostgreSQL, Next.js 16 with React 19, a mobile app on Expo with MapLibre maps.
- Daily work with AI agents: MCP servers, custom subagents and hooks, and my own CDP browser inspector as agent tooling.

### ATB-Market — Lead Software Engineer
2016-06 — present · Dnipro · Ukraine's largest grocery retail network

- Since 2018 build the network's internal services on ASP.NET Core: access control for 2,000+ users (OpenID Connect, ADFS, Kerberos), audit, reporting, integrations with EDI, Oracle EBS and Kafka.
- Engineering practice: xUnit and NSubstitute tests, SonarQube and Jenkins, Serilog, Docker, a private NuGet feed.

Earlier: Freelance and private practice — Full Stack Developer (2015–2016) · Modern Professions Courses — Programming Instructor (2015–2016) · Kryvyi Rih Iron Ore Combine — Software Engineer (2013–2016) · OSSystem — Developer (2012–2013)


## Education and certificates

- **Computer Engineering · computer systems and networks** — Zaporizhzhia Institute of Economics and Information Technologies ()

## Languages

- **Ukrainian** — native
- **English** — technical documentation and written communication