import unittest
from unittest.mock import Mock
from application import UserStoryController
from app import app
from tests.integration import Data


class TestPutMethod(unittest.TestCase):

    def test_put_with_valid_url_and_body(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.get.return_value = Data.user_story_response_data
        my_mock.update.return_value = ({'message': 'User Story Updated successfully'}, 200)

        response = app.test_client().put("/user-stories/4c5f6cc6-464b-490d-8e28-996eac375036",
                                         json=Data.request_body_data,
                                         headers={"Content-Type":"application/json"})

        self.assertEqual(response.status_code, 200, "Invalid Status Code")
        my_mock.get.assert_called_once()
        my_mock.update.assert_called_once()


    def test_with_invalid_id(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.get.return_value = None

        response = app.test_client().put("/user-stories/1000",
                                         json=Data.request_body_data,
                                         headers={"Content-Type": "application/json"})

        self.assertEqual(response.status_code, 400, "Invalid Status Code")
        my_mock.get.assert_called_once()

    def test_missing_request_body(self):
        response = app.test_client().put("/user-stories/4c5f6cc6-464b-490d-8e28-996eac375036",
                                         headers={"Content-Type": "application/json"})

        self.assertEqual(response.status_code, 500, "Invalid Status Code")

