from selenium.webdriver.common.by import By


class BackdropModalFrameLocators:

    BACKDROP = By.CLASS_NAME, ".modal-backdrop"
    BACKDROP_TITLE = By.XPATH, "//h3[@class='ng-binding']"
    BACKDROP_CANCEL_BUTTON = By.XPATH, "//button[text()='Cancel']"
    BACKDROP_OK_BUTTON = By.XPATH, "//button[text()='OK']"
