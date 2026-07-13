import json, os
from datetime import datetime, timezone

MEM = "/home/p62operator/.hermes/memories/voron-prospect-monitor.json"
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

m = json.load(open(MEM))

# Preserve the previous "no-change" awareness if present, else init.
prev_no_change = m.get("no_change_since_last_check", False)
runs_no_change = m.get("runs_since_last_change", 0)

# Record this run's check time + operational flags. DO NOT touch comparison fields.
m["last_check"] = now
m["no_change_since_last_check"] = True
m["last_change_commit"] = "e0929b6"          # commit where data last actually moved
m["last_change_at"] = "2026-07-11T21:03:01Z" # commit timestamp of e0929b6
m["runs_since_last_change"] = runs_no_change + 1
m["csv_source_note"] = "GitHub raw URL 404 (repo private). Used local git clone at ~/.openclaw/workspace-hoi/Voron-Campaign, reset to origin/main (e0929b6). Metrics byte-identical to prior run -> no change."

# Sanity: keep the substantive comparison baseline + previous trend chain untouched.
# (total_prospects, tier/segment/stakeholder counts, enriched_institutions, previous) unchanged.

tmp = MEM + ".tmp"
with open(tmp, "w") as f:
    json.dump(m, f, indent=2, ensure_ascii=False)
os.replace(tmp, MEM)
os.chmod(MEM, 0o600)
print("Memory updated. last_check =", now, "| runs_since_last_change =", m["runs_since_last_change"])
print("Baseline preserved: total_prospects =", m["total_prospects"],
      "| git_commit =", m["git_commit"], "| previous chain intact:", "previous" in m)
