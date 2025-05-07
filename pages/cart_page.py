from selenium.webdriver.common.by import By # type: ignore

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_first_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
