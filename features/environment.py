# features/environment.py
from selenium import webdriver


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome(options=options)


def after_all(context):
    # cleanup after tests run
    context.driver.close()
