from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.NAME, 'email')
        self.password_field = (By.NAME, 'password')
        self.login_button = (By.XPATH, '//button[@type = "submit"]')


    def set_email(self,email):
        WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(self.email_field)
        ).send_keys(email)

    def set_password(self,password):
        WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(self.password_field)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(self.login_button)
        ).click()


