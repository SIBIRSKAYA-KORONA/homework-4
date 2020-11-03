from selenium.webdriver.support.ui import WebDriverWait
from base_classes.component import Component


class MainHeader(Component):
    NICKNAME = '//div[@class="main-header-right__nickname"]'
    BOARDS_BUTTON = '//div[@id="submitBoards"]'
    PROFILE_BUTTON = '//img[@id="submitSettings"]'
    NOTIFICATIONS_BUTTON = '//div[contains(@class, "js-notifications")]'
    LOGOUT_BUTTON = '//div[@id="submitLogout"]'

    def get_nickname(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NICKNAME).text.replace('@', '', 1)
        )

    def open_profile(self):
        self.driver.find_element_by_xpath(self.PROFILE_BUTTON).click()
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url != 'drello.works/profile')

    def open_boards(self):
        self.driver.find_element_by_xpath(self.BOARDS_BUTTON).click()
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url != 'drello.works/boards')

    def open_notifications(self):
        self.driver.find_element_by_xpath(self.NOTIFICATIONS_BUTTON).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT_BUTTON).click()
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url != 'drello.works/login')
