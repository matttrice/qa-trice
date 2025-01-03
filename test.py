from playwright.sync_api import Page, expect

from config import get_url


def test_user_can_view_portfolio(page: Page):
    page.goto(get_url("portfolio"))
    
    expect(page.get_by_text("Portfolio value")).to_be_visible()