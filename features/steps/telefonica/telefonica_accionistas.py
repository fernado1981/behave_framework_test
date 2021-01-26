from behave import when, then, When

from page_object.telefonica.telefonica_accionistas import telefonica_accionistas

accionistas = telefonica_accionistas()

@When('the user is in EurolandTool')
def step_impl(context):
    accionistas.telefonica_en_bolsa(context)


@When('the user tap Nyse tab')
def step_impl(context):
    accionistas.tap_click_nyse(context)


@then('the user get the NY value')
def step_impl(context):
    valor = accionistas.get_value_ny(context)
    assert valor.text is not None
