from locators.backdrop_modal_frame_locators import BackdropModalFrameLocators
from page_objects.base_page import BasePage


class BackdropModalFrame(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.find_element(*BackdropModalFrameLocators.BACKDROP_TITLE)

    @property
    def button_ok(self):
        return self.driver.find_element(*BackdropModalFrameLocators.BACKDROP_OK_BUTTON)
