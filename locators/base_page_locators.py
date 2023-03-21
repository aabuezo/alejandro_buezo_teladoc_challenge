from selenium.webdriver.common.by import By


class BasePageLocators:

    ADD_USER_BUTTON = By.XPATH, "//button[@type='add']"
    TABLE_ROWS = By.CSS_SELECTOR, ".smart-table-data-row.ng-scope"
