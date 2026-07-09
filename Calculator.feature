Feature: Calculator operations
  As a user
  I want to perform arithmetic operations
  So that I can get correct results

  Scenario: Add two numbers
    Given I have the numbers 2 and 3
    When I add them
    Then the result should be 5

  Scenario: Subtract two numbers
    Given I have the numbers 10 and 4
    When I subtract them
    Then the result should be 6

  Scenario: Multiply two numbers
    Given I have the numbers 3 and 4
    When I multiply them
    Then the result should be 12

  Scenario Outline: Divide two numbers
    Given I have the numbers <a> and <b>
    When I divide them
    Then the result should be <result>

    Examples:
      | a  | b | result |
      | 10 | 2 | 5.0    |
      | 7  | 2 | 3.5    |

  Scenario: Divide by zero raises an error
    Given I have the numbers 5 and 0
    When I divide them
    Then a ValueError should be raised
