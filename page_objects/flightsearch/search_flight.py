from page_objects.flightsearch.locators_flight_search import LocatorsFlightSearch


class SearchFlight(LocatorsFlightSearch):

    def __init__(self):
        self.locators = self.locators

    def search_flight_from(self, context, city):
        context.web.find_by_xpath(self.locators["xpath_from"].format(city)).click()

    def search_flight_destination(self, context, city):
        context.web.find_by_xpath(self.locators["xpath_to"].format(city)).click()

    def search_flight(self, context):
        context.web.find_by_xpath(self.locators["xpath_submit"]).click()

    def count_results(self, context):
        elements = context.web.finds_by_xpath_displayed(self.locators["xpath_count_flights"])
        if len(elements) > 1:
            return True
