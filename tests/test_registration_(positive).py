from test_data import url, email, name, password, inputEmail, inputName, inputPassword, btnSignUpInHomePage, \
    btnSignUpPath
from selenium.webdriver.common.by import By


def test_signUp(browser):
    browser.get(url)
    browser.find_element(By.XPATH, btnSignUpInHomePage).click()
    browser.find_element(By.XPATH, inputEmail).send_keys(email)
    browser.find_element(By.XPATH, inputName).send_keys(name)
    browser.find_element(By.XPATH, inputPassword).send_keys(password)
    browser.find_element(By.XPATH, btnSignUpPath).click()
    assert "http://localhost:5000/login" in browser.current_url
