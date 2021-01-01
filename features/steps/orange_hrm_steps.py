from behave import when, then

from page_objects.orangehrm.home_orange_hrm import HomeOrangeHrm
from page_objects.orangehrm.dashboard_orange_hrm import DashboardOrangeHrm

global HOME


@when('the user verify the title page "{titlepage}"')
def title_page(context, titlepage):
    title = context.web.get_title()
    assert title == titlepage


@then('verify that the logo present on page')
def verify_logo(context):
    home = HomeOrangeHrm()
    result = home.view_logo(context)
    assert result is True


# Login
@when('Enter username "{user}" and password "{pwd}"')
def login(context, user, pwd):
    home = HomeOrangeHrm()
    result = home.simple_login_home(context, user, pwd)
    assert result is True


# login table with header
@when('put username "{name}" and password "{pwd}"')
def login_table(context, name, pwd):
    home = HomeOrangeHrm()
    result = home.table_login_home(context, name, pwd)
    assert result is True


# login outline valid
@when('insert username "{user}" and password "{pwd}"')
def login_outline(context, user, pwd):
    home = HomeOrangeHrm()
    result = home.example_login_home(context, user, pwd)
    assert result is True


# finish valid login
@then('User must succesfully login to the Dashboard page')
def dashboard(context):
    home = DashboardOrangeHrm()
    dashboard_head = home.dashboard_header(context)
    assert dashboard_head is True


# finish invalid login
@then('User must unsuccesfully login to the Dashboard page')
def login_error(context):
    home = HomeOrangeHrm()
    result = home.invalid_login(context)
    assert result is True
