from page_object.telefonica.locator import locator

class telefonica_accionistas(locator):

    def __init__(self):
        self.data=locator.data_locator_telefonica_accionistas

    def url_accionistas(self, context):
        return context.web.curent_url()

    def telefonica_en_bolsa(self,context):
        frame = context.web.find_by_class_name(self.data['iframe_euroland_class'])
        context.web.switch_frame(frame)

    def tap_click_nyse(self,context):
        context.web.find_by_xpath(self.data['Nyse']).click()

    def get_value_ny(self,context):
        for text in context.web.finds_by_css_selector(self.data['valNy']):
            return text