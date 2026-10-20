
import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage


@pytest.fixture
def inventory(login_page):
    login_page.login("standard_user", "secret_sauce")

    expect(login_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    return InventoryPage(login_page.page)


def test_add_one_product(inventory):
    inventory.add_backpack()

    expect(inventory.cart_badge()).to_have_text("1")


def test_add_two_products(inventory):
    inventory.add_backpack()
    inventory.add_bike_light()

    expect(inventory.cart_badge()).to_have_text("2")


def test_remove_product(inventory):
    inventory.add_backpack()
    inventory.remove_backpack()

    expect(inventory.cart_badge()).to_have_count(0)
def test_product_appears_in_cart(inventory):
    inventory.add_backpack()
    inventory.open_cart()

    # Wait until cart page is loaded
    expect(inventory.page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    # Verify the specific backpack is visible
    expect(
        inventory.page.get_by_text(
            "Sauce Labs Backpack",
            exact=True
        )
    ).to_be_visible()