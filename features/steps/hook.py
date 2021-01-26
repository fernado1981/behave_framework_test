from behave import given, when

from page_object.orangehrm.home_orange_hrm import HomeOrangeHrm
from page_object.telefonica.google_telefonica import google_telefonica

bing = google_telefonica()

@given('the user is on the search page "{page}"')
def user_on_search_page(context, page):
    if page == "orangehrmlive":
        context.web.open('http://opensource-demo.orangehrmlive.com/')
        context.web.maximize()
    if page == "blazedemo":
        context.web.open("http://blazedemo.com/")
        context.web.maximize()
    if page == 'google':
        context.web.open("https://www.bing.com/?setlang=es")
        context.web.maximize()
        bing.accept_cookies(context)


@when('Click on login button')
def submit_login_form(context):
    submit = HomeOrangeHrm()
    submit.submit_bottom(context)
