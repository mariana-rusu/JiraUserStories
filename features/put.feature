Feature: Update a user story

    Scenario: Successfully update a user story
        Given the API endpoint "/user-stories/4c5f6cc6-464b-490d-8e28-996eac375036" is available
        When a PUT request is made for the endpoint with valid url and body
        Then the response status code should be 200

    Scenario: Update user story using invalid id
        Given the API endpoint "/user-stories/1000" is available
        When a PUT request is made for the endpoint, using invalid user id
        Then the response status code should be 400

    Scenario: Update user story missing request body
        Given the API endpoint "/user-stories/4c5f6cc6-464b-490d-8e28-996eac375036" is available
        When a PUT request is made for the endpoint, missing request body
        Then the response status code should be 500



