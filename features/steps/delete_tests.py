from behave import *
from unittest.mock import Mock
from application import UserStoryController
from app import app
from tests.integration import Data

@when('a DELETE request is made for the endpoint with valid user story id')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.get.return_value = Data.user_story_response_data
    my_mock.delete.return_value = ({"message": "User Story Deleted successfully"}, 200)
    context.my_mock = my_mock

    context.response = app.test_client().delete(context.endpoint)

    context.my_mock.get.assert_called_once_with("c349ae52-a21e-4b38-963e-42d4b975640e")
    context.my_mock.delete.assert_called_once_with("c349ae52-a21e-4b38-963e-42d4b975640e")

@when('a DELETE request is made for the endpoint with invalid user story id')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.get.return_value = None
    context.my_mock = my_mock

    context.response = app.test_client().delete(context.endpoint)

    context.my_mock.get.assert_called_once_with("4c5f6cc6-464b-490d-8e28-996eac375036")



