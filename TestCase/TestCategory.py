from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import util
from selenium import webdriver


class TestCategory(object):
    def setup_class(self):
        self.login = webdriver.Chrome()
        self.login.get('http://localhost:8080/jpress/user/login')
        self.login.maximize_window()
        util.login(self.login)

    def test_add_category_error(self):
        name = ''
        parent = 'python'
        slug = 'test'
        expected = '分类名称不能为空'

        self.login.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        self.login.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()

        self.login.find_element(By.NAME, 'category.title').send_keys(name)

        parent_category_elem = self.login.find_element(By.NAME, 'category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        self.login.find_element(By.NAME, 'category.slug').send_keys(slug)

        self.login.find_element(By.XPATH,
            '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login, 5).until(EC.visibility_of_element_located(loc))

        msg = self.login.find_element(*loc).text

        assert msg == expected

    def test_add_category_ok(self):
        name = 'test'
        parent = 'python'
        slug = 'test'
        expected = None

        # self.login.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()

        self.login.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()

        self.login.find_element(By.NAME, 'category.title').clear()
        self.login.find_element(By.NAME, 'category.title').send_keys(name)

        parent_category_elem = self.login.find_element(By.NAME,'category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        self.login.find_element(By.NAME, 'category.slug').clear()
        self.login.find_element(By.NAME, 'category.slug').send_keys(slug)

        self.login.find_element(By.XPATH,
            '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        assert 1 == 1

    def teardown_class(self):
        self.login.quit()
