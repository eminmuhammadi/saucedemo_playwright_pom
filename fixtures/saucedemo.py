import pytest
from data.constants import *
from data.locators import *
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.fixture
def login_page(page, request) -> LoginPage:
    user_type = request.param
    password = CONSTANTS_USERS.get(user_type)
    if not password:
        raise ValueError(f"No credentials found for user type '{user_type}'")

    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(user_type, password)

    return login_page

@pytest.fixture
def products_page(page, login_page) -> ProductsPage:
    if login_page.check_error_message_exists():
        raise AssertionError(f"Login failed for given user type")
    
    return ProductsPage(page)

@pytest.fixture
def cart_page(page, products_page, request) -> CartPage:
    product_items = request.param
    if not isinstance(product_items, list):
        raise TypeError("Product items should be provided as a list")

    for item in product_items:
            products_page.add_to_cart(item)

    cart_page = CartPage(page)
    cart_page.goto()

    return cart_page