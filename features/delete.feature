Feature: Delete a user story

    Scenario: Successfully delete a user story
        Given the API endpoint "/user-stories/c349ae52-a21e-4b38-963e-42d4b975640e" is available
        When a DELETE request is made for the endpoint with valid user story id
        Then the response status code should be 200

    Scenario: Delete user story using invalid id
        Given the API endpoint "/user-stories/4c5f6cc6-464b-490d-8e28-996eac375036" is available
        When a DELETE request is made for the endpoint with invalid user story id
        Then the response status code should be 400


