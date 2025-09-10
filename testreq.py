import unittest
import requests

BASE_URL = "https://reqres.in/api"

class TestReqresAPI(unittest.TestCase):

    def test_get_users_success(self):
        """Test GET list users returns 200 and contains 'data' key"""
        response = requests.get(f"{BASE_URL}/users?page=2")
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIn('data', json_data)
        self.assertIsInstance(json_data['data'], list)

    def test_get_single_user_valid(self):
        """Test GET single user returns correct user data"""
        user_id = 2
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIn('data', json_data)
        self.assertEqual(json_data['data']['id'], user_id)

    def test_get_single_user_not_found(self):
        """Test GET user not found returns 404"""
        user_id = 23  # Assuming this user does not exist
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        """Test POST create user returns 201 and correct keys"""
        payload = {
            "name": "John Doe",
            "job": "Software Engineer"
        }
        response = requests.post(f"{BASE_URL}/users", data=payload)
        self.assertEqual(response.status_code, 201)
        json_data = response.json()
        self.assertIn('id', json_data)
        self.assertEqual(json_data['name'], payload['name'])
        self.assertEqual(json_data['job'], payload['job'])


if __name__ == "__main__":
    unittest.main()
