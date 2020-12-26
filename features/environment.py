from behave.fixture import use_fixture_by_tag
from allure_behave.hooks import allure_report
from web.factory import get_web

allure_report("%allure_result_folder%")


def before_scenario(context, test):
    web = get_web(context.config.userdata['browser'])
    context.web = web


def after_scenario(context, test):
    context.web.close()
