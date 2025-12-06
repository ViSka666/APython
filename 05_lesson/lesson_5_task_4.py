from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/login")
time.sleep(2)

print("Страница загружена. Заголовок:", driver.title)
print("-" * 50)

# 1. Находим поле "Имя пользователя" по ID
username_field = driver.find_element(By.ID, "username")
print(f"Найдено поле username:")
print(f"  ID: {username_field.get_attribute('id')}")
print(f"  Name: {username_field.get_attribute('name')}")
print(f"  Type: {username_field.get_attribute('type')}")

# Вводим значение tomsmith
username_field.send_keys("tomsmith")
print("✓ Введен username: tomsmith")
time.sleep(1)

# 2. Находим поле "Пароль" по ID
password_field = driver.find_element(By.ID, "password")
print(f"\nНайдено поле password:")
print(f"  ID: {password_field.get_attribute('id')}")
print(f"  Name: {password_field.get_attribute('name')}")
print(f"  Type: {password_field.get_attribute('type')}")

# Вводим значение SuperSecretPassword!
password_field.send_keys("SuperSecretPassword!")
print("✓ Введен password: SuperSecretPassword!")
time.sleep(1)

# 3. Находим кнопку "Вход" (Login)
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print(f"\nНайдена кнопка Login:")
print(f"  Текст: '{login_button.text}'")
print(f"  Type: {login_button.get_attribute('type')}")

# Нажимаем кнопку
login_button.click()
print("✓ Нажата кнопка Login")
time.sleep(2)

# 4. Находим зеленую плашку с сообщением об успехе
success_message = driver.find_element(By.ID, "flash")
message_text = success_message.text.strip()

print("\n" + "="*50)
print("СООБЩЕНИЕ ПОСЛЕ АВТОРИЗАЦИИ:")
print("="*50)
print(message_text)
print("="*50)

# Проверяем, что авторизация прошла успешно
if "You logged into a secure area!" in message_text:
    print("\n✅ Авторизация прошла УСПЕШНО!")
else:
    print("\n⚠️  Авторизация не прошла. Проверьте данные.")

# Дополнительно: выводим текущий URL
print(f"\nТекущий URL: {driver.current_url}")

# Пауза чтобы увидеть результат
time.sleep(2)

# Закрываем браузер
driver.quit()