from behave import *
from page_objects.backdrop_modal_frame import BackdropModalFrame
from page_objects.base_page import BasePage

use_step_matcher('re')


@step('I find user name "(.*)"')
def step_impl(context, user):
    page = BasePage(context.driver)
    log = BasePage.get_logger()
    rows = page.get_table_rows()
    usernames = []
    for row in rows:
        user_row = row.text.split(" ")
        username = user_row[2]
        usernames.append(username.strip())
    log.info(user)
    log.info(usernames)
    assert user in usernames


@when('I click the X to delete the user "(.*)"')
def step_impl(context, user):
    page = BasePage(context.driver)
    log = BasePage.get_logger()
    rows = page.get_table_rows()
    i = 0
    for row in rows:
        i = i + 1
        user_row = row.text.split(" ")
        username = user_row[2]
        if username == user:
            log.info(page.delete_user(i))
            log.info(i)
            break


@then('Confirmation Dialog appears')
def step_impl(context):
    page = BackdropModalFrame(context.driver)
    assert page.title.is_displayed()


@when('I clik OK button to confirm')
def step_impl(context):
    page = BackdropModalFrame(context.driver)
    page.button_ok.click()


@then('The user "(.*)" is deleted')
def step_impl(context, user):
    page = BasePage(context.driver)
    log = BasePage.get_logger()
    rows = page.get_table_rows()
    usernames = []
    for row in rows:
        user_row = row.text.split(" ")
        username = user_row[2]
        usernames.append(username.strip())
    log.info(user)
    log.info(usernames)
    assert user not in usernames
