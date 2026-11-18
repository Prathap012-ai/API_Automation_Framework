import re
from playwright.sync_api import expect


def test_advanced_locators(page):
    page.goto("https://demowebshop.tricentis.com/", wait_until="load")

    books_menu = page.locator(".top-menu a[href='/books']")
    expect(books_menu).to_be_visible()
    books_menu.click()

    first_book = page.locator(".product-grid .item-box h2 a").first
    expect(first_book).to_be_visible()
    first_book_title = first_book.inner_text().strip()
    product_title = page.get_by_text(first_book_title, exact=True)
    expect(product_title).to_be_visible()
    assert first_book_title, "The first displayed book should have a product title"

    search_box = page.locator("#small-searchterms")
    expect(search_box).to_be_visible()
    expect(search_box).to_be_enabled()
    search_box.fill("computer")

    page.get_by_role("button", name="Search").click()

    search_result_titles = page.locator(".product-grid .item-box h2 a")
    computer_related_products = search_result_titles.filter(has_text=re.compile("computer", re.IGNORECASE))
    expect(computer_related_products.first).to_be_visible()
    assert computer_related_products.count() > 0, "Search results should contain computer-related products"