class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://www.way2automation.com/angularjs-protractor/webtables/'

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    