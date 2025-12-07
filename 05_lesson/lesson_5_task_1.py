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
driver.get("http://uitestingplayground.com/classattr")
time.sleep(2)

# Находим СИНЮЮ кнопку (первую) по точным классам
button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-test")

print(f"Найдена синяя кнопка. Текст: '{button.text}'")
print(f"Классы кнопки: {button.get_attribute('class')}")

# Кликаем по кнопке
button.click()
print("Клик по синей кнопке выполнен!")

# Обрабатываем алерт (если появится)
try:
    alert = driver.switch_to.alert
    print(f"Текст алерта: {alert.text}")
    alert.accept()  # Нажимаем OK
    print("Алерт закрыт")
except:
    print("Алерт не появился")

time.sleep(2)
driver.quit()