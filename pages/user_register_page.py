from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserRegisterPage(BasePage):
    username_input = (By.NAME, 'username')
    email_input = (By.NAME, 'email')
    pwd_input = (By.NAME, 'pwd')
    confirmPwd_input = (By.NAME, 'confirmPwd')
    captcha_input = (By.NAME, 'captcha')
    register_btn = (By.CLASS_NAME, 'btn')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_register_page(self):
        self.driver.get("http://localhost:8080/jpress/user/register")
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(*self.username_input)
        self.type_text(username, *self.username_input)

    def input_email(self, email):
        self.clear(*self.email_input)
        self.type_text(email, *self.email_input)

    def input_pwd(self, pwd):
        self.clear(*self.pwd_input)
        self.type_text(pwd, *self.pwd_input)

    def input_confirmPwd(self, confirm_pwd):
        self.clear(*self.confirmPwd_input)
        self.type_text(confirm_pwd, *self.confirmPwd_input)

    def input_captcha(self, captcha):
        self.clear(*self.captcha_input)
        self.type_text(captcha, *self.captcha_input)

    def click_register_btn(self):
        self.click(*self.register_btn)