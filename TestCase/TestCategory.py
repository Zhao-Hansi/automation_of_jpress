from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCategory(object):
    def __init__(self, login):
        self.login = login

    def test_add_category_error(self):
        name = ''
        parent = 'python'
        slug = 'test'
        expected = '分类名称不能为空'

        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()

        self.login.driver.find_element_by_name('category.title').send_keys(name)

        parent_category_elem = self.login.driver.find_element_by_name('category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        self.login.driver.find_element_by_name('category.slug').send_keys(slug)

        self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected

    def test_add_category_ok(self):
        name = 'test'
        parent = 'python'
        slug = 'test'
        expected = None

        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()

        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()

        self.login.driver.find_element_by_name('category.title').clear()
        self.login.driver.find_element_by_name('category.title').send_keys(name)

        parent_category_elem = self.login.driver.find_element_by_name('category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        self.login.driver.find_element_by_name('category.slug').clear()
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)

        self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        assert 1 == 1

    def teardown_class(self):
        self.login.quit()

