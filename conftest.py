import pytest
import os
from playwright.sync_api import Page, expect
from dotenv import load_dotenv

from config import get_header

load_dotenv()

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "base_url": os.getenv("TEST_BASE_URL")
    }


# Module scope to store login context for all tests at beginning of run
# Use function scope to login for each test
@pytest.fixture(scope="module", autouse=True)
def login_context(page: Page):
     page.goto(os.getenv("TEST_LOCALE")+"/sign-in")
    
     page.fill('input[name="username"]', os.getenv("TEST_USERNAME"))
     page.fill('input[name="password"]', os.getenv("TEST_PASSWORD"))
     page.click('button[type="submit"]')
    
     expect(page.get_by_role("button", name=get_header["buy_crypto"])).to_be_visible()