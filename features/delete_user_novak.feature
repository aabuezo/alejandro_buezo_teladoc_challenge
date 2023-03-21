Feature: Delete the user "novak" from the table and validate the user has been deleted
  Scenario: Get to Add User modal
    Given I am in users table page
    And I find user name "novak"
    When I click the X to delete the user "novak"
    Then Confirmation Dialog appears
    When I clik OK button to confirm
    Then The user "novak" is deleted
