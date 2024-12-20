Feature: Automating actions on the FYC platform

  Scenario: Automate platform interaction
    Given I am logged into the platform
    When I navigate to the "Test Automation Project"
    And I switch to the "Details" tab
    And I return to the "Videos" tab
    And I play the video
    And I change the resolution to 480p and then back to 720p
    And I pause the video and exit the project
    And I logout from the platform

