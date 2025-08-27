from business.UserStory import UserStory

user_story_1 = UserStory("c349ae52-a21e-4b38-963e-42d4b975640e")
user_story_1.assignee = "234"
user_story_1.description = "text"
user_story_1.summary = "text"
user_story_1.labels = ["new", "manager"]
user_story_1.project_id = "456"
user_story_1.reporter = "345"
user_story_1.sprint = "25"
user_story_1.issue_type = "23"

user_story_2 = UserStory("4b25aed5-a685-4d1b-b806-e81223c95eaa")
user_story_2.assignee = "234"
user_story_2.description = "text"
user_story_2.summary = "text"
user_story_2.labels = ["new", "manager"]
user_story_2.project_id = "456"
user_story_2.reporter = "345"
user_story_2.sprint = "25"
user_story_2.issue_type = "23"

user_story_response_data = user_story_1
user_stories_response_data = [user_story_1, user_story_2]

request_body_data = {
                    "assignee": "234",
                    "description": "text",
                    "labels": [
                        "new",
                        "manager"
                        ],
                    "project_id": "456",
                    "reporter": "345",
                    "sprint": "25",
                    "summary": "text",
                    "issue_type": "23"
                    }

user_story_expected_data = {
                            "assignee": "234",
                            "description": "text",
                            "labels": [
                                "new",
                                "manager"
                                ],
                            "project_id": "456",
                            "reporter": "345",
                            "sprint": "25",
                            "summary": "text",
                            "user_story_id": "c349ae52-a21e-4b38-963e-42d4b975640e",
                            "issue_type": "23"
                            }


user_stories_expected_data = [
                                 {
                                     "assignee": "234",
                                     "description": "text",
                                     "labels": [
                                         "new",
                                         "manager"
                                     ],
                                     "project_id": "456",
                                     "reporter": "345",
                                     "sprint": "25",
                                     "summary": "text",
                                     "user_story_id": "c349ae52-a21e-4b38-963e-42d4b975640e",
                                     "issue_type": "23"
                                 },
                                 {
                                     "assignee": "234",
                                     "description": "text",
                                     "labels": [
                                         "new",
                                         "manager"
                                     ],
                                     "project_id": "456",
                                     "reporter": "345",
                                     "sprint": "25",
                                     "summary": "text",
                                     "user_story_id": "4b25aed5-a685-4d1b-b806-e81223c95eaa",
                                     "issue_type": "23"
                                 }
                             ]