from selenium.webdriver.common.by import By


class AddUserModalFrameLocators:

    MODAL_TITLE = By.TAG_NAME, "h3"
    MODAL_FRAME = By.CSS_SELECTOR, ".modal.ng-scope"
    INPUTS = {
        "First Name": (By.XPATH, "//input[@name='FirstName']"),
        "Last Name": (By.XPATH, "//input[@name='LastName']"),
        "User Name": (By.XPATH, "//input[@name='UserName']"),
        "Password": (By.XPATH, "//input[@name='Password']"),
        "Email": (By.XPATH, "//input[@name='Email']"),
        "Cell Phone": (By.XPATH, "//input[@name='Mobilephone']")
    }
    INPUT_OPTION_AAA = By.XPATH, "//input[@value='15']"
    INPUT_OPTION_BBB = By.XPATH, "//input[@value='16']"
    SELECT_ROLE = By.XPATH, "//select[@name='RoleId']"
    BUTTON_SAVE = By.CLASS_NAME, ".btn.btn.btn-success"
    BUTTON_CLOSE = By.CLASS_NAME, ".btn.btn-danger"
