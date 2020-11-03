from base_classes.page import Page


class ProfilePage(Page):
    PATH = 'profile'

    @property
    def profile_form(self):
        return LoginForm(self.driver)
