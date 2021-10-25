Feature: Minicompany

  Scenario: Access registered minicompanies

    Given a user accesses the platform homepage (4a)
    When the user clicks Minicompanies
    Then the system displays the list of registered companies

