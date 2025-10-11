import re
from time import sleep
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    page.get_by_role("combobox", name="q").fill("Playwright")
    sleep(1)	
    # page.pause()


# textarea[title="Pesquisar"]
# pytest .\tests\com_pytest\test_example_pytest_4.py --headed --browser=chromium --screenshot=on --video=on --html=report.html
# pytest .\tests\com_pytest\test_example_pytest_4.py --headed --browser=firefox
# pytest .\tests\com_pytest\test_example_pytest_4.py --headed --browser=webkit