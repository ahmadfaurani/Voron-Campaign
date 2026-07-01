# Voron Campaign - RMiT Compliance Checklist (Public Version)
## Complete Implementation Guide for Malaysian Financial Institutions

**Generated:** 2026-07-01  
**License:** CC BY 4.0  
**Source:** Bank Negara Malaysia Policy Document on Risk Management in Technology (RMiT)  
**Compliance Deadline:** Gap Analysis Submission — February 26, 2026

---

## Executive Summary

The revised RMiT policy (November 28, 2025) introduces **stricter accountability**, **enhanced cybersecurity mandates**, and **accelerated compliance timelines** for all BNM-regulated financial institutions.

### Key Changes from 2020 Version:
1. **Personal Liability:** Board members and senior management now personally liable for non-compliance
2. **24/7 SOC Mandate:** All FIs must maintain 24/7 Security Operations Center capability
3. **72-Hour Patching SLA:** Critical vulnerabilities on internet-facing systems must be patched within 72 hours
4. **3-Year Log Retention:** All security logs must be retained for minimum 3 years in tamper-proof storage
5. **Annual Cyber Drill:** Board-level cyber resilience exercise mandatory
6. **Third-Party Risk Enhancement:** Expanded requirements for service provider resilience
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

### 1.1 Board Accountability
- [ ] **Board Charter Updated:** RMiT responsibilities explicitly defined
- [ ] **Board Training:** All Board members completed RMiT awareness training (min 8 hours/year)
- [ ] **Board Risk Committee:** Established with technology risk expertise
- [ ] **Quarterly Briefings:** Board receives quarterly technology risk reports
- [ ] **Annual Assessment:** Board conducts annual self-assessment on technology risk oversight

**Evidence Required:**
- Board Charter (updated)
- Training attendance records
- Board meeting minutes (last 4 quarters)

### 1.2 Senior Management Accountability
- [ ] **CISO Appointment:** Designated Chief Information Security Officer (reporting to CEO/Board)
- [ ] **CIO Appointment:** Designated Chief Information Officer (if not combined)
- [ ] **RACI Matrix:** Clear RACI for technology risk decisions
- [ ] **KPI Integration:** Technology risk KPIs in senior management performance reviews

**Evidence Required:**
- Organizational chart (showing CISO reporting line)
- CISO/CIO job descriptions
- RACI matrix document

### 1.3 Technology Risk Management Framework
- [ ] **Framework Document:** Comprehensive Technology Risk Management Framework approved by Board
- [ ] **Risk Appetite Statement:** Defined risk appetite for technology risks
- [ ] **Risk Register:** Maintained technology risk register
- [ ] **Three Lines of Defense:** Clear delineation of responsibilities

**Evidence Required:**
- Technology Risk Management Framework (Board-approved)
- Risk Appetite Statement (Board-approved)
- Technology Risk Register (current)

---

## Domain 2: CYBERSECURITY STRATEGY

### 2.1 Cybersecurity Strategic Plan
- [ ] **3-Year Plan:** Board-approved 3-year cybersecurity strategic plan
- [ ] **Budget Alignment:** Annual cybersecurity budget aligned with strategic plan
- [ ] **Threat Intelligence:** Formal threat intelligence program
- [ ] **Cybersecurity Policy:** Comprehensive cybersecurity policy (Board-approved)

**Evidence Required:**
- 3-Year Cybersecurity Strategic Plan
- Annual cybersecurity budget documentation
- Cybersecurity Policy (Board-approved)

### 2.2 Security Operations Center (SOC)
- [ ] **24/7 SOC:** Operational 24/7 Security Operations Center
- [ ] **SOC SLA:** Defined SLAs for incident detection, analysis, escalation
- [ ] **SIEM Platform:** Security Information and Event Management system deployed
- [ ] **Log Aggregation:** All security logs aggregated to SIEM (real-time)
- [ ] **Use Cases:** Minimum 50 SIEM use cases implemented

**Evidence Required:**
- SOC operational procedures
- SIEM architecture diagram
- Use case catalog (50+ use cases)

### 2.3 Vulnerability Management
- [ ] **Vulnerability Scanning:** Automated scanning (weekly internet-facing, monthly internal)
- [ ] **Penetration Testing:** Annual penetration testing by independent third party
- [ ] **Critical Patching SLA:** 72 hours for internet-facing systems
- [ ] **High Patching SLA:** 14 days for high vulnerabilities
- [ ] **Medium Patching SLA:** 30 days for medium vulnerabilities

**Evidence Required:**
- Vulnerability scanning reports (last 4 quarters)
- Penetration test reports (last 12 months)
- Patching SLA metrics dashboard

### 2.4 Identity & Access Management
- [ ] **MFA Implementation:** Multi-factor authentication for all privileged/remote access
- [ ] **Privileged Access Management:** PAM solution deployed
- [ ] **Access Review:** Quarterly access reviews for all systems
- [ ] **Joiner-Mover-Leaver:** Automated JML workflow

**Evidence Required:**
- MFA deployment report
- PAM solution architecture
- Access review reports (last 4 quarters)

### 2.5 Security Awareness & Training
- [ ] **Annual Training:** All employees completed annual security awareness training
- [ ] **Phishing Simulation:** Quarterly phishing simulations
- [ ] **Role-Based Training:** Specialized training for IT staff, developers, SOC analysts
- [ ] **Board Training:** Annual cybersecurity training for Board members

**Evidence Required:**
- Training completion reports (last 12 months)
- Phishing simulation reports (last 4 quarters)

---

## Domain 3: LOG MANAGEMENT & RETENTION

### 3.1 Log Collection
- [ ] **Log Sources:** All critical systems configured to generate security logs
- [ ] **Log Standardization:** Logs standardized to common format (CEF, LEEF, or JSON)
- [ ] **Real-Time Collection:** Logs collected in real-time (max 5-minute delay)
- [ ] **Log Integrity:** Logs protected from tampering

### 3.2 Log Retention
- [ ] **3-Year Retention:** All security logs retained for minimum 3 years
- [ ] **Tamper-Proof Storage:** Logs stored in write-once, read-many (WORM) format
- [ ] **Log Archiving:** Automated log archiving process
- [ ] **Log Retrieval:** Ability to retrieve logs within 24 hours for forensic investigation

**Evidence Required:**
- Log retention policy
- Storage architecture diagram
- Log retrieval test results

### 3.3 Log Monitoring & Analysis
- [ ] **Real-Time Monitoring:** 24/7 monitoring of security logs
- [ ] **Alert Thresholds:** Defined alert thresholds for critical events
- [ ] **Correlation Rules:** SIEM correlation rules for detecting complex attacks
- [ ] **Anomaly Detection:** Automated anomaly detection (UEBA or similar)

---

## Domain 4: INCIDENT MANAGEMENT

### 4.1 Incident Response Plan
- [ ] **IRP Document:** Comprehensive Incident Response Plan (Board-approved)
- [ ] **IR Team:** Designated Incident Response Team with defined roles
- [ ] **Communication Plan:** Internal and external communication procedures
- [ ] **Escalation Matrix:** Clear escalation matrix
- [ ] **IR Testing:** Annual IR plan testing (tabletop + live simulation)

**Evidence Required:**
- Incident Response Plan (Board-approved)
- IR team roster and contact list
- IR test reports (last 12 months)

### 4.2 Incident Reporting to BNM
- [ ] **1-Hour Initial Notification:** Process for initial notification within 1 hour
- [ ] **14-Day Full Report:** Process for full incident report within 14 days
- [ ] **30-Day Post-Incident Review:** Process for review within 30 days
- [ ] **Reporting Portal:** Access to BNM Regulatory Reporting Portal

**Evidence Required:**
- BNM notification procedure document
- Sample reports (redacted)
- Post-incident review reports

### 4.3 Incident Metrics & Learning
- [ ] **Incident Dashboard:** Real-time dashboard of security incidents
- [ ] **MTTD/MTTR:** Tracking Mean Time to Detect and Mean Time to Respond
- [ ] **Trend Analysis:** Quarterly trend analysis of incidents
- [ ] **Lessons Learned:** Post-incident lessons learned documented

---

## Domain 5: THIRD-PARTY RISK MANAGEMENT

### 5.1 Third-Party Inventory
- [ ] **Complete Inventory:** Comprehensive inventory of all third-party service providers
- [ ] **Criticality Assessment:** Each provider assessed for criticality
- [ ] **Contract Register:** Centralized register of all third-party contracts
- [ ] **SLA Tracking:** SLA performance tracking for critical providers

### 5.2 Due Diligence & Onboarding
- [ ] **Due Diligence Checklist:** Standardized checklist for all providers
- [ ] **Security Assessment:** Security assessment for all critical providers
- [ ] **Right-to-Audit:** Contractual right-to-audit clause for critical providers
- [ ] **Data Protection:** Data protection requirements in contracts

### 5.3 Ongoing Monitoring
- [ ] **Annual Assessments:** Annual security assessments for critical providers
- [ ] **Performance Reviews:** Quarterly performance reviews
- [ ] **Incident Reporting:** Provider incident reporting requirements (24-hour)
- [ ] **Audit Rights:** Exercise audit rights (at least once every 3 years)

### 5.4 Cloud Computing
- [ ] **Cloud Strategy:** Board-approved cloud computing strategy
- [ ] **Cloud Provider Assessment:** Enhanced due diligence for CSPs
- [ ] **Data Residency:** Data residency requirements documented and enforced
- [ ] **Exit Strategy:** Cloud exit strategy (data portability, migration plan)
- [ ] **Shared Responsibility:** Clear understanding of shared responsibility model

---

## Domain 6: BUSINESS CONTINUITY & DISASTER RECOVERY

### 6.1 Business Impact Analysis
- [ ] **BIA Completed:** Business Impact Analysis for all critical business functions
- [ ] **RTO/RPO Defined:** Recovery Time Objective and Recovery Point Objective defined
- [ ] **Dependency Mapping:** Mapping of technology dependencies
- [ ] **BIA Review:** Annual review and update of BIA

### 6.2 Disaster Recovery Plan
- [ ] **DRP Document:** Comprehensive Disaster Recovery Plan (Board-approved)
- [ ] **DR Site:** Established disaster recovery site (hot/warm/cold)
- [ ] **Data Replication:** Real-time or near-real-time data replication to DR site
- [ ] **DR Testing:** Annual DR testing (full failover test)

**Evidence Required:**
- DRP document (Board-approved)
- DR site architecture
- DR test report (last 12 months)

### 6.3 Cyber Resilience Testing
- [ ] **Annual Cyber Drill:** Annual cyber resilience drill (Board-level participation)
- [ ] **Scenario Diversity:** Multiple scenarios tested (ransomware, DDoS, data breach)
- [ ] **Third-Party Participation:** Key providers included in drills
- [ ] **Drill Report:** Comprehensive drill report with findings

---

## Domain 7: TECHNOLOGY PROJECT MANAGEMENT

### 7.1 Project Governance
- [ ] **Project Charter:** Technology project charter for all major projects
- [ ] **Steering Committee:** Project steering committee with defined membership
- [ ] **Risk Assessment:** Technology risk assessment for all projects
- [ ] **Security Requirements:** Security requirements integrated into project lifecycle

### 7.2 System Development Lifecycle (SDLC)
- [ ] **SDLC Policy:** Formal SDLC policy (Board-approved)
- [ ] **Security Gates:** Security gates at each SDLC phase
- [ ] **Code Review:** Mandatory code review for all applications
- [ ] **Security Testing:** Security testing (SAST/DAST) integrated into CI/CD
- [ ] **Change Management:** Formal change management process

---

## Domain 8: REGULATORY REPORTING & COMPLIANCE

### 8.1 Regulatory Reporting
- [ ] **Reporting Calendar:** Annual regulatory reporting calendar
- [ ] **Report Templates:** Pre-defined templates for all BNM reports
- [ ] **Quality Assurance:** QA process for regulatory reports
- [ ] **Submission Tracking:** Tracking of report submissions
- [ ] **Regulatory Changes:** Process for monitoring regulatory changes

### 8.2 Audit & Examination
- [ ] **Internal Audit Plan:** Annual internal audit plan (technology risk focus)
- [ ] **External Audit:** Annual external audit of technology controls
- [ ] **Audit Findings:** Tracking and remediation of audit findings
- [ ] **Regulatory Examinations:** Preparation for BNM examinations

---

## COMPLIANCE SCORING & SELF-ASSESSMENT

### Scoring Methodology:
- **Fully Compliant (5):** All controls implemented, evidence available, no gaps
- **Mostly Compliant (4):** Minor gaps, remediation plan in place
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
3. Implement GRC platform (or alternative)
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

## CONTACT & SUPPORT

**BNM Regulatory Contact:**  
Bank Negara Malaysia  
Technology Risk Supervision Division  
Email: rmit@bnm.gov.my  
Portal: https://www.bnm.gov.my/regulatory-reporting  

**Document Control:**  
Version: 1.0 (Public)  
Last Updated: 2026-07-01  
Next Review: 2026-10-01 (quarterly)  

---

**License:** CC BY 4.0 — Free to use with attribution  
**Attribution:** "Checklist adapted from Voron Campaign (github.com/ahmadfaurani/Voron-Campaign)"  
**Source:** Bank Negara Malaysia Policy Document on Risk Management in Technology (November 2025)

*This checklist is provided as a reference guide. Financial institutions should consult the official BNM RMiT policy document and seek independent legal/compliance advice for specific interpretation.*
