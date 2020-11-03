from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class Component(object):
    CONTAINER = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def is_open(self):
        if self.CONTAINER is None:
            raise NotImplementedError('CONTAINER is None')

        try:
            WebDriverWait(self.driver, 3, 0.1).until(
                lambda d: d.find_element_by_xpath(self.CONTAINER))
        except TimeoutException:
            return False
        return True

    def wait_for_container(self):
        if self.CONTAINER is None:
            raise NotImplementedError('CONTAINER is None')

        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CONTAINER)
        )
