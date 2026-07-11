# Browser Automation Stack - Setup Guide

**Status:** ⚠️ PARTIAL - Browsers downloaded, system dependencies pending  
**Last Updated:** 2026-06-27  
**Workspace:** `/home/p62operator/.openclaw/workspace-hoi`

---

## Current State

### ✅ What's Working

1. **Playwright Python package** - Installed (v1.59.0)
   - Location: `/home/p62operator/.local/lib/python3.12/site-packages/playwright`
   - Accessible via `/usr/bin/python3.12`

2. **Browser binaries downloaded** - All 3 browsers in cache
   ```
   ~/.cache/ms-playwright/
   ├── chromium-1217/              ✓
   ├── chromium_headless_shell-1217/ ✓
   ├── firefox-1511/               ✓
   └── webkit-2272/                ✓
   ```

3. **Basic navigation** - Works for simple sites (example.com tested successfully)

4. **Browser automation module** - Created at `/home/p62operator/.openclaw/workspace-hoi/browser_automation.py`
   - `BrowserSession` class with context manager
   - Stealth features (webdriver hiding, realistic UA)
   - Pre-configured selectors for 4 Malaysian outlets
   - Screenshot debugging support

### ❌ What's Blocking

**System dependencies missing for Chromium**

Error when launching browser for complex sites:
```
BrowserType.launch: Executable doesn't exist at 
/home/p62operator/.cache/ms-playwright/chromium_headless_shell-1223/...
```

The `playwright install-deps chromium` command requires sudo:
```bash
sudo apt-get install -y \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2
```

**Note:** WebKit also missing dependencies (libgtk-4, libsecret, libenchant, etc.) but Chromium is priority.

---

## Setup Instructions

### Option 1: Install System Dependencies (Recommended)

```bash
# Install Chromium dependencies only (smaller footprint)
playwright install-deps chromium

# Or install all browser dependencies
playwright install-deps
```

**Requires:** sudo access

### Option 2: Use Existing Chrome/Chromium Installation

If Chrome is already installed on the system:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Use system Chrome instead of Playwright's bundled version
    browser = p.chromium.launch(
        executable_path='/usr/bin/google-chrome',  # Adjust path
        headless=True
    )
```

### Option 3: Docker/Container Mode

Run browser automation in a container with pre-installed dependencies:

```bash
docker run --rm \
  -v $(pwd):/workspace \
  -w /workspace \
  mcr.microsoft.com/playwright/python:v1.59.0-jammy \
  python3 browser_automation.py
```

---

## Usage Examples

### Basic Usage

```python
from browser_automation import BrowserSession

with BrowserSession() as browser:
    browser.navigate('https://www.freemalaysiatoday.com/')
    content = browser.get_page_text()
    print(content[:500])
```

### Article Extraction

```python
from browser_automation import extract_from_outlet, OUTLET_SELECTORS

# Extract from FMT
articles = extract_from_outlet(
    outlet='fmt',
    base_url='https://www.freemalaysiatoday.com/',
    debug=True  # Saves screenshots to /tmp/browser_debug
)

for article in articles[:5]:
    print(f"{article['title']} by {article.get('byline', 'Unknown')}")
```

### Custom Selectors

```python
from browser_automation import BrowserSession

selectors = {
    'container': '.article-list',
    'article': 'article.post',
    'title': 'h2 a',
    'link': 'h2 a',
    'byline': '.author span',
    'timestamp': 'time'
}

with BrowserSession(screenshot_dir='/tmp/debug') as browser:
    articles = browser.extract_articles(
        url='https://example-news.com/',
        selectors=selectors,
        wait_for='.article-list'
    )
```

### Berita Harian (JavaScript-heavy)

```python
from browser_automation import BrowserSession

with BrowserSession() as browser:
    # Navigate and wait for content
    browser.navigate(
        'https://www.bharian.com.my/',
        wait_for='.article-list'
    )
    
    # Scroll to trigger lazy loading
    browser.scroll_page(times=3, delay=1.0)
    
    # Take screenshot for debugging
    browser.take_screenshot('bh_homepage.png', full_page=True)
    
    # Extract HTML for parsing
    html = browser.get_page_content()
    
    # Save to file for processing
    with open('/tmp/bh_source.html', 'w') as f:
        f.write(html)
```

---

## Pre-configured Outlets

| Outlet | Key | Status | Notes |
|--------|-----|--------|-------|
| Free Malaysia Today | `fmt` | ⚠️ Needs deps | CSS selectors configured |
| Berita Harian | `berita_harian` | ⚠️ Needs deps | JS rendering required |
| The Edge | `the_edge` | ⚠️ Needs deps | Protected content |
| MalaysiaNow | `malaysianow` | ⚠️ Needs deps | Dynamic homepage |

---

## Troubleshooting

### "Executable doesn't exist"

**Cause:** Playwright version mismatch or browsers not installed

**Fix:**
```bash
# Reinstall browsers for current Playwright version
playwright install chromium

# Verify installation
ls ~/.cache/ms-playwright/
```

### Navigation timeout

**Cause:** Site requires JavaScript, missing system dependencies

**Fix:**
1. Install system dependencies (see above)
2. Increase timeout: `browser.NAVIGATION_TIMEOUT = 120000`
3. Use `wait_until='domcontentloaded'` instead of `'networkidle'`

### Selector not found

**Cause:** Site structure changed, lazy loading not triggered

**Fix:**
```python
# Scroll page first
browser.scroll_page(times=3, delay=0.5)

# Take screenshot to verify
browser.take_screenshot('debug.png')

# Update selectors
selectors = {
    'container': '.new-container-class',  # Updated
    # ...
}
```

---

## Next Steps

1. **Install system dependencies** (requires sudo):
   ```bash
   playwright install-deps chromium
   ```

2. **Test with Berita Harian**:
   ```bash
   cd /home/p62operator/.openclaw/workspace-hoi
   /usr/bin/python3.12 browser_automation.py
   ```

3. **Integrate with existing collection pipeline**:
   - Replace Firecrawl calls for JS-heavy outlets
   - Add browser extraction to daily collection cron job
   - Configure screenshot debugging for failed extractions

4. **Expand outlet coverage**:
   - Add selectors for Sinar Harian, Utusan Malaysia, NST
   - Test with regional outlets (TVS, Sabah outlets)

---

## Files

- `/home/p62operator/.openclaw/workspace-hoi/browser_automation.py` - Main module
- `/home/p62operator/.openclaw/workspace-hoi/intelligence/media-registry/` - Journalist registry output
- `/tmp/browser_debug/` - Debug screenshots (when enabled)

---

## References

- [Playwright Python Docs](https://playwright.dev/python/)
- [Playwright Browser Installation](https://playwright.dev/python/docs/browsers)
- [Browser Automation Skill](../skills/browser-automation.md) - To be created
