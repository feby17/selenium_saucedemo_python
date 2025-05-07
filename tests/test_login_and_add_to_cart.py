import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_login_and_add_product():
    driver = get_driver()

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(2)
    assert inventory.is_loaded(), "Login gagal atau halaman tidak terbuka."

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    time.sleep(1)
    product_name = cart.get_first_product_name()
    print("Produk di keranjang:", product_name)

    driver.quit()
