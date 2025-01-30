import pytest
from utils.driver import create_driver
from time import sleep

def test_website_title():
    driver = create_driver()
    print("Testing started: Checking title")
    driver.get("https://www.saucedemo.com/")
    sleep(3)
    title = driver.title
    assert "Swag Labs" in title
    print("TEST PASSED: Title test")
    driver.quit()
