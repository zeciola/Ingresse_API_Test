from flask import url_for
from tests.unittest.flask_base_for_test import TestBaseFlask


class TestShow(TestBaseFlask):
    def test_show_response_len_one(self):

        self.create_user()
        self.create_user()

        token = self.create_token()

        response = self.client.get(url_for("user.show"), headers=token)

        self.assertEqual(2, len(response.json))


class TestShowId(TestBaseFlask):
    def test_show_by_id(self):

        self.create_user()
        self.create_user()

        token = self.create_token()

        response = self.client.get(
            url_for("user.show_by_id", identificator=1), headers=token
        )

        list_keys_except = {
            "date_of_birth": "2019-04-25",
            "email": "teste@teste.com",
            "id": 1,
            "password": "$pbkdf2-sha512$25000$pPQ.p3SO0fr//5.zVgpBaA$vGKs4h3AyiScje6X8s6oUxPtpW9V57ZKj1Qv9QIlVaA8C2a4/3S3YkpOMBRM1PPnOqERUKBGazphDa2Ny1xJNQ",
            "username": "teste",
        }

        self.assertEqual(response.json[0].get("id"), 1)
        # Teste se tem todas as Keys

        self.assertEqual(response.json[0].keys(), list_keys_except.keys())
        # Testa se não a valores None
        self.assertNotIn(None, response.json[0].values())

    def test_show_by_id_not_valid_id_error(self):

        self.create_user()

        token = self.create_token()

        # Teste de id que não existe

        response = self.client.get(
            url_for("user.show_by_id", identificator=999999), headers=token
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json, [])

        # Teste identificator string

        response = self.client.get(
            url_for(
                "user.show_by_id",
                identificator="""d*(@)(/\ 
                af%@""",
            ),
            headers=token,
        )

        self.assertEqual(response.json, None)


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


class TestChange(TestBaseFlask):
    def test_change_by_id(self):

        self.create_user()

        token = self.create_token()

        change_value = {"username": "Change_OK"}

        response = self.client.put(
            url_for("user.change_id", identificator=1), json=change_value, headers=token
        )

        self.assertEqual(response.json.get("username"), "Change_OK")

    def test_error_change_by_id_not_valid_id(self):

        self.create_user()

        token = self.create_token()

        change_value = {"username": "Change_OK"}

        except_change_value = {"Error": "Error not found user 5465654653"}

        response = self.client.put(
            url_for("user.change_id", identificator=5465654653),
            json=change_value,
            headers=token,
        )

        self.assertEqual(response.json, except_change_value)


class TestDelete(TestBaseFlask):
    def test_delete_by_id(self):

        self.create_user()

        token = self.create_token()

        delete_except = {"msg": "The user for id: 1 has been deleted"}

        response = self.client.delete(
            url_for("user.delete_id", identificator=1), headers=token
        )

        self.assertEqual(response.json, delete_except)

    def test_error_delete_by_id(self):

        self.create_user()

        token = self.create_token()

        delete_except = {"msg": "The user for id: 1 has been deleted"}

        response = self.client.delete(
            url_for("user.delete_id", identificator=16546565), headers=token
        )

        delete_except = {"Error": "Error not found user id: 16546565"}

        self.assertEqual(response.json, delete_except)

        delete_except = {"Error": "Error not found user id: d*(@)'''( af%@"}

        response = self.client.delete(
            url_for("user.delete_id", identificator="d*(@)'''( af%@"), headers=token
        )

        self.assertEqual(response.json, delete_except)
