import pytest


@pytest.mark.smoke
def test_get_products_returns_list(api):
    response = api.get_products()
    assert response.status_code == 200, f"Ожидали получить статус 200, получили {response.status_code}"
    products = response.json()['data']
    assert len(products) > 0, "Список товаров пуст"


@pytest.mark.regression
def test_get_product_by_id(api):
    products = api.get_products().json()["data"]
    product_id = products[0]["id"]
    response = api.get_product(product_id)
    assert response.status_code == 200, f"Ожидали получить статус 200, получили {response.status_code}"
    body = response.json()
    actual_id = body["id"]
    assert actual_id == product_id, f"Ожидали id {product_id}, получили {actual_id}"
 

@pytest.mark.regression
def test_get_nonexistent_product_returns_404(api):
    response = api.get_product("nonexistent123")
    assert response.status_code == 404, f"Ожидали получить статус 404, получили {response.status_code}"
    body = response.json()
    assert body["message"] == "Requested item not found", f"Неожиданный текст ошибки: {body['message']}"

