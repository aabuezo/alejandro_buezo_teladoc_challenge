from selenium.webdriver.support.select import Select
from locators.add_user_modal_frame_locators import AddUserModalFrameLocators
from page_objects.base_page import BasePage


class AddUserModalFrame(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def title(self):
        return self.find_element(*AddUserModalFrameLocators.MODAL_TITLE).text

    def modal_frame_is_present(self):
        return self.driver.find_element(*AddUserModalFrameLocators.MODAL_FRAME).is_present()

    def first_name(self, field):
        return self.driver.find_element(*AddUserModalFrameLocators.INPUTS[field])

    @property
    def optionA(self):
        return self.driver.find_element(*AddUserModalFrameLocators.INPUT_OPTION_AAA)

    @property
    def optionB(self):
        return self.driver.find_element(*AddUserModalFrameLocators.INPUT_OPTION_BBB)

    def select(self):
        return Select(self.driver.find_element(*AddUserModalFrameLocators.SELECT_ROLE))

    @property
    def save_button(self):
        return self.driver.find_element(*AddUserModalFrameLocators.SAVE_BUTTON)

