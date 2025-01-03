import pytest
import os
import logging
from playwright.sync_api import sync_playwright, Page, expect, BrowserContext
from dotenv import load_dotenv

from config import get_header, get_url

load_dotenv()

STORAGE_STATE_PATH = os.getenv("STORAGE_STATE_PATH")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def authenticated_context(browser_name) -> BrowserContext:
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=False)
        
        if os.path.exists(STORAGE_STATE_PATH):
            context = browser.new_context(
                base_url=os.getenv("TEST_BASE_URL"),
                storage_state=STORAGE_STATE_PATH,
            )
        else:
            context = browser.new_context(
                base_url=os.getenv("TEST_BASE_URL"),
            )
        
        page = context.new_page()
        
        page.goto(os.getenv("TEST_LOCALE") + "/sign-in")
        # Ensure the navigation bar is visible
        expect(page.get_by_role("navigation").get_by_role("link").first).to_be_visible()

        page.fill('input[name="username"]', os.getenv("TEST_USERNAME"))
        page.fill('input[name="password"]', os.getenv("TEST_PASSWORD"))
        page.click('button[type="submit"]')
        
        
       # Before the test has a stored storage state, we need device approval via email
        if not os.path.exists(STORAGE_STATE_PATH):
            approve_device_alert = page.locator('p[role="alert"]', has_text="Approve new device")
            expect(approve_device_alert).to_be_visible()
            logger.warning("Storage State needs to be saved. Waiting for you to check email.")

            # Wait for the "Approve new device" message to disappear
            while approve_device_alert.is_visible():
                page.wait_for_timeout(1000)

        expect(page.locator("button").filter(has_text=get_header("buy_crypto"))).to_be_visible()  
        
        # Save/update authentication state to JSON file
        context.storage_state(path=STORAGE_STATE_PATH)
        
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(authenticated_context: BrowserContext) -> Page:
    page = authenticated_context.new_page()
    yield page
    page.close()