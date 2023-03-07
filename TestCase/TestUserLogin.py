from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestUserLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

    def test_user_login_username_error(self):
        username = ''
        pwd = '123456'
        expected = '账号不能为空'

        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected
        alert.accept()

    def test_user_login_ok(self):
        username = 'zhaozexin'
        pwd = '123456'
        expected = '用户中心'

        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        assert self.driver.title == expected

    def teardown_class(self):
        self.driver.quit()

