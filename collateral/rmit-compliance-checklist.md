# BNM RMiT Compliance Checklist 2026
## Revised Policy Document (November 28, 2025)
### Complete Implementation Guide for Malaysian Financial Institutions

**Generated:** 2026-07-01  
**Classification:** TLP:AMBER — For Distribution to BNM-Regulated FIs Only  
**Source:** Bank Negara Malaysia Policy Document on Risk Management in Technology (RMiT)  
**Compliance Deadline:** Gap Analysis Submission — February 26, 2026 (90 days from policy issuance)

---

## Executive Summary

The revised RMiT policy (November 28, 2025) introduces **stricter accountability**, **enhanced cybersecurity mandates**, and **accelerated compliance timelines** for all BNM-regulated financial institutions.

### Key Changes from 2020 Version:
1. **Personal Liability:** Board members and senior management now personally liable for non-compliance (RMiT para 1.3)
2. **24/7 SOC Mandate:** All FIs must maintain 24/7 Security Operations Center capability
3. **72-Hour Patching SLA:** Critical vulnerabilities on internet-facing systems must be patched within 72 hours
4. **3-Year Log Retention:** All security logs must be retained for minimum 3 years in tamper-proof storage
5. **Annual Cyber Drill:** Board-level cyber resilience exercise mandatory (not tabletop)
6. **Third-Party Risk Enhancement:** Expanded Domain 11 requirements for service provider resilience
7. **Cloud Security Framework:** Specific controls for cloud computing platforms
8. **Ethical AI Governance:** Requirements for ethical governance of emerging technologies

### Compliance Phases:
- **Phase 1 (Days 1-30):** Gap Assessment & Board Approval
- **Phase 2 (Days 31-90):** Remediation Planning & Budget Allocation
- **Phase 3 (Days 91-180):** Implementation & Integration
- **Phase 4 (Days 181-270):** Testing & Validation
- **Phase 5 (Days 271-365):** Ongoing Monitoring & Continuous Compliance

---

## Domain 1: GOVERNANCE & OVERSIGHT

### 1.1 Board Accountability (RMiT para 1.3)
- [ ] **Board Charter Updated:** RMiT responsibilities explicitly defined in Board Charter
- [ ] **Board Training:** All Board members completed RMiT awareness training (min 8 hours/year)
- [ ] **Board Risk Committee:** Established with at least one member with technology risk expertise
- [ ] **Quarterly Briefings:** Board receives quarterly technology risk reports (format per RMiT Appendix 2)
- [ ] **Annual Assessment:** Board conducts annual self-assessment on technology risk oversight effectiveness
- [ ] **Personal Liability Acknowledgment:** Board members signed acknowledgment of personal liability under RMiT

**Evidence Required:**
- Board Charter (updated)
- Training attendance records
- Board meeting minutes (last 4 quarters)
- Signed liability acknowledgments

**VoronDRQ Automation:**
- Automated Board report generation (RMiT Appendix 2 format)
- Board training tracking module
- Liability acknowledgment e-signature workflow

### 1.2 Senior Management Accountability (RMiT para 1.4)
- [ ] **CISO Appointment:** Designated Chief Information Security Officer (reporting to CEO/Board)
- [ ] **CIO Appointment:** Designated Chief Information Officer (if not combined with CISO)
- [ ] **RACI Matrix:** Clear RACI for technology risk decisions (Board → CEO → CISO/CIO → Staff)
- [ ] **KPI Integration:** Technology risk KPIs included in senior management performance reviews
- [ ] **Succession Planning:** Documented succession plan for CISO/CIO roles

**Evidence Required:**
- Organizational chart (showing CISO reporting line)
- CISO/CIO job descriptions
- RACI matrix document
- Performance review templates (with tech risk KPIs)
- Succession plan document

### 1.3 Technology Risk Management Framework (RMiT para 2.1)
- [ ] **Framework Document:** Comprehensive Technology Risk Management Framework approved by Board
- [ ] **Risk Appetite Statement:** Defined risk appetite for technology risks (quantitative + qualitative)
- [ ] **Risk Register:** Maintained technology risk register with all identified risks
- [ ] **Risk Assessment Methodology:** Documented methodology for technology risk assessment
- [ ] **Three Lines of Defense:** Clear delineation of 1st, 2nd, 3rd line responsibilities

**Evidence Required:**
- Technology Risk Management Framework (Board-approved)
- Risk Appetite Statement (Board-approved)
- Technology Risk Register (current)
- Risk Assessment Methodology document
- Three Lines of Defense RACI

**VoronDRQ Automation:**
- Pre-built Technology Risk Management Framework template
- Risk register with RMiT taxonomy
- Automated risk assessment workflows
- Three Lines of Defense mapping

---

## Domain 2: CYBERSECURITY STRATEGY (RMiT Domain 10)

### 2.1 Cybersecurity Strategic Plan (RMiT para 10.1)
- [ ] **3-Year Plan:** Board-approved 3-year cybersecurity strategic plan
- [ ] **Budget Alignment:** Annual cybersecurity budget aligned with strategic plan (min 12-18% of IT spend)
- [ ] **Threat Intelligence:** Formal threat intelligence program (internal + external feeds)
- [ ] **Cybersecurity Policy:** Comprehensive cybersecurity policy (Board-approved)
- [ ] **Annual Review:** Strategic plan reviewed and updated annually

**Evidence Required:**
- 3-Year Cybersecurity Strategic Plan (Board-approved)
- Annual cybersecurity budget documentation
- Threat intelligence program charter
- Cybersecurity Policy (Board-approved)
- Annual review minutes

**VoronDRQ Automation:**
- 3-Year Strategic Plan template (RMiT-aligned)
- Budget tracking dashboard
- Threat intelligence integration (via APIs)
- Policy management module

### 2.2 Security Operations Center (RMiT para 10.2)
- [ ] **24/7 SOC:** Operational 24/7 Security Operations Center (in-house or outsourced)
- [ ] **SOC SLA:** Defined SLAs for incident detection, analysis, and escalation
- [ ] **SIEM Platform:** Security Information and Event Management system deployed
- [ ] **Log Aggregation:** All security logs aggregated to SIEM (real-time)
- [ ] **Use Cases:** Minimum 50 SIEM use cases implemented (per RMiT Appendix 5)
- [ ] **SOC Staffing:** Adequate SOC staffing (min 1 analyst per 50 endpoints)
- [ ] **SOC Training:** SOC analysts completed certified training (min 40 hours/year)

**Evidence Required:**
- SOC operational procedures
- SOC SLA document
- SIEM architecture diagram
- Use case catalog (50+ use cases)
- SOC staffing plan
- SOC training records

**VoronDRQ Automation:**
- SOC integration workflows (SIEM connectors)
- Automated SLA monitoring
- Use case library (50+ pre-built RMiT use cases)
- SOC training tracking

### 2.3 Vulnerability Management (RMiT para 10.3)
- [ ] **Vulnerability Scanning:** Automated vulnerability scanning (weekly for internet-facing, monthly for internal)
- [ ] **Penetration Testing:** Annual penetration testing by independent third party
- [ ] **Critical Patching SLA:** Critical vulnerabilities patched within 72 hours (internet-facing)
- [ ] **High Patching SLA:** High vulnerabilities patched within 14 days
- [ ] **Medium Patching SLA:** Medium vulnerabilities patched within 30 days
- [ ] **Low Patching SLA:** Low vulnerabilities patched within 90 days
- [ ] **Patch Testing:** Formal patch testing process before production deployment
- [ ] **Exception Process:** Documented process for patching exceptions (with compensating controls)

**Evidence Required:**
- Vulnerability scanning reports (last 4 quarters)
- Penetration test reports (last 12 months)
- Patching SLA metrics (dashboard)
- Patch testing procedures
- Exception request/approval logs

**VoronDRQ Automation:**
- Automated vulnerability scanning integration (Qualys, Tenable, Rapid7)
- Patching SLA tracking dashboard
- Exception workflow automation
- Penetration test scheduling

### 2.4 Identity & Access Management (RMiT para 10.4)
- [ ] **MFA Implementation:** Multi-factor authentication for all privileged/remote access
- [ ] **Privileged Access Management:** PAM solution deployed for privileged accounts
- [ ] **Access Review:** Quarterly access reviews for all systems
- [ ] **Joiner-Mover-Leaver:** Automated JML workflow for access provisioning/deprovisioning
- [ ] **Password Policy:** Strong password policy (min 12 chars, 90-day rotation, no reuse)
- [ ] **Service Account Management:** Inventory and monitoring of service accounts
- [ ] **Access Logging:** All access attempts logged (successful and failed)

**Evidence Required:**
- MFA deployment report
- PAM solution architecture
- Access review reports (last 4 quarters)
- JML workflow documentation
- Password policy document
- Service account inventory
- Access log samples

**VoronDRQ Automation:**
- MFA compliance monitoring
- Access review automation
- JML workflow integration (HR system)
- Service account discovery

### 2.5 Security Awareness & Training (RMiT para 10.5)
- [ ] **Annual Training:** All employees completed annual security awareness training
- [ ] **Phishing Simulation:** Quarterly phishing simulations (target: <10% click rate)
- [ ] **Role-Based Training:** Specialized training for IT staff, developers, SOC analysts
- [ ] **Board Training:** Annual cybersecurity training for Board members
- [ ] **Training Metrics:** Tracking and reporting of training completion rates
- [ ] **Awareness Campaign:** Ongoing security awareness campaigns (posters, newsletters, etc.)

**Evidence Required:**
- Training completion reports (last 12 months)
- Phishing simulation reports (last 4 quarters)
- Role-based training curriculum
- Board training attendance records
- Training metrics dashboard
- Awareness campaign materials

**VoronDRQ Automation:**
- Training tracking module
- Phishing simulation integration
- Automated compliance reporting
- Awareness campaign template library

---

## Domain 3: LOG MANAGEMENT & RETENTION (RMiT para 10.6)

### 3.1 Log Collection (RMiT para 10.6a)
- [ ] **Log Sources:** All critical systems configured to generate security logs
- [ ] **Log Standardization:** Logs standardized to common format (CEF, LEEF, or JSON)
- [ ] **Real-Time Collection:** Logs collected in real-time (max 5-minute delay)
- [ ] **Log Integrity:** Logs protected from tampering (write-once storage)
- [ ] **Log Coverage:** Minimum 95% of systems sending logs to SIEM

**Evidence Required:**
- Log source inventory
- Log format standardization document
- Log collection architecture diagram
- Log integrity controls documentation
- Log coverage report

### 3.2 Log Retention (RMiT para 10.6b)
- [ ] **3-Year Retention:** All security logs retained for minimum 3 years
- [ ] **Tamper-Proof Storage:** Logs stored in write-once, read-many (WORM) format
- [ ] **Log Archiving:** Automated log archiving process (hot → warm → cold storage)
- [ ] **Log Retrieval:** Ability to retrieve logs within 24 hours for forensic investigation
- [ ] **Retention Policy:** Documented log retention policy (Board-approved)

**Evidence Required:**
- Log retention policy (Board-approved)
- Storage architecture diagram
- Log archiving procedures
- Log retrieval test results
- WORM storage certification

**VoronDRQ Automation:**
- Log retention policy template
- Automated log lifecycle management
- Log retrieval workflow
- Compliance reporting

### 3.3 Log Monitoring & Analysis (RMiT para 10.6c)
- [ ] **Real-Time Monitoring:** 24/7 monitoring of security logs
- [ ] **Alert Thresholds:** Defined alert thresholds for critical events
- [ ] **Correlation Rules:** SIEM correlation rules for detecting complex attacks
- [ ] **Baseline Analysis:** Established baseline for normal activity
- [ ] **Anomaly Detection:** Automated anomaly detection (UEBA or similar)

**Evidence Required:**
- Monitoring procedures
- Alert threshold documentation
- Correlation rule catalog
- Baseline analysis report
- Anomaly detection configuration

---

## Domain 4: INCIDENT MANAGEMENT (RMiT para 10.7)

### 4.1 Incident Response Plan (RMiT para 10.7a)
- [ ] **IRP Document:** Comprehensive Incident Response Plan (Board-approved)
- [ ] **IR Team:** Designated Incident Response Team with defined roles
- [ ] **Communication Plan:** Internal and external communication procedures
- [ ] **Escalation Matrix:** Clear escalation matrix (technical → management → Board)
- [ ] **BNM Notification:** Procedures for BNM notification (1-hour initial, 14-day full report)
- [ ] **Law Enforcement:** Procedures for law enforcement engagement (if applicable)
- [ ] **Customer Notification:** Procedures for customer notification (if applicable)
- [ ] **IR Testing:** Annual IR plan testing (tabletop + live simulation)

**Evidence Required:**
- Incident Response Plan (Board-approved)
- IR team roster and contact list
- Communication templates
- Escalation matrix
- BNM notification procedures
- IR test reports (last 12 months)

**VoronDRQ Automation:**
- IRP template (RMiT-aligned)
- Automated BNM notification workflow
- Escalation automation
- IR testing scenario library

### 4.2 Incident Reporting to BNM (RMiT para 10.7b)
- [ ] **1-Hour Initial Notification:** Process for initial notification within 1 hour of detection
- [ ] **14-Day Full Report:** Process for full incident report within 14 days
- [ ] **30-Day Post-Incident Review:** Process for post-incident review within 30 days
- [ ] **Reporting Portal:** Access to BNM Regulatory Reporting Portal
- [ ] **Report Templates:** Pre-defined report templates (per BNM format)
- [ ] **Reporting Training:** Staff trained on BNM reporting requirements

**Evidence Required:**
- BNM notification procedure document
- Sample initial notification (redacted)
- Sample full report (redacted)
- Post-incident review reports
- BNM portal access credentials (secured)
- Training attendance records

**VoronDRQ Automation:**
- BNM report template library
- Automated timeline tracking (1-hour, 14-day, 30-day deadlines)
- Report generation automation
- Regulatory portal integration

### 4.3 Incident Metrics & Learning (RMiT para 10.7c)
- [ ] **Incident Dashboard:** Real-time dashboard of security incidents
- [ ] **MTTD/MTTR:** Tracking Mean Time to Detect and Mean Time to Respond
- [ ] **Trend Analysis:** Quarterly trend analysis of incidents
- [ ] **Lessons Learned:** Post-incident lessons learned documented and implemented
- [ ] **Control Improvements:** Control improvements based on incident analysis

**Evidence Required:**
- Incident dashboard screenshots
- MTTD/MTTR metrics (last 4 quarters)
- Trend analysis reports
- Lessons learned documentation
- Control improvement tracker

---

## Domain 5: THIRD-PARTY RISK MANAGEMENT (RMiT Domain 11)

### 5.1 Third-Party Inventory (RMiT para 11.1)
- [ ] **Complete Inventory:** Comprehensive inventory of all third-party service providers
- [ ] **Criticality Assessment:** Each provider assessed for criticality (Critical/High/Medium/Low)
- [ ] **Contract Register:** Centralized register of all third-party contracts
- [ ] **SLA Tracking:** SLA performance tracking for all critical providers
- [ ] **Exit Strategy:** Exit strategy documented for each critical provider

**Evidence Required:**
- Third-party inventory (complete)
- Criticality assessment methodology
- Contract register
- SLA performance reports
- Exit strategy documents

**VoronDRQ Automation:**
- Third-party inventory database
- Automated criticality scoring
- Contract lifecycle management
- SLA monitoring dashboard

### 5.2 Due Diligence & Onboarding (RMiT para 11.2)
- [ ] **Due Diligence Checklist:** Standardized due diligence checklist for all providers
- [ ] **Security Assessment:** Security assessment for all critical providers
- [ ] **Right-to-Audit:** Contractual right-to-audit clause for all critical providers
- [ ] **Data Protection:** Data protection requirements in contracts (PDPA + RMiT)
- [ ] **Onboarding Process:** Formal onboarding process for new providers

**Evidence Required:**
- Due diligence checklist
- Security assessment reports
- Contract samples (with right-to-audit)
- Data protection clauses
- Onboarding procedure document

### 5.3 Ongoing Monitoring (RMiT para 11.3)
- [ ] **Annual Assessments:** Annual security assessments for all critical providers
- [ ] **Performance Reviews:** Quarterly performance reviews for critical providers
- [ ] **Incident Reporting:** Provider incident reporting requirements (24-hour notification)
- [ ] **Audit Rights:** Exercise of audit rights (at least once every 3 years for critical providers)
- [ ] **Concentration Risk:** Assessment of concentration risk (single provider dependency)

**Evidence Required:**
- Annual assessment reports
- Performance review minutes
- Provider incident reports
- Audit reports (last 3 years)
- Concentration risk assessment

**VoronDRQ Automation:**
- Automated annual assessment workflows
- Performance review scheduling
- Provider incident tracking
- Audit management module

### 5.4 Cloud Computing (RMiT para 11.4)
- [ ] **Cloud Strategy:** Board-approved cloud computing strategy
- [ ] **Cloud Provider Assessment:** Enhanced due diligence for cloud providers (CSP)
- [ ] **Data Residency:** Data residency requirements documented and enforced
- [ ] **Exit Strategy:** Cloud exit strategy (data portability, migration plan)
- [ ] **Shared Responsibility:** Clear understanding of shared responsibility model
- [ ] **Cloud Security Controls:** Implementation of cloud-specific security controls

**Evidence Required:**
- Cloud strategy document (Board-approved)
- CSP assessment reports
- Data residency compliance report
- Cloud exit plan
- Shared responsibility matrix
- Cloud security control implementation report

---

## Domain 6: BUSINESS CONTINUITY & DISASTER RECOVERY (RMiT Domain 12)

### 6.1 Business Impact Analysis (RMiT para 12.1)
- [ ] **BIA Completed:** Business Impact Analysis for all critical business functions
- [ ] **RTO/RPO Defined:** Recovery Time Objective and Recovery Point Objective defined for each function
- [ ] **Dependency Mapping:** Mapping of technology dependencies for each function
- [ ] **BIA Review:** Annual review and update of BIA
- [ ] **BIA Approval:** BIA approved by senior management

**Evidence Required:**
- BIA report (complete)
- RTO/RPO documentation
- Dependency mapping diagrams
- BIA review minutes
- BIA approval documentation

### 6.2 Disaster Recovery Plan (RMiT para 12.2)
- [ ] **DRP Document:** Comprehensive Disaster Recovery Plan (Board-approved)
- [ ] **DR Site:** Established disaster recovery site (hot/warm/cold)
- [ ] **Data Replication:** Real-time or near-real-time data replication to DR site
- [ ] **DR Testing:** Annual DR testing (full failover test)
- [ ] **DR Test Report:** Documented DR test results with lessons learned
- [ ] **DR Improvements:** Implementation of improvements based on DR tests

**Evidence Required:**
- DRP document (Board-approved)
- DR site architecture
- Data replication configuration
- DR test plan
- DR test report (last 12 months)
- Improvement tracker

**VoronDRQ Automation:**
- DRP template library
- DR test scheduling
- Lessons learned tracking
- Improvement workflow

### 6.3 Cyber Resilience Testing (RMiT para 12.3)
- [ ] **Annual Cyber Drill:** Annual cyber resilience drill (Board-level participation)
- [ ] **Scenario Diversity:** Multiple scenarios tested (ransomware, DDoS, data breach, etc.)
- [ ] **Third-Party Participation:** Key third-party providers included in drills
- [ ] **Drill Report:** Comprehensive drill report with findings
- [ ] **Remediation Plan:** Remediation plan for drill findings

**Evidence Required:**
- Cyber drill plan
- Drill scenarios documentation
- Drill attendance records (Board members)
- Drill report
- Remediation tracker

---

## Domain 7: TECHNOLOGY PROJECT MANAGEMENT (RMiT Domain 5)

### 7.1 Project Governance (RMiT para 5.1)
- [ ] **Project Charter:** Technology project charter for all major projects
- [ ] **Steering Committee:** Project steering committee with defined membership
- [ ] **Risk Assessment:** Technology risk assessment for all projects
- [ ] **Security Requirements:** Security requirements integrated into project lifecycle
- [ ] **Project Reporting:** Regular project reporting to senior management

**Evidence Required:**
- Project charter templates
- Steering committee terms of reference
- Risk assessment reports
- Security requirements documentation
- Project status reports

### 7.2 System Development Lifecycle (RMiT para 5.2)
- [ ] **SDLC Policy:** Formal SDLC policy (Board-approved)
- [ ] **Security Gates:** Security gates at each SDLC phase
- [ ] **Code Review:** Mandatory code review for all applications
- [ ] **Security Testing:** Security testing (SAST/DAST) integrated into CI/CD
- [ ] **Change Management:** Formal change management process

**Evidence Required:**
- SDLC policy document
- Security gate checklist
- Code review records
- Security test reports
- Change management logs

---

## Domain 8: REGULATORY REPORTING & COMPLIANCE (RMiT Domain 1)

### 8.1 Regulatory Reporting (RMiT para 1.5)
- [ ] **Reporting Calendar:** Annual regulatory reporting calendar
- [ ] **Report Templates:** Pre-defined templates for all BNM reports
- [ ] **Quality Assurance:** QA process for regulatory reports
- [ ] **Submission Tracking:** Tracking of report submissions and acknowledgments
- [ ] **Regulatory Changes:** Process for monitoring and implementing regulatory changes

**Evidence Required:**
- Reporting calendar
- Report template library
- QA checklists
- Submission tracking log
- Regulatory change tracker

**VoronDRQ Automation:**
- Regulatory calendar automation
- Report template library (BNM formats)
- Automated QA workflows
- Submission tracking dashboard
- Regulatory change monitoring

### 8.2 Audit & Examination (RMiT para 1.6)
- [ ] **Internal Audit Plan:** Annual internal audit plan (technology risk focus)
- [ ] **External Audit:** Annual external audit of technology controls
- [ ] **Audit Findings:** Tracking and remediation of audit findings
- [ ] **Regulatory Examinations:** Preparation for BNM examinations
- [ ] **Audit Committee Reporting:** Regular reporting to Audit Committee

**Evidence Required:**
- Internal audit plan
- External audit reports
- Audit findings tracker
- BNM examination preparation checklist
- Audit Committee meeting minutes

---

## COMPLIANCE SCORING & SELF-ASSESSMENT

### Scoring Methodology:
- **Fully Compliant (5):** All controls implemented, evidence available, no gaps
- **Mostly Compliant (4):** Minor gaps identified, remediation plan in place
- **Partially Compliant (3):** Significant gaps, remediation underway
- **Non-Compliant (2):** Major gaps, no remediation plan
- **Critical Non-Compliance (1):** Critical gaps, regulatory action likely

### Self-Assessment Template:

| Domain | Control ID | Control Description | Score | Evidence Location | Remediation Plan | Target Date |
|--------|-----------|---------------------|-------|-------------------|------------------|-------------|
| 1 | 1.1 | Board Accountability | | | | |
| 1 | 1.2 | Senior Management Accountability | | | | |
| 2 | 2.1 | Cybersecurity Strategic Plan | | | | |
| ... | ... | ... | | | | |

**Overall Compliance Score:** [Calculate average across all controls]

**Target:** Minimum 4.0 average (Mostly Compliant) for BNM submission

---

## NEXT STEPS & TIMELINE

### Immediate Actions (Days 1-30):
1. Complete this checklist (gap assessment)
2. Present findings to Board Risk Committee
3. Allocate budget for remediation
4. Appoint RMiT Compliance Officer

### Short-Term Actions (Days 31-90):
1. Submit gap analysis to BNM (deadline: February 26, 2026)
2. Begin remediation of critical gaps
3. Implement VoronDRQ (or alternative GRC platform)
4. Conduct Board training on RMiT

### Medium-Term Actions (Days 91-180):
1. Complete remediation of high-priority gaps
2. Conduct first full DR test
3. Complete annual penetration testing
4. Submit first quarterly compliance report to BNM

### Long-Term Actions (Days 181-365):
1. Achieve full compliance across all domains
2. Conduct annual cyber drill (Board participation)
3. Submit annual compliance self-assessment to BNM
4. Plan for continuous compliance monitoring

---

## VORONDRQ MAPPING

This checklist maps directly to VoronDRQ's RMiT compliance modules:

- **Domain 1:** Governance Dashboard + Board Reporting Module
- **Domain 2:** Cybersecurity Strategy Module + SOC Integration
- **Domain 3:** Log Management Module + SIEM Connectors
- **Domain 4:** Incident Management Module + BNM Reporting Automation
- **Domain 5:** Third-Party Risk Module + Vendor Assessment Workflows
- **Domain 6:** BCM/DR Module + Cyber Drill Scenario Library
- **Domain 7:** Project Management Module + SDLC Security Gates
- **Domain 8:** Regulatory Reporting Module + Audit Management

**Implementation Timeline:** 4-8 weeks for full deployment  
**Evidence Automation:** 80% of evidence collection automated  
**Board Reporting:** Real-time compliance dashboard  

---

## CONTACT & SUPPORT

**BNM Regulatory Contact:**  
Bank Negara Malaysia  
Technology Risk Supervision Division  
Email: rmit@bnm.gov.my  
Portal: https://www.bnm.gov.my/regulatory-reporting  

**VoronDRQ Support:**  
Email: support@vorondrq.com  
Phone: +60-3-XXXX-XXXX  
Portal: https://support.vorondrq.com  

**Document Control:**  
Version: 1.0  
Last Updated: 2026-07-01  
Next Review: 2026-10-01 (quarterly)  

---

*This checklist is provided as a reference guide. Financial institutions should consult the official BNM RMiT policy document and seek independent legal/compliance advice for specific interpretation.*
