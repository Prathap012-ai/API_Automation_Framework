import pytest
from playwright.sync_api import expect


BASE_URL = "https://demowebshop.tricentis.com/"


@pytest.fixture
def cross_browser_page(browser_type):
    browser = browser_type.launch()
    page = browser.new_page()
    try:
        yield page
    finally:
        browser.close()


def test_homepage_title(cross_browser_page):
    cross_browser_page.goto(BASE_URL)
    expect(cross_browser_page).to_have_title("Demo Web Shop")


def test_welcome_heading_is_visible(cross_browser_page):
    cross_browser_page.goto(BASE_URL)
    expect(cross_browser_page.get_by_role("heading", name="Welcome to our store")).to_be_visible()


def test_homepage_displays_featured_products(cross_browser_page):
    cross_browser_page.goto(BASE_URL)
    products = cross_browser_page.locator(".product-item")
    expect(products).to_have_count(6)
    expect(products.nth(0).locator(".product-title a")).to_have_text("$25 Virtual Gift Card")


def test_search_returns_matching_products(cross_browser_page):
    cross_browser_page.goto(BASE_URL)
    cross_browser_page.locator("#small-searchterms").fill("laptop")
    cross_browser_page.locator(".search-box-button").click()

    expect(cross_browser_page).to_have_url("https://demowebshop.tricentis.com/search?q=laptop")
    expect(cross_browser_page.locator(".product-item")).to_have_count(1)
    expect(cross_browser_page.locator(".product-item .product-title a")).to_have_text("14.1-inch Laptop")