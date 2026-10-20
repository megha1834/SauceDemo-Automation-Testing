
import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def checkout(login_page):
    login_page.login("standard_user", "secret_sauce")

    expect(login_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    inventory = InventoryPage(login_page.page)
    inventory.add_backpack()
    inventory.open_cart()

    checkout_page = CheckoutPage(login_page.page)
    checkout_page.start_checkout()

    return checkout_page


def test_successful_checkout(checkout):
    checkout.fill_information("Megha", "Rahman", "1207")
    checkout.continue_checkout()
    checkout.finish_checkout()

    expect(checkout.confirmation_message()).to_have_text(
        "Thank you for your order!"
    )


@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("", "Rahman", "1207", "First Name is required"),
        ("Megha", "", "1207", "Last Name is required"),
        ("Megha", "Rahman", "", "Postal Code is required"),
    ]
)
def test_checkout_missing_information(
    checkout, first_name, last_name, postal_code, expected_error
):
    checkout.fill_information(first_name, last_name, postal_code)
    checkout.continue_checkout()

    expect(checkout.error_message()).to_contain_text(expected_error)
