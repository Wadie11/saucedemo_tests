from models.login_page import LoginPage
from models.add_to_cart import AddToCart
from models.cart_page import CartPage
from playwright.sync_api import Page, expect
URL = "https://www.saucedemo.com/inventory.html"
URL_CART = "https://www.saucedemo.com/cart.html"


def test_successful_login(page: Page): 
    username = "standard_user"
    password = "secret_sauce"

    login_page = LoginPage(page)
    login_page.login(username, password)

    assert page.url == URL


def test_failed_login(page: Page): 
    username = "standard_user"
    password = "standard_user"   

    login_page = LoginPage(page)
    login_page.login(username, password)

    expect (login_page.label).to_have_text("Epic sadface: Username and password do not match any user in this service")


def test_add_products_and_verify_cart(page: Page):
    # Login
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    # Add products to cart
    add_cart = AddToCart(page)
    add_cart.goto()
    add_cart.add_product()
    add_cart.go_to_cart()

    # Verify we're on the cart page
    assert page.url == URL_CART

    # Verify both products appear in the cart
    cart_page = CartPage(page)
    cart_page.verify_product_in_cart("Sauce Labs Backpack")
    cart_page.verify_product_in_cart("Sauce Labs Bike Light")

