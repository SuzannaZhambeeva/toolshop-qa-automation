import pytest
import allure

from config.settings import API_URL, BASE_URL


@pytest.mark.smoke
@allure.title("Проверка использования HTTPS в URL приложения и API")
def test_urls_use_https():
    assert API_URL.startswith("https://"), f"API_URL должен начинаться с https://, сейчас: {API_URL}"
    assert BASE_URL.startswith("https://"), f"BASE_URL должен начинаться с https://, сейчас: {BASE_URL}"