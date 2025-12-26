import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    waiter = WebDriverWait(driver, 50)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        waiter.until(EC.presence_of_element_located((By.ID, "delay")))

        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        result_element = driver.find_element(By.CLASS_NAME, "screen")

        waiter.until(
            lambda d: d.find_element(By.CLASS_NAME, "screen").text == "15",
            message=f"Результат не стал равен '15' за отведенное время"
        )

        final_result = result_element.text

        assert final_result == "15", (
            f"Ожидался результат '15', но получено '{final_result}'"
        )
        
    except Exception as e:
        driver.save_screenshot("calculator_error.png")

        try:
            current_display = driver.find_element(By.CLASS_NAME, "screen").text
            print(f"Текущее значение на экране: '{current_display}'")
        except:
            pass
            
        pytest.fail(f"Тест завершился с ошибкой: {e}")
        
    finally:
        driver.quit()