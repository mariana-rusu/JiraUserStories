import unittest
from unittest.mock import Mock
from data_access.UserStoryRepository import UserStoryRepository
from tests.data_access import data


class TestAddMethod(unittest.TestCase):
    dynamodb = Mock()
    user_stories = UserStoryRepository(dynamodb)

    def test_add_user_story(self):
        self.user_stories.table.put_item = Mock(return_value=data.item_created_response)

        response = self.user_stories.add(data.user_story_1)

        self.assertEqual({'message': 'User Story Added successfully'}, response[0])
        self.assertEqual(201, response[1], "Invalid Response Result")
        self.user_stories.table.put_item.assert_called_once()

