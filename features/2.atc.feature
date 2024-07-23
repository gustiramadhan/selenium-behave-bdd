Feature: Add to Cart functionality

Scenario: add to cart specific item
    Given the user is logged in with username "standard_user" and password "secret_sauce"
    When the user add Sauce Lab Backpack to the cart
    Then the cart badge should show "1"

Scenario: Add multiple products to the cart
    Given the user is logged in with username "standard_user" and password "secret_sauce"
    When the user adds "4" items to the Cart
    Then the cart badge should show "4"

Scenario: Remove multiple items from the cart
    Given the user is logged in with username "standard_user" and password "secret_sauce"
    When the user adds "3" items to the cart
    And the user click the cart button
    And the user removes "2" items from the cart
    Then the cart badge should show "1"