import inspect
import logging
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

    def get_table_rows(self):
        return self.driver.find_elements(*BasePageLocators.TABLE_ROWS)

    def delete_user(self, index):
        button, selector = BasePageLocators.DEL_USER_BUTTON
        selector = selector + "[" + str(index) + "]"
        self.driver.find_element(button, selector).click()

    @staticmethod
    def get_logger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)
        return logger
