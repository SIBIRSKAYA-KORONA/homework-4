from base_classes.page import Page
from components.login_form import LoginForm


class LoginPage(Page):
    PATH = 'login'

    @property
    def login_form(self):
        return LoginForm(self.driver)

    def login(self, login, password):
        self.login_form.set_login(login)
        self.login_form.set_password(password)
        self.login_form.submit()
