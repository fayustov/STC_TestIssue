from test_data import url, email, name, password, inputEmail, inputPassword, btnLogin
from selenium.webdriver.common.by import By

btnLoginInHomePage = "//div[@class='navbar-end']//a[contains(text(), 'Login')]"


def test_login(browser):
    browser.get(url)
    browser.find_element(By.XPATH, btnLoginInHomePage).click()
    browser.find_element(By.XPATH, inputEmail).send_keys(email)
    browser.find_element(By.XPATH, inputPassword).send_keys(password)
    browser.find_element(By.XPATH, btnLogin).click()
    assert "http://localhost:5000/profile" in browser.current_url
