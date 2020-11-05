import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class ProfilePageTest(unittest.TestCase):
    profile_page = None

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

        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_change_name_success(self):
        old_name = self.profile_page.profile_form.get_name()
        new_name = old_name + 'a'

        self.profile_page.change_name(new_name)

        self.assertEqual(new_name, self.profile_page.profile_form.get_name())

        self.profile_page.change_name(old_name)

    def test_change_invalid_name(self):
        name = 'a'

        is_change = self.profile_page.change_name(name)

        self.assertTrue(not is_change)

    def test_change_surname_success(self):
        old_surname = self.profile_page.profile_form.get_surname()
        new_surname = old_surname + 'a'

        self.profile_page.change_surname(new_surname)

        self.assertEqual(new_surname, self.profile_page.profile_form.get_surname())

        self.profile_page.change_surname(old_surname)

    def test_change_invalid_surname(self):
        surname = 'a'

        is_change = self.profile_page.change_surname(surname)

        self.assertTrue(not is_change)

    def test_change_avatar_success(self):
        old_link = self.profile_page.profile_form.get_avatar_link()

        self.profile_page.change_avatar(os.path.abspath('../files/ava1.jpg'))
        new_link = self.profile_page.profile_form.get_avatar_link()

        self.assertNotEqual(old_link, new_link)

        self.profile_page.change_avatar(os.path.abspath('../files/ava2.jpg'))

    def test_change_invalid_format_avatar(self):
        old_link = self.profile_page.profile_form.get_avatar_link()

        self.profile_page.change_avatar(os.path.abspath('../files/1.txt'))
        new_link = self.profile_page.profile_form.get_avatar_link()

    def test_change_invalid_size_avatar(self):
        old_link = self.profile_page.profile_form.get_avatar_link()

        self.profile_page.change_avatar(os.path.abspath('../files/ava_big.jpg'))
        new_link = self.profile_page.profile_form.get_avatar_link()

        self.assertEqual(old_link, new_link)

    def test_change_password_success(self):
        old_password = os.environ.get('PASSWORD')
        new_password = old_password + '1'

        is_changed = self.profile_page.change_password(old_password, new_password, new_password)

        self.assertTrue(is_changed)

        self.profile_page.change_password(new_password, old_password, old_password)

    def test_change_invalid_old_password(self):
        old_password = '1'
        new_password = str(time.time())

        is_changed = self.profile_page.change_password(old_password, new_password, new_password)

        self.assertTrue(not is_changed)

    def test_change_invalid_new_password(self):
        old_password = os.environ.get('PASSWORD')
        new_password = '1'

        is_changed = self.profile_page.change_password(old_password, new_password, new_password)

        self.assertTrue(not is_changed)

    def test_change_invalid_repeat_password(self):
        old_password = os.environ.get('PASSWORD')
        new_password = old_password + '1'
        new_password2 = old_password + '2'

        is_changed = self.profile_page.change_password(old_password, new_password, new_password2)

        self.assertTrue(not is_changed)

    def test_change_email_success(self):
        old_email = self.profile_page.profile_form.get_email()
        empty_old_email = len(old_email) == 0
        new_email = 'timofey.razumov@corp.mail.ru' if empty_old_email else old_email + 'm'

        self.profile_page.change_email(new_email)

        self.assertEqual(new_email, self.profile_page.profile_form.get_email())

        if not empty_old_email:
            self.profile_page.change_email(old_email)

    def test_change_email_fail(self):
        email = 'a'

        is_change = self.profile_page.change_email(email)

        self.assertTrue(not is_change)
