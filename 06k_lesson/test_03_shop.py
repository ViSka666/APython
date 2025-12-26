import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sauce_demo_purchase():
    
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        username_field = driver.find_element(By.ID, "user-name").send_keys("standard_user")
        
        password_field = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        login_button = driver.find_element(By.ID, "login-button").click()
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        
        for product_name in products_to_add:
            add_button = driver.find_element(
                By.XPATH, 
                f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
            ).click()
        
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))
        
        checkout_button = driver.find_element(By.ID, "checkout").click()
        
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        
        continue_button = driver.find_element(By.ID, "continue").click()
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        
        total_amount = total_text.split("$")[1]
        
        assert total_amount == "58.29", (
            f"Итоговая сумма должна быть $58.29, но получено ${total_amount}"
        )
        
    except Exception as e:
    
        driver.save_screenshot("shop_error.png")
        
        print(f"Текущий URL: {driver.current_url}")
        print(f"Заголовок страницы: {driver.title}")
        
        try:
            cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
            print(f"Товаров в корзине: {len(cart_items)}")
        except:
            pass
            
        pytest.fail(f"Тест завершился с ошибкой: {e}")
        
    finally:
        driver.quit()