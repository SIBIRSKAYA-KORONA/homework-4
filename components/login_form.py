from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class LoginForm(Component):
    FORM = '//div[@class="auth-form-login"]'
    
    LOGIN = '//input[@id="inputLogin"]'
    PASSWORD = '//input[@id="inputPassword"]'
    SUBMIT = '//div[@id="submit_button"]'
    JOIN_BUTTON = '//a[text()="Регистрация"]'
    INPUT_ERROR = '//div[@id="inputError"]'

    def set_login(self, login: str):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password: str):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url != 'drello.works')

    def open_join(self):
        self.driver.find_element_by_xpath(self.JOIN_BUTTON).click()   

    def check_invalid_login(self):
        return WebDriverWait(self.driver, 0.5, 0.1).until(
            lambda d: len(d.find_element_by_xpath(self.INPUT_ERROR).text) != 0
        )
