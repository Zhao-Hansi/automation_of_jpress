from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        WebDriverWait(self.driver, 1, 5).until(EC.visibility_of(self.driver.find_element(*loc)))
        return self.driver.find_element(*loc)

    def type_text(self, text, *loc):
        WebDriverWait(self.driver, 1, 5).until(EC.visibility_of(self.driver.find_element(*loc)))
        self.find_element(*loc).send_keys(text)

    def click(self, *loc):
        WebDriverWait(self.driver, 1, 5).until(EC.visibility_of(self.driver.find_element(*loc)))
        self.find_element(*loc).click()

    def clear(self, *loc):
        WebDriverWait(self.driver, 1, 5).until(EC.visibility_of(self.driver.find_element(*loc)))
        self.find_element(*loc).clear()

    def get_title(self):
        return self.driver.title
