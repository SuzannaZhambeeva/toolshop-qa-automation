import pytest

from config.settings import USER_EMAIL, USER_PASSWORD


@pytest.mark.smoke
def test_login_with_valid_credentials(api):
    response = api.login(USER_EMAIL, USER_PASSWORD)
    assert response.status_code == 200, f"Ожидали получить статус 200, получили {response.status_code}"
    body = response.json()
    assert "access_token" in body, f"В ответе нет access_token, ключи: {list(body.keys())}"
    assert body["access_token"], "access_token пустой"


@pytest.mark.regression
def test_login_with_wrong_password(api):
    response = api.login(USER_EMAIL, "wrong_password")
    assert response.status_code == 401, f"Ожидали получить статус 401, получили {response.status_code}"
    body = response.json()
    assert body["error"] == "Unauthorized", f"Неожиданный текст ошибки: {body['error']}"
    assert "access_token" not in body, "Сервер выдал access_token при неверном пароле"
