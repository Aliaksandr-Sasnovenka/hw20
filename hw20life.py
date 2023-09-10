import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import rsa
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from secret import password
from secret import privateKey
from secret import username


class Browser:
    browser, service = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Edge(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_life_by(self, user: str, passwd: str):
        self.add_input(by=By.NAME, value='msisdn', text=user)
        self.add_input(by=By.ID, value='password', text=passwd)
        self.click_button(by=By.XPATH, value="//button[starts-with(@class='group relative transition')]")


if __name__ == '__main__':
    browser = Browser(driver='c:/Users/Alex/.wdm/drivers/edgedriver/win64/116.0.1938.76/msedgedriver.exe')

    browser.open_page('https://business.life.com.by/')
    time.sleep(3)

    browser.login_life_by(username, rsa.decrypt(password, privateKey).decode())
    time.sleep(10)

    browser.close_browser()
