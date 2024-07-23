Feature: Validate the login feature

Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters the username "standard_user"
    And the user enters the password "secret_sauce"
    And the user clicks the login button
    Then the user should see the products page

Scenario: Unsuccessful login with invalid credentials
    Given the user is on the login page
    When the user enters the username "invalid_user"
    And the user enters the password "invalid_password"
    And the user clicks the login button
    Then the user should see an error message

Scenario: Unsuccessful login with empty username
    Given the user is on the login page
    When the user enters the password "secret_sauce"
    And the user clicks the login button
    Then the user should see a username is required error message

Scenario: Unsuccessful login with empty password
    Given the user is on the login page
    When the user enters the username "standart_user"
    And the user clicks the login button
    Then the user should see a password is required error message