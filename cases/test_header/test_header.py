import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage
from pages.boards_page import BoardsPage
from pages.profile_page import ProfilePage
from pages.join_page import JoinPage


class HeaderTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))

    def tearDown(self):
        self.driver.quit()

    def test_open_profile(self):
        BoardsPage(self.driver).main_header.open_profile()

    def test_open_notifications(self):
        boards_page = BoardsPage(self.driver)
        boards_page.main_header.open_notifications()

        self.assertTrue(boards_page.notifications.is_visible())

    def test_logout(self):
        BoardsPage(self.driver).main_header.logout()

    def test_open_boards(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()
        profile_page.main_header.open_boards()
