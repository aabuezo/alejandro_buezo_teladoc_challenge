from behave import *
from page_objects.add_user_modal_frame import AddUserModalFrame

use_step_matcher('re')


@given('I am in users table page')
def step_impl(context):
    page = AddUserModalFrame(context.driver)
    context.driver.get(page.url)
    actual_url = context.driver.current_url
    assert actual_url == page.url
