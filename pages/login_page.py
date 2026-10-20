
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()

    def get_error_message(self):
        return self.page.locator("[data-test='error']").inner_text()

    def is_error_visible(self):
        return self.page.locator("[data-test='error']").is_visible()
