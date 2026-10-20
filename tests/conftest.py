
import pytest
from pathlib import Path
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page):
    login = LoginPage(page)
    login.open()
    return login


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page is not None:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            safe_name = "".join(
                c if c.isalnum() or c in "-_" else "_"
                for c in item.nodeid
            )

            screenshot_path = screenshot_dir / f"{safe_name}.png"

            try:
                page.screenshot(
                    path=str(screenshot_path),
                    full_page=True
                )
                print(f"\nFailure screenshot: {screenshot_path}")
            except Exception as error:
                print(f"\nCould not capture screenshot: {error}")
