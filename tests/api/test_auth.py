import pytest

from config.settings import USER_EMAIL, USER_PASSWORD


@pytest.mark.smoke
def test_login_with_valid_credentials(api):
    response = api.login(USER_EMAIL, USER_PASSWORD)
    assert response.status_code == 200, f"Ожидали получить статус 200, получили {response.status_code}"
    body = response.json()
    assert "access_token" in body, f"В ответе нет access_token, ключи: {list(body.keys())}"
    assert body["access_token"], "access_token пустой"

