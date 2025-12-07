from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Инициализация Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Открываем страницу
driver.get("http://uitestingplayground.com/dynamicid")
time.sleep(2)

# Находим синюю кнопку с динамическим ID
# Используем селектор по классу (ID меняется каждый раз)
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

print(f"Найдена кнопка. Текст: '{button.text}'")
print(f"Классы кнопки: {button.get_attribute('class')}")
print(f"ID кнопки (динамическое): {button.get_attribute('id')}")

# Кликаем по кнопке
button.click()
print("Клик по кнопке выполнен!")

time.sleep(2)
driver.quit()