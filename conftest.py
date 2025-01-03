import pytest
import os
from playwright.sync_api import Page, expect, Browser, BrowserContext
from dotenv import load_dotenv

from config import get_header

load_dotenv()

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "base_url": os.getenv("TEST_BASE_URL")
    }


@pytest.fixture(scope="module")
def auth_context(browser: Browser) -> BrowserContext:
    context = browser.new_context(
        base_url=os.getenv("TEST_BASE_URL")
    )
    page = context.new_page()
    
    page.goto(os.getenv("TEST_LOCALE")+"/sign-in")

    page.fill('input[name="username"]', os.getenv("TEST_USERNAME"))
    page.fill('input[name="password"]', os.getenv("TEST_PASSWORD"))
    page.click('button[type="submit"]')
    
    # Validate authenticated page
    expect(page.get_by_role("button", name=get_header("buy_crypto"))).to_be_visible()
    
    storage_state = context.storage_state()
    
    authenticated_context = browser.new_context(
        storage_state=storage_state,
        base_url=os.getenv("TEST_BASE_URL")
    )
    
    yield authenticated_context
    authenticated_context.close()

@pytest.fixture
def page(auth_context: BrowserContext) -> Page:
    page = auth_context.new_page()
    yield page
    page.close()