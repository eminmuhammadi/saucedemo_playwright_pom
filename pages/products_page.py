from data.constants import *
from data.locators import *


class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title_locator = page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)
        self.url = f"{CONSTANTS_BASE_URL}/inventory.html"

    def add_to_cart(self, item_name):
        item_name_locator = self.page.locator(f"button[name=\"{item_name}\"]")
        item_name_locator.click()
