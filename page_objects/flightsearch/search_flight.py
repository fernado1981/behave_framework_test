class search_flight:
    locators = {
        "xpath_from": "//select[@name='fromPort']/option[text()='{}']",
        "xpath_to": "//select[@name='toPort']/option[text()='{}']",
        "xpath_submit": "//input[@type='submit']",
        "xpath_count_flights": "//table/tbody/tr"
    }

    def __init__(self):
        self.fromflight = self.locators["xpath_from"]
        self.toflight = self.locators["xpath_to"]
        self.submit = self.locators["xpath_submit"]
        self.countFights = self.locators["xpath_count_flights"]

    def search_flight_from(self, context, city):
        context.web.find_by_xpath(self.fromflight.format(city)).click()

    def search_flight_destination(self, context, city):
        context.web.find_by_xpath(self.toflight.format(city)).click()

    def search_flight(self, context):
        context.web.find_by_xpath(self.submit).click()

    def count_results(self, context):
        elements = context.web.finds_by_xpath_displayed(self.countFights)
        if len(elements) > 1:
            return True
