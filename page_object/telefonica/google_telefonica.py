from selenium.webdriver.common.keys import Keys

from page_object.telefonica.locator import locator


class google_telefonica(locator):

    def __init__(self):
        self.data=locator.data_locator_google_telefonica

    def open_bing_navigator(self,context):
        context.web.open(self.data['Google_bing'])

    def accept_cookies(self,context):
        context.web.find_by_xpath(self.data['cookies']).click()

    def more_better_remaind(self,context):
        context.web.find_by_xpath(self.data['microsoft_Edge']).click()

    def input_search_bing(self,context):
        context.web.find_by_name('q').send_keys('telefonica', Keys.ENTER)

    def click_first_option(self,context):
        context.web.find_by_xpath(self.data['first']).click()

    def find_logo(self,context):
        atributo = context.web.find_by_xpath(self.data['logo']).get_attribute('alt')
        assert (atributo == "Telefonica.com")

