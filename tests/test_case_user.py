import requests
from payload import *
from utilities.resources import ApiResources
from utilities.configurations import Config


class TestCases:

    def setup_method(self):
        # self.token = None
        self.config = Config()
        self.base_url = self.config["API"]["baseurl"]

    def test_get_users(self):
        url = self.base_url + ApiResources.list_users
        response = requests.get(url, )
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 200
        assert response.json()['page'] == 2

    def test_single_user(self):
        url = self.base_url + ApiResources.list_single_user
        response = requests.get(url, )
        print(response.status_code)
        # print(response.headers)
        # print(response.json())
        # print(response.text)
        # print(response.headers['Content-Type'])
        assert response.status_code == 200
        assert response.json()['data']['first_name'] == 'Janet'
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_user_not_found(self):
        url = self.base_url + ApiResources.user_not_found
        response = requests.get(url, )
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 404

    def test_list_resource(self):
        url = self.base_url + ApiResources.list_resource
        response = requests.get(url, )
        print(response.status_code)
        # print(response.json())
        lis = response.json()['data']
        for dic in lis:
            # print(dic)
            if dic['year'] == 2001:
                # print(dic['year'])
                assert dic['year'] == 2001
        assert response.status_code == 200

    def test_single_resource(self):
        url = self.base_url + ApiResources.list_single_resource
        response = requests.get(url, )
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 200
        assert response.json()['data']['year'] == 2001

    def test_single_resource_not_found(self):
        url = self.base_url + ApiResources.single_resource_not_found
        response = requests.get(url, )
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 404

    def test_create_user(self):   # post request
        url = self.base_url + ApiResources.create_user_post
        response = requests.post(url, data=create_user())
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 201
        assert response.json()['name'] == 'morpheus'

    def test_update_user_put(self):   # put request
        url = self.base_url + ApiResources.update_user_put
        response = requests.put(url, data=update_user())
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 200
        assert response.json()['name'] == 'morpheus'

    def test_update_user_patch(self):   # patch request
        url = self.base_url + ApiResources.update_user_patch
        response = requests.patch(url, data=update_user())
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 200
        assert response.json()['job'] == 'zion resident'

    def test_delete_user(self):
        url = self.base_url + ApiResources.delete_user
        response = requests.delete(url, )
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 204

    def test_register_user(self):   # post request
        url = self.base_url + ApiResources.register_user
        response = requests.post(url, data=register_user())
        print(response.status_code)
        # print(response.json())
        token = response.json()['token']
        print(token)
        assert response.status_code == 200
        assert response.json()['id'] == 4
        assert 'token' in response.text

    def test_register_unsuccessful(self):   # post request
        url = self.base_url + ApiResources.register_unsuccessful
        response = requests.post(url, data=register_unsuccessful())
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 400
        assert response.json()['error'] == 'Missing password'

    def test_login_successful(self):   # post request
        url = self.base_url + ApiResources.login
        response = requests.post(url, data=login_successful())
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 200
        assert 'token' in response.json()

    def test_login_unsuccessful(self):   # post request
        url = self.base_url + ApiResources.login
        response = requests.post(url, data=login_unsuccessful())
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 400
        assert response.json()['error'] == 'Missing password'

    def test_delay_response(self):   # post request
        url = self.base_url + ApiResources.delay_response
        response = requests.get(url, )
        print(response.status_code)
        # print(response.json())
        assert response.status_code == 200

