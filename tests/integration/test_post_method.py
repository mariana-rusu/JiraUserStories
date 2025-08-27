import unittest
from unittest.mock import Mock
from application import UserStoryController
from app import app
from tests.integration import Data


class TestPostMethod(unittest.TestCase):

    def test_post_valid_url_and_body(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.add.return_value = ('User Story Added successfully', 201)
        response = app.test_client().post("/user-stories", json=Data.request_body_data,
                                          headers={"Content-Type":"application/json"})

        self.assertEqual(response.status_code, 201, "Invalid Response Status Code")
        my_mock.add.assert_called_once()

    def test_missing_request_body(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.add.return_value = {'ResponseMetadata': {'HTTPStatusCode': 200}}

        response = app.test_client().post("/user-stories", headers={"Content-Type": "application/json"})

        self.assertEqual(response.status_code, 500, "Invalid Response Status Code")

    def test_missing_headers(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.add.return_value = ('User Story Added successfully', 201)

        response = app.test_client().post("/user-stories", json=Data.request_body_data)

        self.assertEqual(response.status_code, 201, "Invalid Response Status Code")
        my_mock.add.assert_called_once()


