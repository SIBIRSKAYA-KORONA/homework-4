from base_classes.page import Page


class BoardsPage(Page):
    PATH = 'boards'

    @property
    def boards_form(self):
        return LoginForm(self.driver)
