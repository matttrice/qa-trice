import pytest
import os
from playwright.sync_api import Page, expect, Browser, BrowserContext
from dotenv import load_dotenv

from config import get_header, get_url

load_dotenv()

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "base_url": os.getenv("TEST_BASE_URL")
    }


@pytest.fixture(scope="module")
def auth_context(browser: Browser) -> BrowserContext:
    STORAGE_STATE_PATH = os.getenv("STORAGE_STATE_PATH") 
    
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
                
        # Save authentication state to JSON file
        context.storage_state(path=STORAGE_STATE_PATH)

    yield context
    context.close()

@pytest.fixture
def page(auth_context: BrowserContext) -> Page:
    page = auth_context.new_page()
    yield page
    page.close()