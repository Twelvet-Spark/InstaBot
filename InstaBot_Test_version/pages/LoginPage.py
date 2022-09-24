from time import sleep
from selenium.webdriver.common.by import By
import config

class LoginPage:
    def __init__(self, driver, id):
        self.driver = driver
        self.id = id
    
    def login(self):
        username_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")

        username_input.send_keys(config.login_data[self.id]["login"])
        sleep(config.sleep_time)
        password_input.send_keys(config.login_data[self.id]["password"])

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        try:
            sleep(config.sleep_time+4) # Даём новой странице загрузиться
            self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        except Exception:
            print(f"[Драйвер - {self.id}] Вход успешно выполнен\n")
        else:
            print(f"[Драйвер - {self.id}] Вход НЕ выполнен\n")