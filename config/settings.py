import os
from dotenv import load_dotenv

load_dotenv()


def _require(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Переменная окружения {name} не задана. Проверьте файл .env")
    return value


BASE_URL = _require("BASE_URL").rstrip("/")
API_URL = _require("API_URL").rstrip("/")
USER_EMAIL = _require("USER_EMAIL")
USER_PASSWORD = _require("USER_PASSWORD")