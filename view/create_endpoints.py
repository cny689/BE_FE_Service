from flask import request, jsonify
from model.user_dao import UserDao
from service.user_service import UserService

def create_endpoints(app, services):
    user_service  = services.user_service

    @app.route("/test", methods=['POST'])
    def sign_up():
        try:
            user = request.json
            user = user_service.create_new_user(user)
            return jsonify({'message':'ok'}), 200
        except Exception as e :
            return {'error': str(e)}