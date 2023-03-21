from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.add_user_modal_frame_locators import AddUserModalFrameLocators
from page_objects.add_user_modal_frame import AddUserModalFrame
from page_objects.base_page import BasePage

use_step_matcher('re')


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


@step('I select "(.*)" option as Role')
def step_impl(context, role):
    page = AddUserModalFrame(context.driver)
    dropdown = page.select()
    dropdown.select_by_visible_text(role)


@then('The Save button is enabled')
def step_impl(context):
    page = AddUserModalFrame(context.driver)
    assert page.save_button.is_enabled()


@when('I click the Save button')
def step_impl(context):
    page = AddUserModalFrame(context.driver)
    page.save_button.click()


@then('Add User modal div closes and returns to table page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.button.is_displayed()


@step('User "(.*)" is added to the table')
def step_impl(context, user):
    page = BasePage(context.driver)
    log = BasePage.get_logger()
    rows = page.get_table_rows()
    users = []
    for row in rows:
        user_row = row.text.split(" ")
        first_name = user_row[0]
        log.info(first_name)
        users.append(first_name.strip())
    log.info(user)
    log.info(users)
    assert user in users
