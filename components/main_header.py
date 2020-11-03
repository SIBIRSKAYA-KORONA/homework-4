from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component

from selenium.webdriver.support import expected_conditions as EC


class MainHeader(Component):
    NICKNAME = '//div[@class="main-header-right__nickname"]'
    BOARDS_BUTTON = '//div[@id="submitBoards"]'
    PROFILE_BUTTON = '//div[@id="submitSettings"]'
    NOTIFICATIONS_BUTTON = '//div[@class="js-notifications"]'
    LOGOUT_BUTTON = '//div[@id="submitLogout"]'

    def get_nickname(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NICKNAME).text.replace('@', '', 1)
        )

    def open_profile(self):
        self.driver.find_element_by_xpath(self.PROFILE_BUTTON).click()

    def open_boards(self):
        self.driver.find_element_by_xpath(self.BOARDS_BUTTON).click()

    def open_notifications(self):
        self.driver.find_element_by_xpath(self.NOTIFICATIONS_BUTTON).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT_BUTTON).click()
