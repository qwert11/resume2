# Yurii Zaika

**Senior .NET Engineer**

xetr11@gmail.com · t.me/xetr_11 · github.com/qwert11 · Dnipro, Ukraine · remote or hybrid

Senior .NET engineer: ASP.NET Core and Web API on .NET 7, EF Core and T-SQL, integrations over Kafka, EDI, M.E.Doc and Oracle EBS, authentication through OIDC, ADFS and Kerberos. Built the in-house access management system used by 2,000+ people.

## At a glance

- 10 years — in production retail systems, 2016 to now
- 2 000+ — users on the access system I built
- 33 — internal systems of the network carry my code
- .NET 7 — the main platform of the network's internal services

## What I delivered

- Built UAM, the network's in-house access management system: 2,000+ users on OpenID Connect, ADFS and Kerberos, replacing per-system manual permission handling.
- Architected and built the network's SMS notification platform: SMPP and GSM API, .NET Web API and MS SQL, designed for peak-volume campaigns.
- Built the internal web systems stores work with: journals and audit, recyclables with M.E.Doc integration, a support portal, coupons and reporting.
- Deliver fiscal-law changes end to end across the systems: excise stamps and AED, UKTZED codes, customs simplifications, new VAT rates, all in a live retail network without stopping the stores.

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

### UAM — access management · 2020 — 2022
*Developer*

Centralized permissions and authentication for 2,000+ people in the network: roles and access requests, Active Directory integration, sign-in through OpenID Connect, ADFS and Kerberos.

`ASP.NET Core` `C#` `EF Core` `MS SQL` `OIDC` `ADFS` `Angular`


### Store Journals · 2021 — 2023
*Developer*

Journals and audit platform for the network's stores: in-store entry, inspections, regional reporting.

`ASP.NET Core` `Angular 13` `Kendo UI` `EF Core` `MS SQL` `SignalR`


### Recyclables and returnable packaging · 2019 — 2024
*Developer*

Web system for recyclables and pooled packaging with document flow: M.E.Doc integration, supplier exchange over EDI, accounting reports.

`ASP.NET Core` `ASP.NET MVC` `EF Core` `MS SQL` `M.E.Doc` `EDI`


### SMS Messenger · 2020 — 2023
*Architect and developer*

The network's SMS notification platform: an in-house gateway to carriers over SMPP and to modems over GSM API, campaign queues, an API for internal systems.

`ASP.NET Core` `Web API` `SMPP` `GSM API` `MS SQL` `Hangfire`


### API Gateway and reporting service · 2018 — 2020
*Developer*

A gateway for the network's internal services and a reporting service over MS SQL: a single entry point, header and auth propagation, Excel exports.

`.NET Core` `Web API` `MS SQL` `SSRS` `GemBox.Spreadsheet`


### Fiscal workflows: excise stamps, AED, customs · 2019 — 2026
*Owner of the workstream*

End-to-end delivery of legislative change inside the trading system: excise stamp scanning, electronic excise documents, tax invoice adjustments, UKTZED codes, customs simplifications, the 14% VAT rate.

`Delphi` `T-SQL` `MS SQL` `EDI` `M.E.Doc`


## Experience

### Freelance and personal projects — AI / Python and Full Stack Developer
2026-03 — present · Dnipro · remote · Python, ML and full stack work

- Client work: NestJS with Prisma and PostgreSQL, Next.js 16 with React 19, a mobile app on Expo with MapLibre maps.
- Daily work with AI agents: MCP servers, custom subagents and hooks, and my own CDP browser inspector as agent tooling.
- A real-time speech pipeline: faster-whisper on CUDA, pyannote diarization, VAD, WASAPI capture.

### ATB-Market — Lead Application Programmer
2016-06 — present · Dnipro · Ukraine's largest grocery retail network

- Since 2018 also build internal services on ASP.NET Core and Angular: access, audit, reporting, integrations — 33 of the network's systems carry my code.
- UAM: access management for 2,000+ users on OpenID Connect, ADFS and Kerberos.
- Network integrations: EDI and e-document flow, M.E.Doc, Oracle EBS, 1C, Kafka, BizTalk, SSIS and SSRS.
- Engineering practice: xUnit and NSubstitute tests, SonarQube and Jenkins, Serilog, Docker, a private NuGet feed.
- Fiscal-law changes delivered end to end: excise stamps and AED, UKTZED, customs simplifications, VAT rates, in a live retail network.
- In parallel I maintain the legacy Delphi trading client whose functions are moving into the .NET services — I know the system being replaced from the inside.

Earlier: Freelance and private practice — Full Stack Developer (2015–2016) · Modern Professions Courses — Programming Instructor (2015–2016) · Kryvyi Rih Iron Ore Combine — Engineer Programmer (2013–2016) · OSSystem — Developer (2012–2013)


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

## Languages

- **Ukrainian** — native
- **English** — technical documentation and written communication; spoken at basic level