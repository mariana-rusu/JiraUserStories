Feature: Retrieve User Stories info

    Scenario: Successfully retrieve all user stories from DB
        Given the API endpoint "/user-stories" is available
        And there are user stories available in DB
        When a GET request is made for the endpoint
        Then the response status code should be 200
        And the response body contain a list of user stories

    Scenario: Successfully retrieve a user story by id
        Given the API endpoint "/user-stories/c349ae52-a21e-4b38-963e-42d4b975640e" is available
        And there is a user story available in DB
        When a GET request is made for the endpoint
        Then the response status code should be 200
        And the response body contain user story details

    Scenario: Attempt to retrieve a non-existent user story id
        Given the API endpoint "/user-stories/1000" is available
        And there is no user story with id 1000 available in DB
        When a GET request is made for the endpoint
        Then the response status code should be 404
        And response body message is "Item not found"


