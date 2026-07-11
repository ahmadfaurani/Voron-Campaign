# Microsoft Defender Zero-Days — Distribution Package

**Classification:** TLP:GREEN  
**Date:** 2026-05-21  
**Priority:** P1 — CRITICAL  
**Distribution:** CSM, NACSA, MAMPU, Government CISOs, NCII Operators

---

## 📧 Distribution Email Template

**To:** CSM Director, NACSA Director, MAMPU Director, Agency CISOs  
**Subject:** [URGENT] Microsoft Defender Zero-Days (CVE-2026-41091, CVE-2026-45498) — Active Exploitation  
**Classification:** TLP:GREEN

---

**Assalamualaikum / Good Day,**

CyberSecurity Malaysia (HOI Intelligence Cell) is issuing an urgent advisory regarding **two Microsoft Defender zero-day vulnerabilities** that are **actively exploited in the wild** and listed on CISA's Known Exploited Vulnerabilities (KEV) Catalog.

### Executive Summary

| Attribute | CVE-2026-41091 | CVE-2026-45498 |
|-----------|----------------|----------------|
| **Vulnerability Type** | Privilege Escalation | Denial of Service |
| **CVSS Score** | 7.8 (HIGH) | 4.0 (MEDIUM) |
| **Affected Component** | Microsoft Malware Protection Engine | Defender Antimalware Platform |
| **Impact** | SYSTEM privilege access | DoS state on Windows device |
| **Patch Status** | ✅ 1.1.26040.8 | ✅ 4.18.26040.7 |
| **Exploitation** | ✅ **Active in wild** | ✅ **Active in wild** |
| **CISA KEV Listed** | ✅ Yes (May 20, 2026) | ✅ Yes (May 20, 2026) |
| **Federal Deadline** | June 3, 2026 | June 3, 2026 |

### Key Intelligence

1. **Patches Released:** May 21, 2026 (Wednesday) — automatic updates should apply by default
2. **CISA KEV Addition:** May 20, 2026 — confirms active exploitation
3. **CISA BOD 22-01:** Federal agencies must patch by June 3, 2026 (2 weeks)
4. **Attack Vector (CVE-2026-41091):** Improper link resolution before file access (CWE-59)
5. **Attack Vector (CVE-2026-45498):** Antimalware platform DoS trigger

### Immediate Actions Required

**1. Verify Patch Status (All Windows Systems):**
```powershell
# Open Windows Security → Virus & threat protection → Protection Updates
# Check: Settings → About → Antimalware ClientVersion
# Required: Malware Protection Platform ≥ 4.18.26040.7
```

**2. Force Update (If Not Auto-Updated):**
```powershell
# PowerShell: Force Defender update
Update-MpSignature

# Verify version
Get-MpComputerStatus | Select-Object AntimalwareClientVersion
```

**3. Enterprise Deployment:**
- SCCM: Deploy via WSUS/Config Manager
- Intune: Push Defender definition updates
- GPO: Enforce automatic update policy

### Malaysian Impact Assessment

| Sector | Impact Level | Action |
|--------|--------------|--------|
| **Government (MAMPU)** | HIGH — Windows prevalence | Immediate patch verification |
| **GLCs** | HIGH — Enterprise Defender | Verify + document compliance |
| **Financial (BNM)** | HIGH — RMiT compliance | BNM advisory recommended |
| **Healthcare** | MEDIUM — Mixed environment | MOH IT directive |
| **Enterprise** | MEDIUM — Patch management varies | Industry advisory |
| **SME** | LOW — Consumer Windows (auto-update) | Public advisory |

### Timeline

| Event | Date |
|-------|------|
| Exploitation Started | Before May 20, 2026 |
| CISA KEV Listed | May 20, 2026 |
| Patches Released | May 21, 2026 |
| Advisory Issued | May 21, 2026 |
| **Recommended Patch Deadline** | **May 28, 2026 (7 days)** |
| **CISA Federal Deadline** | **June 3, 2026** |

### Contact

**CyberSecurity Malaysia — HOI Intelligence Cell**  
**Email:** [CSM SOC Email]  
**Incident Hotline:** [CSM Hotline]

---

**Attachments:**
1. `msft-defender-zero-days-rapid-intel-brief.md` (Executive + Technical)
2. `msft-defender-remediation-checklist.md` (IT Admin Quick Reference)
3. `msft-defender-enterprise-deployment.md` (SCCM/Intune Guidance)

**Classification:** TLP:GREEN — Recipients may share within their organizations and with relevant stakeholders.

---

## 📎 Attachment 1: Executive Brief (Condensed)

### Microsoft Defender Zero-Days Threat Intelligence Brief

**CVE-2026-41091 + CVE-2026-45498 | Active Exploitation | CISA KEV Listed**

#### Key Judgments

| Judgment | Confidence |
|----------|------------|
| Active exploitation is ongoing | HIGH |
| Patches are effective and should auto-apply | HIGH |
| Enterprise verification is required (auto-update may fail) | HIGH |
| Malaysian government/enterprise Windows deployments are at risk | HIGH |

#### Technical Summary

**CVE-2026-41091 (Privilege Escalation):**
- **Root Cause:** Improper link resolution before file access (CWE-59)
- **Affected:** Microsoft Malware Protection Engine ≤ 1.1.26030.3008
- **Impact:** Attacker gains SYSTEM privileges
- **Prerequisites:** Local access, ability to create malicious file links

**CVE-2026-45498 (Denial of Service):**
- **Affected:** Microsoft Defender Antimalware Platform ≤ 4.18.26030.3011
- **Impact:** DoS state on unpatched Windows devices
- **Prerequisites:** Trigger specific antimalware platform condition

#### Affected Products

| Product | Component | Status |
|---------|-----------|--------|
| Microsoft Defender Antivirus | Malware Protection Engine | Affected (≤1.1.26030.3008) |
| Microsoft Defender Antivirus | Antimalware Platform | Affected (≤4.18.26030.3011) |
| System Center Endpoint Protection | Both components | Affected |
| System Center 2012 R2 Endpoint Protection | Both components | Affected |
| System Center 2012 Endpoint Protection | Both components | Affected |
| Microsoft Security Essentials | Both components | Affected |

#### Patch Versions

| Component | Patched Version | Release Date |
|-----------|-----------------|--------------|
| Malware Protection Engine | 1.1.26040.8 | May 21, 2026 |
| Antimalware Platform | 4.18.26040.7 | May 21, 2026 |

#### Recommendations

| Priority | Action | Owner | Deadline |
|----------|--------|-------|----------|
| **P1** | Verify Defender patch status on all Windows systems | Agency IT | 24 hours |
| **P1** | Force update if not auto-applied | Agency IT | 48 hours |
| **P1** | Enterprise deployment via SCCM/Intune | IT Operations | 48 hours |
| **P2** | Document compliance (version numbers) | Agency IT | 7 days |
| **P2** | Monitor for privilege escalation attempts | SOC | 14 days |
| **P3** | Review endpoint detection rules | SOC | 14 days |

---

## 📎 Attachment 2: Remediation Checklist (IT Admin)

### Microsoft Defender Zero-Days — IT Administrator Quick Reference

**Classification:** TLP:GREEN

#### Step 1: Verify Current Version

**GUI Method:**
1. Open Windows Security (search "Security" in Start menu)
2. Select "Virus & threat protection"
3. Click "Protection Updates"
4. Select "Check for updates"
5. Go to Settings → About
6. Check "Antimalware ClientVersion"

**PowerShell Method:**
```powershell
Get-MpComputerStatus | Select-Object AntimalwareClientVersion, AMEngineVersion, AMProductVersion

# Required versions:
# AntimalwareClientVersion ≥ 4.18.26040.7
# AMEngineVersion ≥ 1.1.26040.8
```

#### Step 2: Force Update (If Needed)

```powershell
# Force Defender signature update
Update-MpSignature

# Force platform update (if available via Windows Update)
Install-Module -Name PSWindowsUpdate
Get-WindowsUpdate -Install -AcceptAll -IgnoreReboot

# Verify after update
Get-MpComputerStatus | Select-Object AntimalwareClientVersion
```

#### Step 3: Enterprise Deployment (SCCM)

```powershell
# SCCM: Deploy Defender updates via Software Update Point
# 1. Sync updates from Microsoft Update
# 2. Create deployment package for Defender updates
# 3. Deploy to all Windows collections
# 4. Monitor compliance via SCCM console

# PowerShell: Check SCCM update status
Get-CMSoftwareUpdate -Name "*Defender*" | Select-Object ArticleID, DatePosted, IsExpired
```

#### Step 4: Enterprise Deployment (Intune)

```powershell
# Intune: Push Defender updates via Endpoint Analytics
# 1. Create proactive remediation package
# 2. Detection script: Check Defender version
# 3. Remediation script: Force update
# 4. Assign to all Windows 10/11 groups

# Detection Script:
Get-MpComputerStatus | Select-Object AntimalwareClientVersion
# Exit code 0 if ≥ 4.18.26040.7, else 1

# Remediation Script:
Update-MpSignature
```

#### Step 5: Document Compliance

```markdown
## Defender Patch Compliance Record

**System:** [hostname]
**Pre-Patch Version:** [version]
**Post-Patch Version:** [version]
**Patch Date:** [ISO8601]
**Deployment Method:** [Auto/SCCM/Intune/Manual]
**Verified By:** [admin name]
**Status:** ✅ COMPLIANT
```

#### Step 6: Monitor for Exploitation

```powershell
# Check Windows Event Logs for suspicious activity
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4688} -MaxEvents 100 |
  Where-Object {$_.Message -like "*MsMpEng*"} |
  Select-Object TimeCreated, Message

# Check for privilege escalation attempts
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4672} |
  Where-Object {$_.Message -like "*SYSTEM*"} |
  Select-Object TimeCreated, AccountName
```

---

## 📎 Attachment 3: Enterprise Deployment Guide

### Microsoft Defender Zero-Days — Enterprise Deployment (SCCM/Intune)

**Classification:** TLP:GREEN

#### SCCM Deployment

**Prerequisites:**
- SCCM Current Branch (latest)
- Software Update Point configured
- Windows 10/11 client collections

**Steps:**

1. **Sync Updates:**
   - SCCM Console → Software Library → Software Updates
   - Right-click "All Software Updates" → Synchronize Software Updates
   - Wait for sync completion (~15 minutes)

2. **Create Deployment Package:**
   - Right-click "All Software Updates" → Create Deployment Package
   - Name: "Defender Zero-Day Patch — May 2026"
   - Add updates: KB5056789 (Engine), KB5056790 (Platform)
   - Download to package source

3. **Deploy to Collections:**
   - Right-click deployment package → Deploy
   - Target: All Windows 10/11 collections
   - Schedule: ASAP (deadline: 48 hours)
   - User experience: Allow restart outside maintenance windows

4. **Monitor Compliance:**
   - SCCM Console → Monitoring → Deployments
   - View compliance by collection
   - Export non-compliant systems for follow-up

#### Intune Deployment

**Prerequisites:**
- Microsoft Intune license
- Windows 10/11 devices enrolled
- Endpoint Analytics configured

**Steps:**

1. **Create Proactive Remediation:**
   - Intune Console → Reports → Endpoint Analytics → Proactive Remediations
   - Create script package: "Defender Zero-Day Verification"

2. **Detection Script:**
```powershell
# Detect-DefenderVersion.ps1
$status = Get-MpComputerStatus
if ($status.AntimalwareClientVersion -ge "4.18.26040.7") {
    Write-Host "COMPLIANT"
    exit 0
} else {
    Write-Host "NON-COMPLIANT"
    exit 1
}
```

3. **Remediation Script:**
```powershell
# Remediate-DefenderUpdate.ps1
Update-MpSignature
Start-Sleep -Seconds 30
$status = Get-MpComputerStatus
if ($status.AntimalwareClientVersion -ge "4.18.26040.7") {
    Write-Host "UPDATE SUCCESSFUL"
    exit 0
} else {
    Write-Host "UPDATE FAILED"
    exit 1
}
```

4. **Assign to Groups:**
   - Assign to: All Windows 10/11 device groups
   - Schedule: Run once, repeat every 4 hours until compliant
   - Notifications: Show to end user (optional)

5. **Monitor Compliance:**
   - Intune Console → Reports → Endpoint Analytics → Script status
   - Export non-compliant devices for manual follow-up

#### GPO Enforcement (Automatic Updates)

**Steps:**

1. **Open Group Policy Management:**
   - gpmc.msc on domain controller

2. **Create/Edit GPO:**
   - Name: "Enforce Defender Auto-Update"
   - Link to: Domain or OU containing Windows systems

3. **Configure Settings:**
   - Computer Configuration → Administrative Templates → Windows Components → Microsoft Defender Antivirus
   - Policy: "Turn on behavior monitoring" → Enabled
   - Policy: "Scan mapped network drives during full scan" → Enabled
   - Policy: "Configure automatic updates" → Enabled (Auto download + notify for install)

4. **Force GPO Update:**
```powershell
gpupdate /force
```

---

**End of Distribution Package**

**Classification:** TLP:GREEN  
**Prepared By:** HOI Intelligence Cell, CyberSecurity Malaysia  
**Date:** 2026-05-21 16:57 UTC
