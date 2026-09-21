# Yurii Zaika

**Senior Delphi Engineer · Legacy Modernization**

xetr11@gmail.com · t.me/xetr_11 · github.com/qwert11 · Dnipro, Ukraine · remote or hybrid

Delphi engineer with ten years of production ownership of a retail trading system: 955 units, 828 forms, MS SQL. Currently migrating the client from Delphi 6 to Delphi 12, with a purpose-built tool that diffs forms and database mappings between the two versions.

## At a glance

- 10 years — in production retail systems, 2016 to now
- 33 — internal systems of the network carry my code
- 2 stacks — Delphi and .NET in parallel, with the business running
- 955 units — and 828 forms in the trading system client

## What I delivered

- Built UAM, the network's in-house access management system: 2,000+ users on OpenID Connect, ADFS and Kerberos, replacing per-system manual permission handling.
- Leading the trading system client migration from Delphi 6 to Delphi 12/13, with a purpose-built tool that diffs forms and database mappings between versions so the switch does not break store operations.
- Architected and built the network's SMS notification platform: SMPP and GSM API, .NET Web API and MS SQL, designed for peak-volume campaigns.
- Deliver fiscal-law changes end to end across the systems: excise stamps and AED, UKTZED codes, customs simplifications, new VAT rates, all in a live retail network without stopping the stores.
- Built the internal web systems stores work with: journals and audit, recyclables with M.E.Doc integration, a support portal, coupons and reporting.

## Stack

- **Data:** MS SQL Server, T-SQL, EF Core 7, ADO.NET, Oracle, PostgreSQL, Firebird, SSIS, SSRS, SQL CLR
- **Integrations:** EDI / ЕДО, M.E.Doc, WCF / SOAP
- **Quality and delivery:** xUnit / NUnit, NSubstitute / Moq, AutoFixture, FluentAssertions, SonarQube, Jenkins, Docker, Serilog / NLog, Elastic APM, Git / приватний NuGet
- **Desktop:** Delphi 6 → 12 / 13, Object Pascal, VCL, DevExpress, FastReport, RX Library, Indy, NativeExcel / NativeXml, ADO / OLE DB
- **Engineering practice:** Legacy modernization, Modular monolith, Three-tier architecture, Integration design, Production ownership

## Key projects

### Trading client migration: Delphi 6 to Delphi 12 · 2024 — 2026
*Migration lead*

Moving the trading system client (955 units, 828 forms) to a modern compiler with a core redesign. Built a separate tool that diffs forms and table mappings between the old and new versions, so the migration runs without stopping stores.

`Delphi 12/13` `Object Pascal` `VCL` `MS SQL` `DevExpress` `FastReport`

https://github.com/qwert11/d6_d13_dbmapping_checker


### Fiscal workflows: excise stamps, AED, customs · 2019 — 2026
*Owner of the workstream*

End-to-end delivery of legislative change inside the trading system: excise stamp scanning, electronic excise documents, tax invoice adjustments, UKTZED codes, customs simplifications, the 14% VAT rate.

`Delphi` `T-SQL` `MS SQL` `EDI` `M.E.Doc`


### UAM — access management · 2020 — 2022
*Developer*

Centralized permissions and authentication for 2,000+ people in the network: roles and access requests, Active Directory integration, sign-in through OpenID Connect, ADFS and Kerberos.

`ASP.NET Core` `C#` `EF Core` `MS SQL` `OIDC` `ADFS` `Angular`


### Store Journals · 2021 — 2023
*Developer*

Journals and audit platform for the network's stores: in-store entry, inspections, regional reporting. The most code-intensive of the web systems.

`ASP.NET Core` `Angular 13` `Kendo UI` `EF Core` `MS SQL` `SignalR`


### Recyclables and returnable packaging · 2019 — 2024
*Developer*

Web system for recyclables and pooled packaging with document flow: M.E.Doc integration, supplier exchange over EDI, accounting reports.

`ASP.NET Core` `ASP.NET MVC` `EF Core` `MS SQL` `M.E.Doc` `EDI`


### SMS Messenger · 2020 — 2023
*Architect and developer*

The network's SMS notification platform: an in-house gateway to carriers over SMPP and to modems over GSM API, campaign queues, an API for internal systems.

`ASP.NET Core` `Web API` `SMPP` `GSM API` `MS SQL` `Hangfire`


## Experience

### ATB-Market — Lead Application Programmer
2016-06 — present · Dnipro · Ukraine's largest grocery retail network

- Own the client side of the network's trading system: 955 units, 828 forms, MS SQL, covering supply documents, pricing and fiscal invoices.
- Since 2018 also build internal services on ASP.NET Core and Angular: access, audit, reporting, integrations — 33 of the network's systems carry my code.
- UAM: access management for 2,000+ users on OpenID Connect, ADFS and Kerberos.
- Network integrations: EDI and e-document flow, M.E.Doc, Oracle EBS, 1C, Kafka, BizTalk, SSIS and SSRS.
- Fiscal-law changes delivered end to end: excise stamps and AED, UKTZED, customs simplifications, VAT rates, in a live retail network.
- Leading the client migration from Delphi 6 to Delphi 12/13 with an in-house form and DB-mapping diff tool.
- Engineering practice: xUnit and NSubstitute tests, SonarQube and Jenkins, Serilog, Docker, a private NuGet feed.

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