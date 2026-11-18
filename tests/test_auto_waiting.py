from playwright.sync_api import expect

def test_auto_waiting(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill("computer")
    page.locator("input.search-box-button").click()

    product_titles = page.locator("h2.product-title a")
    first_product = product_titles.first

    first_product.wait_for(state="visible", timeout=10000)
    expect(first_product).to_be_visible()
    assert product_titles.count() >= 1, "Expected at least one search result"
    