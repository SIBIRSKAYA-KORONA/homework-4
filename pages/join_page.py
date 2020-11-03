from base_classes.page import Page
from components.join_form import JoinForm


class JoinPage(Page):
    PATH = 'join'

    @property
    def join_form(self):
        return JoinForm(self.driver)
