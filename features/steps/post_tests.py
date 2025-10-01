from behave import *
from unittest.mock import Mock
from application import UserStoryController
from app import app
from tests.integration import Data

@when('a POST request is made for the endpoint including json data and headers')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.add.return_value = ('User Story Added successfully', 201)
    context.my_mock = my_mock

    context.response = app.test_client().post(context.endpoint, json=Data.request_body_data,
                                          headers={"Content-Type":"application/json"})
    context.my_mock.add.assert_called_once()

@when('a POST request is made for the endpoint, missing request body')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.add.return_value = {'ResponseMetadata': {'HTTPStatusCode': 200}}
    context.my_mock = my_mock

    context.response = app.test_client().post(context.endpoint, headers={"Content-Type": "application/json"})


@when('a POST request is made for the endpoint, missing headers')
def step_impl(context):
    my_mock = UserStoryController.user_repo = Mock()
    my_mock.add.return_value = ('User Story Added successfully', 201)
    context.my_mock = my_mock

    context.response = app.test_client().post(context.endpoint, json=Data.request_body_data)
    context.my_mock.add.assert_called_once()


