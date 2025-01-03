import pytest
import os
from playwright.sync_api import expect

from config import get_url

def test_user_can_view_portfolio(page: pytest.fixture):
    page.goto(get_url("portfolio"))
    
    expect(page.get_by_text("Portfolio value")).to_be_visible()
    expect(page.get_by_text(os.getenv("TEST_PORTFOLIO_VALUE"), exact=True)).to_be_visible()
