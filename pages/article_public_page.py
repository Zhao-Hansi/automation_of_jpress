from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ArticlePage(BasePage):

    def __init__(self, login):
        BasePage.__init__(self, login.driver)
        self.login = login

    click_article_loc = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]')

    click_article_manage_loc = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a')

    click_add_article_btn_loc = (By.XPATH, '/html/body/div/div/section[3]/div/div/div/div[1]/div/div/a')

    article_title_loc = (By.ID, 'article-title')

    iframe_loc = (By.XPATH, '//*[@id="cke_1_contents"]/iframe')

    body_loc = (By.XPATH, '/html/body')

    add_btn_loc = (By.XPATH, '//*[@id="form"]/div/div[2]/div[1]/div/button[1]')

    article_link_loc = (By.XPATH, '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong/a')

    del_article_link_loc = (By.XPATH, '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/a[3]')

    select_all_checkbox_loc = (By.XPATH, '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input')

    del_all_btn_loc = (By.ID, 'batchDel')

    def click_article(self):
        self.click(*self.click_article_loc)
        sleep(1)

    def click_article_manage(self):
        self.click(*self.click_article_manage_loc)
        sleep(1)

    def click_add_article(self):
        self.click(*self.click_add_article_btn_loc)
        sleep(1)

    def input_article_title(self, title):
        self.type_text(title, *self.article_title_loc)
        sleep(1)

    def input_body(self, body):
        frame1 = self.find_element(*self.iframe_loc)
        self.login.driver.switch_to.frame(frame1)
        self.type_text(body, *self.body_loc)
        self.login.driver.switch_to.default_content()

    def click_add_btn(self):
        self.click(*self.add_btn_loc)

    def del_single_article(self):
        link = self.find_element(*self.article_link_loc)
        ActionChains(self.login.driver).move_to_element(link).perform()

        sleep(1)

        del_elem = self.find_element(*self.del_article_link_loc)
        del_elem.click()

    def del_all_article(self):
        sleep(1)
        self.find_element(*self.click_article_manage_loc).click()
        sleep(1)

        link = self.find_element(*self.select_all_checkbox_loc)
        link.click()

        self.find_element(*self.del_all_btn_loc).click()

        WebDriverWait(self.login.driver, 5).until(EC.alert_is_present())
        alert = self.login.driver.switch_to.alert
        alert.accept()