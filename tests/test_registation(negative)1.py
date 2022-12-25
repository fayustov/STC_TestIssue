from test_data import url, name, password, inputName, inputPassword, btnSignUpInHomePage, btnSignUpPath
from selenium.webdriver.common.by import By


def test_signUpWithNoEmail(browser):
    browser.get(url)
    browser.find_element(By.XPATH, btnSignUpInHomePage).click()
    browser.find_element(By.XPATH, inputName).send_keys(name)
    browser.find_element(By.XPATH, inputPassword).send_keys(password)
    browser.find_element(By.XPATH, btnSignUpPath).click()
    assert "http://localhost:5000/signup" in browser.current_url
