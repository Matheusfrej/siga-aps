from flask_restful import reqparse

class LoginRequestParser(reqparse.RequestParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_argument('email', type=str, help='Email is required', required=True)
        self.add_argument('password', type=str, help='Password is required', required=True)