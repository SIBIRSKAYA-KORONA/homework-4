from base_classes.component import Component


class Notifications(Component):
    CONTAINER = '//div[@class = "header-notifications"]'

    def is_visible(self):
        return self.driver.find_element_by_xpath(self.CONTAINER).is_displayed()
