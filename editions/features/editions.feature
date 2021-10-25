Feature: Editions

  Scenario: Access registered editions (3a)

    Given a user accesses the platform homepage (3a)
    When the user clicks editions
    Then the system displays the list of registered editions
