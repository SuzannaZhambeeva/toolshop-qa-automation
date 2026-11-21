import pytest
from playwright.sync_api import Page
from api.client import ToolshopApi
from config.settings import BASE_URL, USER_EMAIL, USER_PASSWORD
from pages.home_page import HomePage


@pytest.fixture(scope="session")
def api():
    """Клиент API без авторизации."""
    return ToolshopApi()


@pytest.fixture(scope="session")
def auth_api():
    """Авторизованный клиент API"""
    client = ToolshopApi()
    response = client.login(USER_EMAIL, USER_PASSWORD)
    assert response.status_code == 200, f"Не удалось залогиниться: {response.status_code} {response.text}"
    token = response.json()["access_token"]
    client.set_token(token)
    return client


@pytest.fixture()
def open_home_page(page: Page):
    """Открытие главной страницы"""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    return HomePage(page)

