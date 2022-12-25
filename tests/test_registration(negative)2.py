import time

from test_data import url, email, name, inputEmail, inputName, btnSignUpInHomePage, btnSignUpPath
from selenium.webdriver.common.by import By


def test_signUpWithNoPassword(browser):
    browser.get(url)
    browser.find_element(By.XPATH, btnSignUpInHomePage).click()
    browser.find_element(By.XPATH, inputEmail).send_keys(email)
    browser.find_element(By.XPATH, inputName).send_keys(name)
    browser.find_element(By.XPATH, btnSignUpPath).click()
    time.sleep(10)
    assert "http://localhost:5000/signup" in browser.current_url
