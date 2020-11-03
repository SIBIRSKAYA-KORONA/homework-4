from base_classes.component import Component


class ProfileForm(Component):
    CONTAINER = '//div[@class = "profile"]'

    def is_visible(self):
        return self.driver.find_element_by_xpath(self.CONTAINER).is_displayed()
