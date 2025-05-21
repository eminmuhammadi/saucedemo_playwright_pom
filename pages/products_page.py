from data.constants import *
from data.locators import *


class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)
