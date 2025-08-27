from flask import Blueprint, jsonify, request
from application.UserStoryGenerator import UserStoryGenerator
from data_access.UserStoryRepository import UserStoryRepository
import uuid

# Create a Blueprint named 'user_story'
user_story_bp = Blueprint('user_story', __name__)
user_repo = UserStoryRepository()
user_story_g = UserStoryGenerator()

@user_story_bp.route('/<string:user_story_id>', methods = ['GET'])
def get_user_story_by_id(user_story_id: str):
    user_story = user_repo.get(user_story_id)
    if user_story is not None:
        return user_story.to_json()
    else:
        return jsonify({'message': 'Item not found'}), 404

@user_story_bp.route('', methods = ['GET'])
def get_user_stories():
    user_stories = user_repo.get_all()
    result = []
    if len(user_stories) > 0:
        for user_story in user_stories:
            result.append(user_story.to_json())
        return result
    else:
        return jsonify({'message': 'No item found'}), 404

@user_story_bp.route('', methods = ['POST'])
def add_user_story():
    uniq_id = uuid.uuid4()
    try:
        data = request.get_json()
        user_story = user_story_g.create_user_story(str(uniq_id), data)
        response = user_repo.add(user_story)
        if response[-1] == 201:
            return response

    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@user_story_bp.route('/<string:user_story_id>', methods = ['PUT'])
def update_user_story_id(user_story_id: str):
    try:
        data = request.get_json()
        get_item = user_repo.get(user_story_id)
        if get_item is None:
            return jsonify({"message": "Could not update non existent item"}), 400
        else:
            user_story = user_story_g.create_user_story(user_story_id, data)
            response = user_repo.update(user_story_id, user_story)
            if response[-1] == 200:
                return response

    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@user_story_bp.route('/<string:user_story_id>', methods = ['DELETE'])
def delete_user_story_id(user_story_id: str):
    get_item = user_repo.get(user_story_id)
    if get_item is None:
        return jsonify({"message": "Could not delete non existent item"}), 400
    else:
        response = user_repo.delete(user_story_id)
        if response[-1] == 200:
            return response

