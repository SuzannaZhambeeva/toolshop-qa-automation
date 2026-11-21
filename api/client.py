import requests
from config.settings import API_URL


class ToolshopApi:
    TIMEOUT = 10

    def __init__(self, base_url=API_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def get_products(self, page=None):
        return self.session.get(f"{self.base_url}/products", params={"page": page}, timeout=self.TIMEOUT)

    def get_product(self, product_id):
        return self.session.get(f"{self.base_url}/products/{product_id}", timeout=self.TIMEOUT)

    def login(self, email, password):
        return self.session.post(
            f"{self.base_url}/users/login",
            json={
                "email": email,
                "password": password,
            },
            timeout=self.TIMEOUT
        )

    def set_token(self, token):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get_me(self):
        return self.session.get(f"{self.base_url}/users/me", timeout=self.TIMEOUT)
    