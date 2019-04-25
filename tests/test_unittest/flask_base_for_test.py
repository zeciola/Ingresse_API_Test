from unittest import TestCase
from app import create_app
from flask import url_for
from json import loads

class TestBaseFlask(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app_context =  self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()
        self.user = {
            'username': 'teste',
            'password': '1234',
            'email' : 'teste@teste.com'
        }

        def tearDown(self):
            self.app.db.drop_all()

        def create_user():
            self.client.post(url_for(user.register), json=self.user)

        def create_token():
            login_token = self.client.post(url_for(login.login), json=self.user)

            return {
                'Authorization':
                'Bearer ' + loads(login_token.data.decode())['acess_token']
            }
