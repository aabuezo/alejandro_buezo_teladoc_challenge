from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://www.way2automation.com/angularjs-protractor/webtables/'

    @property
    def button(self):
        return self.find_element(*BasePageLocators.ADD_USER_BUTTON)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    