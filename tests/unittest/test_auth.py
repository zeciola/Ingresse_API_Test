from flask import url_for
from tests.unittest.flask_base_for_test import TestBaseFlask
from json import load


class TestLogin(TestBaseFlask):
    def test_login_token(self):

        self.create_user()

        self.user.pop("date_of_birth")

        token = self.client.post(url_for("login.login"), json=self.user)

        token_except = {
            "acess_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTYzMjQ1MTYsIm5iZiI6MTU1NjMyNDUxNiwianRpIjoiMTI4MzBiZDEtYThjZi00NmI1LWJmOTYtZGE2MGY2NWEwZGQ2IiwiZXhwIjoxNTU2MzI0NTc2LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.cMqm9jlp-hPFDIKF8qkjf3YjONX105vOdjl_ZiP3bPA",
            "msg": "sucess",
            "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTYzMjQ1MTYsIm5iZiI6MTU1NjMyNDUxNiwianRpIjoiMDQyZmU5MDAtMjkxNC00YjBhLWIxMDQtMjkwZDQyZTdjMmVjIiwiZXhwIjoxNTU4OTE2NTE2LCJpZGVudGl0eSI6MSwidHlwZSI6InJlZnJlc2gifQ.6Cxa7Gjt0vlkLmf4WGr-dJT-IWVfdwvqERhO3kyaWZU",
        }

        self.assertEqual(token.status_code, 200)

        self.assertEqual(token.json.keys(), token_except.keys())

    def test_error_login_token(self):

        self.create_user()

        self.user.update({"password": "token_error"})

        self.user.pop("date_of_birth")

        login_except = {"msg": "Invalid credentials, please insert a valid credential"}

        response = self.client.post(url_for("login.login"), json=self.user)

        self.assertEqual(response.json, login_except)

        self.user.update({"username": "token_error", "password": "1234"})

        response = self.client.post(url_for("login.login"), json=self.user)

        self.assertEqual(response.json, login_except)

    def test_error_login_miss_required_field(self):

        self.create_user()

        self.user.pop("date_of_birth")

        self.user.pop("username")

        response = self.client.post(url_for("login.login"), json=self.user)

        login_except = {"username": ["Missing data for required field."]}

        self.assertEqual(response.json, login_except)

    def test_error_login_send_date_of_birth(self):

        self.create_user()

        response = self.client.post(url_for("login.login"), json=self.user)

        login_except = {"Error": "Please dont send date_of_birth to login"}

        self.assertEqual(response.json, login_except)
