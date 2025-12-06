from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/inputs")
time.sleep(2)

print("Страница загружена. Заголовок:", driver.title)

# Находим поле ввода типа number
# Вариант 1: По CSS селектору из DevTools
input_field = driver.find_element(By.CSS_SELECTOR, "#content > div > div > div > input[type='number']")

# Вариант 2: Более простой селектор
# input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
# input_field = driver.find_element(By.XPATH, "//input[@type='number']")

print(f"\nНайдено поле ввода:")
print(f"  Тип: {input_field.get_attribute('type')}")
print(f"  Атрибут wfd-id: {input_field.get_attribute('wfd-id')}")
print(f"  Текущее значение: {input_field.get_attribute('value')}")

# Вводим текст "Sky"
input_field.send_keys("Sky")
time.sleep(1)
print("✓ Введено: 'Sky'")
print(f"  Значение после ввода: {input_field.get_attribute('value')}")

# Очищаем поле
input_field.clear()
time.sleep(1)
print("✓ Поле очищено")
print(f"  Значение после очистки: {input_field.get_attribute('value')}")

# Вводим текст "Pro"
input_field.send_keys("Pro")
time.sleep(1)
print("✓ Введено: 'Pro'")
print(f"  Значение после ввода: {input_field.get_attribute('value')}")

print("\n✅ Задание выполнено успешно!")

# Закрываем браузер
time.sleep(1)
driver.quit()