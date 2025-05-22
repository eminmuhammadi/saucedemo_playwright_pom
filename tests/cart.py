# ===================================== #
# Tests
# Ref: https://playwright.dev/python/docs/test-assertions
# ===================================== #
import pytest
from playwright.sync_api import expect
from fixtures.playwright import *
from fixtures.saucedemo import *
from data.constants import *


@pytest.mark.tags("JIRA-1001", "ui", "cart")
@pytest.mark.parametrize("login_page", ["standard_user"], indirect=True)
def test_standard_users_should_be_able_to_see_cart(cart_page):
    expect(cart_page.title_locator).to_have_text(CONSTANTS_CART_PAGE_TITLE)
    expect(cart_page.page).to_have_url(cart_page.url)
    expect(cart_page.inventory_item_name_locator).to_contain_text(CONSTANTS_CART_INVENTORY_ITEM_NAME)