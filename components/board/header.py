from base_classes.component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Header(Component):
    BOARD_TITLE = '//div[@class="board-header-left__title"]'
    BOARD_SETTINGS_BUTTON = '//div[contains(@class, "js-openBoardSettings")]'
    ADD_MEMBERS_BUTTON = '//img[contains(@class, "js-addNewUser")]'

    def check_title(self, title):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element_by_xpath(self.BOARD_TITLE).text == title
            )
        except TimeoutException:
            return False
        return True

    def get_board_title(self):
        return self.driver.find_element_by_xpath(self.BOARD_TITLE).text

    def open_settings(self):
        self.driver.find_element_by_xpath(self.BOARD_SETTINGS_BUTTON).click()

    def open_add_members(self):
        self.driver.find_element_by_xpath(self.ADD_MEMBERS_BUTTON).click()
