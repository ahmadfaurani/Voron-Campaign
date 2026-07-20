#!/usr/bin/env python3
"""
VoronDRQ Daily Enrichment - DNS Assessment Fallback
====================================================
Runs ONLY the DMARC/SPF/DKIM DNS assessment (public DNS records) for the
8 Tier-1 Malaysian bank domains, using dig directly. This is the
self-contained, legitimate portion of voron-daily-enrichment.sh that does
NOT depend on the OpenOSINT activation shim (currently missing) or the
masked API keys in openosint-config.env.

The stakeholder email-verification portion of the run is NOT executed here
because it requires the OpenOSINT environment, whose activation wrapper
(openosint-activate.sh) is absent from disk. Email-verification fields are
emitted as null / "not_run" so downstream parsers do not miscount them.

Output schema matches voron-daily-enrichment.sh (one JSON object per line).
TLP:AMBER - Commercial Intelligence
"""
import json
import subprocess
import sys
from datetime import datetime

DOMAINS = [
    ("maybank.com.my", "Maybank Berhad"),
    ("cimb.com", "CIMB Bank Berhad"),
    ("hlbb.com.my", "Hong Leong Bank Berhad"),
    ("rhbbank.com", "RHB Bank Berhad"),
    ("ambankgroup.com", "AmBank (M) Berhad"),
    ("bankislam.com.my", "Bank Islam Malaysia Berhad"),
    ("ocbc.com.my", "OCBC Bank (Malaysia) Berhad"),
    ("uob.com.my", "UOB Malaysia Berhad"),
]

ROLES = ["ciso", "grc", "cfo", "risk", "compliance", "cio", "internal.audit"]

# Common DKIM selectors to probe (DKIM selectors are org-specific; these are
# the most common defaults). A hit proves DKIM signing is configured; a miss
# does NOT prove absence (the real selector may differ).
DKIM_SELECTORS = [
    "default", "google", "selector1", "selector2",
    "s1", "s2", "mail", "selector", "smtp", "mandrill",
]

RESOLVER = "8.8.8.8"


def dig_txt(name):
    """Return list of TXT record strings for `name`."""
    try:
        out = subprocess.run(
            ["dig", "+short", "+time=5", "+tries=2", "TXT", name, f"@{RESOLVER}"],
            capture_output=True, text=True, timeout=20,
        ).stdout
    except Exception:
        return []
    recs = []
    for line in out.splitlines():
        line = line.strip()
        if line:
            # dig prints each TXT as: "v=DMARC1;" "p=reject;" ... joined.
            # Rejoin quoted fragments into one logical record.
            recs.append(line)
    # dig may emit a multi-fragment record across one line already; join all
    # fragments for the record into a single string by stripping quotes/spaces.
    joined = " ".join(recs).replace('"', "")
    return [r.strip() for r in joined.split("  ") if r.strip()] if joined else []


def get_one_record(name):
    """Return TXT records for `name`, joined; retries to absorb transient
    resolver timeouts/rate-limiting when many queries fire in sequence.
    Filters out CNAME-target lines (which contain no '='), so _dmarc names
    that are CNAME-chained (e.g. to a hosted DMARC provider) return only the
    actual TXT record content."""
    last = ""
    for _attempt in range(3):
        try:
            out = subprocess.run(
                ["dig", "+short", "+time=4", "+tries=2", "TXT", name, f"@{RESOLVER}"],
                capture_output=True, text=True, timeout=25,
            ).stdout.strip()
        except Exception:
            out = ""
        if out:
            lines = [ln.strip() for ln in out.splitlines() if "=" in ln and ln.strip()]
            joined = "".join(lines).replace('"', "").replace(" ", "")
            if joined:
                return joined
        last = out
    return ""


def assess_dmarc(domain):
    raw = get_one_record(f"_dmarc.{domain}")
    low = raw.lower()
    if "v=dmarc1" not in low:
        return {"status": "non-compliant", "record": "(none)", "policy": None}
    # extract p=...
    policy = None
    for tok in raw.split(";"):
        tok = tok.strip()
        if tok.lower().startswith("p="):
            policy = tok[2:].strip().lower()
            break
    if policy == "reject":
        status = "compliant"
    elif policy == "quarantine":
        status = "partial"
    elif policy == "none":
        status = "monitoring"
    else:
        status = "non-compliant"
    return {"status": status, "record": raw, "policy": policy}


def assess_spf(domain):
    raw = get_one_record(domain)
    if "v=spf1" in raw.lower():
        # classify mechanism strength
        if "~all" in raw or "-all" in raw:
            strength = "enforced"
        elif "?all" in raw:
            strength = "neutral"
        else:
            strength = "soft"
        return {"status": "present", "record": raw, "strength": strength}
    return {"status": "absent", "record": "(none)", "strength": None}


def assess_dkim(domain):
    found = []
    for sel in DKIM_SELECTORS:
        raw = get_one_record(f"{sel}._domainkey.{domain}")
        if "v=dkim1" in raw.lower() or "p=" in raw.lower():
            # crude: dkim records contain a public key p=... not p=reject/quarantine
            if "v=dkim1" in raw.lower() or ("p=" in raw and "v=dmarc1" not in raw.lower()):
                found.append({"selector": sel, "record": raw[:120]})
        if found:
            break  # one selector hit is enough to prove DKIM configured
    if found:
        return {"status": "present", "selectors_found": found}
    return {"status": "no_default_selector", "selectors_found": [],
             "note": "DKIM selectors are org-specific; absence of common "
                     "defaults does not prove DKIM is unconfigured."}


def main():
    out_dir = "/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospects/daily-enrichment"
    import os
    os.makedirs(out_dir, exist_ok=True)
    date_str = datetime.now().strftime("%Y%m%d")
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    jsonl_path = f"{out_dir}/enrichment-{date_str}.jsonl"
    summary_path = f"{out_dir}/summary-{date_str}.md"

    today = datetime.now().strftime("%Y-%m-%d")
    jsonl = open(jsonl_path, "w")
    results = []

    print("=== VoronDRQ Daily Enrichment - DNS Assessment (fallback run) ===")
    print(f"Date: {ts}")
    print(f"Output: {jsonl_path}")
    print(f"NOTE: Email verification SKIPPED - openosint-activate.sh missing.\n")

    for domain, institution in DOMAINS:
        print(f"-> {institution} ({domain})")
        dmarc = assess_dmarc(domain)
        spf = assess_spf(domain)
        dkim = assess_dkim(domain)
        print(f"     DMARC: {dmarc['status']} (p={dmarc['policy']})")
        print(f"     SPF:   {spf['status']} ({spf['strength']})")
        print(f"     DKIM:  {dkim['status']}")

        email_verif = {}
        for role in ROLES:
            email_verif[role] = {
                "email": f"{role}@{domain}",
                "verified": None,
                "verification_status": "not_run",
                "reason": "openosint-activate.sh missing; OpenOSINT env unavailable",
            }

        obj = {
            "institution": institution,
            "domain": domain,
            "date": today,
            "email_verifications": email_verif,
            "dns_assessment": {
                "dmarc": dmarc["status"],
                "dmarc_policy": dmarc["policy"],
                "dmarc_record": dmarc["record"],
                "spf": spf["status"],
                "spf_strength": spf["strength"],
                "dkim": dkim["status"],
            },
            "run_mode": "dns_only_fallback",
            "confidence": "MEDIUM",
            "notes": "Email verification not executed (OpenOSINT env unavailable). "
                     "DNS assessment via dig (public records).",
        }
        jsonl.write(json.dumps(obj) + "\n")
        results.append((institution, domain, dmarc, spf, dkim))
        print()

    jsonl.close()

    compliant = sum(1 for _, _, d, _, _ in results if d["status"] == "compliant")
    partial = sum(1 for _, _, d, _, _ in results if d["status"] == "partial")
    monitoring = sum(1 for _, _, d, _, _ in results if d["status"] == "monitoring")
    noncomp = sum(1 for _, _, d, _, _ in results if d["status"] == "non-compliant")
    spf_present = sum(1 for _, _, _, s, _ in results if s["status"] == "present")
    dkim_present = sum(1 for _, _, _, _, k in results if k["status"] == "present")

    with open(summary_path, "w") as f:
        f.write(f"# VoronDRQ Daily Enrichment Summary (DNS-Only Fallback)\n")
        f.write(f"## Date: {ts}\n\n")
        f.write(f"**TLP:AMBER** - Commercial Intelligence\n\n")
        f.write(f"---\n\n")
        f.write(f"## Run Mode\n\n")
        f.write(f"This run executed **only the DNS assessment** (DMARC/SPF/DKIM) "
                f"via `dig` against public resolvers. The stakeholder "
                f"**email-verification** step was **NOT executed** because the "
                f"OpenOSINT activation shim (`openosint-activate.sh`) is missing "
                f"from disk and the OpenOSINT environment could not be activated. "
                f"See the failure section below for remediation.\n\n")
        f.write(f"---\n\n## Execution Summary\n\n")
        f.write(f"| Metric | Value |\n|--------|-------|\n")
        f.write(f"| **Institutions Scanned** | {len(DOMAINS)} |\n")
        f.write(f"| **Email Patterns Tested** | 0 (skipped) |\n")
        f.write(f"| **Emails Verified** | 0 (skipped) |\n")
        f.write(f"| **Verification Rate** | N/A |\n")
        f.write(f"| **DMARC Compliant (p=reject)** | {compliant} / {len(DOMAINS)} |\n")
        f.write(f"| **DMARC Partial (p=quarantine)** | {partial} / {len(DOMAINS)} |\n")
        f.write(f"| **DMARC Monitoring (p=none)** | {monitoring} / {len(DOMAINS)} |\n")
        f.write(f"| **DMARC Non-compliant (none)** | {noncomp} / {len(DOMAINS)} |\n")
        f.write(f"| **SPF Present** | {spf_present} / {len(DOMAINS)} |\n")
        f.write(f"| **DKIM (common selector found)** | {dkim_present} / {len(DOMAINS)} |\n\n")
        f.write(f"---\n\n## Domain Compliance Status\n\n")
        f.write(f"| Institution | Domain | DMARC | Policy | SPF | DKIM |\n")
        f.write(f"|-------------|--------|-------|--------|-----|------|\n")
        for inst, dom, dmarc, spf, dkim in results:
            f.write(f"| {inst} | {dom} | {dmarc['status']} | {dmarc['policy'] or '-'} | "
                    f"{spf['status']} | {dkim['status']} |\n")
        f.write(f"\n---\n\n## Failure: Email Verification Not Run\n\n")
        f.write(f"**Root cause:** `openosint-activate.sh` is missing from disk.\n\n")
        f.write(f"- `voron-daily-enrichment.sh` line 62 does "
                f"`source \"$WORKSPACE/openosint-activate.sh\"` "
                f"(WORKSPACE=/home/p62operator/.openclaw/workspace-hoi).\n")
        f.write(f"- That file does **not** exist. A prior diagnostic "
                f"(`operations/competitive-intel/servicenow-watch/DIAGNOSTIC-20260713.md`) "
                f"noted the correct path should be "
                f"`$WORKSPACE/openosint/openosint-activate.sh`, but that path **also** "
                f"does not exist on disk now.\n")
        f.write(f"- The OpenOSINT **venv itself still exists** at "
                f"`$WORKSPACE/openosint-env/` (binary: `openosint-env/bin/openosint`, "
                f"package openosint-2.23.0), and config at `$WORKSPACE/openosint-config.env`. "
                f"Only the activation **shim** is gone.\n\n")
        f.write(f"**Remediation:**\n\n")
        f.write(f"1. Recreate `$WORKSPACE/openosint-activate.sh` with:\n")
        f.write(f"   ```bash\n")
        f.write(f"   #!/bin/bash\n")
        f.write(f"   source /home/p62operator/.openclaw/workspace-hoi/openosint-env/bin/activate\n")
        f.write(f"   set -a; source /home/p62operator/.openclaw/workspace-hoi/openosint-config.env; set +a\n")
        f.write(f"   export OPENOSINT_ACTIVATED=1\n")
        f.write(f"   ```\n")
        f.write(f"   then `chmod +x` it. Update line 62 of the script if you prefer the "
                f"`openosint/` subdirectory layout.\n")
        f.write(f"2. Verify the API keys in `openosint-config.env` are **real values**, not "
                f"the `***` placeholders currently shown (e.g. `OPENAI_API_KEY`, "
                f"`HAVEIBEENPWNED_API_KEY`). Masked keys will cause `openosint --provider openai` "
                f"to fail auth or return unreliable AI-mediated output.\n")
        f.write(f"3. Re-run: `bash operations/scripts/voron-daily-enrichment.sh`.\n\n")
        f.write(f"---\n\n## Output Files\n\n")
        f.write(f"- **Detailed Results:** `{jsonl_path}`\n")
        f.write(f"- **Summary Report:** `{summary_path}`\n\n")
        f.write(f"---\n\n**Generated:** {ts}  \n")
        f.write(f"**Cronjob ID:** voron-stakeholder-enrichment  \n")
        f.write(f"**Classification:** TLP:AMBER  \n")
        f.write(f"**Run Mode:** dns_only_fallback (email verification skipped)\n")

    print("=== DNS Assessment Complete ===")
    print(f"Institutions: {len(DOMAINS)}")
    print(f"DMARC compliant (p=reject): {compliant}/{len(DOMAINS)}")
    print(f"SPF present: {spf_present}/{len(DOMAINS)}")
    print(f"DKIM (common selector): {dkim_present}/{len(DOMAINS)}")
    print(f"Email verification: SKIPPED (openosint-activate.sh missing)")
    print(f"\nJSONL: {jsonl_path}")
    print(f"Summary: {summary_path}")


if __name__ == "__main__":
    main()
