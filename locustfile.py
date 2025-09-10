from locust import HttpUser, task, between


class ReqresUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_users(self):
        self.client.get("/api/users?page=2")

    @task
    def get_single_user(self):
        self.client.get("/api/users/2")

    @task
    def create_user(self):
        payload = {
            "name": "John Doe",
            "job": "Software Engineer"
        }
        self.client.post("/api/users", data=payload)
