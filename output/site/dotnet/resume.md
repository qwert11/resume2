# Yurii Zaika

**Senior .NET Engineer**

xetr11@gmail.com · t.me/xetr_11 · github.com/qwert11 · Dnipro, Ukraine · remote or hybrid

Senior .NET engineer: ASP.NET Core and Web API, EF Core and T-SQL, integrations over EDI, Kafka and Oracle EBS, authentication through OIDC, ADFS and Kerberos. Built the in-house access management system used by 2,000+ people.

## At a glance

- 10 years — in production retail systems, 2016 to now
- 2 000+ — users on the access system I built
- 33 — internal systems of the network I built or extended
- 8 years — building the network's internal services on ASP.NET Core, since 2018

## What I delivered

- Built UAM, the network's in-house access management system: 2,000+ users on OpenID Connect, ADFS and Kerberos, replacing per-system manual permission handling.
- Architected and built the network's SMS notification platform: SMPP and GSM API, .NET Web API and MS SQL, designed for peak-volume campaigns.
- Built the internal web systems stores work with: journals and audit, recyclables with M.E.Doc integration, a support portal, coupons and reporting.
- Deliver fiscal-law changes end to end across the systems: excise stamps and electronic excise documents (AED), UKTZED commodity codes, customs simplifications, new VAT rates, all in a live retail network without stopping the stores.

## Stack

- **Backend:** C#, .NET (Core 3.1 → 7), ASP.NET Core, ASP.NET MVC, Web API / REST, SignalR, Worker Services, Hangfire, Quartz, AutoMapper
- **Data:** MS SQL Server, T-SQL, PostgreSQL, EF Core, ADO.NET, Oracle, SSIS, SSRS, SQL CLR
- **Front end:** Angular 13, TypeScript, React 19, Next.js 16, Kendo UI for Angular, Telerik UI for ASP.NET Core, Razor / MVC views, Tailwind CSS, Zustand / TanStack Query, Expo / React Native, MapLibre, JavaScript, HTML / CSS
- **Access and security:** OpenID Connect, OAuth2, JWT Bearer, ADFS, Kerberos / Negotiate, Active Directory, RBAC
- **Integrations:** EDI / e-document flow, M.E.Doc, Oracle EBS, 1C, Kafka, BizTalk, WCF / SOAP, SMPP / GSM API, API Gateway
- **Quality and delivery:** xUnit / NUnit, NSubstitute / Moq, AutoFixture, FluentAssertions, SonarQube, Jenkins, Docker, Serilog / NLog, Elastic APM, Git / private NuGet feed
- **Engineering practice:** Production ownership, Legacy modernization, Integration design, Modular monolith, GitHub Actions
- **Working with AI agents:** Claude Code, MCP servers, Custom subagents and hooks, Agent tooling (CDP)

## Key projects

### UAM — access management · 2020 — 2022

Centralized permissions and authentication for 2,000+ people in the network: roles and access requests, Active Directory integration, sign-in through OpenID Connect, ADFS and Kerberos.

`ASP.NET Core` `C#` `EF Core` `MS SQL` `OIDC` `ADFS` `Angular`


### SMS Messenger · 2020 — 2023
*Architect and developer*

The network's SMS notification platform: an in-house gateway to carriers over SMPP and to modems over GSM API, campaign queues, an API for internal systems.

`ASP.NET Core` `Web API` `SMPP` `GSM API` `MS SQL` `Hangfire`


### API Gateway and reporting service · 2018 — 2020

A gateway for the network's internal services and a reporting service over MS SQL: a single entry point, header and auth propagation, Excel exports.

`.NET Core` `Web API` `MS SQL` `SSRS` `GemBox.Spreadsheet`


### Store Journals · 2021 — 2023

Journals and audit platform for the network's stores: in-store entry, inspections, regional reporting, real-time updates over SignalR.

`ASP.NET Core` `Angular 13` `Kendo UI` `EF Core` `MS SQL` `SignalR`


### Recyclables and returnable packaging · 2019 — 2024

Web system for recyclables and pooled packaging with document flow: M.E.Doc integration, supplier exchange over EDI, accounting reports.

`ASP.NET Core` `ASP.NET MVC` `EF Core` `MS SQL` `M.E.Doc` `EDI`


### AM Mobility — web and mobile app · 2026
*Full stack developer*

Client project: a NestJS back end with Swagger and PostgreSQL, a Next.js web app, and an Expo / React Native mobile app with MapLibre maps, geolocation and offline state.

`NestJS` `Next.js` `Expo` `React Native` `PostgreSQL` `MapLibre` `TanStack Query`


## Experience

### ATB-Market — Lead Software Engineer
2016-06 — present · Dnipro · Ukraine's largest grocery retail network

- Since 2018 I build and run the network's internal services on ASP.NET Core and Angular: access, audit, reporting, integrations — 33 of the network's systems I built or extended.
- UAM: access management for 2,000+ users on OpenID Connect, ADFS and Kerberos.
- Architected and built the network's SMS notification platform: SMPP and GSM API, .NET Web API, MS SQL — designed for peak-volume campaigns.
- Network integrations: EDI and e-document flow, M.E.Doc, Oracle EBS, 1C, Kafka, BizTalk, SSIS and SSRS.
- Engineering practice: xUnit and NSubstitute tests, SonarQube and Jenkins, Serilog, Docker, a private NuGet feed.
- In parallel I maintain the legacy Delphi trading client whose functions are moving into the .NET services — I know the system being replaced from the inside.

### Personal projects and freelance — Independent developer
2026-03 — present · Dnipro · remote · alongside the full-time role at ATB-Market

- Client work: NestJS with Prisma and PostgreSQL, Next.js 16 with React 19, a mobile app on Expo with MapLibre maps.
- Daily work with AI agents: MCP servers, custom subagents and hooks, and my own CDP browser inspector as agent tooling.

Earlier: Freelance and private practice — Full Stack Developer (2015–2016) · Modern Professions Courses — Programming Instructor (2015–2016) · Kryvyi Rih Iron Ore Combine — Software Engineer (2013–2016) · OSSystem — Developer (2012–2013)


## Domain knowledge

- **Excise control: electronic excise stamps and documents (AED)** — Stamp scanning, electronic excise documents, document number in the invoice
- **Tax invoices and adjustments** — Issuing, adjustments, field rules aligned with the tax service
- **Commodity classification codes (HS / UKTZED)** — Commodity code synchronization across the network's systems
- **Customs and import clearance** — Customs declarations, import receipts into warehouses, reporting
- **EDI and e-document flow** — Orders, waybills, pooled packaging, supplier exchange
- **VAT rates and pricing regions** — Cross-system rate changes, region setup when a store opens

## Education and certificates

- **Computer Engineering · computer systems and networks** — Zaporizhzhia Institute of Economics and Information Technologies ()
- **Angular 9** — Luxoft (2021)

## Languages

- **Ukrainian** — native
- **English** — technical documentation and written communication