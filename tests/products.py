# ===================================== #
# Tests
# Ref: https://playwright.dev/python/docs/test-assertions
# ===================================== #
import pytest
from playwright.sync_api import expect
from fixtures.playwright import *
from fixtures.saucedemo import *
from data.constants import *


@pytest.mark.tags("JIRA-0001", "ui", "auth")
@pytest.mark.parametrize("login_page", ["standard_user"], indirect=True)
def test_standard_users_should_be_able_to_see_products(products_page):
    expect(products_page.title_locator).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page.page).to_have_url(products_page.url)


@pytest.mark.tags("JIRA-0002", "ui", "auth")
@pytest.mark.parametrize("login_page", ["problem_user"], indirect=True)
def test_problem_users_should_be_able_to_see_products(products_page):
    expect(products_page.title_locator).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page.page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0003", "ui", "auth")
@pytest.mark.parametrize("login_page", ["locked_out_user"], indirect=True)
def test_locked_out_users_should_not_be_able_to_see_products(login_page):
    expect(login_page.error_message).to_have_text(CONSTANTS_AUTH_ERROR_LOCKED_OUT_MESSAGE)


@pytest.mark.tags("JIRA-0004", "ui", "auth")
@pytest.mark.parametrize("login_page", ["performance_glitch_user"], indirect=True)
def test_performance_glitch_users_should_be_able_to_see_products(products_page):
    expect(products_page.title_locator).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page.page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0005", "ui", "auth")
@pytest.mark.parametrize("login_page", ["error_user"], indirect=True)
def test_error_users_should_be_able_to_see_products(products_page):
    expect(products_page.title_locator).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page.page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0006", "ui", "auth")
@pytest.mark.parametrize("login_page", ["visual_user"], indirect=True)
def test_visual_users_should_be_able_to_see_products(products_page):
    expect(products_page.title_locator).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page.page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")