from page_objects.base_page import BasePage


class AddUserModalFrame(BasePage):

    def __init__(self, driver):
        self.driver = driver
