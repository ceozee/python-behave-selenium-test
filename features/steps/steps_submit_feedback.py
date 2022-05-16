from behave import given, when, then, step
from assertpy import assert_that
from features.pages.home_page import HomePage
from features.pages.contact_page import ContactPage


@given('user opens browser and is in home page')
def step_impl(context):
    page = HomePage(context)
    page.visit_home_page()


@given('customer access contact page')
def step_impl(context):
    page = HomePage(context)
    page.click_contact_page()


@when('following fields are entered')
def step_impl(context):
    page = ContactPage(context)
    for row in context.table: page.fill_fields(row['Field'], row['Value'])


@when('submit button is clicked')
def step_impl(context):
    page = ContactPage(context)
    page.click_submit()


@when('customer submits feedback form with the following values')
def step_impl(context):
    page = ContactPage(context)
    for row in context.table:
        if row[0] == 'Forename': context.forename = row[1]
        page.fill_fields(row['Field'], row['Value'])

    page.click_submit()


@then('errors will disappear in contact page')
def step_impl(context):
    page = ContactPage(context)
    header_message = page.get_header_message()
    for row in context.error_table:
        error_message_in_field_existence = len(page.check_field_error_exists(row['Field']))
        assert_that(error_message_in_field_existence).described_as('visbility of element').is_zero()
    assert_that(header_message).is_equal_to('We welcome your feedback - tell it how it is.')


@then('it should display that feedback submission is successful')
def step_impl(context):
    page = ContactPage(context)
    page.wait_sending_feedback_to_disappear()
    header_message = page.get_header_successful_message()   
    assert_that(header_message).described_as('validate name')\
        .is_equal_to(f'Thanks {context.forename}, we appreciate your feedback.')


@then('error in the field is displayed')
def step_impl(context):
    page = ContactPage(context)
    context.error_table = context.table
    for row in context.table:
        error_message_provided = row['Message']
        error_message_displayed = page.get_error_message(row['Field'])
        assert_that(error_message_provided).is_equal_to(error_message_displayed)
