import time

from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.add_user_modal_frame_locators import AddUserModalFrameLocators
from page_objects.add_user_modal_frame import AddUserModalFrame
from page_objects.base_page import BasePage

use_step_matcher('re')


@given('I am in users table page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = AddUserModalFrame(context.driver)
    context.driver.get(page.url)
    actual_url = context.driver.current_url
    assert actual_url == page.url


@when('I click the Add User button')
def step_impl(context):
    page = BasePage(context.driver)
    page.button.click()


@step('I wait for the Add User modal frame to load')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(AddUserModalFrameLocators.MODAL_TITLE)
    )


@then('The modal frame title is "(.*)"')
def step_impl(context, title):
    page = AddUserModalFrame(context.driver)
    assert page.title == title


@given('I am in Add User modal frame')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = AddUserModalFrame(context.driver)
    context.driver.get(page.url)
    page.button.click()
    assert page.modal_frame_is_present


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, name, field):
    page = AddUserModalFrame(context.driver)
    page.first_name(field).send_keys(name)


@step('I select "(.*)" option as Customer')
def step_impl(context, customer):
    page = AddUserModalFrame(context.driver)
    if customer == "Company AAA":
        page.optionA.click()
    else:
        page.optionB.click()
    time.sleep(5)


@step('I select "(.*)" option as Role')
def step_impl(context, role):
    pass


@then('The Save button is enabled')
def step_impl(context):
    pass


@when('I click the Save button')
def step_impl(context):
    pass


@then('Add User modal div closes and returns to table page')
def step_impl(context):
    pass


@step('User "(.*)" is added to the table')
def step_impl(context, user):
    pass

