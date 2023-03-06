from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class CategoryPage(BasePage):

    def __init__(self, login):
        BasePage.__init__(self, login.driver)

    click_article_loc = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]')

    click_category_loc = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a')

    category_name_loc = (By.NAME, 'category.title')

    parent_category_loc = (By.NAME, 'category.pid')

    slug_loc = (By.NAME, 'category.slug')

    add_btn_loc = (By.XPATH, '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button')

    def click_article(self):
        self.click(*self.click_article_loc)
        sleep(1)

    def click_category(self):
        self.click(*self.click_category_loc)

    def input_category_name(self, name):
        self.type_text(name, *self.category_name_loc)

    def select_parent_category(self, parent_name):
        parent_category_elem = self.find_element(*self.parent_category_loc)
        Select(parent_category_elem).select_by_visible_text(parent_name)

    def input_slug(self, slug):
        self.type_text(slug, *self.slug_loc)

    def click_add_btn(self):
        self.click(*self.add_btn_loc)
