import pickle
import random
import string
import time
import ddddocr
from PIL import Image
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_logger():
    import logging
    import logging.handlers
    import datetime

    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger


def get_code(driver, id):
    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    picture_name1 = path + '\\' + str(t) + '.png'

    driver.save_screenshot(picture_name1)

    ce = driver.find_element_by_id(id)

    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    dpr = driver.execute_script('return window.devicePixelRatio')

    print(dpr)
    im = Image.open(picture_name1)
    img = im.crop((left*dpr, top*dpr, right*dpr, height*dpr))

    t = time.time()

    picture_name2 = path + '\\' + str(t) + '.png'
    img.save(picture_name2)
    ocr = ddddocr.DdddOcr()
    with open(picture_name2, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res


def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)


def login(driver):
    username = 'zhaozexin'
    pwd = '123456'

    driver.find_element(By.NAME, 'user').clear()
    driver.find_element(By.NAME, 'user').send_keys(username)
    driver.find_element(By.NAME, 'pwd').clear()
    driver.find_element(By.NAME, 'pwd').send_keys(pwd)
    driver.find_element(By.CLASS_NAME, 'btn').click()
