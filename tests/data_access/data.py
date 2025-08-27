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

item_found_response = {
    'Item': {
        'summary': 'test data',
        'reporter': '345',
        'labels': [
            'new',
            'manager'
        ],
        'assignee': '234',
        'sprint': '25',
        'user_story_id': '24c7c1d4-1570-4bfd-80a0-77fe7ccc1c2d',
        'project_id': '456',
        'description': 'test data'
    },
    'ResponseMetadata': {
        'RequestId': 'OSRUA25632FE5SDO781M0FJ37JVV4KQNSO5AEMVJF66Q9ASUAAJG',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'server': 'Server',
            'date': 'Wed, 12 Mar 2025 18:44:26 GMT',
            'content-type': 'application/x-amz-json-1.0',
            'content-length': '257',
            'connection': 'keep-alive',
            'x-amzn-requestid': 'OSRUA25632FE5SDO781M0FJ37JVV4KQNSO5AEMVJF66Q9ASUAAJG',
            'x-amz-crc32': '3044764770'
        },
        'RetryAttempts': 0
    }
}

items_found_response = {
    'Items': [{
        'summary': 'test data',
        'reporter': '345',
        'labels': [
            'new',
            'manager'
        ],
        'assignee': '234',
        'sprint': '25',
        'user_story_id': '24c7c1d4-1570-4bfd-80a0-77fe7ccc1c2d',
        'project_id': '456',
        'description': 'test data'
    },
        {
        'summary': 'test data',
        'reporter': '345',
        'labels': [
            'new',
            'manager'
        ],
        'assignee': '234',
        'sprint': '25',
        'user_story_id': 'c349ae52-a21e-4b38-963e-42d4b975640e',
        'project_id': '456',
        'description': 'test data'
        }],
    'ResponseMetadata': {
        'RequestId': 'OSRUA25632FE5SDO781M0FJ37JVV4KQNSO5AEMVJF66Q9ASUAAJG',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'server': 'Server',
            'date': 'Wed, 12 Mar 2025 18:44:26 GMT',
            'content-type': 'application/x-amz-json-1.0',
            'content-length': '257',
            'connection': 'keep-alive',
            'x-amzn-requestid': 'OSRUA25632FE5SDO781M0FJ37JVV4KQNSO5AEMVJF66Q9ASUAAJG',
            'x-amz-crc32': '3044764770'
        },
        'RetryAttempts': 0
    }
}

item_not_found_response = {
    'ResponseMetadata': {
        'HTTPHeaders': {
            'connection': 'keep-alive',
            'content-length': '2',
            'content-type': 'application/x-amz-json-1.0',
            'date': 'Fri, 14 Mar 2025 17:56:33 GMT',
            'server': 'Server',
            'x-amz-crc32': '2745614147',
            'x-amzn-requestid': 'O3NB2NP1BAUIC3C55O4AQB75KFVV4KQNSO5AEMVJF66Q9ASUAAJG'
        },
        'HTTPStatusCode': 200,
        'RequestId': 'O3NB2NP1BAUIC3C55O4AQB75KFVV4KQNSO5AEMVJF66Q9ASUAAJG',
        'RetryAttempts': 0
    }
}

item_created_response = {
    'ResponseMetadata': {
        'RequestId': 'TO7GIA2N5BHRLE4M8H9N1E0QPNVV4KQNSO5AEMVJF66Q9ASUAAJG',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'server': 'Server',
            'date': 'Fri, 14 Mar 2025 18:53:13 GMT',
            'content-type': 'application/x-amz-json-1.0',
            'content-length': '2',
            'connection': 'keep-alive',
            'x-amzn-requestid': 'TO7GIA2N5BHRLE4M8H9N1E0QPNVV4KQNSO5AEMVJF66Q9ASUAAJG',
            'x-amz-crc32': '2745614147'
        },
        'RetryAttempts': 0
    }
}

item_deleted_response = {
    'ResponseMetadata': {
        'RequestId': '71E5T80N6704EUE74M1OSQ0697VV4KQNSO5AEMVJF66Q9ASUAAJG',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'server': 'Server',
            'date': 'Mon, 17 Mar 2025 16:31:13 GMT',
            'content-type': 'application/x-amz-json-1.0',
            'content-length': '2',
            'connection': 'keep-alive',
            'x-amzn-requestid': '71E5T80N6704EUE74M1OSQ0697VV4KQNSO5AEMVJF66Q9ASUAAJG',
            'x-amz-crc32': '2745614147'
        }, 'RetryAttempts': 0
    }
}