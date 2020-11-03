from base_classes.page import Page
from components.profile_form import ProfileForm


class ProfilePage(Page):
    PATH = 'profile'

    @property
    def profile_form(self):
        return ProfileForm()
