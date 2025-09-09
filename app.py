from flask import Flask, request
from application.UserStoryController import user_story_bp
import logging

logging.basicConfig(level=logging.DEBUG, format="{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M")
logger = logging.getLogger("app")

app = Flask(__name__)
app.register_blueprint(user_story_bp, url_prefix='/user-stories')

@app.before_request
def before_request():
    content_type_header = request.headers.get('Content-Type')
    authorization_header = request.headers.get('Authorization')
    logger.info("Content type: " + str(content_type_header))
    logger.info("Authorization: " + str(authorization_header))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
