from data.constants import *
from data.locators import *


class CartPage:
    def __init__(self, page):
        self.page = page
        self.title_locator = page.locator(LOCATORS_CART_PAGE_TITLE)
        self.url = f"{CONSTANTS_BASE_URL}/cart.html"
        self.inventory_item_name_locator = page.locator(LOCATORS_CART_INVENTORY_ITEM_NAME)

    def goto(self):
        self.page.goto(self.url)