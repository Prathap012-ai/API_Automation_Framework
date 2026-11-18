from playwright.sync_api import expect


def test_handle_iframe(page):
    page.goto("https://the-internet.herokuapp.com/iframe")

    heading = page.locator("h3")
    expect(heading).to_contain_text("An iFrame")

    editor = page.frame_locator("iframe#mce_0_ifr").locator("body")
    editor.fill("")
    editor.fill("Welcome to Playwright Python Automation")

    expect(editor).to_have_text("Welcome to Playwright Python Automation")
    print(editor.inner_text())
