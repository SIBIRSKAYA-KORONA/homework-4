import urllib.parse

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from components.main_header import MainHeader
from components.notifications_form import Notifications


class Page(object):
    PROTOCOL = 'https://'
    BASE_URL = 'drello.works/'
    PATH = ''

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.main_header = MainHeader(driver)
        self.notifications = Notifications(driver)

    @property
    def location(self):
        return urllib.parse.urljoin(self.PROTOCOL + self.BASE_URL, self.PATH)

    @property
    def url(self):
        return urllib.parse.urljoin(self.BASE_URL, self.PATH)

    def open(self):
        self.driver.get(self.location)
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != self.url)
        self.driver.maximize_window()
