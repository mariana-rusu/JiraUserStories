import unittest
from unittest.mock import Mock
from data_access.UserStoryRepository import UserStoryRepository
from tests.data_access import data


class TestGetMethod(unittest.TestCase):
    dynamodb = Mock()
    user_stories = UserStoryRepository(dynamodb)

    def test_when_user_story_exists(self):
        self.user_stories.table.get_item = Mock(return_value=data.item_found_response)

        response = self.user_stories.get("24c7c1d4-1570-4bfd-80a0-77fe7ccc1c2d")

        self.user_stories.table.get_item.assert_called_once()
        self.assertEqual("24c7c1d4-1570-4bfd-80a0-77fe7ccc1c2d", response.user_story_id)
        self.assertEqual("test data", response.description)
        self.assertEqual("test data", response.summary)
        self.assertEqual(['new', 'manager'], response.labels)
        self.assertEqual("456", response.project_id)
        self.assertEqual("25", response.sprint)
        self.assertEqual("345", response.reporter)
        self.assertEqual("234", response.assignee)

    def test_when_user_story_doesnt_exist(self):
        self.user_stories.table.get_item = Mock(return_value=data.item_not_found_response)

        response = self.user_stories.get("24c7c1d4-1570-4bfd-80a0-77fe7ccc1c2d45")

        self.user_stories.table.get_item.assert_called_once()
        self.assertEqual(response, None, "Invalid Response Result")

    def test_when_user_story_id_is_not_string(self):
        response = self.user_stories.get(234)

        self.assertEqual("user_story_id should be string", response, "Invalid Response Result")
