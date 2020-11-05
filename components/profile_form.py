from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class ProfileForm(Component):
    CONTAINER = '//div[@class="profile"]'

    NAME = '//input[@id="inputName"]'
    NAME_ERROR = '//div[@id="inputNameError"]'
    SURNAME = '//input[@id="inputSurname"]'
    SURNAME_ERROR = '//div[@id="inputSurnameError"]'
    SUBMIT_ABOUT = '//div[@id="submitAbout"]'

    AVATAR_LINK = '//img[@class="profile-settings__avatar--round"]'
    AVATAR_ERROR = '//div[@id="inputNameError"]'
    SUBMIT_AVATAR = '//input[@id="avatarInput"]'

    OLD_PASSWORD = '//input[@id="inputOldPassword"]'
    OLD_PASSWORD_ERROR = '//div[@id="inputOldPasswordError"]'
    NEW_PASSWORD = '//input[@id="inputPassword"]'
    NEW_PASSWORD_REPEAT = '//input[@id="inputPasswordRepeat"]'
    NEW_PASSWORD_ERROR = '//div[@id="inputPasswordError"]'
    SUBMIT_PASSWORD = '//div[@id="submitPasswords"]'

    EMAIL = '//input[@id="inputEmail"]'
    EMAIL_ERROR = '//div[@id="inputEmailError"]'
    SUBMIT_EMAIL = '//div[@id="submitEmail"]'

    def set_name(self, name: str):
        self.driver.find_element_by_xpath(self.NAME).clear()
        self.driver.find_element_by_xpath(self.NAME).send_keys(name)

    def set_surname(self, surname: str):
        self.driver.find_element_by_xpath(self.SURNAME).clear()
        self.driver.find_element_by_xpath(self.SURNAME).send_keys(surname)

    def set_avatar(self, path_to_avatar: str):
        self.driver.find_element_by_xpath(self.SUBMIT_AVATAR).send_keys(path_to_avatar)

    def set_old_password(self, old_password: str):
        self.driver.find_element_by_xpath(self.OLD_PASSWORD).send_keys(old_password)

    def set_new_password(self, new_password: str):
        self.driver.find_element_by_xpath(self.NEW_PASSWORD).send_keys(new_password)

    def set_new_password_repeat(self, new_password_repeat: str):
        self.driver.find_element_by_xpath(self.NEW_PASSWORD_REPEAT).send_keys(new_password_repeat)

    def set_email(self, email: str):
        self.driver.find_element_by_xpath(self.EMAIL).clear()
        self.driver.find_element_by_xpath(self.EMAIL).send_keys(email)

    def get_name(self):
        return self.driver.find_element_by_xpath(self.NAME).get_attribute('value')

    def get_surname(self):
        return self.driver.find_element_by_xpath(self.SURNAME).get_attribute('value')

    def get_avatar_link(self):
        return self.driver.find_element_by_xpath(self.AVATAR_LINK).get_attribute('src')

    def get_email(self):
        return self.driver.find_element_by_xpath(self.EMAIL).get_attribute('value')

    def is_invalid_name(self):
        try:
            return WebDriverWait(self.driver, 2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]).until(
                lambda d: len(d.find_element_by_xpath(self.NAME_ERROR).text) != 0
            )
        except TimeoutException:
            return False

    def is_invalid_surname(self):
        try:
            return WebDriverWait(self.driver, 2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]).until(
                lambda d: len(d.find_element_by_xpath(self.SURNAME_ERROR).text) != 0
            )
        except TimeoutException:
            return False

    def is_invalid_avatar(self):
        try:
            return WebDriverWait(self.driver, 3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]).until(
                lambda d: len(d.find_element_by_xpath(self.AVATAR_ERROR).text) != 0
            )
        except TimeoutException:
            return False

    def is_invalid_old_password(self):
        try:
            return WebDriverWait(self.driver, 3).until(
                lambda d: len(d.find_element_by_xpath(self.OLD_PASSWORD_ERROR).text) != 0
            )
        except TimeoutException:
            return False

    def is_invalid_new_password(self):
        try:
            return WebDriverWait(self.driver, 2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]).until(
                lambda d: len(d.find_element_by_xpath(self.NEW_PASSWORD_ERROR).text) != 0
            )
        except TimeoutException:
            return False

    def is_invalid_email(self):
        try:
            return WebDriverWait(self.driver, 2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]).until(
                lambda d: len(d.find_element_by_xpath(self.EMAIL_ERROR).text) != 0
            )
        except TimeoutException:
            return False

    def submit_about(self):
        self.driver.find_element_by_xpath(self.SUBMIT_ABOUT).click()

    def submit_password(self):
        self.driver.find_element_by_xpath(self.SUBMIT_PASSWORD).click()

    def submit_email(self):
        self.driver.find_element_by_xpath(self.SUBMIT_EMAIL).click()
