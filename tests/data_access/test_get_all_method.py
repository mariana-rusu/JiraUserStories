import unittest
from unittest.mock import Mock
from data_access.UserStoryRepository import UserStoryRepository
from tests.data_access import data

class TestGetAllMethod(unittest.TestCase):
    dynamodb = Mock()
    user_stories = UserStoryRepository(dynamodb)

    def test_when_user_stories_returned(self):
        self.user_stories.table.scan = Mock(return_value=data.items_found_response)

        response = self.user_stories.get_all()

        self.assertEqual(2,len(response))
        self.user_stories.table.scan.assert_called_once()


    def test_when_no_user_stories_returned(self):
        self.user_stories.table.scan = Mock(return_value=data.item_not_found_response)

        response = self.user_stories.get_all()

        self.assertEqual([], response, "Invalid Response Result")
        self.user_stories.table.scan.assert_called_once()