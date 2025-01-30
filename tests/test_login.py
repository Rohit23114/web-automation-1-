import pytest
from selenium.webdriver.common.by import By
from utils.driver import create_driver
from time import sleep

def test_login_successful():
    driver = create_driver()
    print("Testing started: Login")
    driver.get("https://www.saucedemo.com/")
    sleep(3)

    # Perform login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    sleep(5)

    # Assert successful login
    text = driver.find_element(By.CLASS_NAME, "title").text 
    assert "products" in text.lower()
    print("TEST PASSED: Login successful")
    driver.quit()
