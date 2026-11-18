from pathlib import Path

from playwright.sync_api import expect


def test_handle_dialogs_and_downloads(page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="JavaScript Alerts").click()

    dialogs = []
    accept_dialog = True

    def handle_dialog(dialog):
        dialogs.append((dialog.type, dialog.message))
        if accept_dialog:
            dialog.accept()
        else:
            dialog.dismiss()

    page.on("dialog", handle_dialog)

    page.get_by_role("button", name="Click for JS Alert").click()
    assert dialogs[-1] == ("alert", "I am a JS Alert")
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

    page.get_by_role("button", name="Click for JS Confirm").click()
    assert dialogs[-1] == ("confirm", "I am a JS Confirm")
    expect(page.locator("#result")).to_have_text("You clicked: Ok")

    accept_dialog = False
    page.get_by_role("button", name="Click for JS Confirm").click()
    assert dialogs[-1] == ("confirm", "I am a JS Confirm")
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")

    # page.goto("https://the-internet.herokuapp.com/download")
    page.go_back()
    page.get_by_text("File Download", exact=True).click()
    with page.expect_download() as download_info:
        page.get_by_role("link", name="hello.txt", exact=True).click()

    download = download_info.value
    print(f"Suggested filename: {download.suggested_filename}")
    download_path = download.path()
    assert download_path is not None
    assert Path(download_path).is_file()
