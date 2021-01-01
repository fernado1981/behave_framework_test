from behave import when, then
from page_objects.flightsearch.search_flight import SearchFlight


@when('the user selects a departure city "{city}"')
def user_select_departure_city(context, city):
    departure_city = SearchFlight()
    departure_city.search_flight_from(context, city)


@when('the user selects a destination city "{city}"')
def user_select_destination_city(context, city):
    destination_city = SearchFlight()
    destination_city.search_flight_destination(context, city)


@when("the user tap on Find Flights button")
def user_clicks_on_find_flights(context):
    find_flights = SearchFlight()
    find_flights.search_flight(context)


@then("flights are presented on the search result page")
def flights_are_found(context):
    flights_presented = SearchFlight()
    flights = flights_presented.count_results(context)
    assert flights is True
