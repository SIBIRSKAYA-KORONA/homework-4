from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class JoinForm(Component):
    CONTAINER = '//div[@class="auth-form-join"]'

    NAME = '//input[@id="inputName"]'
    SURNAME = '//input[@id="inputSurname"]'
    LOGIN = '//input[@id="inputNickname"]'
    PASSWORD = '//input[@id="inputPassword"]'
    PASSWORD_REPEAT = '//input[@id="inputPasswordRepeat"]'
    SUBMIT = '//div[@id="submit_button"]'
    LOGIN_BUTTON = '//a[text()="Уже с нами?"]'

    def set_name(self, name: str):
        self.driver.find_element_by_xpath(self.NAME).send_keys(name)

    def set_surname(self, surname: str):
        self.driver.find_element_by_xpath(self.SURNAME).send_keys(surname)

    def set_login(self, login: str):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password: str):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def set_password_repeat(self, password_repeat: str):
        self.driver.find_element_by_xpath(self.PASSWORD_REPEAT).send_keys(password_repeat)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != 'drello.works')

    def open_login(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
