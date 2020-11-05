import os
import unittest
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from components.boards.board_templates import BoardTemplates
from pages.board_page import BoardPage
from pages.boards_page import BoardsPage
from pages.login_page import LoginPage


class BoardsPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        self.login_page = LoginPage(self.driver)
        self.login_page.open()

        login = os.environ.get('LOGIN')
        password = os.environ.get('PASSWORD')
        self.login_page.login(login, password)

        self.boards_page = BoardsPage(self.driver)
        self.boards_page.wait_for_container()

    def tearDown(self):
        self.driver.quit()

    def test_board_create_success(self):
        board_name = f'test_board_create_success{str(time.time())}'

        self.boards_page.create_board(board_name)

        board_page = BoardPage(self.driver)
        board_page.wait_for_container()
        self.assertEqual(board_name, board_page.header.get_board_title())

        board_page.header.open_settings()
        board_page.settings_popup.delete_board()

    def test_board_create_cancel(self):
        board_name = f'test_board_create_cancel{str(time.time())}'

        create_board_form = self.boards_page.create_board_form
        create_board_form.open()
        create_board_form.set_board_title(board_name)
        create_board_form.close()

        try:
            board = self.boards_page.boards_list.get_board(board_name)
        except TimeoutException:
            board = None

        self.assertIsNone(board)

    def test_create_template_week_plan_board(self):
        board_templates = BoardTemplates(self.driver)
        board_templates.create_week_plan_board()

        board_page = BoardPage(self.driver)
        board_page.wait_for_container()
        self.assertEqual(board_templates.WEEK_PLAN_BOARD_NAME, board_page.header.get_board_title())

        board_page.header.open_settings()
        board_page.settings_popup.delete_board()

    def test_create_template_management_board(self):
        board_templates = BoardTemplates(self.driver)
        board_templates.create_project_management_board()

        board_page = BoardPage(self.driver)
        board_page.wait_for_container()
        self.assertEqual(board_templates.PROJECT_MANAGEMENT_BOARD_NAME, board_page.header.get_board_title())

        board_page.header.open_settings()
        board_page.settings_popup.delete_board()

    def test_open_board(self):
        board_name = f'test_open_board_{str(time.time())}'
        self.boards_page.create_board(board_name)

        board_page = BoardPage(self.driver)
        board_page.wait_for_container()

        self.boards_page.open()
        self.boards_page.boards_list.open_board(board_name)

        board_page.wait_for_container()
        self.assertEqual(board_name, board_page.header.get_board_title())

        board_page.header.open_settings()
        board_page.settings_popup.delete_board()
