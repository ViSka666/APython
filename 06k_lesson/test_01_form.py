import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
    edge_options = EdgeOptions()
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    edge_options.add_argument('--log-level=3')
    edge_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Edge(options=edge_options)
    waiter = WebDriverWait(driver, 10)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        waiter.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        
        zip_field = driver.find_element(By.NAME, "zip-code").clear()
        
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")
        
        submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        
        waiter.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success, .alert-danger"))
        )
        
        zip_code_display = driver.find_element(By.ID, "zip-code")
        zip_code_classes = zip_code_display.get_attribute("class")
        
        assert "alert-danger" in zip_code_classes, (
            f"Поле Zip code должно быть подсвечено красным (alert-danger)."
            f"Текущие классы: {zip_code_classes}"
        )
        assert zip_code_display.text == "N/A", (
            f"Поле Zip code должно содержать 'N/A'."
            f"Текущий текст: {zip_code_display.text}"
        )
        
        green_field_ids = [
            "first-name", "last-name", "address", "e-mail", 
            "phone", "city", "country", "job-position", "company"
        ]
        
        for field_id in green_field_ids:
            field_element = driver.find_element(By.ID, field_id)
            field_classes = field_element.get_attribute("class")
            
            assert "alert-success" in field_classes, (
                f"Поле {field_id} должно быть подсвечено зеленым (alert-success). "
                f"Текущие классы: {field_classes}"
            )
            
            assert field_element.text != "N/A", (
                f"Поле {field_id} не должно содержать 'N/A'. "
                f"Текущий текст: {field_element.text}"
            )
        
    except Exception as e:
        driver.save_screenshot("error_screenshot.png")
        pytest.fail(f"Тест завершился с ошибкой: {e}")
        
    finally:
        driver.quit()