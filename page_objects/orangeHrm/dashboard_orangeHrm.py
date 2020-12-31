from page_objects.orangeHrm.locators_orangeHrm import homeorangeHrm


class dashboard_orangeHrm(homeorangeHrm):

    def __init__(self):
        self.locators = self.locators_dashboard

    def dashboard_header(self, context):
        text = context.web.get_text_xpath(self.locators["xpath_dashboard_header"])
        if text == self.locators["Dashboard_header_name"]:
            return True
        return False
