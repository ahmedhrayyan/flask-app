from datetime import timedelta, datetime
from flask import Flask, request, abort, jsonify, _request_ctx_stack
from database import init_db, User
from auth import requires_auth, AuthError
import jwt


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_pyfile("config.py")
    init_db(app)

    # ROUTES
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json() or {}
        if 'username' not in data or 'password' not in data:
            abort(422, 'username and password expected in request body')

        username = data['username']
        password = data['password']
        user = User.query.get(username)
        if not user:
            abort(422, 'username or password is not correct')

        if not user.checkpw(str(password)):
            abort(422, 'username or password is not correct')

        payload = {
            'sub': username,
            'exp': datetime.now() + timedelta(days=30)
        }
        token = jwt.encode(payload, app.secret_key, 'HS256')
        return jsonify({
            'success': True,
            'token': str(token, 'utf-8')
        })

    @app.route("/private")
    @requires_auth
    def get_private():
        return jsonify({
            'success': True,
            'current_user': _request_ctx_stack.top.curr_user
        })

    @app.route('/public')
    def get_public():
        return jsonify({
            'success': True
        })

    # ERROR HANDELERS
    @app.errorhandler(422)
    def un_processable(error):
        return jsonify({
            'success': False,
            'message': error.description,
            'code': 422
        }), 422
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': error.description,
            'code': 404
        }), 404
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': error.description,
            'code': 405
        }), 405
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'message': error.message,
            'code': error.code
        }), error.code

    return app
