from selenium.webdriver.common.by import By # type: ignore

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return "inventory.html" in self.driver.current_url

    def add_first_product_to_cart(self):
        self.driver.find_element(By.XPATH, "(//button[contains(text(),'Add to cart')])[1]").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
