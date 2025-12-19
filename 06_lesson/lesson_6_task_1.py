from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 16)

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()
waiter.until(
   EC.visibility_of_element_located(
       (By.XPATH, "//div[@id='content']//p[contains(@class, 'bg-success')]")
   )
)

print(driver.find_element(By.ID, "content").text)

driver.quit()