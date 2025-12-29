from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

wait = WebDriverWait(driver, 10)

# Step 1: Click on "Allow all"
try:
    allow_all_button = wait.until(
        EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
    )
    allow_all_button.click()
except Exception as e:
    print(f"Cookie banner not found or already dismissed: {e}")

# Step 2: Locate the target element
start_free_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Start free with Email')]"))
)

# Step 3: Scroll using ActionChains and click
actions = ActionChains(driver)
actions.move_to_element(start_free_button).pause(0.3).click().perform()

# Step 4: Confirm page loaded
heading = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Get started for free')]"))
)

assert heading.is_displayed(), "Expected heading was not found on the new page"