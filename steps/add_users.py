from behave import *

use_step_matcher('re')


@given('I am in users table page')
def step_impl(context):
    pass


@when('I click "(.*)" button')
def step_impl(context, button):
    pass


@then('Add User modal div shows up')
def step_impl(context):
    pass


@step('The title is "(.*)"')
def step_impl(context, title):
    pass


@given('I am in Add User modal div')
def step_impl(context):
    pass


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, name, field):
    pass


@step('I select "(.*)" option as Customer')
def step_impl(context, customer):
    pass


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

