from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

wait = WebDriverWait(driver, 10)

# Accept cookie banner if visible
try:
    allow_all_button = wait.until(
        EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
    )
    allow_all_button.click()
except:
    pass  # Cookie banner already dismissed

# Scroll down manually by 800 pixels
driver.execute_script("window.scrollBy(0, 200);")

# Locate and click the target element after scroll
start_free_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Start free with Email')]"))
)
start_free_button.click()

# Assert that the expected heading is visible
heading = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Get started for free')]"))
)

assert heading.is_displayed(), "Expected heading was not found on the new page"
