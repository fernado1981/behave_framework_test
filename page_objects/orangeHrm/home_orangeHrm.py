from page_objects.orangeHrm.locators_orangeHrm import homeorangeHrm


class home(homeorangeHrm):

    def __init__(self):
        self.locator = self.locators

    def simple_login_home(self, context, user, pwd):
        userName = context.web.find_by_id_displayed(self.locators["id_username"])
        password = context.web.find_by_id_displayed(self.locators["id_password"])
        if userName is True and password is True:
            context.web.find_by_id(self.locators["id_username"]).send_keys(user)
            context.web.find_by_id(self.locators["id_password"]).send_keys(pwd)
            return True
        return False

    def table_login_home(self, context, name, pwd):
        for row in context.table:
            context.temp_name = row['name']
            context.temp_password = row['pwd']
            userName = context.web.find_by_id_displayed(self.locators["id_username"])
            password = context.web.find_by_id_displayed(self.locators["id_password"])
            if userName is True and password is True:
                context.web.find_by_id(self.locators["id_username"]).send_keys(context.temp_name)
                context.web.find_by_id(self.locators["id_password"]).send_keys(context.temp_password)
                return True
            return False

    def example_login_home(self, context, user, pwd):
        context.temp_name = user
        context.temp_password = pwd
        userName = context.web.find_by_id_displayed(self.locators["id_username"])
        password = context.web.find_by_id_displayed(self.locators["id_password"])
        if userName is True and password is True:
            context.web.find_by_id(self.locators["id_username"]).send_keys(context.temp_name)
            context.web.find_by_id(self.locators["id_password"]).send_keys(context.temp_password)
            return True
        return False

    def invalid_login(self, context):
        message = context.web.get_text_xpath(self.locators["xpath_message_error"])
        if message == "Invalid credentials":
            return True
        return False

    def view_logo(self, context):
        logo = context.web.find_by_xpath_displayed(self.locators["xpath_logo"])
        return logo

    def submit_bottom(self, context):
        context.web.find_by_id(self.locators["id_btn_login"]).click()
