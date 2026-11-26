import pytest
import allure

from config.settings import USER_EMAIL, USER_PASSWORD


@pytest.mark.smoke
@allure.title("Успешная авторизация с корректными данными")
def test_login_with_valid_credentials(api):
    response = api.login(USER_EMAIL, USER_PASSWORD)
    assert response.status_code == 200, f"Ожидали получить статус 200, получили {response.status_code}"
    body = response.json()
    assert "access_token" in body, f"В ответе нет access_token, ключи: {list(body.keys())}"
    assert body["access_token"], "access_token пустой"
    

@pytest.mark.smoke
@allure.title("Получение данных авторизованного пользователя")
def test_get_me_with_token(auth_api):
    response = auth_api.get_me()
    assert response.status_code == 200, f"Ожидали получить статус 200, получили {response.status_code}"
    body = response.json()
    assert body["email"] == USER_EMAIL, f"Ожидали {USER_EMAIL}, получили {body['email']}"


@pytest.mark.regression
@allure.title("Запрос данных пользователя без токена авторизации")
def test_get_me_without_token(api):
    response = api.get_me()
    assert response.status_code == 401, f"Ожидали получить статус 401, получили {response.status_code}"
    body = response.json()
    assert body["message"] == "Unauthorized", f"Неожиданный текст ошибки: {body['message']}"


@pytest.mark.regression
@allure.title("Авторизация с некорректными данными: {param_id}")
@pytest.mark.parametrize(
    "email, password, expected_error", 
    [
        (USER_EMAIL, "wrong_password", "Unauthorized"),
        ("nobody@example.com", "wrong_password", "Unauthorized"),
        ("", USER_PASSWORD, "Invalid login request"),
        (USER_EMAIL, "", "Invalid login request"),
        ("not-an-email", "wrong_password", "Unauthorized"),
    ],
    ids=[
        "wrong_password",
        "nonexistent_email",
        "empty_email",
        "empty_password",
        "invalid_email_format",
    ]
)
def test_login_with_invalid_credentials(api, email, password, expected_error):
    response = api.login(email, password)
    assert response.status_code == 401, f"Ожидали получить статус 401, получили {response.status_code}"
    body = response.json()
    assert body["error"] == expected_error, f"Неожиданный текст ошибки: {body['error']}"
    assert "access_token" not in body, "Сервер выдал access_token при неверных данных"


