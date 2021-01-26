from behave import given, when, then, When

from page_object.telefonica.locator import locator
from page_object.telefonica.telefonica_accionistas import telefonica_accionistas
from page_object.telefonica.telefonica_home import telefonica_home

home = telefonica_home()
accionistas = telefonica_accionistas()
data = locator.data_locator_telefonica_accionistas

@When('the user is in "telefonica.com" home page')
def step_impl(context):
    home.title_page(context)

@When('the user accept the cookies')
def step_impl(context):
    home.cookies(context)


@when('the user selects "Acciones e inversores" tab nav')
def step_impl(context):
    home.select_accionistas_tab(context)


@then('the user is in "shareholders-investors"  page')
def step_impl(context):
    url = accionistas.url_accionistas(context)
    assert (url == data['url'])
