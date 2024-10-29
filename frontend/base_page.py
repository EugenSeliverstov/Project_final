import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://discord.com/login'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def send_message(self, locator, text_m):
        element = self.find_element(locator)
        element.send_keys(text_m)
        pyautogui.press('enter')


    def click(self, locator, time=10):
        element = self.find_element(locator, time)
        element.click()

    def hover(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)