from behave import *
from unittest.mock import Mock
from application import UserStoryController
from app import app
from tests.integration import Data

@when('a PUT request is made for the endpoint with valid url and body')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.get.return_value = Data.user_story_response_data
    my_mock.update.return_value = ({'message': 'User Story Updated successfully'}, 200)
    context.my_mock = my_mock

    context.response = app.test_client().put(context.endpoint,
                                         json=Data.request_body_data,
                                         headers={"Content-Type":"application/json"})
    context.my_mock.get.assert_called_once()
    context.my_mock.update.assert_called_once()

@when('a PUT request is made for the endpoint, using invalid user id')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.get.return_value = None
    context.my_mock = my_mock

    context.response = app.test_client().put(context.endpoint,
                                         json=Data.request_body_data,
                                         headers={"Content-Type": "application/json"})
    context.my_mock.get.assert_called_once()


@when('a PUT request is made for the endpoint, missing request body')
def step_impl(context):
    context.response = app.test_client().put(context.endpoint,
                                         headers={"Content-Type": "application/json"})



