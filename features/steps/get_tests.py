from behave import *
from unittest.mock import Mock
from application import UserStoryController
from app import app
from tests.integration import Data

@given('the API endpoint "{endpoint}" is available')
def step_impl(context, endpoint):
    context.endpoint = endpoint

@given('there are user stories available in DB')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.get_all.return_value = Data.user_stories_response_data
    context.my_mock = my_mock

@given('there is a user story available in DB')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.get.return_value = Data.user_story_response_data
    context.my_mock = my_mock

@given('there is no user story with id 1000 available in DB')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.get.return_value = None
    context.my_mock = my_mock

@when('a GET request is made for the endpoint')
def step_impl(context):
    context.response = app.test_client().get(context.endpoint)

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected status code {status_code}, but got {context.response.status_code}"

@then('the response body contain a list of user stories')
def step_impl(context):
    assert context.response.get_json() == Data.user_stories_expected_data
    context.my_mock.get_all.assert_called_once_with()

@then('the response body contain user story details')
def step_impl(context):
    assert context.response.get_json() == Data.user_story_expected_data
    context.my_mock.get.assert_called_once_with("c349ae52-a21e-4b38-963e-42d4b975640e")

@then('response body message is "{message}"')
def step_impl(context, message):
    response_data = context.response.get_json()
    assert response_data['message'] == message
    context.my_mock.get.assert_called_once_with("1000")


