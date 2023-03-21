from selenium.webdriver.common.by import By


class AddUserModalFrameLocators:

    MODAL_TITLE = By.TAG_NAME, "h3"
    INPUT_FIRST_NAME = By.XPATH, "//input[@name='FirstName']"  # required
    INPUT_LAST_NAME = By.XPATH, "//input[@name='LastName']"
    INPUT_USERNAME = By.XPATH, "//input[@name='UserName']"
    INPUT_PASSWORD = By.XPATH, "//input[@name='Password']"
    INPUT_OPTION_AAA = By.XPATH, "//input[@value='15']"
    INPUT_OPTION_BBB = By.XPATH, "//input[@value='16']"
    SELECT_ROLE = By.XPATH, "//select[@name='RoleId']"
    INPUT_EMAIL = By.XPATH, "//input[@name='Email']"
    INPUT_MOBILE = By.XPATH, "//input[@name='Mobilephone']"
    BUTTON_SAVE = By.CLASS_NAME, ".btn.btn.btn-success"
    BUTTON_CLOSE = By.CLASS_NAME, ".btn.btn-danger"
