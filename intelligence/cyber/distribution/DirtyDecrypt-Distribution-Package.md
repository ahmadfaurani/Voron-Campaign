# DirtyDecrypt (CVE-2026-31635) — Distribution Package

**Classification:** TLP:GREEN  
**Date:** 2026-05-21  
**Priority:** P1 — CRITICAL  
**Distribution:** CSM, NACSA, MAMPU, Government CISOs, NCII Operators

---

## 📧 Distribution Email Template

**To:** CSM Director, NACSA Director, MAMPU Director, Agency CISOs  
**Subject:** [URGENT] Linux Kernel LPE Vulnerability (CVE-2026-31635) — Public PoC Available  
**Classification:** TLP:GREEN

---

**Assalamualaikum / Good Day,**

CyberSecurity Malaysia (HOI Intelligence Cell) is issuing an urgent advisory regarding **CVE-2026-31635 (DirtyDecrypt)**, a high-severity Linux kernel local privilege escalation vulnerability with **publicly available exploit code**.

### Executive Summary

| Attribute | Details |
|-----------|---------|
| **Vulnerability** | DirtyDecrypt (aka DirtyCBC) |
| **CVE ID** | CVE-2026-31635 |
| **Severity** | HIGH (Root privilege escalation) |
| **PoC Status** | ✅ **PUBLIC** (Working exploit on GitHub) |
| **Patch Status** | ✅ Available (April 25, 2026) |
| **Affected Systems** | Fedora, Arch Linux, openSUSE Tumbleweed, RHEL/CentOS Stream (kernel-ml) |
| **Container Escape** | ✅ Yes (Host root → all Kubernetes pods/secrets) |

### Key Intelligence

1. **Root Cause:** Missing copy-on-write (COW) guard in Linux kernel RxGK subsystem
2. **Attack Vector:** Local unprivileged user → root via page-cache corruption
3. **Target Files:** /etc/shadow, /etc/sudoers, SUID binaries
4. **Container Risk:** Successful exploitation grants access to all pods, container runtime sockets, Kubernetes secrets on affected worker nodes
5. **Exploitation Precedent:** Sister vulnerability "Copy Fail" (CVE-2026-31431) is **actively exploited** and CISA KEV-listed

### Immediate Actions Required

**1. Verify Exposure (All Linux Systems):**
```bash
zcat /proc/config.gz | grep RXGK
# If CONFIG_RXGK=y or CONFIG_RXGK=m → AFFECTED
```

**2. Patch Immediately (Affected Distributions):**
```bash
# Fedora
sudo dnf upgrade --refresh kernel kernel-core kernel-modules && sudo systemctl reboot

# Arch Linux
sudo pacman -Syu linux linux-headers && sudo systemctl reboot

# openSUSE Tumbleweed
sudo zypper dup && sudo systemctl reboot
```

**3. Kubernetes-Specific Hardening:**
- Rebuild worker node images with patched kernel
- Enforce Pod Security Admission (restricted profile)
- Set `allowPrivilegeEscalation: false` cluster-wide
- Deploy Falco runtime detection rules (see technical appendix)

**4. Workaround (If Patching Delayed):**
```bash
# Blacklist affected kernel modules
echo "blacklist rxrpc" >> /etc/modprobe.d/blacklist.conf
echo "blacklist esp4" >> /etc/modprobe.d/blacklist.conf
echo "blacklist esp6" >> /etc/modprobe.d/blacklist.conf
# ⚠️ WARNING: Breaks IPsec VPN and AFS mounts
```

### Malaysian Impact Assessment

| Sector | Impact Level | Action |
|--------|--------------|--------|
| **Government (MAMPU)** | HIGH — Fedora/Arch workstations | Immediate patch verification |
| **MyGovCloud (K8s)** | CRITICAL — Container escape vector | Worker node rebuild required |
| **GLCs (Linux infra)** | HIGH — Rolling release distros | Patch within 24 hours |
| **Financial (BNM)** | MEDIUM — Enterprise Linux | Verify + patch |
| **Telco/Energy (NCII)** | HIGH — Kubernetes clusters | Priority remediation |

### Timeline

| Event | Date |
|-------|------|
| Patch Released | April 25, 2026 |
| PoC Public | May 9-10, 2026 |
| Advisory Issued | May 21, 2026 |
| **Recommended Patch Deadline** | **May 23, 2026 (48 hours)** |

### Contact

**CyberSecurity Malaysia — HOI Intelligence Cell**  
**Email:** [CSM SOC Email]  
**Incident Hotline:** [CSM Hotline]

---

**Attachments:**
1. `dirtydecrypt-rapid-intel-brief.md` (Executive + Technical)
2. `dirtydecrypt-remediation-checklist.md` (IT Admin Quick Reference)
3. `dirtydecrypt-kubernetes-hardening.md` (K8s-Specific Guidance)

**Classification:** TLP:GREEN — Recipients may share within their organizations and with relevant stakeholders.

---

## 📎 Attachment 1: Executive Brief (Condensed)

### DirtyDecrypt Threat Intelligence Brief

**CVE-2026-31635 | Linux Kernel LPE | Public PoC**

#### Key Judgments

| Judgment | Confidence |
|----------|------------|
| Exploitation is trivial with public PoC | HIGH |
| Container escape is achievable on unpatched K8s nodes | HIGH |
| Malaysian government Linux deployments are at risk | MEDIUM |
| Patch adoption is the primary mitigation | HIGH |

#### Technical Summary

- **Affected Component:** Linux kernel RxGK subsystem (rxgk_decrypt_skb function)
- **Vulnerability Class:** Missing COW guard → shared page-cache write
- **Privileges Gained:** Root (via /etc/shadow, /etc/sudoers, or SUID binary corruption)
- **Prerequisites:** Local unprivileged access, CONFIG_RXGK enabled

#### IOC Summary

| Type | Indicator | Confidence |
|------|-----------|------------|
| **GitHub PoC** | github.com/v12-security/pocs | HIGH |
| **GitHub PoC** | github.com/0xBlackash/CVE-2026-31635 | HIGH |
| **Kernel Function** | rxgk_decrypt_skb() | HIGH |
| **Config Flag** | CONFIG_RXGK=y or =m | HIGH |

#### Recommendations

| Priority | Action | Owner | Deadline |
|----------|--------|-------|----------|
| **P1** | Inventory affected Linux systems | Agency IT | 24 hours |
| **P1** | Patch all affected systems | Agency IT | 48 hours |
| **P1** | Rebuild K8s worker nodes with patched kernel | DevOps | 48 hours |
| **P2** | Enforce Pod Security Admission (restricted) | DevOps | 7 days |
| **P2** | Deploy Falco runtime detection rules | SOC | 7 days |
| **P3** | Verify patch status via audit script | Agency IT | 7 days |

---

## 📎 Attachment 2: Remediation Checklist (IT Admin)

### DirtyDecrypt — IT Administrator Quick Reference

**Classification:** TLP:GREEN

#### Step 1: Verify Exposure

```bash
# Check kernel config
zcat /proc/config.gz | grep RXGK

# Expected output (NOT AFFECTED):
# # CONFIG_RXGK is not set

# If you see:
# CONFIG_RXGK=y  OR  CONFIG_RXGK=m
# → YOU ARE AFFECTED
```

#### Step 2: Check Current Kernel Version

```bash
uname -r
# Document current version before upgrade
```

#### Step 3: Apply Patch

**Fedora:**
```bash
sudo dnf upgrade --refresh kernel kernel-core kernel-modules
sudo systemctl reboot
```

**Arch Linux:**
```bash
sudo pacman -Syu linux linux-headers
sudo systemctl reboot
```

**openSUSE Tumbleweed:**
```bash
sudo zypper dup
sudo systemctl reboot
```

**RHEL/CentOS Stream (kernel-ml):**
```bash
sudo dnf upgrade --refresh kernel-ml kernel-ml-core kernel-ml-modules
sudo systemctl reboot
```

#### Step 4: Verify Patch Applied

```bash
# After reboot, verify new kernel version
uname -r

# Compare with patched versions:
# Fedora: ≥ 6.8.9-300.fc40 (or later)
# Arch: ≥ 6.8.9-arch1-1 (or later)
# openSUSE: ≥ 6.8.9-1-default (or later)
```

#### Step 5: Document Compliance

```markdown
## Patch Compliance Record

**System:** [hostname]
**Pre-Patch Kernel:** [version]
**Post-Patch Kernel:** [version]
**Patch Date:** [ISO8601]
**Verified By:** [admin name]
**Status:** ✅ COMPLIANT
```

#### Workaround (Last Resort Only)

```bash
# Only if patching is impossible within 24 hours
# WARNING: Breaks IPsec VPN and AFS mounts

echo "blacklist rxrpc" >> /etc/modprobe.d/blacklist.conf
echo "blacklist esp4" >> /etc/modprobe.d/blacklist.conf
echo "blacklist esp6" >> /etc/modprobe.d/blacklist.conf

# Reboot required
sudo systemctl reboot
```

---

## 📎 Attachment 3: Kubernetes Hardening Guide

### DirtyDecrypt — Kubernetes-Specific Guidance

**Classification:** TLP:GREEN

#### Threat Model

**Attack Chain:**
1. Attacker gains unprivileged access to K8s worker node (e.g., compromised pod)
2. Exploits DirtyDecrypt on host kernel
3. Gains root on worker node
4. Accesses all pods, container runtime sockets, Kubernetes secrets on that node

#### Immediate Actions

**1. Inventory Worker Nodes:**
```bash
kubectl get nodes -o wide

# For each node, SSH and run:
zcat /proc/config.gz | grep RXGK
```

**2. Patch Worker Nodes:**
```bash
# Drain node first
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data

# Patch kernel (see remediation checklist above)
sudo dnf upgrade --refresh kernel && sudo systemctl reboot

# Uncordon after reboot
kubectl uncordon <node-name>
```

**3. Enforce Pod Security Admission:**
```yaml
# Apply to all namespaces
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
```

**4. Set Default Security Context:**
```yaml
# In all pod specs
securityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
  runAsNonRoot: true
```

**5. Deploy Falco Runtime Detection:**
```yaml
# Detect privilege escalation attempts
- rule: Container Escaped to Host
  desc: Detect process escaping container to host
  condition: (proc.name in (known_exploits)) and (container.id != host)
  output: "Privilege escalation detected (user=%user.name container=%container.id)"
  priority: CRITICAL
```

#### Post-Incident Verification

```bash
# Verify all nodes patched
kubectl get nodes -o json | jq '.items[].status.nodeInfo.kernelVersion'

# Check for unpatched nodes
for node in $(kubectl get nodes -o jsonpath='{.items[*].metadata.name}'); do
  echo "Checking $node..."
  # SSH and verify kernel version
done
```

---

**End of Distribution Package**

**Classification:** TLP:GREEN  
**Prepared By:** HOI Intelligence Cell, CyberSecurity Malaysia  
**Date:** 2026-05-21 16:55 UTC
