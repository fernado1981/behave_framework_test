from page_objects.orangehrm.locators_orange_hrm import LocatorsHomeOrangeHrm


class DashboardOrangeHrm(LocatorsHomeOrangeHrm):

    def __init__(self):
        self.locators = self.locators_dashboard

    def dashboard_header(self, context):
        text = context.web.get_text_xpath(self.locators["xpath_dashboard_header"])
        if text == self.locators["Dashboard_header_name"]:
            return True
        return False
