import pytest
import re
import allure

from playwright.sync_api import Page, expect

from config.settings import BASE_URL
from pages.home_page import HomePage
from pages.product_page import ProductPage
from conftest import open_home_page

@pytest.mark.smoke
@allure.title("Открытие карточки товара")
def test_open_product(page: Page, open_home_page: HomePage):
    
    #проверка появления товаров
    expect(open_home_page.product_names.first).to_be_visible()

    open_home_page.search_product("hammer")
    open_home_page.open_product("Hammer")
    
    # Проверка URL через регулярное выражение
    expect(page).to_have_url(
        re.compile(r".*/product/[^/]+$")
    )

    product_page = ProductPage(page)
    
    # Проверка названия и цены
    expect(product_page.product_name).to_have_text("Hammer")
    expect(product_page.product_price).to_have_text("12.58")


@pytest.mark.smoke
@allure.title("Добавление товара в корзину")
def test_add_product_to_cart(page: Page, open_home_page:HomePage):
    expect(open_home_page.product_names.first).to_be_visible()
    open_home_page.search_product("hammer")
    open_home_page.open_product("Hammer")

    product_page = ProductPage(page)
    product_page.add_to_cart()

    expect(product_page.cart_quantity).to_have_text("1")

