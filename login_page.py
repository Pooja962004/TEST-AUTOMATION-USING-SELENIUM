from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def __init__(self, driver, base_url="https://the-internet.herokuapp.com"):
        self.driver = driver
        self.base_url = base_url

    def load(self):
        self.driver.get(self.base_url + "/login")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def flash_text(self):
        return self.driver.find_element(*self.FLASH).text
