Feature: TELEFONICA
Background:
  Given the user is on the search page "google"
    And the user select the first option for telefonica
    When the user is in "telefonica.com" home page
    And the user accept the cookies


  Scenario: telefonica_Acionistas get value Nyse
    And the user is in EurolandTool
    And the user tap Nyse tab
    Then the user get the NY value