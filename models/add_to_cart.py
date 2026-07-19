from playwright.sync_api import Page

class AddToCart:
    def __init__(self, page: Page):
        self.page = page

        self.product1_name = page.get_by_text("Sauce Labs Backpack", exact=True)
        self.product1_btn = page.locator("button[name='add-to-cart-sauce-labs-backpack']")

        self.product2_name = page.get_by_text("Sauce Labs Bike Light", exact=True)
        self.product2_btn = page.locator("button[name='add-to-cart-sauce-labs-bike-light']")

        self.shopping_cart_btn = page.locator("#shopping_cart_container a")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def add_product(self):
        self.product1_btn.click()
        self.product2_btn.click()

    def go_to_cart(self):
        self.shopping_cart_btn.click()

