from pathlib import Path
from playwright.sync_api import expect


BASE_URL = "https://demowebshop.tricentis.com/"
REPORTS_DIR = Path(__file__).resolve().parents[1] / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
VIDEOS_DIR = REPORTS_DIR / "videos"
TRACE_PATH = REPORTS_DIR / "trace.zip"


def _capture_screenshots(page, prefix):
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    page.goto(BASE_URL, wait_until="domcontentloaded")
    expect(page).to_have_title("Demo Web Shop")
    page.screenshot(path=str(SCREENSHOTS_DIR / f"{prefix}_homepage.png"))

    page.locator('a[href="/books"]').first.click()
    expect(page).to_have_url(f"{BASE_URL}books")
    expect(page).to_have_title("Demo Web Shop. Books")
    page.screenshot(path=str(SCREENSHOTS_DIR / f"{prefix}_books.png"))
    page.screenshot(path=str(SCREENSHOTS_DIR / f"{prefix}_books_full_page.png"),full_page=True,)


def _record_video(browser):
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    context = browser.new_context(record_video_dir=str(VIDEOS_DIR))
    page = context.new_page()
    video = page.video

    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        expect(page).to_have_title("Demo Web Shop")

        page.locator('a[href="/books"]').first.click()
        expect(page).to_have_url(f"{BASE_URL}books")
        page.locator("#products-orderby").select_option(label="Name: A to Z")
        page.get_by_role("link", name="Computing and Internet", exact=True).click()
        expect(page).to_have_url(f"{BASE_URL}computing-and-internet")
        page.go_back()
        expect(page.locator("h1")).to_have_text("Books")
    finally:
        page.close()
        context.close()

    video_path = Path(video.path())
    assert video_path.is_file() and video_path.stat().st_size > 0, (
        f"Expected a non-empty Playwright video at {video_path}"
    )
    assert video_path.parent.resolve() == VIDEOS_DIR.resolve()
    return video_path


def _capture_trace(context, page):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.locator('a[href="/books"]').first.click()
    expect(page).to_have_url(f"{BASE_URL}books")
    page.locator("input.search-box-text").fill("computer")
    page.locator("input.search-box-text").press("Enter")
    expect(page).to_have_url(f"{BASE_URL}search?q=computer")
    expect(page.locator(".product-title").first).to_contain_text("computer")

    context.tracing.stop(path=str(TRACE_PATH))
    assert TRACE_PATH.is_file() and TRACE_PATH.stat().st_size > 0, (
        f"Expected a non-empty Playwright trace at {TRACE_PATH}"
    )


def test_capture_homepage_and_books_screenshots(page):
    _capture_screenshots(page, "part_a")


def test_record_video_of_books_interactions(browser):
    _record_video(browser)


def test_trace_books_search(context, page):
    """Inspect the saved trace with: playwright show-trace reports/trace.zip."""
    _capture_trace(context, page)


def test_capture_screenshots_video_and_trace_together(browser, context, page):
    _capture_screenshots(page, "combined")
    _record_video(browser)
    _capture_trace(context, page)
