# Jira User Stories
### Introduction
Jira User Stories is a REST API used to retrieve a specific or all the existing user stories from the server, save, modify or delete and existing ones.
### Jira User Stories Features
* Users can get details of a user story
* Users can get details of all the user stories
* Users can create new user story
* Users can update details on an existing user story
* User can delete user story

### API Endpoints
| HTTP Verbs | Endpoints                    | Action                                     |
|------------|------------------------------|--------------------------------------------|
| GET        | /user-stories                | To retrieve all User Stories from DynamoDB |
| GET        | /user-stories/:user_story_id | To retrieve details of a single User Story |
| POST       | /user-stories                | To create a new User Story                 |
| PUT        | /user-stories/:user_story_id | To update an User Story                    |
| DELETE     | /user-stories/:user_story_id | To delete an User Story                    |
### Technologies Used
* [Python](https://www.python.org/) Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically type-checked and garbage-collected. 
* [Flask](https://flask.palletsprojects.com/en/stable/) Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
* [Requests](https://pypi.org/project/requests/) The Python requests library is a popular and widely-used third-party library for making HTTP requests. 
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.
* [Unittest](https://docs.python.org/3/library/unittest.html) Python Unittest is a built-in testing framework that provides a set of tools for testing our code's functionality in a more systematic and organized manner.
* [Mock](https://docs.python.org/3/library/unittest.mock-examples.html) Mocking in Python with unittest.mock allows you to simulate complex logic or unpredictable dependencies, such as responses from external services. 
* [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html) Amazon DynamoDB is a managed NoSQL database service provided by Amazon Web Services. It supports key-value and document data structures and is designed to handle a wide range of applications requiring scalability and performance.
### Author
* [Mariana Rusu](https://github.com/mariana-rusu)
