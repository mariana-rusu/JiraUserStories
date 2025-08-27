from business.UserStory import UserStory

class UserStoryGenerator:
    def __init__(self):
        pass

    def create_user_story(self, user_story_id: str, request: dict) -> UserStory:
        user_story = UserStory(user_story_id)

        if "summary" in request.keys():
            user_story.summary = request["summary"]
        if "description" in request.keys():
            user_story.description = request["description"]
        if "project_id" in request.keys():
            user_story.project_id = request["project_id"]
        if "issue_type" in request.keys():
            user_story.issue_type = request["issue_type"]
        if "assignee" in request.keys():
            user_story.assignee = request["assignee"]
        if "labels" in request.keys():
            user_story.labels = request["labels"]
        if "sprint" in request.keys():
            user_story.sprint = request["sprint"]
        if "reporter" in request.keys():
            user_story.reporter = request["reporter"]

        return user_story
