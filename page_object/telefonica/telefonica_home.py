from page_object.telefonica.locator import locator

class telefonica_home(locator):

    def __init__(self):
        self.data=locator.data_locator_telefonica_home

    def title_page(self,context):
        title=context.web.title()
        assert(title == 'Telefónica')

    def cookies(self,context):
        context.web.find_by_xpath(self.data['accept_cookies']).click()

    def select_accionistas_tab(self,context):
        context.web.find_by_xpath(self.data['Accionistas']).click()