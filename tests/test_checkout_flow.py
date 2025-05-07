import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore

def test_checkout_flow():
    driver = get_driver()

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    # Tunggu sampai tombol checkout tersedia
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()


    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    ).click()

    complete_text = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert complete_text == "Thank you for your order!"

    print("Checkout berhasil diselesaikan.")
    driver.quit()
