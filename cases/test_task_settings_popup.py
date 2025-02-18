import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.board_page import BoardPage
from pages.boards_page import BoardsPage
from pages.login_page import LoginPage

from components.task.task_settings_popup import TaskSettingsPopup


class TaskSettingsPopupTest(unittest.TestCase):
    BOARD_TITLE = 'TEST BOARD NAME'
    COLUMN_TITLE = 'TEST COLUMN'
    TASK_TITLE = 'TEST_TASK'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(3)

        self.login_page = LoginPage(self.driver)
        self.login_page.open()

        login = os.environ.get('LOGIN')
        password = os.environ.get('PASSWORD')
        self.login_page.login(login, password)

        self.boards_page = BoardsPage(self.driver)
        self.boards_page.wait_for_container()
        self.boards_page.create_board(self.BOARD_TITLE)

        self.board_page = BoardPage(self.driver)
        self.board_page.wait_for_container()

        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        self.column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)
        self.column.task_list.create_task(self.TASK_TITLE)
        task = self.column.task_list.get_task_by_title(self.TASK_TITLE)
        task.open_settings()

        self.popup = TaskSettingsPopup(self.driver)
        self.popup.wait_for_container()

    def tearDown(self):
        self.boards_page.open()
        self.boards_page.wait_for_container()
        self.boards_page.boards_list.open_board(self.BOARD_TITLE)
        self.board_page.wait_for_container()

        self.board_page.header.open_settings()
        self.board_page.settings_popup.delete_board()
        self.boards_page.wait_for_container()

        self.driver.quit()

    def test_rename_task(self):
        new_name = "Your new name"
        self.popup.rename_task(new_name)

        self.driver.refresh()
        self.popup.wait_for_container()

        self.assertEqual(self.popup.get_task_name(), new_name)

    def test_change_task_description(self):
        description = "Your new description"
        self.popup.change_description(description)

        self.assertEqual(self.popup.get_task_description(), description)

    def test_create_new_label_for_board(self):
        label_name = 'Super-super label'
        self.popup.click_add_new_label_button()
        self.popup.create_new_label_with_name(label_name)
        self.popup.close_add_labels_popup()
        self.driver.refresh()
        self.popup.wait_for_container()
        label_exist = self.popup.is_label_with_provided_name_exist(label_name)
        self.assertTrue(label_exist)

    def test_add_label_to_task(self):
        label_name = 'Super-super label'
        self.popup.click_add_new_label_button()
        self.popup.create_new_label_with_name(label_name)
        self.popup.close_add_labels_popup()
        self.driver.refresh()
        self.popup.wait_for_container()

        label_exist = self.popup.is_label_with_provided_name_exist(label_name)
        self.assertTrue(label_exist)
        self.popup.add_label_with_name_to_task(label_name)
        label_binded = self.popup.is_label_with_provided_name_bind_to_task(label_name)
        self.assertTrue(label_binded)

    def test_delete_task(self):
        self.popup.delete_task()
        self.assertIsNone(self.column.task_list.get_task_by_title(self.TASK_TITLE))

    def test_create_checklist(self):
        checklist_name = 'New checklist'
        self.popup.create_new_checklist_with_name(checklist_name)
        self.assertTrue(self.popup.is_checklist_with_provided_name_exist(checklist_name))

    def test_delete_checklist(self):
        checklist_name = 'New checklist'
        self.popup.create_new_checklist_with_name(checklist_name)
        self.popup.delete_checklist_with_name(checklist_name)
        self.driver.refresh()
        self.popup.wait_for_container()
        self.assertFalse(self.popup.is_checklist_with_provided_name_exist(checklist_name))

    def test_create_comment(self):
        comment_text = 'New comment text'
        self.popup.create_comment_with_text(comment_text)

        self.assertTrue(self.popup.is_comment_with_provided_text_exist(comment_text))

    def test_delete_comment(self):
        comment_text = 'New comment text'
        self.popup.create_comment_with_text(comment_text)
        self.popup.delete_comment()

        self.assertFalse(self.popup.is_comment_with_provided_text_exist(comment_text))

    def test_add_item_to_checklist(self):
        checklist_name = 'New checklist'
        self.popup.create_new_checklist_with_name(checklist_name)
        item_text = 'New text'
        self.popup.add_item_into_checklist(item_text)
        self.assertTrue(self.popup.is_checklist_item_with_provided_text_exist(item_text))

    def test_mark_item_in_checklist(self):
        checklist_name = 'New checklist'
        self.popup.create_new_checklist_with_name(checklist_name)
        item_text = 'New text'
        self.popup.add_item_into_checklist(item_text)
        self.popup.click_on_item_checkbox()

        self.assertTrue(self.popup.is_item_in_checklist_marked())
