import pytest

from config.settings import API_URL, BASE_URL


@pytest.mark.smoke
def test_urls_use_https():
    assert API_URL.startswith("https://"), f"API_URL должен начинаться с https://, сейчас: {API_URL}"
    assert BASE_URL.startswith("https://"), f"BASE_URL должен начинаться с https://, сейчас: {BASE_URL}"