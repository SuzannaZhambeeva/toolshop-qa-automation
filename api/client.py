import requests
from config.settings import API_URL


class ToolshopApi:
    def __init__(self, base_url=API_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Accept":"application/json"})