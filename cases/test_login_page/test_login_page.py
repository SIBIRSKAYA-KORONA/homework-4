import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage
from pages.join_page import JoinPage
from pages.boards_page import BoardsPage


class LoginPageTest(unittest.TestCase):
    login_page = None

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_success_login(self):
        login = os.environ.get('LOGIN')
        password = os.environ.get('PASSWORD')
        self.login_page.sign_in(login, password)

        nickname = self.login_page.main_header.get_nickname()
        self.assertEqual(login, nickname)

    def test_invalid_login(self):
        login = '123'
        password = '321'
        self.login_page.sign_in(login, password)

        is_visible = self.login_page.login_form.check_invalid_login()
        self.assertTrue(is_visible)

    def test_click_on_join(self):
        self.login_page.login_form.open_join()

        join_form = JoinPage(self.driver).join_form

        self.assertTrue(join_form.is_open)
