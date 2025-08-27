import unittest
from unittest.mock import Mock
from application import UserStoryController
from app import app
from tests.integration import Data


class TestGetMethod(unittest.TestCase):

    def test_get_all(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.get_all.return_value = Data.user_stories_response_data

        response = app.test_client().get('/user-stories')

        self.assertEqual(response.status_code, 200, "Invalid Response Status Code")
        self.assertEqual(response.get_json(), Data.user_stories_expected_data)
        my_mock.get_all.assert_called_once_with()

    def test_get_by_id(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.get.return_value = Data.user_story_response_data

        response = app.test_client().get("/user-stories/c349ae52-a21e-4b38-963e-42d4b975640e")

        self.assertEqual(response.status_code, 200, "Invalid Response Status Code")
        self.assertEqual(response.get_json(), Data.user_story_expected_data)
        my_mock.get.assert_called_once_with("c349ae52-a21e-4b38-963e-42d4b975640e")

    def test_get_by_invalid_id(self):
        my_mock = UserStoryController.user_repo = Mock()
        my_mock.get.return_value = None

        response = app.test_client().get("/user-stories/1000")

        self.assertEqual(response.status_code, 404, "Invalid Response Status Code")
        my_mock.get.assert_called_once_with("1000")



