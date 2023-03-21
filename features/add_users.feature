Feature: Add a user and validate the user has been added to the table
  Scenario: Get to Add User modal
    Given I am in users table page
    When I click "Add User" button
    Then Add User modal div shows up
    And The title is "Add User"

  Scenario: Add a new user
    Given I am in Add User modal div
    When I enter "John" in the "First Name" field
    And I enter "Doe" in the "Last Name" field
    And I enter "jdoe" in the "User Name" field
    And I enter "123456" in the "Password" field
    And I select "Company AAA" option as Customer
    And I select "Admin" option as Role
    And I enter "jdoe@email.com" in the "Email" field
    And I enter "111222333" in the "Cell Phone" field
    Then The Save button is enabled
    When I click the Save button
    Then Add User modal div closes and returns to table page
    And User "John" is added to the table
