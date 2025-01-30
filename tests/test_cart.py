import pytest
from selenium.webdriver.common.by import By
from utils.driver import create_driver
from time import sleep

def test_add_to_cart():
    driver = create_driver()
    print("Testing started: Add to cart")
    driver.get("https://www.saucedemo.com/")
    sleep(3)

    # Find all add-to-cart buttons and click the first 3
    add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for btn in add_to_cart_btns[:3]:
        btn.click()

    # Check if the cart badge reflects the added items
    cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert "3" in cart_value.text
    print("TEST PASSED: Add to cart")
    driver.quit()

def test_remove_from_cart():
    driver = create_driver()
    print("Testing started: Remove from cart")
    driver.get("https://www.saucedemo.com/")
    sleep(3)

    # Find all add-to-cart buttons and click the first 3 items
    add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for btn in add_to_cart_btns[:3]:
        btn.click()

    # Now remove 2 items
    remove_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for btn in remove_btns[:2]:
        btn.click()

    # Check if the cart badge reflects the removed items
    cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert "1" in cart_value.text
    print("TEST PASSED: Remove from cart")
    driver.quit()

