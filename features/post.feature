Feature: Create a new user story

    Scenario: Successfully create new user story
        Given the API endpoint "/user-stories" is available
        When a POST request is made for the endpoint including json data and headers
        Then the response status code should be 201

    Scenario: Create user story missing request body
        Given the API endpoint "/user-stories" is available
        When a POST request is made for the endpoint, missing request body
        Then the response status code should be 500

    Scenario: Create user story missing headers
        Given the API endpoint "/user-stories" is available
        When a POST request is made for the endpoint, missing headers
        Then the response status code should be 201



