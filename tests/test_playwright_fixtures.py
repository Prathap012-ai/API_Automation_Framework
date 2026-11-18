from playwright.sync_api import expect


def test_homepage_title(page):
    page.goto("https://demowebshop.tricentis.com/")
    title = page.title()
    print(f"Title of the page: '{title}'")
    expect(page).to_have_title("Demo Web Shop")



