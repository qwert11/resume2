# Yurii Zaika

**Lead Software Engineer · .NET & Delphi**

xetr11@gmail.com · t.me/xetr_11 · github.com/qwert11 · Dnipro, Ukraine · remote or hybrid

Ten years inside the core systems of ATB-Market, Ukraine's largest grocery retail network: ASP.NET Core services that keep taking over functions from the Delphi trading platform the stores run on daily. Access control for 2,000+ users, fiscal and EDI integrations, and an ongoing Delphi 6 to Delphi 12/13 client migration.

## At a glance

- 10 years — in production retail systems, 2016 to now
- 2 000+ — users on the access system I built
- 33 — internal systems of the network I built or extended
- 2 stacks — Delphi and .NET in parallel, with the business running

## What I delivered

- Built UAM, the network's in-house access management system: 2,000+ users on OpenID Connect, ADFS and Kerberos, replacing per-system manual permission handling.
- Leading the trading system client migration from Delphi 6 to Delphi 12/13, with a purpose-built tool that diffs UI and database mappings between versions so the switch does not break store operations.
- Architected and built the network's SMS notification platform: SMPP and GSM API, .NET Web API and MS SQL, designed for peak-volume campaigns.
- Deliver fiscal-law changes end to end across the systems: excise stamps and electronic excise documents (AED), UKTZED commodity codes, customs simplifications, new VAT rates, all in a live retail network without stopping the stores.
- Built the internal web systems stores work with: journals and audit, recyclables with M.E.Doc integration, a support portal, coupons and reporting.
- Built a real-time speech pipeline in Python: faster-whisper on GPU, pyannote diarization, VAD and streaming capture.

## Stack

- **Backend:** C#, .NET (Core 3.1 → 7), ASP.NET Core, ASP.NET MVC, Web API / REST, SignalR, Worker Services, Hangfire, Quartz, AutoMapper
- **Front end:** Angular 13, TypeScript, React 19, Next.js 16, Kendo UI for Angular, Telerik UI for ASP.NET Core, Razor / MVC views, Tailwind CSS, Zustand / TanStack Query, Expo / React Native, MapLibre, JavaScript, HTML / CSS
- **Data:** MS SQL Server, T-SQL, PostgreSQL, EF Core, ADO.NET, Oracle, Firebird, SSIS, SSRS, SQL CLR
- **Access and security:** OpenID Connect, OAuth2, JWT Bearer, ADFS, Kerberos / Negotiate, Active Directory, RBAC
- **Integrations:** EDI / e-document flow, M.E.Doc, Oracle EBS, 1C, Kafka, BizTalk, WCF / SOAP, SMPP / GSM API, API Gateway
- **Quality and delivery:** xUnit / NUnit, NSubstitute / Moq, AutoFixture, FluentAssertions, SonarQube, Jenkins, Docker, Serilog / NLog, Elastic APM, Git / private NuGet feed
- **Engineering practice:** Production ownership, Legacy modernization, Integration design, Modular monolith, GitHub Actions
- **Desktop:** Delphi 6 → 12 / 13, Object Pascal, VCL, DevExpress, FastReport, RX Library, Indy, NativeExcel / NativeXml, ADO / OLE DB
- **Python:** Python 3.11, FastAPI, SQLAlchemy 2, Alembic, Pydantic, Typer CLI, Playwright, selectolax, NumPy, pytest, ruff
- **Speech and ML:** faster-whisper (CUDA), pyannote.audio, VAD, Speaker diarization, Quality evaluation: RTF, latency, Streaming audio pipelines, WASAPI / sounddevice, PyTorch / GPU
- **Working with AI agents:** Claude Code, MCP servers, Custom subagents and hooks, Agent tooling (CDP), Prompt engineering
- **Node.js back end:** NestJS, Prisma, Node.js

## Key projects

### Trading client migration: Delphi 6 to Delphi 12/13 · 2024 — present
*Migration lead*

Moving the trading system client to a modern compiler with a core redesign. Built a separate tool that diffs UI and table mappings between the old and new versions, so the migration runs without stopping stores.

`Delphi 12/13` `Object Pascal` `VCL` `MS SQL` `DevExpress` `FastReport`

https://github.com/qwert11/d6_d13_dbmapping_checker


### UAM — access management · 2020 — 2022

Centralized permissions and authentication for 2,000+ people in the network: roles and access requests, Active Directory integration, sign-in through OpenID Connect, ADFS and Kerberos.

`ASP.NET Core` `C#` `EF Core` `MS SQL` `OIDC` `ADFS` `Angular`


### Store Journals · 2021 — 2023

Journals and audit platform for the network's stores: in-store entry, inspections, regional reporting, real-time updates over SignalR.

`ASP.NET Core` `Angular 13` `Kendo UI` `EF Core` `MS SQL` `SignalR`


### Fiscal workflows: excise stamps, e-excise documents, customs · 2019 — present
*Owner of the workstream*

End-to-end delivery of legislative change inside the trading system: excise stamp scanning, electronic excise documents, tax invoice adjustments, UKTZED codes, customs simplifications, the 14% VAT rate.

`Delphi` `T-SQL` `MS SQL` `EDI` `M.E.Doc`


### Real-time speech pipeline · 2026 — present
*Author*

Real-time speech recognition from calls: parallel microphone and system-audio capture, VAD-based segmentation, faster-whisper on GPU, pyannote diarization with incremental clustering, translation. A separate regression suite — RTF, latency under load, noise robustness — shows exactly where quality is lost.

`Python 3.11` `faster-whisper` `pyannote.audio` `CUDA` `FastAPI` `NumPy` `WASAPI`


### Real-estate data pipeline · 2026
*Author*

A listings parser with pagination, normalization and price history: SQLAlchemy 2 models with Alembic migrations over PostgreSQL, two transports — plain HTTP and Playwright for protected pages — a Typer CLI, pydantic-settings config and pytest coverage.

`Python` `SQLAlchemy 2` `Alembic` `PostgreSQL` `Playwright` `selectolax` `Typer` `pytest`


## Experience

### ATB-Market — Lead Software Engineer
2016-06 — present · Dnipro · Ukraine's largest grocery retail network

- Own the client side of the trading system that the network's stores run on daily: supply documents, pricing and fiscal invoices, MS SQL.
- Since 2018 also build internal services on ASP.NET Core and Angular: access, audit, reporting, integrations — 33 of the network's systems I built or extended.
- UAM: access management for 2,000+ users on OpenID Connect, ADFS and Kerberos.
- Architected and built the network's SMS notification platform: SMPP and GSM API, .NET Web API, MS SQL — designed for peak-volume campaigns.
- Network integrations: EDI and e-document flow, M.E.Doc, Oracle EBS, 1C, Kafka, BizTalk, SSIS and SSRS.
- Fiscal-law changes delivered end to end: excise stamps and AED, UKTZED, customs simplifications, VAT rates, in a live retail network.
- Leading the client migration from Delphi 6 to Delphi 12/13 with an in-house tool that diffs UI and DB mappings between versions.
- Engineering practice: xUnit and NSubstitute tests, SonarQube and Jenkins, Serilog, Docker, a private NuGet feed.

### Personal projects and freelance — Independent developer
2026-03 — present · Dnipro · remote · alongside the full-time role at ATB-Market

- A real-time speech pipeline: faster-whisper on CUDA, pyannote diarization, VAD, WASAPI capture.
- And a regression suite for it: RTF, latency under load, noise robustness, quality ceilings — decisions come from measurements, not impressions.
- A real-estate parser in Python: SQLAlchemy 2 and Alembic over PostgreSQL, Playwright and selectolax, a Typer CLI, pytest and ruff.
- A listings pipeline over six sources with geocoding, deduplication and catalog publishing through GitHub Actions.
- A legacy-code analyzer: Python parses .dfm and .pas files and diffs stored-procedure calls, Next.js renders the system map with annotations.
- Client work: NestJS with Prisma and PostgreSQL, Next.js 16 with React 19, a mobile app on Expo with MapLibre maps.
- Daily work with AI agents: MCP servers, custom subagents and hooks, and my own CDP browser inspector as agent tooling.

### Kryvyi Rih Iron Ore Combine — Software Engineer
2013-06 — 2016-06 · Kryvyi Rih · underground ore mining

- A system for ore extraction and shipment accounting, developed and maintained in production.
- Automated per-shift distribution of consumables and hazard-pay meals.
- Maintained production-preparation and budgeting systems; implemented Firebird table synchronization.

Earlier: Freelance and private practice — Full Stack Developer (2015–2016) · Modern Professions Courses — Programming Instructor (2015–2016) · OSSystem — Developer (2012–2013)


## Domain knowledge

- **Excise control: electronic excise stamps and documents (AED)** — Stamp scanning, electronic excise documents, document number in the invoice
- **Tax invoices and adjustments** — Issuing, adjustments, field rules aligned with the tax service
- **Commodity classification codes (HS / UKTZED)** — Commodity code synchronization across the network's systems
- **Customs and import clearance** — Customs declarations, import receipts into warehouses, reporting
- **EDI and e-document flow** — Orders, waybills, pooled packaging, supplier exchange
- **VAT rates and pricing regions** — Cross-system rate changes, region setup when a store opens

## Education and certificates

- **Computer Engineering · computer systems and networks** — Zaporizhzhia Institute of Economics and Information Technologies ()
- **Mining Engineer, underground development** — Kryvyi Rih Technical University ()
- **Angular 9** — Luxoft (2021)

## Languages

- **Ukrainian** — native
- **English** — technical documentation and written communication