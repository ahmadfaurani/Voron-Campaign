# OpenOSINT Integration Guide
## PRN Johor 2026 Political Intelligence Operations
**TLP:AMBER** | Part of Approved Tech Stack

---

## Installation Summary

**Location:** `/home/p62operator/.openclaw/workspace-hoi/openosint-env`  
**Version:** OpenOSINT v2.23.0  
**Python:** 3.11.15 (uv-managed venv)

### Quick Start

```bash
# Activate environment
cd /home/p62operator/.openclaw/workspace-hoi
source openosint-env/bin/activate

# Interactive AI REPL (default)
openosint

# Direct tool scan (no AI)
openosint email target@example.com
openosint username johndoe99
openosint github username

# Web UI
openosint web
```

---

## Configuration

### 1. Edit Configuration File
```bash
nano /home/p62operator/.openclaw/workspace-hoi/openosint-config.env
```

### 2. Active Configuration (Aras Integrasi)

**Already Configured:**
```bash
OPENAI_BASE_URL=https://model.arasintegrasi.ai/v1
OPENAI_MODEL=Qwen/Qwen3.5-397B-A17B
OPENAI_API_KEY=sk-***
```

**Usage:**
```bash
# All tools work with Aras Integrasi endpoint
openosint --provider openai github username
openosint --provider openai email target@example.com
openosint --provider openai username johndoe99
```

### 3. Optional OSINT Tool API Keys

| Tool | API Key | Purpose | Get Key |
|------|---------|---------|---------|
| **HaveIBeenPwned** | `HAVEIBEENPWNED_API_KEY` | Breach data verification | https://haveibeenpwned.com/API/v3 |

| Tool | Key | Use Case |
|------|-----|----------|
| `SHODAN_API_KEY` | Infrastructure reconnaissance | Cyber threat intel on targets |
| `IP2LOCATION_API_KEY` | VPN/Proxy/Tor detection | Verify contact authenticity |
| `BRIGHTDATA_API_KEY` | Live Google dorks + scraping | Advanced OSINT collection |
| `VIRUSTOTAL_API_KEY` | Malware/URL reputation | Link safety verification |
| `CENSYS_API_ID` + `CENSYS_SECRET` | Certificate search | Infrastructure mapping |

---

## Available Tools (18 Total)

### Core Investigation Tools

| Command | Description | Powered By |
|---------|-------------|------------|
| `openosint email <email>` | Social accounts linked to email | holehe |
| `openosint username <handle>` | Username across 300+ platforms | sherlock |
| `openosint github <username>` | GitHub profile + commit emails | GitHub API |
| `openosint dns <domain>` | DNS records + email security | dnspython |

### Breach & Reputation

| Command | Description | API Required |
|---------|-------------|--------------|
| `openosint --parallel email <email>` | Email + breach scan (parallel) | HaveIBeenPwned |
| `openosint abuseipdb <ip>` | IP abuse reputation | AbuseIPDB |
| `openosint virustotal <target>` | AV verdict (70+ engines) | VirusTotal |

### Infrastructure Intelligence

| Command | Description | API Required |
|---------|-------------|--------------|
| `openosint shodan <ip>` | Open ports, banners, CVEs | Shodan |
| `openosint censys <ip\|domain>` | Certificates, infrastructure | Censys |
| `openosint ip2location <ip>` | Geolocation + VPN/Proxy flags | IP2Location |

### Advanced Collection

| Command | Description | API Required |
|---------|-------------|--------------|
| `openosint search-dorks-live <query>` | Live Google dork results | Bright Data |
| `openosint scrape <url>` | Fetch URL (bypass Cloudflare) | Bright Data |
| `openosint footprint <entity>` | Entity-aware SERP footprint | Bright Data |

---

## Integration with Existing Workstream

### Journalist Registry Verification

Use OpenOSINT to verify journalist contacts before activation:

```bash
# Verify email authenticity (breach history, social accounts)
openosint --parallel email journalist@outlet.com.my

# Check username consistency across platforms
openosint username journalist_byline

# GitHub verification for tech journalists
openosint github journalist_handle
```

### Political Figure Monitoring

```bash
# Multi-target investigation (create targets.txt)
openosint multi targets.txt

# Example targets.txt:
candidate@example.com
@political_handle
political-figure.github.io
```

### Infrastructure Reconnaissance

For cyber threat assessment on campaign infrastructure:

```bash
# Check if campaign sites use VPN/Proxy hosting
openosint ip2location <campaign-site-ip>

# Scan for exposed services
openosint shodan <campaign-domain>

# DNS security analysis
openosint dns <campaign-domain>
```

---

## Output & Reporting

### Report Location
```
/home/p62operator/.openclaw/workspace-hoi/openosint-reports/
```

### Report Format
- **Markdown:** `YYYY-MM-DD_HH-MM-SS_report.md`
- **PDF:** `YYYY-MM-DD_HH-MM-SS_report.pdf` (auto-generated)

### Session History
```
/home/p62operator/.openclaw/workspace-hoi/openosint-history/
```

All REPL sessions are automatically saved for audit trail.

---

## MCP Server Integration

OpenOSINT exposes all 18 tools via MCP (Model Context Protocol):

### For Claude Code
```bash
claude mcp add openosint python \
  /home/p62operator/.openclaw/workspace-hoi/openosint-env/bin/openosint-mcp
```

### For Claude Desktop
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "openosint": {
      "command": "/home/p62operator/.openclaw/workspace-hoi/openosint-env/bin/openosint-mcp"
    }
  }
}
```

---

## Automation Patterns

### Daily Journalist Verification Sprint
```bash
#!/bin/bash
# Save as: ~/.hermes/scripts/openosint-verify-journalists.sh
cd /home/p62operator/.openclaw/workspace-hoi
source openosint-env/bin/activate

# Process pending verifications
while IFS=, read -r email outlet; do
  openosint --parallel email "$email" --json \
    >> openosint-reports/journalist-verification-$(date +%Y%m%d).jsonl
done < journalist-registry-pending.csv
```

### Campaign Infrastructure Monitor
```bash
#!/bin/bash
# Save as: ~/.hermes/scripts/openosint-monitor-infra.sh
cd /home/p62operator/.openclaw/workspace-hoi
source openosint-env/bin/activate

# Monitor known campaign domains
for domain in $(cat campaign-domains.txt); do
  openosint dns "$domain" --json
  openosint ip2location $(dig +short "$domain" | head -1) --json
done >> openosint-reports/infra-monitor-$(date +%Y%m%d).jsonl
```

---

## Security Notes

**TLP:AMBER Classification:**
- All OpenOSINT outputs inherit TLP:AMBER classification
- Reports stored in workspace are subject to same handling rules as other intel
- API keys in `.env` file should be chmod 600

**Token Security:**
- API keys stored in `openosint-config.env`
- Recommended: `chmod 600 openosint-config.env`
- Rotate tokens if exposed in conversation history

**Data Retention:**
- Session history: Automatic (indefinite, per user preference)
- Reports: Manual review and archival recommended quarterly

---

## Troubleshooting

### "No API key configured"
```bash
# Source the config before running
export $(cat openosint-config.env | grep -v '^#' | xargs)
```

### "Provider not responding"
```bash
# Check Anthropic status
curl -I https://api.anthropic.com

# Switch to local Ollama (no API key needed)
openosint --provider ollama --ollama-model llama3.2
```

### Tool-specific errors
```bash
# Enable verbose logging
openosint -v email target@example.com
```

---

## Next Steps

1. **Configure API Keys:** Edit `openosint-config.env` with your keys
2. **Test Installation:** Run `openosint email test@example.com`
3. **Integrate with Workflow:** Add to journalist verification sprint
4. **Set Up Automation:** Create cron jobs for routine scans

---

**Document Version:** 1.0  
**Last Updated:** 2026-07-08  
**Maintainer:** PRN Johor 2026 Operations Team
