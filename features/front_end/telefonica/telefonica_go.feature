Feature: GO_TELEFONICA

  Scenario: go telefonica
    Given the user is on the search page "google"
    And the user select the first option for telefonica
    When the user is in "telefonica.com" home page
    Then the user see telefonica logo


