import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

def test_negative_login():
    driver = get_driver()
    login = LoginPage(driver)

    login.open()
    login.login("standard_user", "wrong_password")

    time.sleep(1)
    # Cek error message muncul
    error_msg = driver.find_element("css selector", "h3[data-test='error']").text
    assert "Username and password do not match" in error_msg

    print("Test login gagal berhasil diverifikasi.")
    driver.quit()
