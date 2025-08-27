from business.IRepository import IRepository
from business.UserStory import UserStory
from application.UserStoryGenerator import UserStoryGenerator
import boto3


class UserStoryRepository(IRepository):
    def __init__(self, dynamodb=None):
        if dynamodb:
            self.dynamodb = dynamodb
        else:
            self.dynamodb = boto3.resource('dynamodb')

        self.table = self.dynamodb.Table('UserStories')
        self.user_story_g = UserStoryGenerator()

    def get(self, user_story_id: str):
        if isinstance(user_story_id, str):
            response = self.table.get_item(
                Key={'user_story_id': user_story_id},
                AttributesToGet = [
                    'user_story_id', 'summary', 'description', 'project_id', 'issue_type', 'assignee', 'labels', 'sprint', 'reporter'
                ]
            )

            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                if 'Item' in response:
                    user_story_id = response['Item']['user_story_id']
                    user_story = self.user_story_g.create_user_story(user_story_id, response['Item'])
                    return user_story
                return None
            return None
        else:
            return "user_story_id should be string"

    def get_all(self):
        response = self.table.scan(
            AttributesToGet=[
                'user_story_id', 'summary', 'description', 'project_id', 'issue_type', 'assignee', 'labels', 'sprint', 'reporter'
            ]
        )
        user_stories = []

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            if 'Items' in response:
                for item in response['Items']:
                    user_story_id = item['user_story_id']
                    user_story = self.user_story_g.create_user_story(user_story_id, item)
                    user_stories.append(user_story)

        return user_stories


    def add(self, user_story: UserStory):
        user_story_to_json = user_story.to_json()
        user_story_to_add = {}
        for key, value in user_story_to_json.items():
            if value is not None:
                user_story_to_add[key] = value

        response = self.table.put_item(
            Item=user_story_to_add
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {'message': 'User Story Added successfully'}, 201


    def update(self, user_story_id: str, user_story: UserStory):
        update_expression = "SET "
        expression_attribute_values = {}
        user_story_d = user_story.to_json()
        for key, value in user_story_d.items():
            if key != "user_story_id" and value is not None:
                update_expression += f"{key} = :{key}, "
                expression_attribute_values[f":{key}"] = value
        update_expression = update_expression.rstrip(", ")

        response = self.table.update_item(
            Key={'user_story_id': user_story_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {'message': 'User Story Updated successfully'}, 200


    def delete(self, user_story_id: str):
        response = self.table.delete_item(
            Key={'user_story_id': user_story_id},
        )
        print(response)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {'message': 'User Story Deleted successfully'}, 200
