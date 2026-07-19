from playwright.sync_api import Page


class LoginPage: 
    def __init__(self, page:Page):
        self.page = page
        self.page.goto("https://www.saucedemo.com/")

        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")

        self.btn = page.get_by_role("button", name="Login")

        self.label = self.page.locator("h3")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

        self.btn.click()
