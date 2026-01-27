import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    username = os.getenv("LT_USERNAME")
    access_key = os.getenv("LT_ACCESS_KEY")
    grid_url = "hub.lambdatest.com/wd/hub"

    lt_options = {
        "user": username,
        "accessKey": access_key,
        "build": "Scrolling in Selenium",
        "name": "Scroll Test Case X",
        "platformName": "Windows 11",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "selenium_version": "latest"
    }

    options = webdriver.ChromeOptions()
    options.set_capability('LT:Options', lt_options)

    url = f"https://{username}:{access_key}@{grid_url}"
    
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")

    yield driver

    driver.quit()

def test_scroll_with_scrollIntoView(driver):
    product = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@id='mz-product-listing-image-81218410-0-1']")
    ))

    driver.execute_script("arguments[0].scrollIntoView(true);", product)

    product.click()

    assert "product_id=31" in driver.current_url

def test_scroll_with_action_chains(driver):
    product = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@id='mz-product-listing-image-81218410-0-1']")
    ))

    ActionChains(driver).move_to_element(product).pause(0.5).click().perform()

    assert "product_id=31" in driver.current_url

def test_scroll_with_scrollBy(driver):
    driver.execute_script("window.scrollBy(0, 1200);")
    
    driver.execute_script("window.scrollBy(0, 1200);")

    product = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@id='mz-product-listing-image-81218410-0-1']")
    ))

    product.click()

    assert "product_id=31" in driver.current_url

