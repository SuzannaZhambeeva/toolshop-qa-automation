import pytest


@pytest.mark.smoke
def test_get_products_returns_list(api):
    response = api.get_products()
    assert response.status_code == 200, f"Ожидали получить статус 200, получили {response.status_code}"
    products = response.json()["data"]
    assert len(products) > 0, "Список товаров пуст"


