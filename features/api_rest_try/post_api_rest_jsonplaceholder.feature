Feature: Test CRUD methods in Sample REST API testing framework

Background:
	Given I set sample REST API url

  @test
  Scenario: POST post example
    Given I Set POST posts api endpoint
    When I Set HEADER param request content type as "application/json."
    And Set request Body "<title>" "<body>" "<userId>"
          |title | body     | userId |
          |admin | admin123 | 4      |
    And Send a POST HTTP request
    Then I receive valid HTTP response code 201
    And Response BODY "POST" is non-empty.