from playwright.sync_api import sync_playwright

def test_open_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://playwright.dev")
        assert "Playwright" in page.title()
        browser.close()

# pytest .\tests\test_example_pytest_2.py