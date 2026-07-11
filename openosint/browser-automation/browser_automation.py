#!/usr/bin/env python3
"""
Browser Automation Module for HOI Workspace
============================================
Playwright-based browser automation for JavaScript-rendered Malaysian news outlets.

Use cases:
- Berita Harian (requires JS rendering)
- The Edge (protected content)
- MalaysiaNow (dynamic homepage)
- Any outlet requiring stealth browser

Usage:
    from browser_automation import BrowserSession
    
    with BrowserSession() as browser:
        articles = browser.extract_articles('https://www.freemalaysiatoday.com/')
        print(f"Found {len(articles)} articles")
"""

import os
import sys
import time
import logging
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime

try:
    from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext, ViewportSize
    from playwright._impl._errors import TimeoutError as PlaywrightTimeout
except ImportError:
    print("ERROR: Playwright not installed. Run: pip install playwright && playwright install")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BrowserSession:
    """
    Managed browser session with stealth features for Malaysian news extraction.
    
    Features:
    - Headless Chromium with realistic viewport
    - User-Agent rotation
    - JavaScript rendering
    - Screenshot capability for debugging
    - Timeout handling
    - Proxy support (optional)
    """
    
    # Realistic User-Agents for Malaysian context
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    ]
    
    # Default viewport for Malaysian news sites
    DEFAULT_VIEWPORT = ViewportSize(width=1920, height=1080)
    
    # Timeout settings (ms)
    NAVIGATION_TIMEOUT = 60000  # 60 seconds
    WAIT_FOR_SELECTOR_TIMEOUT = 10000  # 10 seconds
    
    def __init__(
        self,
        headless: bool = True,
        user_agent: Optional[str] = None,
        viewport: Optional[ViewportSize] = None,
        proxy: Optional[str] = None,
        slow_mo: int = 0,
        screenshot_dir: Optional[str] = None
    ):
        """
        Initialize browser session.
        
        Args:
            headless: Run browser in headless mode (default: True)
            user_agent: Custom User-Agent string (default: random from list)
            viewport: Viewport dimensions (default: 1920x1080)
            proxy: Proxy server URL (e.g., "http://proxy:8080")
            slow_mo: Slow down operations by X ms (useful for debugging)
            screenshot_dir: Directory to save debug screenshots
        """
        self.headless = headless
        self.user_agent = user_agent or self.USER_AGENTS[0]
        self.viewport = viewport or self.DEFAULT_VIEWPORT
        self.proxy = proxy
        self.slow_mo = slow_mo
        self.screenshot_dir = screenshot_dir
        self.playwright = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        
        if self.screenshot_dir:
            Path(self.screenshot_dir).mkdir(parents=True, exist_ok=True)
    
    def __enter__(self):
        """Context manager entry."""
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
    
    def start(self):
        """Launch browser and create page."""
        logger.info("Starting browser session...")
        
        self.playwright = sync_playwright().start()
        
        # Launch browser with stealth settings
        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-gpu',
            ]
        )
        
        # Create context with realistic settings
        self.context = self.browser.new_context(
            user_agent=self.user_agent,
            viewport=self.viewport,
            proxy={'server': self.proxy} if self.proxy else None,
            locale='en-MY',
            timezone_id='Asia/Kuala_Lumpur',
            offline=False,
        )
        
        # Inject stealth scripts
        self.context.add_init_script("""
            // Override navigator.webdriver
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            
            // Override navigator.plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
            
            // Override navigator.languages
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en', 'ms-MY', 'ms']
            });
        """)
        
        self.page = self.context.new_page()
        assert self.page is not None
        self.page.set_default_navigation_timeout(self.NAVIGATION_TIMEOUT)
        self.page.set_default_timeout(self.WAIT_FOR_SELECTOR_TIMEOUT)
        
        logger.info(f"Browser launched: {self.user_agent[:50]}...")
        return self
    
    def close(self):
        """Close browser and cleanup."""
        logger.info("Closing browser session...")
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        logger.info("Browser session closed")
    
    def navigate(self, url: str, wait_for: Optional[str] = None) -> Page:
        """
        Navigate to URL with optional wait condition.
        
        Args:
            url: Target URL
            wait_for: CSS selector to wait for (e.g., '.article-list')
        
        Returns:
            Page object
        """
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        
        logger.info(f"Navigating to: {url}")
        
        try:
            self.page.goto(url, wait_until='networkidle')
            
            if wait_for:
                logger.info(f"Waiting for selector: {wait_for}")
                self.page.wait_for_selector(wait_for, state='visible')
            
            # Take screenshot if debug mode enabled
            if self.screenshot_dir:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                screenshot_path = Path(self.screenshot_dir) / f"{timestamp}_navigate.png"
                self.page.screenshot(path=str(screenshot_path), full_page=True)
                logger.info(f"Screenshot saved: {screenshot_path}")
            
            return self.page
            
        except PlaywrightTimeout:
            logger.error(f"Navigation timeout for {url}")
            if self.screenshot_dir and self.page:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                screenshot_path = Path(self.screenshot_dir) / f"{timestamp}_timeout.png"
                self.page.screenshot(path=str(screenshot_path), full_page=True)
            raise
    
    def extract_articles(
        self,
        url: str,
        selectors: Dict[str, str],
        wait_for: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Extract article metadata from a news page.
        
        Args:
            url: Page URL
            selectors: Dict with CSS selectors:
                - 'container': Article list container
                - 'article': Individual article element
                - 'title': Headline selector
                - 'link': Article link selector
                - 'byline': Author/byline selector (optional)
                - 'timestamp': Date/time selector (optional)
            wait_for: Selector to wait for before extraction
        
        Returns:
            List of article dicts with title, url, byline, timestamp
        """
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        
        logger.info(f"Extracting articles from: {url}")
        
        self.navigate(url, wait_for=wait_for)
        
        articles = []
        
        # Find article container
        container = self.page.query_selector(selectors['container'])
        if not container:
            logger.warning(f"Container not found: {selectors['container']}")
            return articles
        
        # Find individual articles
        article_elements = container.query_selector_all(selectors['article'])
        logger.info(f"Found {len(article_elements)} article elements")
        
        for i, article_el in enumerate(article_elements):
            try:
                article_data: Dict[str, Any] = {
                    'index': i,
                    'extracted_at': datetime.now().isoformat()
                }
                
                # Extract title
                if 'title' in selectors:
                    title_el = article_el.query_selector(selectors['title'])
                    article_data['title'] = title_el.inner_text().strip() if title_el else None
                
                # Extract link
                if 'link' in selectors:
                    link_el = article_el.query_selector(selectors['link'])
                    if link_el:
                        href = link_el.get_attribute('href')
                        if href:
                            article_data['url'] = href if href.startswith('http') else f"https://{url.split('/')[2]}{href}"
                
                # Extract byline
                if 'byline' in selectors:
                    byline_el = article_el.query_selector(selectors['byline'])
                    article_data['byline'] = byline_el.inner_text().strip() if byline_el else None
                
                # Extract timestamp
                if 'timestamp' in selectors:
                    timestamp_el = article_el.query_selector(selectors['timestamp'])
                    article_data['timestamp'] = timestamp_el.inner_text().strip() if timestamp_el else None
                
                articles.append(article_data)
                
            except Exception as e:
                logger.warning(f"Error extracting article {i}: {e}")
                continue
        
        logger.info(f"Successfully extracted {len(articles)} articles")
        return articles
    
    def scroll_page(self, times: int = 3, delay: float = 0.5):
        """
        Scroll page to trigger lazy loading.
        
        Args:
            times: Number of scroll iterations
            delay: Delay between scrolls (seconds)
        """
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        
        logger.info(f"Scrolling page {times} times...")
        
        for i in range(times):
            self.page.evaluate("window.scrollBy(0, window.innerHeight)")
            time.sleep(delay)
            logger.info(f"Scroll {i+1}/{times} complete")
    
    def get_page_content(self) -> str:
        """Get full page HTML content."""
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        return self.page.content()
    
    def get_page_text(self) -> str:
        """Get visible text content."""
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        return self.page.inner_text('body')
    
    def take_screenshot(self, filename: str, full_page: bool = True):
        """
        Take screenshot of current page.
        
        Args:
            filename: Output filename (without path)
            full_page: Capture full page or viewport only
        """
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        
        if not self.screenshot_dir:
            logger.warning("Screenshot directory not configured")
            return
        
        screenshot_path = Path(self.screenshot_dir) / filename
        self.page.screenshot(path=str(screenshot_path), full_page=full_page)
        logger.info(f"Screenshot saved: {screenshot_path}")


# Pre-configured selectors for Malaysian news outlets
OUTLET_SELECTORS = {
    'fmt': {
        'container': '.latest-news',
        'article': '.news-item',
        'title': 'h3 a',
        'link': 'h3 a',
        'byline': '.author',
        'timestamp': '.date',
        'wait_for': '.latest-news'
    },
    'berita_harian': {
        'container': '.article-list',
        'article': 'article',
        'title': 'h2 a',
        'link': 'h2 a',
        'byline': '.author-name',
        'timestamp': 'time',
        'wait_for': '.article-list'
    },
    'the_edge': {
        'container': '.article-grid',
        'article': '.article-card',
        'title': 'h3 a',
        'link': 'a.card-link',
        'byline': '.author',
        'timestamp': '.published-date',
        'wait_for': '.article-grid'
    },
    'malaysianow': {
        'container': '.news-list',
        'article': '.news-item',
        'title': 'h4 a',
        'link': 'a.read-more',
        'byline': '.byline',
        'timestamp': '.timestamp',
        'wait_for': '.news-list'
    }
}


def extract_from_outlet(outlet: str, base_url: str, debug: bool = False) -> List[Dict[str, Any]]:
    """
    Convenience function to extract articles from a known outlet.
    
    Args:
        outlet: Outlet key from OUTLET_SELECTORS (fmt, berita_harian, the_edge, malaysianow)
        base_url: Base URL of the outlet
        debug: Enable debug screenshots
    
    Returns:
        List of article dicts
    """
    if outlet not in OUTLET_SELECTORS:
        logger.error(f"Unknown outlet: {outlet}. Available: {list(OUTLET_SELECTORS.keys())}")
        return []
    
    selectors = OUTLET_SELECTORS[outlet]
    screenshot_dir = '/tmp/browser_debug' if debug else None
    
    with BrowserSession(screenshot_dir=screenshot_dir) as browser:
        articles = browser.extract_articles(
            url=base_url,
            selectors=selectors,
            wait_for=selectors.get('wait_for')
        )
    
    return articles


if __name__ == '__main__':
    # Test extraction from FMT
    print("=" * 60)
    print("Browser Automation Test - FMT")
    print("=" * 60)
    
    articles = extract_from_outlet('fmt', 'https://www.freemalaysiatoday.com/', debug=True)
    
    print(f"\nExtracted {len(articles)} articles:\n")
    for i, article in enumerate(articles[:5], 1):
        print(f"{i}. {article.get('title', 'N/A')}")
        print(f"   By: {article.get('byline', 'N/A')}")
        print(f"   URL: {article.get('url', 'N/A')}")
        print()
    
    print("=" * 60)
    print("Test complete!")
