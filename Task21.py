from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Saucedemo:

    def __init__(self):
        self.url = "https://www.saucedemo.com/"
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    def open_url(self):
        try:
            self.driver.get(self.url)
            print("Opening URL successful")
            sleep(3)
        except Exception as selenium_error:
            print(f"Error opening URL: {selenium_error}")

    def get_cookies(self):
        try:
            cookies = self.driver.get_cookies()
            print("Showing Cookies:")
            for cookie in cookies:
                print(f"{cookie['name']}: {cookie['value']}")
        except Exception as selenium_error:
            print(f"Error getting cookies: {selenium_error}")

    def login(self):
        try:
            username = 'standard_user'
            password = 'secret_sauce'
            username_textbox = self.driver.find_element(By.ID, 'user-name').send_keys(username)
            pass_textbox = self.driver.find_element(By.ID, 'password').send_keys(password)
            login_button = self.driver.find_element(By.ID, 'login-button').click()
            print("Logging in successful")
        except NoSuchElementException as selenium_error:
            print(f"Error logging in: {selenium_error}")

    def logout(self):
        try:
            menu_button = self.driver.find_element(By.ID, 'react-burger-menu-btn').click()
            logout_button = self.driver.find_element(By.ID, 'logout_sidebar_link').click()
            print("Logging out successful")
        except NoSuchElementException as selenium_error:
            print(f"Error logging out: {selenium_error}")

    def shutdown(self):
        try:
            self.driver.quit()
            print("Browser closed")
        except Exception as selenium_error:
            print(f"Error closing the browser: {selenium_error}")

try:
    req = Saucedemo()
    req.open_url()
    req.get_cookies()
    req.login()
    req.get_cookies()
    req.logout()
finally:
    req.shutdown()
