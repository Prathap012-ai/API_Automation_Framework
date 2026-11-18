import re

from playwright.sync_api import expect

def handle_request(route):
    url = route.request.url
    print(f"Intercepted URL:{url}")

    if ".jpg" in url or ".png" in url or ".jpeg" in url:
        print("Image request aborted")
        route.abort()
    else:
        route.continue_()

def test_network_interception(page):
    page.route("**/*", handle_request)
    page.goto(
        "https://demowebshop.tricentis.com/",
        wait_until="domcontentloaded",
        timeout=30000
    )

    assert page.title() == "Demo Web Shop"
    print("Homepage loaded successfully..")
