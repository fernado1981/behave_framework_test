from web_source.web_factory import get_web

def before_scenario(context, test):
    web = get_web("chrome")
    context.web = web


def after_scenario(context, test):
    context.web.close()

