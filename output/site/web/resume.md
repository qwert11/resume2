# Yurii Zaika

**Full Stack Engineer · .NET & Angular**

xetr11@gmail.com · t.me/xetr_11 · github.com/qwert11 · Dnipro, Ukraine · remote or hybrid

Full stack engineer: ASP.NET Core and Web API on the back end, Angular 13 with Kendo UI and Razor on the front, real-time over SignalR. Internal systems for a retail network: access control, audit, reporting, integrations.

## At a glance

- 10 years — in production retail systems, 2016 to now
- 2 000+ — users on the access system I built
- 33 — internal systems of the network carry my code
- .NET 7 — the main service platform; 3.1, 5 and 6 also in support

## What I delivered

- Built UAM, the network's in-house access management system: 2,000+ users on OpenID Connect, ADFS and Kerberos, replacing per-system manual permission handling.
- Architected and built the network's SMS notification platform: SMPP and GSM API, .NET Web API and MS SQL, designed for peak-volume campaigns.
- Deliver fiscal-law changes end to end across the systems: excise stamps and AED, UKTZED codes, customs simplifications, new VAT rates, all in a live retail network without stopping the stores.
- Built the internal web systems stores work with: journals and audit, recyclables with M.E.Doc integration, a support portal, coupons and reporting.
- Wrote its quality regression suite — RTF, latency, noise robustness, accuracy ceilings — and drive decisions from the numbers rather than impressions.

## Stack

- **Backend:** C#, .NET 7 / 6 / 5, .NET Core 3.1, ASP.NET Core, ASP.NET MVC, Web API / REST, SignalR, Worker Services, Hangfire, Quartz, AutoMapper, Flurl.Http
- **Data:** MS SQL Server, T-SQL, EF Core 7, ADO.NET, Oracle, PostgreSQL, Firebird, SSIS, SSRS, SQL CLR
- **Front end:** Angular 13, TypeScript, Kendo UI for Angular, Telerik UI for ASP.NET Core, Razor / MVC views, JavaScript, HTML / CSS, jQuery
- **Integrations:** EDI / ЕДО, M.E.Doc, Oracle EBS, 1С, Kafka, BizTalk, WCF / SOAP, SMPP / GSM API, API Gateway, GemBox.Spreadsheet
- **Access and security:** OpenID Connect, OAuth2, JWT Bearer, ADFS, Kerberos / Negotiate, Active Directory, RBAC
- **Quality and delivery:** xUnit / NUnit, NSubstitute / Moq, AutoFixture, FluentAssertions, SonarQube, Jenkins, Docker, Serilog / NLog, Elastic APM, Git / приватний NuGet
- **Engineering practice:** Legacy modernization, Modular monolith, Three-tier architecture, Integration design, Production ownership
- **Working with AI agents:** Claude Code, MCP-сервери, Custom subagents and hooks, Agent tooling (CDP)
- **JS / TS ecosystem:** Next.js 16, React 19, NestJS, Prisma, Expo / React Native, Tailwind CSS, Zustand / TanStack Query, MapLibre, Vite, Node.js

## Key projects

### AM Mobility — web and mobile app · 2026
*Full stack developer*

Client project: a NestJS back end with Swagger and PostgreSQL, a Next.js web app, and an Expo / React Native mobile app with MapLibre maps, geolocation and offline state.

`NestJS` `Next.js` `Expo` `React Native` `PostgreSQL` `MapLibre` `TanStack Query`


### UAM — access management · 2020 — 2022
*Developer*

Centralized permissions and authentication for 2,000+ people in the network: roles and access requests, Active Directory integration, sign-in through OpenID Connect, ADFS and Kerberos.

`ASP.NET Core` `C#` `EF Core` `MS SQL` `OIDC` `ADFS` `Angular`


### Store Journals · 2021 — 2023
*Developer*

Journals and audit platform for the network's stores: in-store entry, inspections, regional reporting. The most code-intensive of the web systems.

`ASP.NET Core` `Angular 13` `Kendo UI` `EF Core` `MS SQL` `SignalR`


### API Gateway and reporting service · 2018 — 2020
*Developer*

A gateway for the network's internal services and a reporting service over MS SQL: a single entry point, header and auth propagation, Excel exports.

`.NET Core` `Web API` `MS SQL` `SSRS` `GemBox.Spreadsheet`


### Real-estate data pipeline · 2026
*Author*

A listings parser with pagination, normalization and price history: SQLAlchemy 2 models with Alembic migrations over PostgreSQL, two transports — plain HTTP and Playwright for protected pages — a Typer CLI, pydantic-settings config and pytest coverage.

`Python` `SQLAlchemy 2` `Alembic` `PostgreSQL` `Playwright` `selectolax` `Typer` `pytest`


### Legacy system map · 2026
*Author*

A tool for mapping the trading system before migration: Python parses .dfm and .pas files, extracts stored-procedure calls and form relations, and a Next.js app renders it as an annotated map.

`Python` `Next.js` `TypeScript` `PostgreSQL`


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

### Freelance and private practice — Full Stack Developer
2015-07 — 2016-07 · Kryvyi Rih

- An automated car dealership system on Java and Firebird: vehicles, sales and reporting.
- Online stores on WordPress / WooCommerce and OpenCart, plus a custom WordPress plugin.

### Modern Professions Courses — Programming Instructor
2015-01 — 2016-01 · Kryvyi Rih

- A beginners' course: OOP, Java Core, Hibernate, SQL, from first programs to working with a database.
- Wrote the course materials and labs, and took groups from zero to their first projects.

### Kryvyi Rih Iron Ore Combine — Engineer Programmer
2013-06 — 2016-06 · Kryvyi Rih · underground ore mining

- A system for ore extraction and shipment accounting, developed and maintained in production.
- Automated per-shift distribution of consumables and hazard-pay meals.
- Maintained production-preparation and budgeting systems; implemented Firebird table synchronization.

### OSSystem — Developer
2012-11 — 2013-04 · Odesa

- Development on Master INSURANCE, an insurance automation system: three-tier architecture with ORM over Oracle, reports in XL Report.
- Maintained Expo, a system tracking vehicle and container movement across port territories.


## Domain knowledge

- **Excise stamps (eAcciz / AED)** — Stamp scanning, electronic excise documents, document number in the invoice
- **Tax invoices and adjustments** — Issuing, adjustments, field rules aligned with the tax service
- **UKTZED commodity codes** — Commodity code synchronization across the network's systems
- **Customs simplifications** — Customs declarations, import receipts into warehouses, reporting
- **EDI and e-document flow** — Orders, waybills, pooled packaging, supplier exchange
- **VAT rates and pricing regions** — Cross-system rate changes, region setup when a store opens

## Education and certificates

- **Computer Engineering · computer systems and networks** — Zaporizhzhia Institute of Economics and Information Technologies (2008 — 2011)
- **Mining Engineer, underground development** — Kryvyi Rih Technical University (1998 — 2003)
- **Angular 9** — Luxoft (2021)
- **Programming in Delphi** — Institute of Modern Professions (2006)

## Languages

- **Ukrainian** — native
- **English** — technical documentation and written communication; spoken at basic level