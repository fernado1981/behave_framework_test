from behave import given,Then

from page_object.telefonica.google_telefonica import google_telefonica

bing = google_telefonica()

@given('the user select the first option for telefonica')
def step_impl(context):
    bing.input_search_bing(context)
    bing.more_better_remaind(context)
    bing.click_first_option(context)

@Then('the user see telefonica logo')
def step_impl(context):
    bing.find_logo(context)
