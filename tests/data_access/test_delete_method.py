import unittest
from unittest.mock import Mock
from data_access.UserStoryRepository import UserStoryRepository
from tests.data_access import data

class TestDeleteMethod(unittest.TestCase):
    dynamodb = Mock()
    user_stories = UserStoryRepository(dynamodb)

    def test_when_user_story_id_exists(self):
        self.user_stories.table.delete_item = Mock(return_value=data.item_deleted_response)

        response = self.user_stories.delete("c349ae52-a21e-4b38-963e-42d4b975640e")

        self.user_stories.table.delete_item.assert_called_once()
        self.assertEqual(response[-1], 200, "Invalid Response Result")
