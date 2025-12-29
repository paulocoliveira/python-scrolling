from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# Locate the target element
start_free_button = driver.find_element(By.XPATH, "//a[contains(text(),'Start free with Email')]")

# Scroll to the element
driver.execute_script("arguments[0].scrollIntoView(true);", start_free_button)

# Click the element
start_free_button.click()

# Assert that the new page is loaded by checking the heading
heading = driver.find_element(By.XPATH, "//h2[contains(text(),'Get started for free')]")

assert heading.is_displayed(), "Expected heading was not found on the new page"