from flask import url_for
from tests.unittest.flask_base_for_test import TestBaseFlask


class TestShow(TestBaseFlask):
    def test_show_response_empty(self):

        self.create_user()

        token = self.create_token()

        response = self.client.get(
            url_for("user.show"), 
            headers=token
            )

        self.assertEqual(1, len(response.json))


class TestDefalt(TestBaseFlask):
    def test_json_response_from_defalt(self):

        response = self.client.get(url_for("user.defalt"))

        except_response = {"Ingresse API Online": True}

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json, except_response)


class TestRegister(TestBaseFlask):

    # Deve retornar o payload sem o id
    def test_register_user(self):

        response = self.client.post(url_for("user.register"), json=self.user)

        self.assertEqual(response.status_code, 201)

        response.json.pop("id")

        # Testa as keys
        self.assertEqual(response.json.keys(), self.user.keys())

        # Testa se os values não são None
        self.assertNotIn(None, response.json.values())

    def test_error_miss_username_register_user(self):

        self.user.pop("username")

        response = self.client.post(url_for("user.register"), json=self.user)

        except_response = {"username": ["Missing data for required field."]}

        self.assertEqual(response.json, except_response)

    def test_error_schema_register_user(self):

        response = self.client.post(url_for("user.register"), json="adsada")

        except_response = {"_schema": ["Invalid input type."]}

        self.assertEqual(response.json, except_response)
