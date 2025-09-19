import time
from pages.login_page import LoginPage

def test_successful_login(driver, base_url):
    lp = LoginPage(driver, base_url)
    lp.load()
    lp.login("tomsmith", "SuperSecretPassword!")
    time.sleep(1)
    assert "You logged into a secure area!" in lp.flash_text()

def test_invalid_login(driver, base_url):
    lp = LoginPage(driver, base_url)
    lp.load()
    lp.login("wronguser", "wrongpass")
    time.sleep(1)
    assert "Your username is invalid!" in lp.flash_text()

def test_navigation_after_login(driver, base_url):
    lp = LoginPage(driver, base_url)
    lp.load()
    lp.login("tomsmith", "SuperSecretPassword!")
    time.sleep(1)
    assert "/secure" in driver.current_url
