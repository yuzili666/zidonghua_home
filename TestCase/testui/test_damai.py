import os
import time
from selenium import webdriver
from Common.baseui import baseUI

URL = "https://www.damai.cn/"# PC页面

USERNAME = '18556359869'
PASSWORD = 'Yzl1033843829'


class TestDamai():

    def test_start(self):
        # 打开浏览器
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")
        # 打开浏览器
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.set_page_load_timeout(15)  # 网页加载超时为10s
        driver.set_script_timeout(10)  # js脚本运行超时10s
        driver.implicitly_wait(10)  # 元素查找超时时间10s

        base = baseUI(driver)
        # 打开网址
        driver.get(URL)
        login = driver.find_element_by_xpath("//span[text()='登录']")
        login.click()
        time.sleep(4)

        username = driver.find_element_by_xpath("//input[@placeholder='请输入手机号或邮箱']")
        username.send_keys(USERNAME)
        password = driver.find_element_by_xpath("//input[@aria-label='请输入登录密码']")
        password.send_keys(PASSWORD)
        time.sleep(4)
        driver.quit()


