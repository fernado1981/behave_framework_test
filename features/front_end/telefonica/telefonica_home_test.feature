Feature: TELEFONICA
Background:
  Given the user is on the search page "google"
    And the user select the first option for telefonica
    When the user is in "telefonica.com" home page
    And the user accept the cookies

  Scenario: telefonica_home to shareholders-investors
    And the user selects "Acciones e inversores" tab nav
    Then the user is in "shareholders-investors"  page