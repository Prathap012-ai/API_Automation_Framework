import pytest

from utils.api_methods import APIMethods


@pytest.fixture()
def api():
    print("API setup started")
    api = APIMethods()
    yield api
    print("API teardown completed")

import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield  browser
        browser.close()

@pytest.fixture()
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture()
def page(context):
    page = context.new_page()
    yield page
    page.close()
