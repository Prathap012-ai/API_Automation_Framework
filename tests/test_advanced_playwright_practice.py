from pathlib import Path
import re

from playwright.sync_api import expect


BASE_URL = "https://demowebshop.tricentis.com/"
ARTIFACTS_DIR = Path(__file__).resolve().parents[1] / "reports" / "advanced_playwright_practice"
SCREENSHOT_PATH = ARTIFACTS_DIR / "product_added_to_cart.png"
TRACE_PATH = ARTIFACTS_DIR / "playwright_trace.zip"


def test_advanced_playwright_practice(context, page):
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        expect(page).to_have_title("Demo Web Shop")

        page.locator('.top-menu a[href="/books"]').click()
        expect(page).to_have_url(f"{BASE_URL}books")
        expect(page).to_have_title("Demo Web Shop. Books")
        expect(page.locator(".product-grid .item-box")).to_have_count(6)

        page.locator("#small-searchterms").fill("computer")
        page.get_by_role("button", name="Search").click()
        expect(page).to_have_url(f"{BASE_URL}search?q=computer")

        search_results = page.locator(".product-grid .item-box h2 a")
        expect(search_results).to_have_count(4)
        product_names = [name.strip() for name in search_results.all_text_contents()]
        assert all(re.search(r"computer", name, re.IGNORECASE) for name in product_names), (
            f"Expected computer-related search results, received: {product_names}"
        )

        selected_product = product_names[0]
        search_results.first.click()
        expect(page.locator(".product-name")).to_have_text(selected_product)
        expect(page.locator(".product-essential")).to_be_visible()
        expect(page).to_have_title(f"Demo Web Shop. {selected_product}")

        page.get_by_label("Slow", exact=True).check()
        page.get_by_label("2 GB", exact=True).check()
        page.get_by_label("320 GB", exact=True).check()
        page.locator('input[id^="add-to-cart-button"]').click()

        page.locator('a[href="/cart"]').first.click(timeout=2000)
        expect(page).to_have_url(f"{BASE_URL}cart")
        cart_products = page.locator(".cart-item-row .product-name")
        expect(cart_products).to_have_count(1)
        expect(cart_products.first).to_have_text(selected_product)
        expect(page.locator(".cart-item-row")).to_contain_text(
            "Processor: Slow"
        )
        expect(page.locator(".cart-item-row")).to_contain_text("RAM: 2 GB")
        expect(page.locator(".cart-item-row")).to_contain_text("HDD: 320 GB")

        page.screenshot(path=str(SCREENSHOT_PATH), full_page=True)
    finally:
        context.tracing.stop(path=str(TRACE_PATH))

    assert SCREENSHOT_PATH.is_file() and SCREENSHOT_PATH.stat().st_size > 0, (
        f"Expected a non-empty screenshot at {SCREENSHOT_PATH}"
    )
    assert TRACE_PATH.is_file() and TRACE_PATH.stat().st_size > 0, (
        f"Expected a non-empty Playwright trace at {TRACE_PATH}"
    )
