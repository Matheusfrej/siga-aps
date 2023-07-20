from flask_restful import reqparse

class LoginRequestParser(reqparse.RequestParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_argument('email', type=str, help='Email is required', required=True)
        self.add_argument('senha', type=str, help='Senha is required', required=True)