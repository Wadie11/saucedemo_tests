from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator("[data-test='inventory-item-name']")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def verify_product_in_cart(self, product_name: str):
        expect(self.cart_items.get_by_text(product_name, exact=True)).to_be_visible()