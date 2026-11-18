from playwright.sync_api import expect


def test_multiple_tabs(page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator('.top-menu a[href="/books"]').click()

    product_link = page.locator(".product-item .product-title a").first
    product_name = product_link.inner_text().strip()
    product_link.evaluate("(link) => link.target = '_blank'")

    with page.expect_popup() as popup_info:
        product_link.click()

    popup = popup_info.value
    try:
        popup.wait_for_load_state("domcontentloaded")
        print(f"New tab URL: {popup.url}")
        print(f"New tab title: {popup.title()}")
        expect(popup.locator("h1")).to_have_text(product_name)
        expect(popup.locator(".product-essential")).to_be_visible()
        print(popup.locator(".product-essential").count())
    finally:
        popup.close()
