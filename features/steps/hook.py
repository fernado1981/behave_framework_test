from behave import given, when

from page_objects.orangehrm.home_orange_hrm import HomeOrangeHrm


@given('the user is on the search page "{page}"')
def user_on_search_page(context, page):
    if page == "orangehrmlive":
        context.web.open('http://opensource-demo.orangehrmlive.com/')
    if page == "blazedemo":
        context.web.open("http://blazedemo.com/")


@when('Click on login button')
def submit_login_form(context):
    submit = HomeOrangeHrm()
    submit.submit_bottom(context)
