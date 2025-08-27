import unittest
from unittest.mock import Mock
from application import UserStoryController
from app import app
from tests.integration import Data


class TestDeleteMethod(unittest.TestCase):

    def test_with_valid_id(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.get.return_value = Data.user_story_response_data
        my_mock.delete.return_value = ({"message": "User Story Deleted successfully"}, 200)
        response = app.test_client().delete("/user-stories/c349ae52-a21e-4b38-963e-42d4b975640e")

        self.assertEqual(response.status_code, 200, "Invalid Status Code")
        my_mock.get.assert_called_once_with("c349ae52-a21e-4b38-963e-42d4b975640e")
        my_mock.delete.assert_called_once_with("c349ae52-a21e-4b38-963e-42d4b975640e")


    def test_with_invalid_id(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.get.return_value = None

        response = app.test_client().delete("/user-stories/4c5f6cc6-464b-490d-8e28-996eac375036")

        self.assertEqual(response.status_code, 400, "Invalid Status Code")
        my_mock.get.assert_called_once_with("4c5f6cc6-464b-490d-8e28-996eac375036")