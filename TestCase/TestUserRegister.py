import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.user_register_page import UserRegisterPage
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from utils import util
from TestData import login_data


class TestUserRegister(object):

    def setup_class(self) -> None:
        self.driver = webdriver.Chrome()
        self.registerPage = UserRegisterPage(self.driver)
        self.registerPage.goto_register_page()

    @pytest.mark.parametrize('username,email,pwd,confirmPwd,captcha,expected', login_data)
    def test1_register(self, username, email, pwd, confirm_pwd, captcha, expected):

        self.registerPage.input_username(username)
        self.registerPage.input_email(email)

        self.registerPage.input_pwd(pwd)
        self.registerPage.input_confirmPwd(confirm_pwd)

        if captcha != '666':
            captcha = util.get_code(self.driver, 'captcha-img')

        self.registerPage.input_captcha(captcha)
        self.registerPage.click_register_btn()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected

        alert.accept()

    def teardown_class(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-sv', 'testUserRegister.py'])
