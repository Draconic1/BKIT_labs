Feature: Test

  Scenario: Test db
    Given I have db name = tour.db
    When I open db
    Then I expect to get 1 == result[0]
