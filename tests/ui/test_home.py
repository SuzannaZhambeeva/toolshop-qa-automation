import pytest
import allure

from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from config.settings import BASE_URL


@pytest.mark.smoke
@allure.title("Открытие главной страницы")
def test_home_page_opens(open_home_page: HomePage):
    expect(open_home_page.product_names.first).to_be_visible()


@pytest.mark.smoke
@allure.title("Поиск товара по названию")
def test_search_product(open_home_page: HomePage):
    open_home_page.search_product("hammer")

    product = open_home_page.product_names.filter(has_text="Hammer").first
    expect(product).to_be_visible()


@pytest.mark.smoke
@allure.title("Поиск несуществующего товара")
def test_search_nonexistent_product(open_home_page: HomePage):

    expect(open_home_page.product_names.first).to_be_visible()

    open_home_page.search_product("xyznonexistent12345")

    expect(open_home_page.no_results).to_have_text(
        "There are no products found."
    )
    expect(open_home_page.product_names).to_have_count(0)



